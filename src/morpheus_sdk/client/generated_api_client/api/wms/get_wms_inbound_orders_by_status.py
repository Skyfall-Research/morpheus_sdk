import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inbound_orders_by_status_priority_item import GetWMSInboundOrdersByStatusPriorityItem
from ...models.get_wms_inbound_orders_by_status_response_200 import GetWMSInboundOrdersByStatusResponse200
from ...models.get_wms_inbound_orders_by_status_status_item import GetWMSInboundOrdersByStatusStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: list[GetWMSInboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    priority: Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = []
    for status_item_data in status:
        status_item = status_item_data.value
        json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

    params["vendorId"] = vendor_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    json_priority: Union[Unset, list[str]] = UNSET
    if not isinstance(priority, Unset):
        json_priority = []
        for priority_item_data in priority:
            priority_item = priority_item_data.value
            json_priority.append(priority_item)

    params["priority"] = json_priority

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inbound-orders/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInboundOrdersByStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]:
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
    status: list[GetWMSInboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    priority: Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]:
    """Get inbound orders by status


    ## Get WMS Inbound Orders by Status

    Retrieve filtered list of inbound orders by operational status with comprehensive filtering options
    for warehouse management and receiving coordination.

    ### Features
    - **Multi-Status Filtering**: Support for multiple order statuses simultaneously
    - **Warehouse Scoping**: Filter orders by specific warehouse facilities
    - **Vendor Analysis**: Filter by vendor for supplier performance tracking
    - **Date Range Analysis**: Historical and scheduled delivery date filtering
    - **Priority Management**: Filter by priority levels for operational focus
    - **Performance Optimization**: Sorted results for efficient receiving workflows

    ### Business Logic
    - Status array parameter enables multi-status queries for operational dashboards
    - Warehouse filtering supports multi-facility operations
    - Vendor filtering enables supplier performance analysis and coordination
    - Date range filtering uses expectedDeliveryDate for scheduling and planning
    - Priority filtering supports operational prioritization of receiving activities
    - Results sorted by expected delivery date and priority for workflow optimization

    ### Query Parameters
    - **status**: Required - Order status array (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **vendorId**: Optional - Filter by vendor for supplier-specific analysis
    - **dateStart**: Optional - Start date for delivery date filtering
    - **dateEnd**: Optional - End date for delivery date filtering
    - **priority**: Optional - Priority level filtering for operational focus

    ### Use Cases
    - **Receiving Dashboard**: View orders by status for daily receiving operations
    - **Vendor Management**: Track orders by vendor for supplier coordination
    - **Capacity Planning**: Analyze incoming orders by date range for resource planning
    - **Priority Operations**: Focus on high-priority orders for critical receiving
    - **Status Monitoring**: Track order progression through receiving lifecycle


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSInboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        priority (Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        vendor_id=vendor_id,
        date_start=date_start,
        date_end=date_end,
        priority=priority,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSInboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    priority: Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]:
    """Get inbound orders by status


    ## Get WMS Inbound Orders by Status

    Retrieve filtered list of inbound orders by operational status with comprehensive filtering options
    for warehouse management and receiving coordination.

    ### Features
    - **Multi-Status Filtering**: Support for multiple order statuses simultaneously
    - **Warehouse Scoping**: Filter orders by specific warehouse facilities
    - **Vendor Analysis**: Filter by vendor for supplier performance tracking
    - **Date Range Analysis**: Historical and scheduled delivery date filtering
    - **Priority Management**: Filter by priority levels for operational focus
    - **Performance Optimization**: Sorted results for efficient receiving workflows

    ### Business Logic
    - Status array parameter enables multi-status queries for operational dashboards
    - Warehouse filtering supports multi-facility operations
    - Vendor filtering enables supplier performance analysis and coordination
    - Date range filtering uses expectedDeliveryDate for scheduling and planning
    - Priority filtering supports operational prioritization of receiving activities
    - Results sorted by expected delivery date and priority for workflow optimization

    ### Query Parameters
    - **status**: Required - Order status array (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **vendorId**: Optional - Filter by vendor for supplier-specific analysis
    - **dateStart**: Optional - Start date for delivery date filtering
    - **dateEnd**: Optional - End date for delivery date filtering
    - **priority**: Optional - Priority level filtering for operational focus

    ### Use Cases
    - **Receiving Dashboard**: View orders by status for daily receiving operations
    - **Vendor Management**: Track orders by vendor for supplier coordination
    - **Capacity Planning**: Analyze incoming orders by date range for resource planning
    - **Priority Operations**: Focus on high-priority orders for critical receiving
    - **Status Monitoring**: Track order progression through receiving lifecycle


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSInboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        priority (Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        vendor_id=vendor_id,
        date_start=date_start,
        date_end=date_end,
        priority=priority,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSInboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    priority: Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]:
    """Get inbound orders by status


    ## Get WMS Inbound Orders by Status

    Retrieve filtered list of inbound orders by operational status with comprehensive filtering options
    for warehouse management and receiving coordination.

    ### Features
    - **Multi-Status Filtering**: Support for multiple order statuses simultaneously
    - **Warehouse Scoping**: Filter orders by specific warehouse facilities
    - **Vendor Analysis**: Filter by vendor for supplier performance tracking
    - **Date Range Analysis**: Historical and scheduled delivery date filtering
    - **Priority Management**: Filter by priority levels for operational focus
    - **Performance Optimization**: Sorted results for efficient receiving workflows

    ### Business Logic
    - Status array parameter enables multi-status queries for operational dashboards
    - Warehouse filtering supports multi-facility operations
    - Vendor filtering enables supplier performance analysis and coordination
    - Date range filtering uses expectedDeliveryDate for scheduling and planning
    - Priority filtering supports operational prioritization of receiving activities
    - Results sorted by expected delivery date and priority for workflow optimization

    ### Query Parameters
    - **status**: Required - Order status array (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **vendorId**: Optional - Filter by vendor for supplier-specific analysis
    - **dateStart**: Optional - Start date for delivery date filtering
    - **dateEnd**: Optional - End date for delivery date filtering
    - **priority**: Optional - Priority level filtering for operational focus

    ### Use Cases
    - **Receiving Dashboard**: View orders by status for daily receiving operations
    - **Vendor Management**: Track orders by vendor for supplier coordination
    - **Capacity Planning**: Analyze incoming orders by date range for resource planning
    - **Priority Operations**: Focus on high-priority orders for critical receiving
    - **Status Monitoring**: Track order progression through receiving lifecycle


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSInboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        priority (Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        vendor_id=vendor_id,
        date_start=date_start,
        date_end=date_end,
        priority=priority,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSInboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    priority: Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]]:
    """Get inbound orders by status


    ## Get WMS Inbound Orders by Status

    Retrieve filtered list of inbound orders by operational status with comprehensive filtering options
    for warehouse management and receiving coordination.

    ### Features
    - **Multi-Status Filtering**: Support for multiple order statuses simultaneously
    - **Warehouse Scoping**: Filter orders by specific warehouse facilities
    - **Vendor Analysis**: Filter by vendor for supplier performance tracking
    - **Date Range Analysis**: Historical and scheduled delivery date filtering
    - **Priority Management**: Filter by priority levels for operational focus
    - **Performance Optimization**: Sorted results for efficient receiving workflows

    ### Business Logic
    - Status array parameter enables multi-status queries for operational dashboards
    - Warehouse filtering supports multi-facility operations
    - Vendor filtering enables supplier performance analysis and coordination
    - Date range filtering uses expectedDeliveryDate for scheduling and planning
    - Priority filtering supports operational prioritization of receiving activities
    - Results sorted by expected delivery date and priority for workflow optimization

    ### Query Parameters
    - **status**: Required - Order status array (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **vendorId**: Optional - Filter by vendor for supplier-specific analysis
    - **dateStart**: Optional - Start date for delivery date filtering
    - **dateEnd**: Optional - End date for delivery date filtering
    - **priority**: Optional - Priority level filtering for operational focus

    ### Use Cases
    - **Receiving Dashboard**: View orders by status for daily receiving operations
    - **Vendor Management**: Track orders by vendor for supplier coordination
    - **Capacity Planning**: Analyze incoming orders by date range for resource planning
    - **Priority Operations**: Focus on high-priority orders for critical receiving
    - **Status Monitoring**: Track order progression through receiving lifecycle


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSInboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        priority (Union[Unset, list[GetWMSInboundOrdersByStatusPriorityItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrdersByStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            vendor_id=vendor_id,
            date_start=date_start,
            date_end=date_end,
            priority=priority,
        )
    ).parsed
