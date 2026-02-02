import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_replenishment_metrics_replenishment_type_item import (
    GetWMSReplenishmentMetricsReplenishmentTypeItem,
)
from ...models.get_wms_replenishment_metrics_response_200 import GetWMSReplenishmentMetricsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]] = UNSET,
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

    json_replenishment_type: Union[Unset, list[str]] = UNSET
    if not isinstance(replenishment_type, Unset):
        json_replenishment_type = []
        for replenishment_type_item_data in replenishment_type:
            replenishment_type_item = replenishment_type_item_data.value
            json_replenishment_type.append(replenishment_type_item)

    params["replenishmentType"] = json_replenishment_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/replenishments/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSReplenishmentMetricsResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSReplenishmentMetricsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSReplenishmentMetricsResponse200]:
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
    replenishment_type: Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]] = UNSET,
) -> Response[GetWMSReplenishmentMetricsResponse200]:
    """Get replenishment metrics


    ## Get Replenishment Metrics

    Retrieve comprehensive analytics and metrics for replenishment operations.

    **Metrics Provided:**
    - Total replenishments count
    - Status breakdown (pending vs completed)
    - Average completion time in hours
    - Performance by replenishment type
    - Top replenished products

    **Use Cases:**
    - Operational performance monitoring
    - Replenishment efficiency analysis
    - Resource planning and optimization
    - Executive reporting dashboards


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        replenishment_type (Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSReplenishmentMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        replenishment_type=replenishment_type,
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
    replenishment_type: Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]] = UNSET,
) -> Optional[GetWMSReplenishmentMetricsResponse200]:
    """Get replenishment metrics


    ## Get Replenishment Metrics

    Retrieve comprehensive analytics and metrics for replenishment operations.

    **Metrics Provided:**
    - Total replenishments count
    - Status breakdown (pending vs completed)
    - Average completion time in hours
    - Performance by replenishment type
    - Top replenished products

    **Use Cases:**
    - Operational performance monitoring
    - Replenishment efficiency analysis
    - Resource planning and optimization
    - Executive reporting dashboards


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        replenishment_type (Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSReplenishmentMetricsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        replenishment_type=replenishment_type,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    replenishment_type: Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]] = UNSET,
) -> Response[GetWMSReplenishmentMetricsResponse200]:
    """Get replenishment metrics


    ## Get Replenishment Metrics

    Retrieve comprehensive analytics and metrics for replenishment operations.

    **Metrics Provided:**
    - Total replenishments count
    - Status breakdown (pending vs completed)
    - Average completion time in hours
    - Performance by replenishment type
    - Top replenished products

    **Use Cases:**
    - Operational performance monitoring
    - Replenishment efficiency analysis
    - Resource planning and optimization
    - Executive reporting dashboards


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        replenishment_type (Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSReplenishmentMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        replenishment_type=replenishment_type,
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
    replenishment_type: Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]] = UNSET,
) -> Optional[GetWMSReplenishmentMetricsResponse200]:
    """Get replenishment metrics


    ## Get Replenishment Metrics

    Retrieve comprehensive analytics and metrics for replenishment operations.

    **Metrics Provided:**
    - Total replenishments count
    - Status breakdown (pending vs completed)
    - Average completion time in hours
    - Performance by replenishment type
    - Top replenished products

    **Use Cases:**
    - Operational performance monitoring
    - Replenishment efficiency analysis
    - Resource planning and optimization
    - Executive reporting dashboards


    Args:
        world_id (str):
        warehouse_id (Union[Unset, str]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        replenishment_type (Union[Unset, list[GetWMSReplenishmentMetricsReplenishmentTypeItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSReplenishmentMetricsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            replenishment_type=replenishment_type,
        )
    ).parsed
