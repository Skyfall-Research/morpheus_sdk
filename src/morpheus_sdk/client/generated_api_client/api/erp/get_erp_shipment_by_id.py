from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_shipment_by_id_response_200 import GetERPShipmentByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/shipments/{shipment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPShipmentByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPShipmentByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetERPShipmentByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPShipmentByIdResponse200]]:
    """Get ERP shipment by ID


    Retrieve specific ERP shipment by shipment ID for detailed logistics information access.

    **Core Features**:
    - **Direct Access**: Get shipment by unique shipment identifier
    - **Complete Profile**: Returns full shipment data including line items, tracking, and events
    - **Fast Lookup**: Optimized query using indexed shipmentId field
    - **Logistics Intelligence**: Access comprehensive shipment data for operations

    **Use Cases**:
    - **Shipment Details**: Get complete shipment information for logistics operations
    - **Customer Service**: Resolve shipping inquiries using shipment ID references
    - **Tracking Operations**: Access shipment details for tracking and updates
    - **Integration Support**: Direct API access for external logistics system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPShipmentByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPShipmentByIdResponse200]]:
    """Get ERP shipment by ID


    Retrieve specific ERP shipment by shipment ID for detailed logistics information access.

    **Core Features**:
    - **Direct Access**: Get shipment by unique shipment identifier
    - **Complete Profile**: Returns full shipment data including line items, tracking, and events
    - **Fast Lookup**: Optimized query using indexed shipmentId field
    - **Logistics Intelligence**: Access comprehensive shipment data for operations

    **Use Cases**:
    - **Shipment Details**: Get complete shipment information for logistics operations
    - **Customer Service**: Resolve shipping inquiries using shipment ID references
    - **Tracking Operations**: Access shipment details for tracking and updates
    - **Integration Support**: Direct API access for external logistics system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPShipmentByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        shipment_id=shipment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPShipmentByIdResponse200]]:
    """Get ERP shipment by ID


    Retrieve specific ERP shipment by shipment ID for detailed logistics information access.

    **Core Features**:
    - **Direct Access**: Get shipment by unique shipment identifier
    - **Complete Profile**: Returns full shipment data including line items, tracking, and events
    - **Fast Lookup**: Optimized query using indexed shipmentId field
    - **Logistics Intelligence**: Access comprehensive shipment data for operations

    **Use Cases**:
    - **Shipment Details**: Get complete shipment information for logistics operations
    - **Customer Service**: Resolve shipping inquiries using shipment ID references
    - **Tracking Operations**: Access shipment details for tracking and updates
    - **Integration Support**: Direct API access for external logistics system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPShipmentByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPShipmentByIdResponse200]]:
    """Get ERP shipment by ID


    Retrieve specific ERP shipment by shipment ID for detailed logistics information access.

    **Core Features**:
    - **Direct Access**: Get shipment by unique shipment identifier
    - **Complete Profile**: Returns full shipment data including line items, tracking, and events
    - **Fast Lookup**: Optimized query using indexed shipmentId field
    - **Logistics Intelligence**: Access comprehensive shipment data for operations

    **Use Cases**:
    - **Shipment Details**: Get complete shipment information for logistics operations
    - **Customer Service**: Resolve shipping inquiries using shipment ID references
    - **Tracking Operations**: Access shipment details for tracking and updates
    - **Integration Support**: Direct API access for external logistics system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPShipmentByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
        )
    ).parsed
