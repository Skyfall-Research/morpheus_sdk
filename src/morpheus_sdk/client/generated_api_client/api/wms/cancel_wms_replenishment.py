from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.cancel_wms_replenishment_body import CancelWMSReplenishmentBody
from ...models.cancel_wms_replenishment_response_200 import CancelWMSReplenishmentResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    replenishment_id: str,
    *,
    body: CancelWMSReplenishmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/replenishments/{replenishment_id}/cancel",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[CancelWMSReplenishmentResponse200]:
    if response.status_code == 200:
        response_200 = CancelWMSReplenishmentResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[CancelWMSReplenishmentResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelWMSReplenishmentBody,
) -> Response[CancelWMSReplenishmentResponse200]:
    """Cancel replenishment


    ## Cancel Replenishment Request

    Cancel a replenishment request with reason and audit information.

    **Business Process:**
    - Changes status to CANCELLED regardless of current state
    - Records cancellation metadata (reason, cancelledBy, cancelledDate)
    - Maintains audit trail for operational analysis
    - Prevents further workflow processing

    **Use Cases:**
    - Process termination and cleanup
    - Business rule changes
    - Error correction and recovery
    - Resource reallocation

    **Field Mapping:**
    - Sets `status` to CANCELLED
    - Updates cancellation audit fields


    Args:
        world_id (str):
        replenishment_id (str):
        body (CancelWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelWMSReplenishmentResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        replenishment_id=replenishment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelWMSReplenishmentBody,
) -> Optional[CancelWMSReplenishmentResponse200]:
    """Cancel replenishment


    ## Cancel Replenishment Request

    Cancel a replenishment request with reason and audit information.

    **Business Process:**
    - Changes status to CANCELLED regardless of current state
    - Records cancellation metadata (reason, cancelledBy, cancelledDate)
    - Maintains audit trail for operational analysis
    - Prevents further workflow processing

    **Use Cases:**
    - Process termination and cleanup
    - Business rule changes
    - Error correction and recovery
    - Resource reallocation

    **Field Mapping:**
    - Sets `status` to CANCELLED
    - Updates cancellation audit fields


    Args:
        world_id (str):
        replenishment_id (str):
        body (CancelWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelWMSReplenishmentResponse200
    """

    return sync_detailed(
        world_id=world_id,
        replenishment_id=replenishment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelWMSReplenishmentBody,
) -> Response[CancelWMSReplenishmentResponse200]:
    """Cancel replenishment


    ## Cancel Replenishment Request

    Cancel a replenishment request with reason and audit information.

    **Business Process:**
    - Changes status to CANCELLED regardless of current state
    - Records cancellation metadata (reason, cancelledBy, cancelledDate)
    - Maintains audit trail for operational analysis
    - Prevents further workflow processing

    **Use Cases:**
    - Process termination and cleanup
    - Business rule changes
    - Error correction and recovery
    - Resource reallocation

    **Field Mapping:**
    - Sets `status` to CANCELLED
    - Updates cancellation audit fields


    Args:
        world_id (str):
        replenishment_id (str):
        body (CancelWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CancelWMSReplenishmentResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        replenishment_id=replenishment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    replenishment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CancelWMSReplenishmentBody,
) -> Optional[CancelWMSReplenishmentResponse200]:
    """Cancel replenishment


    ## Cancel Replenishment Request

    Cancel a replenishment request with reason and audit information.

    **Business Process:**
    - Changes status to CANCELLED regardless of current state
    - Records cancellation metadata (reason, cancelledBy, cancelledDate)
    - Maintains audit trail for operational analysis
    - Prevents further workflow processing

    **Use Cases:**
    - Process termination and cleanup
    - Business rule changes
    - Error correction and recovery
    - Resource reallocation

    **Field Mapping:**
    - Sets `status` to CANCELLED
    - Updates cancellation audit fields


    Args:
        world_id (str):
        replenishment_id (str):
        body (CancelWMSReplenishmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CancelWMSReplenishmentResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            replenishment_id=replenishment_id,
            client=client,
            body=body,
        )
    ).parsed
