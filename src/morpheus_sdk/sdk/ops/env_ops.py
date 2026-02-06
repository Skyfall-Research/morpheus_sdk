import logging
from typing import Optional

from ...client.generated_api_client.models.create_world_body import CreateWorldBody
from ...models.model_env import ModelCreateEnvInputs, ModelEnvOutput
from ...client.api.world import World, AsyncWorld

logger = logging.getLogger("morpheus_sdk")
from ...client.generated_api_client.types import UNSET

# ...

def execute_create_sync(wrapper: World, inputs: ModelCreateEnvInputs) -> ModelEnvOutput:
    try:
        # Bypass generated client due to parsing issues
        client = wrapper.client
        
        payload = {
            "name": inputs.name,
            "layout": inputs.layout
        }
        if inputs.description:
            payload["description"] = inputs.description
        if inputs.real_hours_per_sim_day is not None:
             payload["realHoursPerSimDay"] = inputs.real_hours_per_sim_day

        # Use relative URL as base_url is set in httpx client
        response = client.get_httpx_client().post("/world", json=payload)

        if response.status_code == 200:
            data = response.json()
            # extract world_id just like the wrapper would
            if "world" in data and "_id" in data["world"]:
                 wrapper.world_id = data["world"]["_id"]
            elif "world" in data and "field_id" in data["world"]:
                 wrapper.world_id = data["world"]["field_id"]
                 
            return ModelEnvOutput(
                status=200, 
                data=data, 
                error=None
            )
        else:
             return ModelEnvOutput(status=response.status_code, error=response.text)

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


def execute_pause_sync(wrapper: World) -> ModelEnvOutput:
    try:
        data = wrapper.pause()
        return ModelEnvOutput(status=200, data=data, error=None)
    except Exception as e:
        logger.error(f"Pause failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

async def execute_pause_async(wrapper: AsyncWorld) -> ModelEnvOutput:
    try:
        data = await wrapper.pause()
        return ModelEnvOutput(status=200, data=data, error=None)
    except Exception as e:
        logger.error(f"Pause failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

def execute_resume_sync(wrapper: World) -> ModelEnvOutput:
    try:
        data = wrapper.resume()
        return ModelEnvOutput(status=200, data=data, error=None)
    except Exception as e:
        logger.error(f"Resume failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

async def execute_resume_async(wrapper: AsyncWorld) -> ModelEnvOutput:
    try:
        data = await wrapper.resume()
        return ModelEnvOutput(status=200, data=data, error=None)
    except Exception as e:
        logger.error(f"Resume failed: {e}")
        return ModelEnvOutput(status=500, error=str(e))

