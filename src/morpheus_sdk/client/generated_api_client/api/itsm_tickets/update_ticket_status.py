from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_ticket_status_body import UpdateTicketStatusBody
from ...models.update_ticket_status_response_200 import UpdateTicketStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: UUID,
    ticket_id: str,
    *,
    body: UpdateTicketStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/tickets/{ticket_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateTicketStatusResponse200]:
    if response.status_code == 200:
        response_200 = UpdateTicketStatusResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateTicketStatusResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: UUID,
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTicketStatusBody,
) -> Response[UpdateTicketStatusResponse200]:
    """Update ticket status only

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        ticket_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateTicketStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTicketStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        ticket_id=ticket_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTicketStatusBody,
) -> Optional[UpdateTicketStatusResponse200]:
    """Update ticket status only

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        ticket_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateTicketStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTicketStatusResponse200
    """

    return sync_detailed(
        world_id=world_id,
        ticket_id=ticket_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTicketStatusBody,
) -> Response[UpdateTicketStatusResponse200]:
    """Update ticket status only

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        ticket_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateTicketStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateTicketStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        ticket_id=ticket_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    ticket_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTicketStatusBody,
) -> Optional[UpdateTicketStatusResponse200]:
    """Update ticket status only

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        ticket_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateTicketStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateTicketStatusResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            ticket_id=ticket_id,
            client=client,
            body=body,
        )
    ).parsed
