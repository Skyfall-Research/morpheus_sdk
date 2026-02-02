import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inbound_orders_by_vendor_response_200 import GetWMSInboundOrdersByVendorResponse200
from ...models.get_wms_inbound_orders_by_vendor_status_item import GetWMSInboundOrdersByVendorStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    vendor_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inbound-orders/vendor/{vendor_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInboundOrdersByVendorResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    vendor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]:
    """Get orders by vendor


    ## Get WMS Inbound Orders by Vendor

    Retrieve inbound orders filtered by specific vendor for supplier relationship management and vendor
    performance analysis.

    ### Features
    - **Vendor-Specific Analysis**: Complete view of orders from specific vendors
    - **Multi-Filter Support**: Warehouse, status, and date range filtering
    - **Performance Tracking**: Vendor-specific order history and patterns
    - **Supplier Coordination**: Support vendor communication and coordination
    - **Historical Analysis**: Date-based filtering for vendor performance trends

    ### Business Logic
    - vendorId must reference orders with matching vendor.vendorId field
    - Supports filtering by warehouse for multi-facility vendor analysis
    - Status filtering enables analysis of vendor orders by operational stage
    - Date range filtering uses expectedDeliveryDate for delivery performance analysis
    - Results sorted by expected delivery date (descending) for chronological view

    ### Path Parameters
    - **vendorId**: Required - Unique identifier for the vendor

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **status**: Optional - Filter by order status for operational analysis
    - **dateStart**: Optional - Start date for vendor order analysis
    - **dateEnd**: Optional - End date for vendor order analysis

    ### Use Cases
    - **Vendor Management**: Review all orders from specific vendor for relationship management
    - **Performance Analysis**: Analyze vendor delivery patterns and reliability
    - **Supplier Communication**: Access vendor-specific order details during coordination
    - **Contract Management**: Review vendor order history for contract negotiations
    - **Quality Tracking**: Monitor vendor order quality and delivery performance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        vendor_id (str):  Example: VND-SWIFT-001.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        status (Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        vendor_id=vendor_id,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    vendor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]:
    """Get orders by vendor


    ## Get WMS Inbound Orders by Vendor

    Retrieve inbound orders filtered by specific vendor for supplier relationship management and vendor
    performance analysis.

    ### Features
    - **Vendor-Specific Analysis**: Complete view of orders from specific vendors
    - **Multi-Filter Support**: Warehouse, status, and date range filtering
    - **Performance Tracking**: Vendor-specific order history and patterns
    - **Supplier Coordination**: Support vendor communication and coordination
    - **Historical Analysis**: Date-based filtering for vendor performance trends

    ### Business Logic
    - vendorId must reference orders with matching vendor.vendorId field
    - Supports filtering by warehouse for multi-facility vendor analysis
    - Status filtering enables analysis of vendor orders by operational stage
    - Date range filtering uses expectedDeliveryDate for delivery performance analysis
    - Results sorted by expected delivery date (descending) for chronological view

    ### Path Parameters
    - **vendorId**: Required - Unique identifier for the vendor

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **status**: Optional - Filter by order status for operational analysis
    - **dateStart**: Optional - Start date for vendor order analysis
    - **dateEnd**: Optional - End date for vendor order analysis

    ### Use Cases
    - **Vendor Management**: Review all orders from specific vendor for relationship management
    - **Performance Analysis**: Analyze vendor delivery patterns and reliability
    - **Supplier Communication**: Access vendor-specific order details during coordination
    - **Contract Management**: Review vendor order history for contract negotiations
    - **Quality Tracking**: Monitor vendor order quality and delivery performance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        vendor_id (str):  Example: VND-SWIFT-001.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        status (Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        vendor_id=vendor_id,
        client=client,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    vendor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]:
    """Get orders by vendor


    ## Get WMS Inbound Orders by Vendor

    Retrieve inbound orders filtered by specific vendor for supplier relationship management and vendor
    performance analysis.

    ### Features
    - **Vendor-Specific Analysis**: Complete view of orders from specific vendors
    - **Multi-Filter Support**: Warehouse, status, and date range filtering
    - **Performance Tracking**: Vendor-specific order history and patterns
    - **Supplier Coordination**: Support vendor communication and coordination
    - **Historical Analysis**: Date-based filtering for vendor performance trends

    ### Business Logic
    - vendorId must reference orders with matching vendor.vendorId field
    - Supports filtering by warehouse for multi-facility vendor analysis
    - Status filtering enables analysis of vendor orders by operational stage
    - Date range filtering uses expectedDeliveryDate for delivery performance analysis
    - Results sorted by expected delivery date (descending) for chronological view

    ### Path Parameters
    - **vendorId**: Required - Unique identifier for the vendor

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **status**: Optional - Filter by order status for operational analysis
    - **dateStart**: Optional - Start date for vendor order analysis
    - **dateEnd**: Optional - End date for vendor order analysis

    ### Use Cases
    - **Vendor Management**: Review all orders from specific vendor for relationship management
    - **Performance Analysis**: Analyze vendor delivery patterns and reliability
    - **Supplier Communication**: Access vendor-specific order details during coordination
    - **Contract Management**: Review vendor order history for contract negotiations
    - **Quality Tracking**: Monitor vendor order quality and delivery performance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        vendor_id (str):  Example: VND-SWIFT-001.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        status (Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        vendor_id=vendor_id,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    vendor_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]]:
    """Get orders by vendor


    ## Get WMS Inbound Orders by Vendor

    Retrieve inbound orders filtered by specific vendor for supplier relationship management and vendor
    performance analysis.

    ### Features
    - **Vendor-Specific Analysis**: Complete view of orders from specific vendors
    - **Multi-Filter Support**: Warehouse, status, and date range filtering
    - **Performance Tracking**: Vendor-specific order history and patterns
    - **Supplier Coordination**: Support vendor communication and coordination
    - **Historical Analysis**: Date-based filtering for vendor performance trends

    ### Business Logic
    - vendorId must reference orders with matching vendor.vendorId field
    - Supports filtering by warehouse for multi-facility vendor analysis
    - Status filtering enables analysis of vendor orders by operational stage
    - Date range filtering uses expectedDeliveryDate for delivery performance analysis
    - Results sorted by expected delivery date (descending) for chronological view

    ### Path Parameters
    - **vendorId**: Required - Unique identifier for the vendor

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **status**: Optional - Filter by order status for operational analysis
    - **dateStart**: Optional - Start date for vendor order analysis
    - **dateEnd**: Optional - End date for vendor order analysis

    ### Use Cases
    - **Vendor Management**: Review all orders from specific vendor for relationship management
    - **Performance Analysis**: Analyze vendor delivery patterns and reliability
    - **Supplier Communication**: Access vendor-specific order details during coordination
    - **Contract Management**: Review vendor order history for contract negotiations
    - **Quality Tracking**: Monitor vendor order quality and delivery performance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        vendor_id (str):  Example: VND-SWIFT-001.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        status (Union[Unset, list[GetWMSInboundOrdersByVendorStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrdersByVendorResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            vendor_id=vendor_id,
            client=client,
            warehouse_id=warehouse_id,
            status=status,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
