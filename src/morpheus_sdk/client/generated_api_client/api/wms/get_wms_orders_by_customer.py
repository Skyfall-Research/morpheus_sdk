import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_orders_by_customer_response_200 import GetWMSOrdersByCustomerResponse200
from ...models.get_wms_orders_by_customer_status_item import GetWMSOrdersByCustomerStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    customer_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSOrdersByCustomerStatusItem]] = UNSET,
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
        "url": f"/{world_id}/wms/outbound-orders/customer/{customer_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSOrdersByCustomerResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSOrdersByCustomerResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSOrdersByCustomerResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSOrdersByCustomerStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetWMSOrdersByCustomerResponse200]:
    """Get all orders for specific customer


    **Customer Order History**

    Retrieve all outbound orders for a specific customer with optional filtering.

    **Filtering Options:**
    - Warehouse-specific orders
    - Status-based filtering
    - Date range filtering

    **Sorting:**
    - Orders sorted by `orderDate` descending (newest first)
    - No pagination applied - returns all matching orders

    **Use Cases:**
    - Customer service inquiries
    - Order history analysis
    - Account management


    Args:
        world_id (str):
        customer_id (str):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSOrdersByCustomerStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOrdersByCustomerResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        customer_id=customer_id,
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
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSOrdersByCustomerStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetWMSOrdersByCustomerResponse200]:
    """Get all orders for specific customer


    **Customer Order History**

    Retrieve all outbound orders for a specific customer with optional filtering.

    **Filtering Options:**
    - Warehouse-specific orders
    - Status-based filtering
    - Date range filtering

    **Sorting:**
    - Orders sorted by `orderDate` descending (newest first)
    - No pagination applied - returns all matching orders

    **Use Cases:**
    - Customer service inquiries
    - Order history analysis
    - Account management


    Args:
        world_id (str):
        customer_id (str):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSOrdersByCustomerStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOrdersByCustomerResponse200
    """

    return sync_detailed(
        world_id=world_id,
        customer_id=customer_id,
        client=client,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSOrdersByCustomerStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetWMSOrdersByCustomerResponse200]:
    """Get all orders for specific customer


    **Customer Order History**

    Retrieve all outbound orders for a specific customer with optional filtering.

    **Filtering Options:**
    - Warehouse-specific orders
    - Status-based filtering
    - Date range filtering

    **Sorting:**
    - Orders sorted by `orderDate` descending (newest first)
    - No pagination applied - returns all matching orders

    **Use Cases:**
    - Customer service inquiries
    - Order history analysis
    - Account management


    Args:
        world_id (str):
        customer_id (str):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSOrdersByCustomerStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOrdersByCustomerResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        customer_id=customer_id,
        warehouse_id=warehouse_id,
        status=status,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    customer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSOrdersByCustomerStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetWMSOrdersByCustomerResponse200]:
    """Get all orders for specific customer


    **Customer Order History**

    Retrieve all outbound orders for a specific customer with optional filtering.

    **Filtering Options:**
    - Warehouse-specific orders
    - Status-based filtering
    - Date range filtering

    **Sorting:**
    - Orders sorted by `orderDate` descending (newest first)
    - No pagination applied - returns all matching orders

    **Use Cases:**
    - Customer service inquiries
    - Order history analysis
    - Account management


    Args:
        world_id (str):
        customer_id (str):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSOrdersByCustomerStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOrdersByCustomerResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            customer_id=customer_id,
            client=client,
            warehouse_id=warehouse_id,
            status=status,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
