import logging
from typing import Optional

from ..client.generated_api_client.client import Client
from ..client.generated_api_client.api.system import get_docs
from ..client.api.world import World, AsyncWorld
from ..client.api.act import Act, AsyncAct
from ..client.api.observation import Observation, AsyncObservation
from ..client.api.verify import Verify, AsyncVerify
from ..client.api.tasks import Tasks, AsyncTasks
from ..client.api.action_space import ActionSpace, AsyncActionSpace

from ..models.model_http_client import ModelHttpClientInputs
from ..models.model_env import ModelCreateEnvInputs, ModelEnvOutput
from ..models.model_act import ModelActInputs, ModelActObservation
from ..models.model_state import ModelStateInputs, ModelStateOutputs
from ..models.model_verify import (
    ModelVerifyInputs, 
    ModelVerifyOutput,
    ModelVerifyTicketInputs,
    ModelVerifyEntityInputs
)
from ..models.model_task import ModelTaskInputs, ModelTaskOutputs
from ..models.model_action_space import (
    ModelActionSpaceInputs, 
    ModelActionSpaceObservation,
    ModelActionSpaceMeshDocsInputs,
    ModelActionSpaceTrajectoryInputs
)

# Operations
from .ops.env_ops import execute_create_sync, execute_delete_sync, execute_reset_sync, execute_create_async, execute_delete_async, execute_reset_async
from .ops.act_ops import execute_act_sync, execute_act_async
from .ops.observe_ops import execute_observe_sync, execute_observe_async
from .ops.verify_ops import execute_verify_sync, execute_verify_async
from .ops.task_ops import execute_task_sync, execute_task_async
from .ops.action_space_ops import execute_action_space_sync, execute_action_space_async

# Configure default logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("morpheus_sdk")

__all__ = [
    "Morpheus",
    "AsyncMorpheus",
    "Client",
    "ModelHttpClientInputs",
    "ModelCreateEnvInputs", 
    "ModelEnvOutput",
    "ModelActInputs", 
    "ModelActObservation",
    "ModelStateInputs", 
    "ModelStateOutputs",
    "ModelVerifyInputs", 
    "ModelVerifyOutput",
    "ModelVerifyTicketInputs",
    "ModelVerifyEntityInputs",
    "ModelTaskInputs", 
    "ModelTaskOutputs",
    "ModelActionSpaceInputs", 
    "ModelActionSpaceObservation",
    "ModelActionSpaceMeshDocsInputs",
    "ModelActionSpaceTrajectoryInputs",
]

class Morpheus:
    def __init__(self, settings: ModelHttpClientInputs = ModelHttpClientInputs(), world_id: Optional[str] = None):
        self.settings = settings
        self.world_id = world_id
        
        # Initialize Client
        self.client = Client(
            base_url=settings.base_url,
            headers=settings.headers,
            timeout=settings.timeout
        )
        
        # Initialize Wrappers
        self._world_wrapper = World(self.client)
        if self.world_id:
             self._world_wrapper.world_id = self.world_id
             
        self._act_wrapper = Act(self.client)
        
        # These wrappers require world_id, will be instantiated/updated when world_id is available
        self._obs_wrapper: Optional[Observation] = None
        self._verify_wrapper: Optional[Verify] = None
        self._task_wrapper: Optional[Tasks] = None
        self._action_space_wrapper: Optional[ActionSpace] = None

        if self.world_id:
            self._update_wrappers()

        # Connection Check
        try:
            get_docs.sync_detailed(client=self.client)
            logger.info("Morpheus SDK connected successfully.")
        except Exception as e:
            logger.warning(f"Failed to connect to Morpheus backend: {e}")

    def _update_wrappers(self):
        if not self.world_id:
            return
        self._obs_wrapper = Observation(self.client, self.world_id)
        self._verify_wrapper = Verify(self.client, self.world_id)
        self._task_wrapper = Tasks(self.client, self.world_id)
        self._action_space_wrapper = ActionSpace(self.client, self.world_id)

    def create(self, inputs: ModelCreateEnvInputs) -> ModelEnvOutput:
        result = execute_create_sync(self._world_wrapper, inputs)
        if result.status == 200 and result.data:
             # Assume wrapper updated its own local ID, but we strictly need to grab it from wrapper or result
             # Current ops implementation calls wrapper.create which returns body. 
             # Wrapper implementation sets self.world_id.
             # So we can just fetch it from wrapper.
             self.world_id = self._world_wrapper.world_id
             self._update_wrappers()
        return result

    def delete(self) -> ModelEnvOutput:
        return execute_delete_sync(self._world_wrapper)

    def reset(self) -> ModelEnvOutput:
        return execute_reset_sync(self._world_wrapper)

    def act(self, inputs: ModelActInputs) -> ModelActObservation:
        return execute_act_sync(self._act_wrapper, inputs)

    def observe(self, inputs: ModelStateInputs) -> ModelStateOutputs:
        return execute_observe_sync(self._obs_wrapper, inputs, self.world_id)
    
    def verify(self, inputs: ModelVerifyInputs) -> ModelVerifyOutput:
        return execute_verify_sync(self._verify_wrapper, inputs)

    def task(self, inputs: ModelTaskInputs) -> ModelTaskOutputs:
        return execute_task_sync(self._task_wrapper, inputs)

    def action_space(self, inputs: ModelActionSpaceInputs) -> ModelActionSpaceObservation:
        return execute_action_space_sync(self._action_space_wrapper, inputs)

