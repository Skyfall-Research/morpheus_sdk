
from morpheus_sdk.models.model_env import ModelCreateEnvInputs
from morpheus_sdk.models.model_http_client import ModelHttpAsyncClientOutputs


async def create_world(client: ModelHttpAsyncClientOutputs, inputs: ModelCreateEnvInputs) -> dict:
    response = await client.post("/world", json=inputs.model_dump())
    return response.json()
    
async def delete_world(client: ModelHttpAsyncClientOutputs, world_id: str) -> dict:
    response = await client.delete(f"/world/{world_id}")
    return response.json()

async def get_world(client: ModelHttpAsyncClientOutputs, world_id: str) -> dict:
    response = await client.get(f"/world/{world_id}")
    return response.json()