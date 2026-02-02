from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verification_result import VerificationResult
from ...models.verify_ticket_body import VerifyTicketBody
from ...models.verify_ticket_response_404 import VerifyTicketResponse404
from ...models.verify_ticket_response_500 import VerifyTicketResponse500
from ...types import Response


def _get_kwargs(
    world_id: UUID,
    *,
    body: VerifyTicketBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/verification/verify-ticket",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]:
    if response.status_code == 200:
        response_200 = VerificationResult.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = VerifyTicketResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = VerifyTicketResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTicketBody,
) -> Response[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]:
    """Forensic Verification of a Ticket

     Executes the verification engine against a specific historical FAILURE TICKET. Use this to analyze
    root causes of past failures. It re-evaluates the invariant checks in the context of the *current*
    world state, but focusing on the entities linked to the original ticket.

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTicketBody,
) -> Optional[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]:
    """Forensic Verification of a Ticket

     Executes the verification engine against a specific historical FAILURE TICKET. Use this to analyze
    root causes of past failures. It re-evaluates the invariant checks in the context of the *current*
    world state, but focusing on the entities linked to the original ticket.

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTicketBody,
) -> Response[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]:
    """Forensic Verification of a Ticket

     Executes the verification engine against a specific historical FAILURE TICKET. Use this to analyze
    root causes of past failures. It re-evaluates the invariant checks in the context of the *current*
    world state, but focusing on the entities linked to the original ticket.

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyTicketBody,
) -> Optional[Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]]:
    """Forensic Verification of a Ticket

     Executes the verification engine against a specific historical FAILURE TICKET. Use this to analyze
    root causes of past failures. It re-evaluates the invariant checks in the context of the *current*
    world state, but focusing on the entities linked to the original ticket.

    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyTicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VerificationResult, VerifyTicketResponse404, VerifyTicketResponse500]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
