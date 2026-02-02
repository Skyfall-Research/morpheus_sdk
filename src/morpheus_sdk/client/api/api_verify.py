from morpheus_sdk.models.model_http_client import ModelHttpAsyncClientOutputs

async def verify_ticket(client: ModelHttpAsyncClientOutputs, world_id: str, ticket_id: str) -> dict:
    response = await client.get(f"/{world_id}/verification/verify-ticket", params={"ticket_id": ticket_id})
    return response.json()

async def verify_enitiy(client: ModelHttpAsyncClientOutputs, world_id: str) -> dict:
    response = await client.get(f"/{world_id}/verification/verify-entity")
    return response.json()