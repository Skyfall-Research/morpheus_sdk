from typing import Optional, Union
from uuid import UUID

from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.system import get_docs_mesh
from ...client.generated_api_client.models.get_docs_mesh_method import GetDocsMeshMethod
from ...client.generated_api_client.models.get_docs_mesh_response_200 import GetDocsMeshResponse200
from ...client.generated_api_client.api.od import get_od_by_id
from ...client.generated_api_client.models.get_od_by_id_response_200 import GetODByIdResponse200

class ActionSpace:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    def mesh_docs(
        self,
        service: str,
        action: Optional[str] = None,
        method: Optional[Union[GetDocsMeshMethod, str]] = None,
        include_examples: bool = True
    ) -> GetDocsMeshResponse200:
        """
        Get detailed service mesh documentation.
        """
        # Handle inputs
        kwargs = {
            "service": service,
            "include_examples": include_examples
        }
        
        if action is not None:
            kwargs["action"] = action
            
        if method is not None:
            if isinstance(method, str):
                kwargs["method"] = GetDocsMeshMethod(method)
            else:
                kwargs["method"] = method

        response = get_docs_mesh.sync_detailed(
            client=self.client,
            **kwargs
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetDocsMeshResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for mesh docs: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get mesh docs: {response.status_code} {response.content}")

    def get_trajectory(self, od_id: str) -> GetODByIdResponse200:
        """
        Get an Operational Descriptor (trajectory) by ID.
        """
        response = get_od_by_id.sync_detailed(
            client=self.client,
            world_id=self.world_id,
            od_id=od_id
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetODByIdResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for get trajectory: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get trajectory: {response.status_code} {response.content}")


class AsyncActionSpace:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    async def mesh_docs(
        self,
        service: str,
        action: Optional[str] = None,
        method: Optional[Union[GetDocsMeshMethod, str]] = None,
        include_examples: bool = True
    ) -> GetDocsMeshResponse200:
        """
        Get detailed service mesh documentation.
        """
        # Handle inputs
        kwargs = {
            "service": service,
            "include_examples": include_examples
        }
        
        if action is not None:
            kwargs["action"] = action
            
        if method is not None:
            if isinstance(method, str):
                kwargs["method"] = GetDocsMeshMethod(method)
            else:
                kwargs["method"] = method

        response = await get_docs_mesh.asyncio_detailed(
            client=self.client,
            **kwargs
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetDocsMeshResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for mesh docs: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get mesh docs: {response.status_code} {response.content}")

    async def get_trajectory(self, od_id: str) -> GetODByIdResponse200:
        """
        Get an Operational Descriptor (trajectory) by ID.
        """
        response = await get_od_by_id.asyncio_detailed(
            client=self.client,
            world_id=self.world_id,
            od_id=od_id
        )

        if response.status_code == 200:
            if isinstance(response.parsed, GetODByIdResponse200):
                return response.parsed
            raise Exception(f"Unexpected response type for get trajectory: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to get trajectory: {response.status_code} {response.content}")
