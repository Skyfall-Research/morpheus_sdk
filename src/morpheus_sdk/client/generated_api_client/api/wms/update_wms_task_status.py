from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_task_status_body import UpdateWMSTaskStatusBody
from ...models.update_wms_task_status_response_200 import UpdateWMSTaskStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    task_id: str,
    *,
    body: UpdateWMSTaskStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/tasks/{task_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSTaskStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSTaskStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]:
    """Update task status


    ## Update Task Status

    Update task status with automatic timestamp tracking and workflow progression.

    **Status Workflow:**
    - **CREATED** → RELEASED (task becomes available)
    - **RELEASED** → ASSIGNED (assigned to user)
    - **ASSIGNED** → IN_PROGRESS (work started)
    - **IN_PROGRESS** → COMPLETED (successfully finished)
    - Any status → CANCELLED/SUSPENDED (exception handling)

    **Use Cases:**
    - Workflow progression tracking
    - Real-time task status updates
    - Performance measurement
    - Exception handling and recovery

    **Field Mapping:**
    - Updates `taskStatus` field directly
    - Automatically sets corresponding timestamp fields in `timing` object
    - Updates assignment fields when user information provided


    Args:
        world_id (str):
        task_id (str):
        body (UpdateWMSTaskStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSTaskStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]:
    """Update task status


    ## Update Task Status

    Update task status with automatic timestamp tracking and workflow progression.

    **Status Workflow:**
    - **CREATED** → RELEASED (task becomes available)
    - **RELEASED** → ASSIGNED (assigned to user)
    - **ASSIGNED** → IN_PROGRESS (work started)
    - **IN_PROGRESS** → COMPLETED (successfully finished)
    - Any status → CANCELLED/SUSPENDED (exception handling)

    **Use Cases:**
    - Workflow progression tracking
    - Real-time task status updates
    - Performance measurement
    - Exception handling and recovery

    **Field Mapping:**
    - Updates `taskStatus` field directly
    - Automatically sets corresponding timestamp fields in `timing` object
    - Updates assignment fields when user information provided


    Args:
        world_id (str):
        task_id (str):
        body (UpdateWMSTaskStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSTaskStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSTaskStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]:
    """Update task status


    ## Update Task Status

    Update task status with automatic timestamp tracking and workflow progression.

    **Status Workflow:**
    - **CREATED** → RELEASED (task becomes available)
    - **RELEASED** → ASSIGNED (assigned to user)
    - **ASSIGNED** → IN_PROGRESS (work started)
    - **IN_PROGRESS** → COMPLETED (successfully finished)
    - Any status → CANCELLED/SUSPENDED (exception handling)

    **Use Cases:**
    - Workflow progression tracking
    - Real-time task status updates
    - Performance measurement
    - Exception handling and recovery

    **Field Mapping:**
    - Updates `taskStatus` field directly
    - Automatically sets corresponding timestamp fields in `timing` object
    - Updates assignment fields when user information provided


    Args:
        world_id (str):
        task_id (str):
        body (UpdateWMSTaskStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSTaskStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSTaskStatusResponse200]]:
    """Update task status


    ## Update Task Status

    Update task status with automatic timestamp tracking and workflow progression.

    **Status Workflow:**
    - **CREATED** → RELEASED (task becomes available)
    - **RELEASED** → ASSIGNED (assigned to user)
    - **ASSIGNED** → IN_PROGRESS (work started)
    - **IN_PROGRESS** → COMPLETED (successfully finished)
    - Any status → CANCELLED/SUSPENDED (exception handling)

    **Use Cases:**
    - Workflow progression tracking
    - Real-time task status updates
    - Performance measurement
    - Exception handling and recovery

    **Field Mapping:**
    - Updates `taskStatus` field directly
    - Automatically sets corresponding timestamp fields in `timing` object
    - Updates assignment fields when user information provided


    Args:
        world_id (str):
        task_id (str):
        body (UpdateWMSTaskStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSTaskStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
