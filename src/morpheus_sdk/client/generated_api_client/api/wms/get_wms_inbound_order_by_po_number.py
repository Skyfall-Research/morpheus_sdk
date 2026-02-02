from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inbound_order_by_po_number_response_200 import GetWMSInboundOrderByPoNumberResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    po_number: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inbound-orders/po/{po_number}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInboundOrderByPoNumberResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    po_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]:
    """Get inbound order by PO number


    ## Get WMS Inbound Order by PO Number

    Retrieve inbound order information using purchase order number for ERP integration and vendor
    coordination.

    ### Features
    - **ERP Integration**: Direct lookup by purchase order number from ERP systems
    - **Vendor Communication**: Quick access to orders during vendor coordination
    - **Receiving Verification**: Verify incoming deliveries against purchase orders
    - **Cross-Reference Lookup**: Alternative lookup method for operational flexibility
    - **Real-Time Data**: Current order status and receiving progress information

    ### Business Logic
    - poNumber must reference an existing purchase order within the world
    - Returns complete order information including vendor details and line items
    - Supports ERP integration workflows and vendor communication processes
    - Enables receiving verification against purchase order documentation
    - Provides alternative lookup method when order ID is not available

    ### Path Parameters
    - **poNumber**: Required - Purchase order number from ERP system

    ### Use Cases
    - **ERP Integration**: Lookup orders during automated ERP synchronization
    - **Vendor Coordination**: Verify order details during vendor communication
    - **Receiving Verification**: Confirm incoming deliveries against purchase orders
    - **Customer Service**: Assist with order inquiries using purchase order references
    - **Cross-System Lookup**: Bridge between ERP and WMS systems using common identifiers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        po_number (str):  Example: PO-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        po_number=po_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    po_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]:
    """Get inbound order by PO number


    ## Get WMS Inbound Order by PO Number

    Retrieve inbound order information using purchase order number for ERP integration and vendor
    coordination.

    ### Features
    - **ERP Integration**: Direct lookup by purchase order number from ERP systems
    - **Vendor Communication**: Quick access to orders during vendor coordination
    - **Receiving Verification**: Verify incoming deliveries against purchase orders
    - **Cross-Reference Lookup**: Alternative lookup method for operational flexibility
    - **Real-Time Data**: Current order status and receiving progress information

    ### Business Logic
    - poNumber must reference an existing purchase order within the world
    - Returns complete order information including vendor details and line items
    - Supports ERP integration workflows and vendor communication processes
    - Enables receiving verification against purchase order documentation
    - Provides alternative lookup method when order ID is not available

    ### Path Parameters
    - **poNumber**: Required - Purchase order number from ERP system

    ### Use Cases
    - **ERP Integration**: Lookup orders during automated ERP synchronization
    - **Vendor Coordination**: Verify order details during vendor communication
    - **Receiving Verification**: Confirm incoming deliveries against purchase orders
    - **Customer Service**: Assist with order inquiries using purchase order references
    - **Cross-System Lookup**: Bridge between ERP and WMS systems using common identifiers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        po_number (str):  Example: PO-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        po_number=po_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    po_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]:
    """Get inbound order by PO number


    ## Get WMS Inbound Order by PO Number

    Retrieve inbound order information using purchase order number for ERP integration and vendor
    coordination.

    ### Features
    - **ERP Integration**: Direct lookup by purchase order number from ERP systems
    - **Vendor Communication**: Quick access to orders during vendor coordination
    - **Receiving Verification**: Verify incoming deliveries against purchase orders
    - **Cross-Reference Lookup**: Alternative lookup method for operational flexibility
    - **Real-Time Data**: Current order status and receiving progress information

    ### Business Logic
    - poNumber must reference an existing purchase order within the world
    - Returns complete order information including vendor details and line items
    - Supports ERP integration workflows and vendor communication processes
    - Enables receiving verification against purchase order documentation
    - Provides alternative lookup method when order ID is not available

    ### Path Parameters
    - **poNumber**: Required - Purchase order number from ERP system

    ### Use Cases
    - **ERP Integration**: Lookup orders during automated ERP synchronization
    - **Vendor Coordination**: Verify order details during vendor communication
    - **Receiving Verification**: Confirm incoming deliveries against purchase orders
    - **Customer Service**: Assist with order inquiries using purchase order references
    - **Cross-System Lookup**: Bridge between ERP and WMS systems using common identifiers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        po_number (str):  Example: PO-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        po_number=po_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    po_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]]:
    """Get inbound order by PO number


    ## Get WMS Inbound Order by PO Number

    Retrieve inbound order information using purchase order number for ERP integration and vendor
    coordination.

    ### Features
    - **ERP Integration**: Direct lookup by purchase order number from ERP systems
    - **Vendor Communication**: Quick access to orders during vendor coordination
    - **Receiving Verification**: Verify incoming deliveries against purchase orders
    - **Cross-Reference Lookup**: Alternative lookup method for operational flexibility
    - **Real-Time Data**: Current order status and receiving progress information

    ### Business Logic
    - poNumber must reference an existing purchase order within the world
    - Returns complete order information including vendor details and line items
    - Supports ERP integration workflows and vendor communication processes
    - Enables receiving verification against purchase order documentation
    - Provides alternative lookup method when order ID is not available

    ### Path Parameters
    - **poNumber**: Required - Purchase order number from ERP system

    ### Use Cases
    - **ERP Integration**: Lookup orders during automated ERP synchronization
    - **Vendor Coordination**: Verify order details during vendor communication
    - **Receiving Verification**: Confirm incoming deliveries against purchase orders
    - **Customer Service**: Assist with order inquiries using purchase order references
    - **Cross-System Lookup**: Bridge between ERP and WMS systems using common identifiers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        po_number (str):  Example: PO-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrderByPoNumberResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            po_number=po_number,
            client=client,
        )
    ).parsed
