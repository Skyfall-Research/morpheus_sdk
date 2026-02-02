from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_active_tasks_response_200 import GetWMSActiveTasksResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    zone_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["zoneId"] = zone_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/tasks/active",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSActiveTasksResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSActiveTasksResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSActiveTasksResponse200]:
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
    zone_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSActiveTasksResponse200]:
    """Get active tasks


    ## Get Active Tasks

    Retrieve all currently active (non-completed) tasks with optional zone filtering.

    **Active Status Definition:**
    - CREATED, RELEASED, ASSIGNED, IN_PROGRESS (excludes COMPLETED, CANCELLED, SUSPENDED)

    **Use Cases:**
    - Real-time operational dashboards
    - Work-in-progress monitoring
    - Resource allocation planning
    - Zone-specific task management

    **Field Mapping:**
    - Filters using `taskStatus` field with `$in` operator
    - Optional `zoneId` filtering
    - Sorted by priority descending, then creation time ascending


    Args:
        world_id (str):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSActiveTasksResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
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
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSActiveTasksResponse200]:
    """Get active tasks


    ## Get Active Tasks

    Retrieve all currently active (non-completed) tasks with optional zone filtering.

    **Active Status Definition:**
    - CREATED, RELEASED, ASSIGNED, IN_PROGRESS (excludes COMPLETED, CANCELLED, SUSPENDED)

    **Use Cases:**
    - Real-time operational dashboards
    - Work-in-progress monitoring
    - Resource allocation planning
    - Zone-specific task management

    **Field Mapping:**
    - Filters using `taskStatus` field with `$in` operator
    - Optional `zoneId` filtering
    - Sorted by priority descending, then creation time ascending


    Args:
        world_id (str):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSActiveTasksResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        zone_id=zone_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSActiveTasksResponse200]:
    """Get active tasks


    ## Get Active Tasks

    Retrieve all currently active (non-completed) tasks with optional zone filtering.

    **Active Status Definition:**
    - CREATED, RELEASED, ASSIGNED, IN_PROGRESS (excludes COMPLETED, CANCELLED, SUSPENDED)

    **Use Cases:**
    - Real-time operational dashboards
    - Work-in-progress monitoring
    - Resource allocation planning
    - Zone-specific task management

    **Field Mapping:**
    - Filters using `taskStatus` field with `$in` operator
    - Optional `zoneId` filtering
    - Sorted by priority descending, then creation time ascending


    Args:
        world_id (str):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSActiveTasksResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSActiveTasksResponse200]:
    """Get active tasks


    ## Get Active Tasks

    Retrieve all currently active (non-completed) tasks with optional zone filtering.

    **Active Status Definition:**
    - CREATED, RELEASED, ASSIGNED, IN_PROGRESS (excludes COMPLETED, CANCELLED, SUSPENDED)

    **Use Cases:**
    - Real-time operational dashboards
    - Work-in-progress monitoring
    - Resource allocation planning
    - Zone-specific task management

    **Field Mapping:**
    - Filters using `taskStatus` field with `$in` operator
    - Optional `zoneId` filtering
    - Sorted by priority descending, then creation time ascending


    Args:
        world_id (str):
        zone_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSActiveTasksResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            zone_id=zone_id,
        )
    ).parsed
