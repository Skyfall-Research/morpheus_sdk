from typing import Any, Optional, List
from uuid import UUID

from ...client.generated_api_client.client import Client
from ...client.generated_api_client.api.itsm_tickets import get_ticket, get_tickets, update_ticket, update_ticket_status
from ...client.generated_api_client.models.update_ticket_body import UpdateTicketBody
from ...client.generated_api_client.models.update_ticket_status_body import UpdateTicketStatusBody
from ...client.generated_api_client.models.update_ticket_status_body_status import UpdateTicketStatusBodyStatus
from ...client.generated_api_client.models.get_tickets_response_200 import GetTicketsResponse200
from ...client.generated_api_client.models.get_ticket_response_200 import GetTicketResponse200
from ...client.generated_api_client.models.update_ticket_response_200 import UpdateTicketResponse200

class Tasks:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    def list(self, **kwargs) -> GetTicketsResponse200:
        """
        List tickets with optional filtering.
        kwargs can match arguments of get_tickets.sync_detailed:
        status, priority, impact, urgency, department, assigned_to, date_start, date_end, limit, cursor
        """
        response = get_tickets.sync_detailed(client=self.client, world_id=self.world_id, **kwargs)
        if response.status_code == 200:
            return response.parsed
        else:
             raise Exception(f"Failed to list tickets: {response.status_code} {response.content}")

    def get(self, ticket_id: str) -> GetTicketResponse200:
        response = get_ticket.sync_detailed(client=self.client, world_id=self.world_id, ticket_id=ticket_id)
        if response.status_code == 200:
            return response.parsed
        else:
             raise Exception(f"Failed to get ticket {ticket_id}: {response.status_code} {response.content}")

    def update(self, ticket_id: str, body: UpdateTicketBody) -> UpdateTicketResponse200:
        response = update_ticket.sync_detailed(client=self.client, world_id=self.world_id, ticket_id=ticket_id, body=body)
        if response.status_code == 200:
            return response.parsed
        else:
             raise Exception(f"Failed to update ticket {ticket_id}: {response.status_code} {response.content}")

    def mark_done(self, ticket_id: str):
        body = UpdateTicketStatusBody(status=UpdateTicketStatusBodyStatus.CLOSED)
        response = update_ticket_status.sync_detailed(client=self.client, world_id=self.world_id, ticket_id=ticket_id, body=body)
        if response.status_code != 200:
             raise Exception(f"Failed to mark ticket {ticket_id} as done: {response.status_code} {response.content}")

class AsyncTasks:
    def __init__(self, client: Client, world_id: str):
        self.client = client
        self.world_id = UUID(world_id)

    async def list(self, **kwargs) -> GetTicketsResponse200:
        response = await get_tickets.asyncio_detailed(client=self.client, world_id=self.world_id, **kwargs)
        if response.status_code == 200:
            return response.parsed
        else:
             raise Exception(f"Failed to list tickets: {response.status_code} {response.content}")

    async def get(self, ticket_id: str) -> GetTicketResponse200:
        response = await get_ticket.asyncio_detailed(client=self.client, world_id=self.world_id, ticket_id=ticket_id)
        if response.status_code == 200:
            return response.parsed
        else:
             raise Exception(f"Failed to get ticket {ticket_id}: {response.status_code} {response.content}")

    async def update(self, ticket_id: str, body: UpdateTicketBody) -> UpdateTicketResponse200:
        response = await update_ticket.asyncio_detailed(client=self.client, world_id=self.world_id, ticket_id=ticket_id, body=body)
        if response.status_code == 200:
            return response.parsed
        else:
             raise Exception(f"Failed to update ticket {ticket_id}: {response.status_code} {response.content}")

    async def mark_done(self, ticket_id: str):
        body = UpdateTicketStatusBody(status=UpdateTicketStatusBodyStatus.CLOSED)
        response = await update_ticket_status.asyncio_detailed(client=self.client, world_id=self.world_id, ticket_id=ticket_id, body=body)
        if response.status_code != 200:
             raise Exception(f"Failed to mark ticket {ticket_id} as done: {response.status_code} {response.content}")
