from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_tasks_by_user_response_200 import GetWMSTasksByUserResponse200
from ...models.get_wms_tasks_by_user_status_item import GetWMSTasksByUserStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    user_id: str,
    *,
    status: Union[Unset, list[GetWMSTasksByUserStatusItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/tasks/user/{user_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSTasksByUserResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSTasksByUserResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSTasksByUserResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSTasksByUserStatusItem]] = UNSET,
) -> Response[GetWMSTasksByUserResponse200]:
    """Get tasks by user


    ## Get Tasks by User

    Retrieve all tasks assigned to a specific user with optional status filtering.

    **Use Cases:**
    - Personal task queues for warehouse workers
    - Productivity tracking per user
    - Workload distribution analysis
    - Performance evaluation

    **Field Mapping:**
    - Filters by `assignment.userId` field
    - Optional status filtering on `taskStatus`
    - Sorted by priority descending, then creation date ascending


    Args:
        world_id (str):
        user_id (str):
        status (Union[Unset, list[GetWMSTasksByUserStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTasksByUserResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        user_id=user_id,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSTasksByUserStatusItem]] = UNSET,
) -> Optional[GetWMSTasksByUserResponse200]:
    """Get tasks by user


    ## Get Tasks by User

    Retrieve all tasks assigned to a specific user with optional status filtering.

    **Use Cases:**
    - Personal task queues for warehouse workers
    - Productivity tracking per user
    - Workload distribution analysis
    - Performance evaluation

    **Field Mapping:**
    - Filters by `assignment.userId` field
    - Optional status filtering on `taskStatus`
    - Sorted by priority descending, then creation date ascending


    Args:
        world_id (str):
        user_id (str):
        status (Union[Unset, list[GetWMSTasksByUserStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTasksByUserResponse200
    """

    return sync_detailed(
        world_id=world_id,
        user_id=user_id,
        client=client,
        status=status,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSTasksByUserStatusItem]] = UNSET,
) -> Response[GetWMSTasksByUserResponse200]:
    """Get tasks by user


    ## Get Tasks by User

    Retrieve all tasks assigned to a specific user with optional status filtering.

    **Use Cases:**
    - Personal task queues for warehouse workers
    - Productivity tracking per user
    - Workload distribution analysis
    - Performance evaluation

    **Field Mapping:**
    - Filters by `assignment.userId` field
    - Optional status filtering on `taskStatus`
    - Sorted by priority descending, then creation date ascending


    Args:
        world_id (str):
        user_id (str):
        status (Union[Unset, list[GetWMSTasksByUserStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSTasksByUserResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        user_id=user_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    user_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSTasksByUserStatusItem]] = UNSET,
) -> Optional[GetWMSTasksByUserResponse200]:
    """Get tasks by user


    ## Get Tasks by User

    Retrieve all tasks assigned to a specific user with optional status filtering.

    **Use Cases:**
    - Personal task queues for warehouse workers
    - Productivity tracking per user
    - Workload distribution analysis
    - Performance evaluation

    **Field Mapping:**
    - Filters by `assignment.userId` field
    - Optional status filtering on `taskStatus`
    - Sorted by priority descending, then creation date ascending


    Args:
        world_id (str):
        user_id (str):
        status (Union[Unset, list[GetWMSTasksByUserStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSTasksByUserResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            user_id=user_id,
            client=client,
            status=status,
        )
    ).parsed
