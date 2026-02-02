from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.patch_wms_inbound_order_body import PatchWMSInboundOrderBody
from ...models.patch_wms_inbound_order_response_200 import PatchWMSInboundOrderResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    inbound_order_id: str,
    *,
    body: PatchWMSInboundOrderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/wms/inbound-orders/{inbound_order_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]:
    if response.status_code == 200:
        response_200 = PatchWMSInboundOrderResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInboundOrderBody,
) -> Response[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]:
    r"""Partially update inbound order


    ## Patch WMS Inbound Order

    Partially update an inbound order with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **orderStatus**: Update the order status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **priority**: Update the order priority (RUSH, URGENT, NORMAL, STANDARD)
    - **dates**: Update date fields like expectedArrival

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports dot notation for nested fields (e.g., \"dates.expectedArrival\")

    ### Use Cases
    - Update order status as it progresses through receiving workflow
    - Change priority based on business needs
    - Update expected arrival dates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (PatchWMSInboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInboundOrderBody,
) -> Optional[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]:
    r"""Partially update inbound order


    ## Patch WMS Inbound Order

    Partially update an inbound order with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **orderStatus**: Update the order status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **priority**: Update the order priority (RUSH, URGENT, NORMAL, STANDARD)
    - **dates**: Update date fields like expectedArrival

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports dot notation for nested fields (e.g., \"dates.expectedArrival\")

    ### Use Cases
    - Update order status as it progresses through receiving workflow
    - Change priority based on business needs
    - Update expected arrival dates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (PatchWMSInboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PatchWMSInboundOrderResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInboundOrderBody,
) -> Response[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]:
    r"""Partially update inbound order


    ## Patch WMS Inbound Order

    Partially update an inbound order with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **orderStatus**: Update the order status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **priority**: Update the order priority (RUSH, URGENT, NORMAL, STANDARD)
    - **dates**: Update date fields like expectedArrival

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports dot notation for nested fields (e.g., \"dates.expectedArrival\")

    ### Use Cases
    - Update order status as it progresses through receiving workflow
    - Change priority based on business needs
    - Update expected arrival dates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (PatchWMSInboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInboundOrderBody,
) -> Optional[Union[ErrorResponse, PatchWMSInboundOrderResponse200]]:
    r"""Partially update inbound order


    ## Patch WMS Inbound Order

    Partially update an inbound order with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **orderStatus**: Update the order status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **priority**: Update the order priority (RUSH, URGENT, NORMAL, STANDARD)
    - **dates**: Update date fields like expectedArrival

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports dot notation for nested fields (e.g., \"dates.expectedArrival\")

    ### Use Cases
    - Update order status as it progresses through receiving workflow
    - Change priority based on business needs
    - Update expected arrival dates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (PatchWMSInboundOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PatchWMSInboundOrderResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            inbound_order_id=inbound_order_id,
            client=client,
            body=body,
        )
    ).parsed
