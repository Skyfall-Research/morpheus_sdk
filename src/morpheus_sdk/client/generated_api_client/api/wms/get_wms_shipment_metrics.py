import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_shipment_metrics_response_200 import GetWMSShipmentMetricsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, list[str]] = UNSET,
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

    json_carrier: Union[Unset, list[str]] = UNSET
    if not isinstance(carrier, Unset):
        json_carrier = carrier

    params["carrier"] = json_carrier

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/shipments/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSShipmentMetricsResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSShipmentMetricsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSShipmentMetricsResponse200]:
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
    carrier: Union[Unset, list[str]] = UNSET,
) -> Response[GetWMSShipmentMetricsResponse200]:
    """Get comprehensive shipment analytics


    **Shipment Performance Analytics**

    Provide comprehensive metrics for outbound shipment performance analysis.

    **Metrics Included:**
    - Total, shipped, delivered, and exception shipment counts
    - Average transit time calculations
    - On-time delivery performance tracking
    - Carrier performance breakdown with individual metrics
    - Daily shipment volume trends

    **Advanced Features:**
    - MongoDB aggregation pipeline for complex analytics
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Multi-carrier performance comparison
    - Transit time calculations in days


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        carrier=carrier,
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
    carrier: Union[Unset, list[str]] = UNSET,
) -> Optional[GetWMSShipmentMetricsResponse200]:
    """Get comprehensive shipment analytics


    **Shipment Performance Analytics**

    Provide comprehensive metrics for outbound shipment performance analysis.

    **Metrics Included:**
    - Total, shipped, delivered, and exception shipment counts
    - Average transit time calculations
    - On-time delivery performance tracking
    - Carrier performance breakdown with individual metrics
    - Daily shipment volume trends

    **Advanced Features:**
    - MongoDB aggregation pipeline for complex analytics
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Multi-carrier performance comparison
    - Transit time calculations in days


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentMetricsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        carrier=carrier,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    carrier: Union[Unset, list[str]] = UNSET,
) -> Response[GetWMSShipmentMetricsResponse200]:
    """Get comprehensive shipment analytics


    **Shipment Performance Analytics**

    Provide comprehensive metrics for outbound shipment performance analysis.

    **Metrics Included:**
    - Total, shipped, delivered, and exception shipment counts
    - Average transit time calculations
    - On-time delivery performance tracking
    - Carrier performance breakdown with individual metrics
    - Daily shipment volume trends

    **Advanced Features:**
    - MongoDB aggregation pipeline for complex analytics
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Multi-carrier performance comparison
    - Transit time calculations in days


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSShipmentMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        carrier=carrier,
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
    carrier: Union[Unset, list[str]] = UNSET,
) -> Optional[GetWMSShipmentMetricsResponse200]:
    """Get comprehensive shipment analytics


    **Shipment Performance Analytics**

    Provide comprehensive metrics for outbound shipment performance analysis.

    **Metrics Included:**
    - Total, shipped, delivered, and exception shipment counts
    - Average transit time calculations
    - On-time delivery performance tracking
    - Carrier performance breakdown with individual metrics
    - Daily shipment volume trends

    **Advanced Features:**
    - MongoDB aggregation pipeline for complex analytics
    - Configurable reporting periods
    - Warehouse-specific metrics
    - Multi-carrier performance comparison
    - Transit time calculations in days


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        carrier (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSShipmentMetricsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            carrier=carrier,
        )
    ).parsed
