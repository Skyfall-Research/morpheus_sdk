from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.verification_result import VerificationResult
from ...models.verify_entity_body import VerifyEntityBody
from ...models.verify_entity_response_400 import VerifyEntityResponse400
from ...models.verify_entity_response_500 import VerifyEntityResponse500
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: VerifyEntityBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/verification/verify-entity",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]:
    if response.status_code == 200:
        response_200 = VerificationResult.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = VerifyEntityResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = VerifyEntityResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyEntityBody,
) -> Response[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]:
    """On-Demand Process Verification

     Executes the verification engine On-Demand against a specific LIVE ENTITY to confirm process health.
    Use this after applying fixes to verify that a specific Order, Task, or Workflow is now valid. This
    creates a virtual verification context and does *not* require an existing failure ticket.

    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyEntityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]
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
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyEntityBody,
) -> Optional[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]:
    """On-Demand Process Verification

     Executes the verification engine On-Demand against a specific LIVE ENTITY to confirm process health.
    Use this after applying fixes to verify that a specific Order, Task, or Workflow is now valid. This
    creates a virtual verification context and does *not* require an existing failure ticket.

    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyEntityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyEntityBody,
) -> Response[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]:
    """On-Demand Process Verification

     Executes the verification engine On-Demand against a specific LIVE ENTITY to confirm process health.
    Use this after applying fixes to verify that a specific Order, Task, or Workflow is now valid. This
    creates a virtual verification context and does *not* require an existing failure ticket.

    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyEntityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VerifyEntityBody,
) -> Optional[Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]]:
    """On-Demand Process Verification

     Executes the verification engine On-Demand against a specific LIVE ENTITY to confirm process health.
    Use this after applying fixes to verify that a specific Order, Task, or Workflow is now valid. This
    creates a virtual verification context and does *not* require an existing failure ticket.

    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (VerifyEntityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[VerificationResult, VerifyEntityResponse400, VerifyEntityResponse500]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
