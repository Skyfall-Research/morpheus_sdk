import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_task_logs_response_200 import GetWMSTaskLogsResponse200
from ...models.get_wms_task_logs_status_item import GetWMSTaskLogsStatusItem
from ...models.get_wms_task_logs_task_types_item import GetWMSTaskLogsTaskTypesItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    task_ids: Union[Unset, list[str]] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskLogsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    status: Union[Unset, list[GetWMSTaskLogsStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_task_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(task_ids, Unset):
        json_task_ids = task_ids

    params["taskIds"] = json_task_ids

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

    params["zoneId"] = zone_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSTaskLogsResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSTaskLogsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSTaskLogsResponse200]:
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
    task_ids: Union[Unset, list[str]] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskLogsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    status: Union[Unset, list[GetWMSTaskLogsStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSTaskLogsResponse200]:
    """Get task logs


    ## Get Task Logs

    Retrieve comprehensive task logs with advanced filtering capabilities for operational monitoring.

    **Use Cases:**
    - Operational audit trails and compliance
    - Performance analysis and bottleneck identification
    - Task completion tracking and verification
    - Historical data analysis and reporting

    **Field Mapping:**
    - Filters by `taskId`, `taskType`, `assignment.userId` arrays
    - Date filtering on `timing.createdAt` field
    - Zone-based filtering using `zoneId`
    - Status filtering using `taskStatus` field


    Args:
        world_id (str):
        task_ids (Union[Unset, list[str]]):
        task_types (Union[Unset, list[GetWMSTaskLogsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        status (Union[Unset, list[GetWMSTaskLogsStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTaskLogsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_ids=task_ids,
        task_types=task_types,
        user_ids=user_ids,
        status=status,
        date_start=date_start,
        date_end=date_end,
        zone_id=zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_ids: Union[Unset, list[str]] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskLogsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    status: Union[Unset, list[GetWMSTaskLogsStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSTaskLogsResponse200]:
    """Get task logs


    ## Get Task Logs

    Retrieve comprehensive task logs with advanced filtering capabilities for operational monitoring.

    **Use Cases:**
    - Operational audit trails and compliance
    - Performance analysis and bottleneck identification
    - Task completion tracking and verification
    - Historical data analysis and reporting

    **Field Mapping:**
    - Filters by `taskId`, `taskType`, `assignment.userId` arrays
    - Date filtering on `timing.createdAt` field
    - Zone-based filtering using `zoneId`
    - Status filtering using `taskStatus` field


    Args:
        world_id (str):
        task_ids (Union[Unset, list[str]]):
        task_types (Union[Unset, list[GetWMSTaskLogsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        status (Union[Unset, list[GetWMSTaskLogsStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTaskLogsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        task_ids=task_ids,
        task_types=task_types,
        user_ids=user_ids,
        status=status,
        date_start=date_start,
        date_end=date_end,
        zone_id=zone_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_ids: Union[Unset, list[str]] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskLogsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    status: Union[Unset, list[GetWMSTaskLogsStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSTaskLogsResponse200]:
    """Get task logs


    ## Get Task Logs

    Retrieve comprehensive task logs with advanced filtering capabilities for operational monitoring.

    **Use Cases:**
    - Operational audit trails and compliance
    - Performance analysis and bottleneck identification
    - Task completion tracking and verification
    - Historical data analysis and reporting

    **Field Mapping:**
    - Filters by `taskId`, `taskType`, `assignment.userId` arrays
    - Date filtering on `timing.createdAt` field
    - Zone-based filtering using `zoneId`
    - Status filtering using `taskStatus` field


    Args:
        world_id (str):
        task_ids (Union[Unset, list[str]]):
        task_types (Union[Unset, list[GetWMSTaskLogsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        status (Union[Unset, list[GetWMSTaskLogsStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTaskLogsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_ids=task_ids,
        task_types=task_types,
        user_ids=user_ids,
        status=status,
        date_start=date_start,
        date_end=date_end,
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    task_ids: Union[Unset, list[str]] = UNSET,
    task_types: Union[Unset, list[GetWMSTaskLogsTaskTypesItem]] = UNSET,
    user_ids: Union[Unset, list[str]] = UNSET,
    status: Union[Unset, list[GetWMSTaskLogsStatusItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSTaskLogsResponse200]:
    """Get task logs


    ## Get Task Logs

    Retrieve comprehensive task logs with advanced filtering capabilities for operational monitoring.

    **Use Cases:**
    - Operational audit trails and compliance
    - Performance analysis and bottleneck identification
    - Task completion tracking and verification
    - Historical data analysis and reporting

    **Field Mapping:**
    - Filters by `taskId`, `taskType`, `assignment.userId` arrays
    - Date filtering on `timing.createdAt` field
    - Zone-based filtering using `zoneId`
    - Status filtering using `taskStatus` field


    Args:
        world_id (str):
        task_ids (Union[Unset, list[str]]):
        task_types (Union[Unset, list[GetWMSTaskLogsTaskTypesItem]]):
        user_ids (Union[Unset, list[str]]):
        status (Union[Unset, list[GetWMSTaskLogsStatusItem]]):
        date_start (Union[Unset, datetime.datetime]):
        date_end (Union[Unset, datetime.datetime]):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTaskLogsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            task_ids=task_ids,
            task_types=task_types,
            user_ids=user_ids,
            status=status,
            date_start=date_start,
            date_end=date_end,
            zone_id=zone_id,
        )
    ).parsed
