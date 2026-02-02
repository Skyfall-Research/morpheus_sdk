from typing import Optional
from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.world import create_world, delete_world, reset_world
from ...client.generated_api_client.models.create_world_body import CreateWorldBody

class World:
    def __init__(self, client: Client):
        self.client = client
        self.world_id: Optional[str] = None

    def create(self, body: CreateWorldBody) -> CreateWorldBody:
        response = create_world.sync_detailed(client=self.client, body=body)
        if response.status_code == 200:
            if response.parsed and response.parsed.world and response.parsed.world.id:
                self.world_id = response.parsed.world.id
            return body
        else:
             raise Exception(f"Failed to create world: {response.status_code} {response.content}")

    def delete(self):
        if not self.world_id:
             raise Exception("World ID not set. Call create() first.")
        
        response = delete_world.sync_detailed(client=self.client, world_id=self.world_id)
        if response.status_code != 200:
             raise Exception(f"Failed to delete world: {response.status_code} {response.content}")

    def reset(self):
         if not self.world_id:
             raise Exception("World ID not set. Call create() first.")
         
         response = reset_world.sync_detailed(client=self.client, world_id=self.world_id)
         if response.status_code != 200:
             raise Exception(f"Failed to reset world: {response.status_code} {response.content}")

class AsyncWorld:
    def __init__(self, client: Client):
        self.client = client
        self.world_id: Optional[str] = None

    async def create(self, body: CreateWorldBody) -> CreateWorldBody:
        response = await create_world.asyncio_detailed(client=self.client, body=body)
        if response.status_code == 200:
            if response.parsed and response.parsed.world and response.parsed.world.id:
                self.world_id = response.parsed.world.id
            return body
        else:
             raise Exception(f"Failed to create world: {response.status_code} {response.content}")

    async def delete(self):
        if not self.world_id:
             raise Exception("World ID not set. Call create() first.")
        
        response = await delete_world.asyncio_detailed(client=self.client, world_id=self.world_id)
        if response.status_code != 200:
             raise Exception(f"Failed to delete world: {response.status_code} {response.content}")

    async def reset(self):
         if not self.world_id:
             raise Exception("World ID not set. Call create() first.")
         
         response = await reset_world.asyncio_detailed(client=self.client, world_id=self.world_id)
         if response.status_code != 200:
             raise Exception(f"Failed to reset world: {response.status_code} {response.content}")
