import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_task_performance_metrics_response_200 import GetWMSTaskPerformanceMetricsResponse200
from ...models.get_wms_task_performance_metrics_task_types_item import GetWMSTaskPerformanceMetricsTaskTypesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    task_types: Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_task_types: Union[Unset, list[str]] = UNSET
    if not isinstance(task_types, Unset):
        json_task_types = []
        for task_types_item_data in task_types:
            task_types_item = task_types_item_data.value
            json_task_types.append(task_types_item)

    params["taskTypes"] = json_task_types

    json_user_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(user_ids, Unset):
        json_user_ids = user_ids

    params["userIds"] = json_user_ids

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
        "url": f"/{world_id}/wms/tasks/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSTaskPerformanceMetricsResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSTaskPerformanceMetricsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSTaskPerformanceMetricsResponse200]:
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
    task_types: Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetWMSTaskPerformanceMetricsResponse200]:
    """Get task performance metrics


    ## Get Task Performance Metrics

    Retrieve comprehensive analytics for task performance and productivity measurement.

    **Metrics Provided:**
    - Total and completed task counts
    - Average task duration and on-time completion rates
    - Productivity analysis by user
    - Performance breakdown by task type

    **Use Cases:**
    - Operational performance monitoring
    - Labor productivity analysis
    - Process optimization insights
    - Executive reporting dashboards


    Args:
        world_id (str):
        task_types (Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTaskPerformanceMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_types=task_types,
        user_ids=user_ids,
        date_start=date_start,
        date_end=date_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_types: Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetWMSTaskPerformanceMetricsResponse200]:
    """Get task performance metrics


    ## Get Task Performance Metrics

    Retrieve comprehensive analytics for task performance and productivity measurement.

    **Metrics Provided:**
    - Total and completed task counts
    - Average task duration and on-time completion rates
    - Productivity analysis by user
    - Performance breakdown by task type

    **Use Cases:**
    - Operational performance monitoring
    - Labor productivity analysis
    - Process optimization insights
    - Executive reporting dashboards


    Args:
        world_id (str):
        task_types (Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTaskPerformanceMetricsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        task_types=task_types,
        user_ids=user_ids,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_types: Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[GetWMSTaskPerformanceMetricsResponse200]:
    """Get task performance metrics


    ## Get Task Performance Metrics

    Retrieve comprehensive analytics for task performance and productivity measurement.

    **Metrics Provided:**
    - Total and completed task counts
    - Average task duration and on-time completion rates
    - Productivity analysis by user
    - Performance breakdown by task type

    **Use Cases:**
    - Operational performance monitoring
    - Labor productivity analysis
    - Process optimization insights
    - Executive reporting dashboards


    Args:
        world_id (str):
        task_types (Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTaskPerformanceMetricsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_types=task_types,
        user_ids=user_ids,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_types: Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[GetWMSTaskPerformanceMetricsResponse200]:
    """Get task performance metrics


    ## Get Task Performance Metrics

    Retrieve comprehensive analytics for task performance and productivity measurement.

    **Metrics Provided:**
    - Total and completed task counts
    - Average task duration and on-time completion rates
    - Productivity analysis by user
    - Performance breakdown by task type

    **Use Cases:**
    - Operational performance monitoring
    - Labor productivity analysis
    - Process optimization insights
    - Executive reporting dashboards


    Args:
        world_id (str):
        task_types (Union[Unset, list[GetWMSTaskPerformanceMetricsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTaskPerformanceMetricsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            task_types=task_types,
            user_ids=user_ids,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
