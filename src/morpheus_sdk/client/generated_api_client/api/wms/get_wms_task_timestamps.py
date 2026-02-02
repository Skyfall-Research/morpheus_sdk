import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_task_timestamps_response_200 import GetWMSTaskTimestampsResponse200
from ...models.get_wms_task_timestamps_task_types_item import GetWMSTaskTimestampsTaskTypesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    task_id: Union[Unset, str] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    include_historical: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["taskId"] = task_id

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

    params["includeHistorical"] = include_historical

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/tasks/timestamps",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSTaskTimestampsResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSTaskTimestampsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSTaskTimestampsResponse200]:
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
    task_id: Union[Unset, str] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    include_historical: Union[Unset, bool] = False,
) -> Response[GetWMSTaskTimestampsResponse200]:
    """Get task timestamps


    ## Get Task Timestamps

    Retrieve timing data for tasks with detailed timestamp analysis capabilities.

    **Use Cases:**
    - Performance analysis and cycle time calculation
    - Process optimization and bottleneck identification
    - Labor planning and capacity modeling
    - SLA compliance monitoring

    **Field Mapping:**
    - Returns selected fields: `taskId`, `taskType`, `assignment.userId`, `timing` object
    - Excludes historical completed tasks unless `includeHistorical` is true
    - Date filtering on `timing.createdAt`


    Args:
        world_id (str):
        task_id (Union[Unset, str]):
        task_types (Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        include_historical (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTaskTimestampsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_id=task_id,
        task_types=task_types,
        user_ids=user_ids,
        date_start=date_start,
        date_end=date_end,
        include_historical=include_historical,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_id: Union[Unset, str] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    include_historical: Union[Unset, bool] = False,
) -> Optional[GetWMSTaskTimestampsResponse200]:
    """Get task timestamps


    ## Get Task Timestamps

    Retrieve timing data for tasks with detailed timestamp analysis capabilities.

    **Use Cases:**
    - Performance analysis and cycle time calculation
    - Process optimization and bottleneck identification
    - Labor planning and capacity modeling
    - SLA compliance monitoring

    **Field Mapping:**
    - Returns selected fields: `taskId`, `taskType`, `assignment.userId`, `timing` object
    - Excludes historical completed tasks unless `includeHistorical` is true
    - Date filtering on `timing.createdAt`


    Args:
        world_id (str):
        task_id (Union[Unset, str]):
        task_types (Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        include_historical (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTaskTimestampsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        task_id=task_id,
        task_types=task_types,
        user_ids=user_ids,
        date_start=date_start,
        date_end=date_end,
        include_historical=include_historical,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_id: Union[Unset, str] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    include_historical: Union[Unset, bool] = False,
) -> Response[GetWMSTaskTimestampsResponse200]:
    """Get task timestamps


    ## Get Task Timestamps

    Retrieve timing data for tasks with detailed timestamp analysis capabilities.

    **Use Cases:**
    - Performance analysis and cycle time calculation
    - Process optimization and bottleneck identification
    - Labor planning and capacity modeling
    - SLA compliance monitoring

    **Field Mapping:**
    - Returns selected fields: `taskId`, `taskType`, `assignment.userId`, `timing` object
    - Excludes historical completed tasks unless `includeHistorical` is true
    - Date filtering on `timing.createdAt`


    Args:
        world_id (str):
        task_id (Union[Unset, str]):
        task_types (Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        include_historical (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTaskTimestampsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_id=task_id,
        task_types=task_types,
        user_ids=user_ids,
        date_start=date_start,
        date_end=date_end,
        include_historical=include_historical,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_id: Union[Unset, str] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    include_historical: Union[Unset, bool] = False,
) -> Optional[GetWMSTaskTimestampsResponse200]:
    """Get task timestamps


    ## Get Task Timestamps

    Retrieve timing data for tasks with detailed timestamp analysis capabilities.

    **Use Cases:**
    - Performance analysis and cycle time calculation
    - Process optimization and bottleneck identification
    - Labor planning and capacity modeling
    - SLA compliance monitoring

    **Field Mapping:**
    - Returns selected fields: `taskId`, `taskType`, `assignment.userId`, `timing` object
    - Excludes historical completed tasks unless `includeHistorical` is true
    - Date filtering on `timing.createdAt`


    Args:
        world_id (str):
        task_id (Union[Unset, str]):
        task_types (Union[Unset, list[GetWMSTaskTimestampsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        include_historical (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTaskTimestampsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            task_id=task_id,
            task_types=task_types,
            user_ids=user_ids,
            date_start=date_start,
            date_end=date_end,
            include_historical=include_historical,
        )
    ).parsed
