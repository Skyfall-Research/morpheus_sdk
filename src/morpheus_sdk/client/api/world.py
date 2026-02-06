from typing import Optional
from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.world import create_world, delete_world, reset_world, list_worlds
from ...client.generated_api_client.models.create_world_body import CreateWorldBody


class World:
    def __init__(self, client: Client):
        self.client = client
        self.world_id: Optional[str] = None

    def create(self, body: CreateWorldBody) -> CreateWorldBody:
        response = create_world.sync_detailed(client=self.client, body=body)
        if response.status_code == 200:
            if response.parsed and response.parsed.world and response.parsed.world.field_id:
                self.world_id = response.parsed.world.field_id
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
    
    def get_default_world(self):
        response = list_worlds.sync_detailed(client=self.client, is_default=True)
        if response.status_code == 200:
            if response.parsed and response.parsed.worlds and len(response.parsed.worlds) > 0:
                self.world_id = response.parsed.worlds[0].field_id
                return response.parsed.worlds[0]
            else:
                raise Exception("No default world found")
        else:
             raise Exception(f"Failed to get default world: {response.status_code} {response.content}")

    def pause(self):
        # Endpoint: PUT /:worldId/od/schedules/pause
        url = f"/{self.world_id}/od/schedules/pause"
        response = self.client.get_httpx_client().put(url)
        if response.status_code != 200:
             raise Exception(f"Pause failed: {response.text}")
        return response.json()

    def resume(self):
        # Endpoint: PUT /:worldId/od/schedules/resume
        url = f"/{self.world_id}/od/schedules/resume"
        response = self.client.get_httpx_client().put(url)
        if response.status_code != 200:
             raise Exception(f"Resume failed: {response.text}")
        return response.json()

class AsyncWorld:
    def __init__(self, client: Client):
        self.client = client
        self.world_id: Optional[str] = None

    async def create(self, body: CreateWorldBody) -> CreateWorldBody:
        response = await create_world.asyncio_detailed(client=self.client, body=body)
        if response.status_code == 200:
            if response.parsed and response.parsed.world and response.parsed.world.field_id:
                self.world_id = response.parsed.world.field_id
            return body
        else:
             raise Exception(f"Failed to create world: {response.status_code} {response.content}")
    
    async def pause(self):
        url = f"/{self.world_id}/od/schedules/pause"
        response = await self.client.get_async_httpx_client().put(url)
        if response.status_code != 200:
             raise Exception(f"Pause failed: {response.text}")
        return response.json()

    async def resume(self):
        url = f"/{self.world_id}/od/schedules/resume"
        response = await self.client.get_async_httpx_client().put(url)
        if response.status_code != 200:
             raise Exception(f"Resume failed: {response.text}")
        return response.json()

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

    async def get_default_world(self):
        response = await list_worlds.asyncio_detailed(client=self.client, is_default=True)
        if response.status_code == 200:
            if response.parsed and response.parsed.worlds and len(response.parsed.worlds) > 0:
                self.world_id = response.parsed.worlds[0].field_id
                return response.parsed.worlds[0]
            else:
                raise Exception("No default world found")
        else:
             raise Exception(f"Failed to get default world: {response.status_code} {response.content}")