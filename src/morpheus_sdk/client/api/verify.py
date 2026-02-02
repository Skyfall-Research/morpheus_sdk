from typing import Union, Optional
from uuid import UUID

from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.verification import verify_entity, verify_ticket
from ...client.generated_api_client.models.verify_entity_body import VerifyEntityBody
from ...client.generated_api_client.models.verify_ticket_body import VerifyTicketBody
from ...client.generated_api_client.models.verification_result import VerificationResult
from ...client.generated_api_client.models.verify_entity_body_entity_type import VerifyEntityBodyEntityType

class Verify:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    def ticket(self, ticket_id: str) -> VerificationResult:
        body = VerifyTicketBody(ticket_id=ticket_id)
        response = verify_ticket.sync_detailed(client=self.client, world_id=self.world_id, body=body)
        
        if response.status_code == 200:
            if isinstance(response.parsed, VerificationResult):
                return response.parsed
            # Should not happen based on types but safety check
            raise Exception(f"Unexpected response type for verify ticket: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to verify ticket {ticket_id}: {response.status_code} {response.content}")

    def entity(
        self, 
        od_id: str, 
        entity_id: Optional[str] = None, 
        entity_type: Optional[Union[VerifyEntityBodyEntityType, str]] = None
    ) -> VerificationResult:
        
        # Handle string input for convenience
        # Handle inputs
        kwargs = {}
        if entity_id is not None:
            kwargs["entity_id"] = entity_id

        if entity_type is not None:
            if isinstance(entity_type, str):
                kwargs["entity_type"] = VerifyEntityBodyEntityType(entity_type)
            else:
                kwargs["entity_type"] = entity_type

        body = VerifyEntityBody(od_id=od_id, **kwargs)
        response = verify_entity.sync_detailed(client=self.client, world_id=self.world_id, body=body)

        if response.status_code == 200:
            if isinstance(response.parsed, VerificationResult):
                return response.parsed
            raise Exception(f"Unexpected response type for verify entity: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to verify entity {entity_id}: {response.status_code} {response.content}")

class AsyncVerify:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    async def ticket(self, ticket_id: str) -> VerificationResult:
        body = VerifyTicketBody(ticket_id=ticket_id)
        response = await verify_ticket.asyncio_detailed(client=self.client, world_id=self.world_id, body=body)
        
        if response.status_code == 200:
            if isinstance(response.parsed, VerificationResult):
                return response.parsed
            raise Exception(f"Unexpected response type for verify ticket: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to verify ticket {ticket_id}: {response.status_code} {response.content}")

    async def entity(
        self, 
        od_id: str, 
        entity_id: Optional[str] = None, 
        entity_type: Optional[Union[VerifyEntityBodyEntityType, str]] = None
    ) -> VerificationResult:
        
        # Handle string input for convenience
        # Handle inputs
        kwargs = {}
        if entity_id is not None:
            kwargs["entity_id"] = entity_id

        if entity_type is not None:
            if isinstance(entity_type, str):
                kwargs["entity_type"] = VerifyEntityBodyEntityType(entity_type)
            else:
                kwargs["entity_type"] = entity_type

        body = VerifyEntityBody(od_id=od_id, **kwargs)
        response = await verify_entity.asyncio_detailed(client=self.client, world_id=self.world_id, body=body)

        if response.status_code == 200:
            if isinstance(response.parsed, VerificationResult):
                return response.parsed
            raise Exception(f"Unexpected response type for verify entity: {type(response.parsed)}")
        else:
             raise Exception(f"Failed to verify entity {entity_id}: {response.status_code} {response.content}")
