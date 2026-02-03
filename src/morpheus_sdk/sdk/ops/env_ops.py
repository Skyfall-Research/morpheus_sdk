import logging
from typing import Optional

from ...client.generated_api_client.models.create_world_body import CreateWorldBody
from ...models.model_env import ModelCreateEnvInputs, ModelEnvOutput
from ...client.api.world import World, AsyncWorld

logger = logging.getLogger("morpheus_sdk")

def execute_create_sync(wrapper: World, inputs: ModelCreateEnvInputs) -> ModelEnvOutput:
    try:
        body = CreateWorldBody(
            name=inputs.name,
            description=inputs.description,
            layout=inputs.layout,
            real_hours_per_sim_day=inputs.real_hours_per_sim_day
        )
        created_body = wrapper.create(body)
        return ModelEnvOutput(
            status=200, 
            data=created_body.to_dict(), 
            error=None
        )
    except Exception as e:
        logger.error(f"Create failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

async def execute_create_async(wrapper: AsyncWorld, inputs: ModelCreateEnvInputs) -> ModelEnvOutput:
    try:
        body = CreateWorldBody(
            name=inputs.name,
            description=inputs.description,
            layout=inputs.layout,
            real_hours_per_sim_day=inputs.real_hours_per_sim_day
        )
        created_body = await wrapper.create(body)
        return ModelEnvOutput(
            status=200, 
            data=created_body.to_dict(), 
            error=None
        )
    except Exception as e:
        logger.error(f"Create failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

def execute_delete_sync(wrapper: World) -> ModelEnvOutput:
    try:
        wrapper.delete()
        return ModelEnvOutput(status=200, data={"message": "World deleted"}, error=None)
    except Exception as e:
        logger.error(f"Delete failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

async def execute_delete_async(wrapper: AsyncWorld) -> ModelEnvOutput:
    try:
        await wrapper.delete()
        return ModelEnvOutput(status=200, data={"message": "World deleted"}, error=None)
    except Exception as e:
        logger.error(f"Delete failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

def execute_reset_sync(wrapper: World) -> ModelEnvOutput:
    try:
        wrapper.reset()
        return ModelEnvOutput(status=200, data={"message": "World reset"}, error=None)
    except Exception as e:
        logger.error(f"Reset failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

async def execute_reset_async(wrapper: AsyncWorld) -> ModelEnvOutput:
    try:
        await wrapper.reset()
        return ModelEnvOutput(status=200, data={"message": "World reset"}, error=None)
    except Exception as e:
        logger.error(f"Reset failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))
