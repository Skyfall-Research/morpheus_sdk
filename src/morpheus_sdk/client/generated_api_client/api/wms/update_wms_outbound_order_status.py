from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_outbound_order_status_body import UpdateWMSOutboundOrderStatusBody
from ...models.update_wms_outbound_order_status_response_200 import UpdateWMSOutboundOrderStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
    *,
    body: UpdateWMSOutboundOrderStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/outbound-orders/{order_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSOutboundOrderStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSOutboundOrderStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]:
    """Update order status with automatic timestamp tracking


    **Order Status Management**

    Update order status with automatic workflow timestamp tracking.

    **Automatic Timing Updates:**
    - RELEASED → `timing.releasedAt`
    - ALLOCATED → `timing.allocatedAt`
    - PICKING → `timing.pickingStartedAt`
    - PICKED → `timing.pickedAt`
    - PACKED → `timing.packedAt`
    - SHIPPED → `timing.shippedAt`

    **Business Workflow:**
    Each status represents a key milestone in order fulfillment with precise timing capture.


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSOutboundOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSOutboundOrderStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]:
    """Update order status with automatic timestamp tracking


    **Order Status Management**

    Update order status with automatic workflow timestamp tracking.

    **Automatic Timing Updates:**
    - RELEASED → `timing.releasedAt`
    - ALLOCATED → `timing.allocatedAt`
    - PICKING → `timing.pickingStartedAt`
    - PICKED → `timing.pickedAt`
    - PACKED → `timing.packedAt`
    - SHIPPED → `timing.shippedAt`

    **Business Workflow:**
    Each status represents a key milestone in order fulfillment with precise timing capture.


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSOutboundOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        order_id=order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSOutboundOrderStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]:
    """Update order status with automatic timestamp tracking


    **Order Status Management**

    Update order status with automatic workflow timestamp tracking.

    **Automatic Timing Updates:**
    - RELEASED → `timing.releasedAt`
    - ALLOCATED → `timing.allocatedAt`
    - PICKING → `timing.pickingStartedAt`
    - PICKED → `timing.pickedAt`
    - PACKED → `timing.packedAt`
    - SHIPPED → `timing.shippedAt`

    **Business Workflow:**
    Each status represents a key milestone in order fulfillment with precise timing capture.


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSOutboundOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSOutboundOrderStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]]:
    """Update order status with automatic timestamp tracking


    **Order Status Management**

    Update order status with automatic workflow timestamp tracking.

    **Automatic Timing Updates:**
    - RELEASED → `timing.releasedAt`
    - ALLOCATED → `timing.allocatedAt`
    - PICKING → `timing.pickingStartedAt`
    - PICKED → `timing.pickedAt`
    - PACKED → `timing.packedAt`
    - SHIPPED → `timing.shippedAt`

    **Business Workflow:**
    Each status represents a key milestone in order fulfillment with precise timing capture.


    Args:
        world_id (str):
        order_id (str):
        body (UpdateWMSOutboundOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSOutboundOrderStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
