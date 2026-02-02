from morpheus_sdk.models.model_http_client import ModelHttpAsyncClientOutputs


async def get_task(client: ModelHttpAsyncClientOutputs, world_id: str, task_id: str) -> dict:
    response = await client.get(f"/{world_id}/task/{task_id}")
    return response.json()

async def update_task(client: ModelHttpAsyncClientOutputs, world_id: str, task_id: str, inputs: ModelCreateEnvInputs) -> dict:
    response = await client.put(f"/{world_id}/task/{task_id}", json=inputs.model_dump())
    return response.json()

async def list_tasks(client: ModelHttpAsyncClientOutputs, world_id: str) -> dict:
    response = await client.get(f"/{world_id}/task")
    return response.json()