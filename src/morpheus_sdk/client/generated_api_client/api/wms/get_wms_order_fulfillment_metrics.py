import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_order_fulfillment_metrics_order_type_item import GetWMSOrderFulfillmentMetricsOrderTypeItem
from ...models.get_wms_order_fulfillment_metrics_response_200 import GetWMSOrderFulfillmentMetricsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    order_type: Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    json_order_type: Union[Unset, list[str]] = UNSET
    if not isinstance(order_type, Unset):
        json_order_type = []
        for order_type_item_data in order_type:
            order_type_item = order_type_item_data.value
            json_order_type.append(order_type_item)

    params["orderType"] = json_order_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/outbound-orders/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSOrderFulfillmentMetricsResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSOrderFulfillmentMetricsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSOrderFulfillmentMetricsResponse200]:
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
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    order_type: Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]] = UNSET,
) -> Response[GetWMSOrderFulfillmentMetricsResponse200]:
    """Get comprehensive fulfillment analytics


    **Fulfillment Analytics Dashboard**

    Provide comprehensive metrics for outbound order performance analysis.

    **Metrics Included:**
    - Total and completed order counts
    - Average fulfillment time (hours from order to ship)
    - On-time shipment performance
    - Fulfillment rate percentage
    - Order status distribution
    - Top customers by volume

    **Advanced Features:**
    - MongoDB aggregation pipeline for performance
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Customer ranking by order volume


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        order_type (Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOrderFulfillmentMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        order_type=order_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    order_type: Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]] = UNSET,
) -> Optional[GetWMSOrderFulfillmentMetricsResponse200]:
    """Get comprehensive fulfillment analytics


    **Fulfillment Analytics Dashboard**

    Provide comprehensive metrics for outbound order performance analysis.

    **Metrics Included:**
    - Total and completed order counts
    - Average fulfillment time (hours from order to ship)
    - On-time shipment performance
    - Fulfillment rate percentage
    - Order status distribution
    - Top customers by volume

    **Advanced Features:**
    - MongoDB aggregation pipeline for performance
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Customer ranking by order volume


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        order_type (Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOrderFulfillmentMetricsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        order_type=order_type,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    order_type: Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]] = UNSET,
) -> Response[GetWMSOrderFulfillmentMetricsResponse200]:
    """Get comprehensive fulfillment analytics


    **Fulfillment Analytics Dashboard**

    Provide comprehensive metrics for outbound order performance analysis.

    **Metrics Included:**
    - Total and completed order counts
    - Average fulfillment time (hours from order to ship)
    - On-time shipment performance
    - Fulfillment rate percentage
    - Order status distribution
    - Top customers by volume

    **Advanced Features:**
    - MongoDB aggregation pipeline for performance
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Customer ranking by order volume


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        order_type (Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSOrderFulfillmentMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        order_type=order_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    order_type: Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]] = UNSET,
) -> Optional[GetWMSOrderFulfillmentMetricsResponse200]:
    """Get comprehensive fulfillment analytics


    **Fulfillment Analytics Dashboard**

    Provide comprehensive metrics for outbound order performance analysis.

    **Metrics Included:**
    - Total and completed order counts
    - Average fulfillment time (hours from order to ship)
    - On-time shipment performance
    - Fulfillment rate percentage
    - Order status distribution
    - Top customers by volume

    **Advanced Features:**
    - MongoDB aggregation pipeline for performance
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Customer ranking by order volume


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        order_type (Union[Unset, list[GetWMSOrderFulfillmentMetricsOrderTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSOrderFulfillmentMetricsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            order_type=order_type,
        )
    ).parsed