class AsyncMorpheus:
    def __init__(self, settings: ModelHttpClientInputs = ModelHttpClientInputs(), world_id: Optional[str] = None):
        self.settings = settings
        self.world_id = world_id
        
        self.client = Client(
            base_url=settings.base_url,
            headers=settings.headers,
            timeout=settings.timeout
        )
        
        self._world_wrapper = AsyncWorld(self.client)
        if self.world_id:
             self._world_wrapper.world_id = self.world_id
             
        self._act_wrapper = AsyncAct(self.client)
        
        self._obs_wrapper: Optional[AsyncObservation] = None
        self._verify_wrapper: Optional[AsyncVerify] = None
        self._task_wrapper: Optional[AsyncTasks] = None
        self._action_space_wrapper: Optional[AsyncActionSpace] = None

        if self.world_id:
            self._update_wrappers()

    def _update_wrappers(self):
        if not self.world_id:
            return
        self._obs_wrapper = AsyncObservation(self.client, self.world_id)
        self._verify_wrapper = AsyncVerify(self.client, self.world_id)
        self._task_wrapper = AsyncTasks(self.client, self.world_id)
        self._action_space_wrapper = AsyncActionSpace(self.client, self.world_id)

    async def connect(self):
        try:
            await get_docs.asyncio_detailed(client=self.client)
            logger.info("AsyncMorpheus SDK connected successfully.")
        except Exception as e:
            logger.warning(f"Failed to connect to Morpheus backend: {e}")

    async def create(self, inputs: ModelCreateEnvInputs) -> ModelEnvOutput:
        result = await execute_create_async(self._world_wrapper, inputs)
        if result.status == 200 and result.data:
             self.world_id = self._world_wrapper.world_id
             self._update_wrappers()
        return result

    async def delete(self) -> ModelEnvOutput:
        return await execute_delete_async(self._world_wrapper)

    async def reset(self) -> ModelEnvOutput:
        return await execute_reset_async(self._world_wrapper)

    async def act(self, inputs: ModelActInputs) -> ModelActObservation:
        return await execute_act_async(self._act_wrapper, inputs)

    async def observe(self, inputs: ModelStateInputs) -> ModelStateOutputs:
        return await execute_observe_async(self._obs_wrapper, inputs, self.world_id)

    async def verify(self, inputs: ModelVerifyInputs) -> ModelVerifyOutput:
        return await execute_verify_async(self._verify_wrapper, inputs)

    async def task(self, inputs: ModelTaskInputs) -> ModelTaskOutputs:
        return await execute_task_async(self._task_wrapper, inputs)

    async def action_space(self, inputs: ModelActionSpaceInputs) -> ModelActionSpaceObservation:
        return await execute_action_space_async(self._action_space_wrapper, inputs)
