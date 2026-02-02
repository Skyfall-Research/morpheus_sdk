from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_outbound_shipment_body import CreateWMSOutboundShipmentBody
from ...models.create_wms_outbound_shipment_response_201 import CreateWMSOutboundShipmentResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSOutboundShipmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/shipments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSOutboundShipmentResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]:
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
    body: CreateWMSOutboundShipmentBody,
) -> Response[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]:
    """Create new outbound shipment


    **Create New Outbound Shipment**

    Creates a new outbound shipment for carrier dispatch with comprehensive line item and address
    management.

    **Key Features:**
    - Multi-line shipment support with order references
    - Carrier integration with SCAC codes and service levels
    - Address validation and routing
    - Status workflow tracking from creation to delivery
    - Document management and tracking event history

    **Validation Requirements:**
    - warehouseId, lines array, and toAddress are required
    - Unique shipmentId generation via service identifier
    - Proper carrier and service level specification

    **Status Workflow:**
    CREATED → MANIFESTED → LOADING → LOADED → SHIPPED → IN_TRANSIT → DELIVERED


    Args:
        world_id (str):
        body (CreateWMSOutboundShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]
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
    body: CreateWMSOutboundShipmentBody,
) -> Optional[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]:
    """Create new outbound shipment


    **Create New Outbound Shipment**

    Creates a new outbound shipment for carrier dispatch with comprehensive line item and address
    management.

    **Key Features:**
    - Multi-line shipment support with order references
    - Carrier integration with SCAC codes and service levels
    - Address validation and routing
    - Status workflow tracking from creation to delivery
    - Document management and tracking event history

    **Validation Requirements:**
    - warehouseId, lines array, and toAddress are required
    - Unique shipmentId generation via service identifier
    - Proper carrier and service level specification

    **Status Workflow:**
    CREATED → MANIFESTED → LOADING → LOADED → SHIPPED → IN_TRANSIT → DELIVERED


    Args:
        world_id (str):
        body (CreateWMSOutboundShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]
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
    body: CreateWMSOutboundShipmentBody,
) -> Response[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]:
    """Create new outbound shipment


    **Create New Outbound Shipment**

    Creates a new outbound shipment for carrier dispatch with comprehensive line item and address
    management.

    **Key Features:**
    - Multi-line shipment support with order references
    - Carrier integration with SCAC codes and service levels
    - Address validation and routing
    - Status workflow tracking from creation to delivery
    - Document management and tracking event history

    **Validation Requirements:**
    - warehouseId, lines array, and toAddress are required
    - Unique shipmentId generation via service identifier
    - Proper carrier and service level specification

    **Status Workflow:**
    CREATED → MANIFESTED → LOADING → LOADED → SHIPPED → IN_TRANSIT → DELIVERED


    Args:
        world_id (str):
        body (CreateWMSOutboundShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]
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
    body: CreateWMSOutboundShipmentBody,
) -> Optional[Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]]:
    """Create new outbound shipment


    **Create New Outbound Shipment**

    Creates a new outbound shipment for carrier dispatch with comprehensive line item and address
    management.

    **Key Features:**
    - Multi-line shipment support with order references
    - Carrier integration with SCAC codes and service levels
    - Address validation and routing
    - Status workflow tracking from creation to delivery
    - Document management and tracking event history

    **Validation Requirements:**
    - warehouseId, lines array, and toAddress are required
    - Unique shipmentId generation via service identifier
    - Proper carrier and service level specification

    **Status Workflow:**
    CREATED → MANIFESTED → LOADING → LOADED → SHIPPED → IN_TRANSIT → DELIVERED


    Args:
        world_id (str):
        body (CreateWMSOutboundShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSOutboundShipmentResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
