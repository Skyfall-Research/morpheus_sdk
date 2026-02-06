import gymnasium as gym
from gymnasium.utils.env_checker import check_env
from unittest.mock import MagicMock, patch
import numpy as np

import morpheus_sdk.gym

def verify_gym_env():
    print("Verifying Morpheus Gym Environment...")

    with patch("morpheus_sdk.gym.env.Morpheus") as MockMorpheus:
        mock_instance = MockMorpheus.return_value
        mock_instance.world_id = "test-world-id"
        mock_instance.observe.return_value.model_dump.return_value = {"status": "ok"}
        mock_instance.act.return_value.model_dump.return_value = {"success": True}

        env = gym.make("Morpheus-v0")
        
        print("1. Environment Initialization: OK")

        try:
            check_env(env.unwrapped, skip_render_check=True)
            print("2. Gymnasium Compliance Check: OK")
        except Exception as e:
            print(f"2. Gymnasium Compliance Check: FAILED\n{e}")
            return

        try:
            obs, info = env.reset()
            assert isinstance(obs, dict), "Observation must be a dict"
            assert "raw_state_json" in obs, "Observation must contain raw_state_json"
            print("3. Reset: OK")
        except Exception as e:
            print(f"3. Reset: FAILED\n{e}")

        try:
            action = {"path": "/api/test", "method": "POST", "body": {}}
            obs, reward, terminated, truncated, info = env.step(action)
            assert isinstance(obs, dict)
            assert isinstance(reward, float)
            assert isinstance(terminated, bool)
            assert isinstance(truncated, bool)
            assert isinstance(info, dict)
            print("4. Step: OK")
        except Exception as e:
            print(f"4. Step: FAILED\n{e}")

    print("\nVerification Complete.")

if __name__ == "__main__":
    verify_gym_env()
