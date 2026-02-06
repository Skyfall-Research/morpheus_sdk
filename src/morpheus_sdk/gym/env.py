import gymnasium as gym
from gymnasium import spaces
import numpy as np
import json
import string
import uuid
from typing import Any, Dict, Optional, Tuple, Union

from ..sdk.morpheus import Morpheus, ModelHttpClientInputs, ModelCreateEnvInputs, ModelActInputs, ModelStateInputs

class MorpheusEnv(gym.Env):
    """
    OpenAI Gym (Gymnasium) wrapper for the Morpheus Simulator.
    
    This environment allows agents to interact with Morpheus worlds using the standard 
    reset/step interface.
    """
    metadata = {"render_modes": ["human"]}

    def __init__(self, 
                 sdk_settings: Optional[ModelHttpClientInputs] = None, 
                 env_config: Optional[ModelCreateEnvInputs] = None,
                 render_mode: Optional[str] = None):
        """
        Initialize the Morpheus Environment.

        Args:
            sdk_settings: Configuration for connecting to the Morpheus backend.
            env_config: Configuration for creating the world on reset().
            render_mode: standard gym render mode argument.
        """
        self.render_mode = render_mode
        
        # Initialize SDK
        self.sdk = Morpheus(settings=sdk_settings or ModelHttpClientInputs())
        unique_suffix = uuid.uuid4().hex[:8]
        self.env_config = env_config or ModelCreateEnvInputs(
            name=f"Gym-Morpheus-World-{unique_suffix}",
            layout="perishables-food-manufacturer"
        )
        
        # Define Spaces
        
        # We need to allow all printable characters for JSON content and paths
        printable_chars = string.printable

        # Action space: A flexible dictionary allowing the agent to specify path, method, and body.
        self.action_space = spaces.Dict({
            "path": spaces.Text(max_length=256, charset=printable_chars),
            "method": spaces.Text(max_length=10, charset=printable_chars),
        })

        # Observation space: The full state return from Morpheus.
        self.observation_space = spaces.Dict({
            "world_id": spaces.Text(max_length=64, charset=printable_chars),
            "raw_state_json": spaces.Text(max_length=1000000, charset=printable_chars) 
        })

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        options: Optional[Dict[str, Any]] = None,
    ) -> Tuple[Dict[str, Any], Dict[str, Any]]:
        """
        Create a new simulation world or reset the existing one.
        """
        super().reset(seed=seed)
        
        # If options contains config overrides, use them
        config = self.env_config
        if options and "env_config" in options:
             # Basic override logic
             pass
        
        # Create/overwrite the world
        try:
            # We always create a fresh world for a clean episode, or we could support .reset() 
            # if the backend supports true resets. The backend .reset() exists.
            if self.sdk.world_id:
                self.sdk.reset()
            else:
                self.sdk.create(config)
            
            # Fetch initial state
            obs = self._get_obs()
            info = self._get_info()
            
            return obs, info
            
        except Exception as e:
            # Fallback if connection fails or API errors
            raise RuntimeError(f"Failed to reset Morpheus environment: {e}")

    def step(self, action: Dict[str, Any]) -> Tuple[Dict[str, Any], float, bool, bool, Dict[str, Any]]:
        """
        Execute an action in the environment.
        
        Args:
            action: Dict containing "path", "method", and "body".
        """
        path = action.get("path")
        method = action.get("method", "POST")
        body = action.get("body", {})
        
        if not path:
             raise ValueError("Action must contain 'path'")

        # Execute Action
        try:
            act_input = ModelActInputs(path=path, method=method, body=body)
            act_result = self.sdk.act(act_input)
            last_result = act_result.model_dump()
        except Exception as e:
            # Handle invalid actions (common with random sampling in check_env)
            # We return the current state and an error info
            last_result = {"status": 400, "error": str(e), "success": False}
        
        # Observe State
        obs = self._get_obs()
        info = self._get_info()
        
        # Add the immediate action result to info
        info["last_action_result"] = last_result

        
        # Reward Calculation
        # This is where a Gym Wrapper usually needs specific logic. 
        # For a generic simulator, reward is 0 unless specified otherwise.
        reward = 0.0
        
        # Termination conditions
        terminated = False
        truncated = False
        
        return obs, reward, terminated, truncated, info

    def render(self):
        if self.render_mode == "human":
            print(f"World ID: {self.sdk.world_id}")

    def close(self):
        if self.sdk.world_id:
            try:
                self.sdk.delete()
            except:
                pass

    def pause(self):
        """Pause the simulation."""
        self.sdk.pause()

    def resume(self):
        """Resume the simulation."""
        self.sdk.resume()


    def _get_obs(self) -> Dict[str, Any]:
        """Helper to get current observation"""
        # We request a basic state. Can be tuned via options.
        # In a test mock, we must ensure model_dump returns a dict.
        state_obj = self.sdk.observe(ModelStateInputs(include={"logs": True, "audit_log": True}, limit=10))
        
        # Handle potential mock object returning dict directly or pydantic model
        state_dict = state_obj.model_dump() if hasattr(state_obj, 'model_dump') else state_obj
        if not isinstance(state_dict, dict):
             state_dict = {}

        return {
            "world_id": self.sdk.world_id or "",
            "raw_state_json": json.dumps(state_dict, default=str)
        }
        
    def _get_info(self) -> Dict[str, Any]:
        return {}
