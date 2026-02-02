from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_inbound_order_body import CreateWMSInboundOrderBody
from ...models.create_wms_inbound_order_response_201 import CreateWMSInboundOrderResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSInboundOrderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/inbound-orders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSInboundOrderResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]:
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
    body: CreateWMSInboundOrderBody,
) -> Response[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]:
    """Create new inbound order


    ## Create WMS Inbound Order

    Create a new inbound order for receiving inventory into the warehouse, supporting purchase orders,
    transfers, returns, and sample deliveries.

    ### Features
    - **Order Type Support**: PO, RETURN, TRANSFER, SAMPLE order types
    - **Vendor Management**: Complete vendor information and contact details
    - **Line-Item Tracking**: Detailed product lines with quantities and specifications
    - **Status Lifecycle**: Comprehensive order status from EXPECTED to CLOSED
    - **Appointment Integration**: Optional appointment scheduling for receiving coordination
    - **Batch Tracking**: Lot number and expiration date management for compliance

    ### Business Logic
    - Validates required fields: warehouseId and order lines are mandatory
    - Prevents duplicate PO numbers within the same warehouse
    - Auto-generates unique inboundOrderId using WMS service prefix
    - Initializes order status to EXPECTED for incoming inventory management
    - Calculates total expected lines and quantities from line items
    - Establishes audit trail for all subsequent modifications and receiving activities

    ### Use Cases
    - **Purchase Order Processing**: Create inbound orders from ERP purchase orders
    - **Transfer Management**: Handle warehouse-to-warehouse inventory transfers
    - **Return Processing**: Manage returned merchandise and defective product receipts
    - **Sample Tracking**: Process product samples and promotional materials
    - **Vendor Coordination**: Coordinate receiving schedules with supplier deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInboundOrderBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'poNumber': 'PO-2024-001234', 'asnNumber': 'ASN-
            VND001-20241127', 'vendor': {'vendorId': 'VND-SWIFT-001', 'vendorName': 'Swift
            Manufacturing Co.', 'contactEmail': 'receiving@swift-mfg.com', 'contactPhone':
            '+1-555-0123'}, 'orderType': 'PO', 'dates': {'expectedArrival': '2024-11-28T10:00:00Z'},
            'appointmentId': 'tms_appointment_674565c1234567890abcdef', 'totals': {'pallets': 5,
            'cases': 120, 'units': 2400, 'expectedLines': 8}, 'lines': [{'lineNumber': 1, 'productId':
            'PROD-WIDGET-001', 'sku': 'SKU-WDG-BLU-SM', 'productName': 'Blue Widget Small',
            'expectedQuantity': 300, 'uom': 'EA', 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}], 'receivingNotes': 'Handle with care - fragile items. Check lot
            numbers carefully.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]
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
    body: CreateWMSInboundOrderBody,
) -> Optional[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]:
    """Create new inbound order


    ## Create WMS Inbound Order

    Create a new inbound order for receiving inventory into the warehouse, supporting purchase orders,
    transfers, returns, and sample deliveries.

    ### Features
    - **Order Type Support**: PO, RETURN, TRANSFER, SAMPLE order types
    - **Vendor Management**: Complete vendor information and contact details
    - **Line-Item Tracking**: Detailed product lines with quantities and specifications
    - **Status Lifecycle**: Comprehensive order status from EXPECTED to CLOSED
    - **Appointment Integration**: Optional appointment scheduling for receiving coordination
    - **Batch Tracking**: Lot number and expiration date management for compliance

    ### Business Logic
    - Validates required fields: warehouseId and order lines are mandatory
    - Prevents duplicate PO numbers within the same warehouse
    - Auto-generates unique inboundOrderId using WMS service prefix
    - Initializes order status to EXPECTED for incoming inventory management
    - Calculates total expected lines and quantities from line items
    - Establishes audit trail for all subsequent modifications and receiving activities

    ### Use Cases
    - **Purchase Order Processing**: Create inbound orders from ERP purchase orders
    - **Transfer Management**: Handle warehouse-to-warehouse inventory transfers
    - **Return Processing**: Manage returned merchandise and defective product receipts
    - **Sample Tracking**: Process product samples and promotional materials
    - **Vendor Coordination**: Coordinate receiving schedules with supplier deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInboundOrderBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'poNumber': 'PO-2024-001234', 'asnNumber': 'ASN-
            VND001-20241127', 'vendor': {'vendorId': 'VND-SWIFT-001', 'vendorName': 'Swift
            Manufacturing Co.', 'contactEmail': 'receiving@swift-mfg.com', 'contactPhone':
            '+1-555-0123'}, 'orderType': 'PO', 'dates': {'expectedArrival': '2024-11-28T10:00:00Z'},
            'appointmentId': 'tms_appointment_674565c1234567890abcdef', 'totals': {'pallets': 5,
            'cases': 120, 'units': 2400, 'expectedLines': 8}, 'lines': [{'lineNumber': 1, 'productId':
            'PROD-WIDGET-001', 'sku': 'SKU-WDG-BLU-SM', 'productName': 'Blue Widget Small',
            'expectedQuantity': 300, 'uom': 'EA', 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}], 'receivingNotes': 'Handle with care - fragile items. Check lot
            numbers carefully.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSInboundOrderResponse201, ErrorResponse]
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
    body: CreateWMSInboundOrderBody,
) -> Response[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]:
    """Create new inbound order


    ## Create WMS Inbound Order

    Create a new inbound order for receiving inventory into the warehouse, supporting purchase orders,
    transfers, returns, and sample deliveries.

    ### Features
    - **Order Type Support**: PO, RETURN, TRANSFER, SAMPLE order types
    - **Vendor Management**: Complete vendor information and contact details
    - **Line-Item Tracking**: Detailed product lines with quantities and specifications
    - **Status Lifecycle**: Comprehensive order status from EXPECTED to CLOSED
    - **Appointment Integration**: Optional appointment scheduling for receiving coordination
    - **Batch Tracking**: Lot number and expiration date management for compliance

    ### Business Logic
    - Validates required fields: warehouseId and order lines are mandatory
    - Prevents duplicate PO numbers within the same warehouse
    - Auto-generates unique inboundOrderId using WMS service prefix
    - Initializes order status to EXPECTED for incoming inventory management
    - Calculates total expected lines and quantities from line items
    - Establishes audit trail for all subsequent modifications and receiving activities

    ### Use Cases
    - **Purchase Order Processing**: Create inbound orders from ERP purchase orders
    - **Transfer Management**: Handle warehouse-to-warehouse inventory transfers
    - **Return Processing**: Manage returned merchandise and defective product receipts
    - **Sample Tracking**: Process product samples and promotional materials
    - **Vendor Coordination**: Coordinate receiving schedules with supplier deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInboundOrderBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'poNumber': 'PO-2024-001234', 'asnNumber': 'ASN-
            VND001-20241127', 'vendor': {'vendorId': 'VND-SWIFT-001', 'vendorName': 'Swift
            Manufacturing Co.', 'contactEmail': 'receiving@swift-mfg.com', 'contactPhone':
            '+1-555-0123'}, 'orderType': 'PO', 'dates': {'expectedArrival': '2024-11-28T10:00:00Z'},
            'appointmentId': 'tms_appointment_674565c1234567890abcdef', 'totals': {'pallets': 5,
            'cases': 120, 'units': 2400, 'expectedLines': 8}, 'lines': [{'lineNumber': 1, 'productId':
            'PROD-WIDGET-001', 'sku': 'SKU-WDG-BLU-SM', 'productName': 'Blue Widget Small',
            'expectedQuantity': 300, 'uom': 'EA', 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}], 'receivingNotes': 'Handle with care - fragile items. Check lot
            numbers carefully.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]
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
    body: CreateWMSInboundOrderBody,
) -> Optional[Union[CreateWMSInboundOrderResponse201, ErrorResponse]]:
    """Create new inbound order


    ## Create WMS Inbound Order

    Create a new inbound order for receiving inventory into the warehouse, supporting purchase orders,
    transfers, returns, and sample deliveries.

    ### Features
    - **Order Type Support**: PO, RETURN, TRANSFER, SAMPLE order types
    - **Vendor Management**: Complete vendor information and contact details
    - **Line-Item Tracking**: Detailed product lines with quantities and specifications
    - **Status Lifecycle**: Comprehensive order status from EXPECTED to CLOSED
    - **Appointment Integration**: Optional appointment scheduling for receiving coordination
    - **Batch Tracking**: Lot number and expiration date management for compliance

    ### Business Logic
    - Validates required fields: warehouseId and order lines are mandatory
    - Prevents duplicate PO numbers within the same warehouse
    - Auto-generates unique inboundOrderId using WMS service prefix
    - Initializes order status to EXPECTED for incoming inventory management
    - Calculates total expected lines and quantities from line items
    - Establishes audit trail for all subsequent modifications and receiving activities

    ### Use Cases
    - **Purchase Order Processing**: Create inbound orders from ERP purchase orders
    - **Transfer Management**: Handle warehouse-to-warehouse inventory transfers
    - **Return Processing**: Manage returned merchandise and defective product receipts
    - **Sample Tracking**: Process product samples and promotional materials
    - **Vendor Coordination**: Coordinate receiving schedules with supplier deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInboundOrderBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'poNumber': 'PO-2024-001234', 'asnNumber': 'ASN-
            VND001-20241127', 'vendor': {'vendorId': 'VND-SWIFT-001', 'vendorName': 'Swift
            Manufacturing Co.', 'contactEmail': 'receiving@swift-mfg.com', 'contactPhone':
            '+1-555-0123'}, 'orderType': 'PO', 'dates': {'expectedArrival': '2024-11-28T10:00:00Z'},
            'appointmentId': 'tms_appointment_674565c1234567890abcdef', 'totals': {'pallets': 5,
            'cases': 120, 'units': 2400, 'expectedLines': 8}, 'lines': [{'lineNumber': 1, 'productId':
            'PROD-WIDGET-001', 'sku': 'SKU-WDG-BLU-SM', 'productName': 'Blue Widget Small',
            'expectedQuantity': 300, 'uom': 'EA', 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}], 'receivingNotes': 'Handle with care - fragile items. Check lot
            numbers carefully.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSInboundOrderResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
