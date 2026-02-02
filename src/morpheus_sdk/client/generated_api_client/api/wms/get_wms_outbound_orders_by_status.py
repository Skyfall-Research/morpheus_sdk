import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_outbound_orders_by_status_order_type_item import GetWMSOutboundOrdersByStatusOrderTypeItem
from ...models.get_wms_outbound_orders_by_status_priority_item import GetWMSOutboundOrdersByStatusPriorityItem
from ...models.get_wms_outbound_orders_by_status_response_200 import GetWMSOutboundOrdersByStatusResponse200
from ...models.get_wms_outbound_orders_by_status_status_item import GetWMSOutboundOrdersByStatusStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: list[GetWMSOutboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    order_type: Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]] = UNSET,
    priority: Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = []
    for status_item_data in status:
        status_item = status_item_data.value
        json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

    params["customerId"] = customer_id

    json_order_type: Union[Unset, list[str]] = UNSET
    if not isinstance(order_type, Unset):
        json_order_type = []
        for order_type_item_data in order_type:
            order_type_item = order_type_item_data.value
            json_order_type.append(order_type_item)

    params["orderType"] = json_order_type

    json_priority: Union[Unset, list[str]] = UNSET
    if not isinstance(priority, Unset):
        json_priority = []
        for priority_item_data in priority:
            priority_item = priority_item_data.value
            json_priority.append(priority_item)

    params["priority"] = json_priority

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/outbound-orders/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSOutboundOrdersByStatusResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSOutboundOrdersByStatusResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSOutboundOrdersByStatusResponse200]:
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
    status: list[GetWMSOutboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    order_type: Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]] = UNSET,
    priority: Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Response[GetWMSOutboundOrdersByStatusResponse200]:
    """Get orders filtered by status with advanced filtering


    **Status-Based Order Filtering**

    Retrieve outbound orders filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Customer-specific orders
    - Order type filtering
    - Date range filtering
    - Priority-based filtering
    - Cursor-based pagination

    **Sorting Logic:**
    - Primary: Priority (ascending - URGENT first)
    - Secondary: Order date (ascending - oldest first)

    **Pagination:**
    - Cursor-based with overflow detection
    - Configurable page limits
    - Total count included


    Args:
        world_id (str):
        status (list[GetWMSOutboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        order_type (Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]]):
        priority (Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOutboundOrdersByStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        customer_id=customer_id,
        order_type=order_type,
        priority=priority,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSOutboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    order_type: Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]] = UNSET,
    priority: Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Optional[GetWMSOutboundOrdersByStatusResponse200]:
    """Get orders filtered by status with advanced filtering


    **Status-Based Order Filtering**

    Retrieve outbound orders filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Customer-specific orders
    - Order type filtering
    - Date range filtering
    - Priority-based filtering
    - Cursor-based pagination

    **Sorting Logic:**
    - Primary: Priority (ascending - URGENT first)
    - Secondary: Order date (ascending - oldest first)

    **Pagination:**
    - Cursor-based with overflow detection
    - Configurable page limits
    - Total count included


    Args:
        world_id (str):
        status (list[GetWMSOutboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        order_type (Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]]):
        priority (Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOutboundOrdersByStatusResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        customer_id=customer_id,
        order_type=order_type,
        priority=priority,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSOutboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    order_type: Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]] = UNSET,
    priority: Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Response[GetWMSOutboundOrdersByStatusResponse200]:
    """Get orders filtered by status with advanced filtering


    **Status-Based Order Filtering**

    Retrieve outbound orders filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Customer-specific orders
    - Order type filtering
    - Date range filtering
    - Priority-based filtering
    - Cursor-based pagination

    **Sorting Logic:**
    - Primary: Priority (ascending - URGENT first)
    - Secondary: Order date (ascending - oldest first)

    **Pagination:**
    - Cursor-based with overflow detection
    - Configurable page limits
    - Total count included


    Args:
        world_id (str):
        status (list[GetWMSOutboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        order_type (Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]]):
        priority (Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOutboundOrdersByStatusResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        customer_id=customer_id,
        order_type=order_type,
        priority=priority,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSOutboundOrdersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    order_type: Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]] = UNSET,
    priority: Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, float] = UNSET,
) -> Optional[GetWMSOutboundOrdersByStatusResponse200]:
    """Get orders filtered by status with advanced filtering


    **Status-Based Order Filtering**

    Retrieve outbound orders filtered by status with comprehensive query capabilities.

    **Advanced Filtering Options:**
    - Multiple status selection
    - Warehouse-specific filtering
    - Customer-specific orders
    - Order type filtering
    - Date range filtering
    - Priority-based filtering
    - Cursor-based pagination

    **Sorting Logic:**
    - Primary: Priority (ascending - URGENT first)
    - Secondary: Order date (ascending - oldest first)

    **Pagination:**
    - Cursor-based with overflow detection
    - Configurable page limits
    - Total count included


    Args:
        world_id (str):
        status (list[GetWMSOutboundOrdersByStatusStatusItem]):
        warehouse_id (Union[Unset, str]):
        customer_id (Union[Unset, str]):
        order_type (Union[Unset, list[GetWMSOutboundOrdersByStatusOrderTypeItem]]):
        priority (Union[Unset, list[GetWMSOutboundOrdersByStatusPriorityItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, float]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOutboundOrdersByStatusResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            customer_id=customer_id,
            order_type=order_type,
            priority=priority,
            date_start=date_start,
            date_end=date_end,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
