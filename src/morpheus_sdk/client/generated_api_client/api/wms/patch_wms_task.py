from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.patch_wms_task_body import PatchWMSTaskBody
from ...models.patch_wms_task_response_200 import PatchWMSTaskResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    task_id: str,
    *,
    body: PatchWMSTaskBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/wms/tasks/{task_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, PatchWMSTaskResponse200]]:
    if response.status_code == 200:
        response_200 = PatchWMSTaskResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, PatchWMSTaskResponse200]]:
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
    body: PatchWMSTaskBody,
) -> Response[Union[ErrorResponse, PatchWMSTaskResponse200]]:
    """Partially update task


    ## Patch WMS Task

    Partially update a warehouse task with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **taskStatus**: Update the task status (CREATED, RELEASED, ASSIGNED, IN_PROGRESS, COMPLETED,
    CANCELLED, SUSPENDED)
    - **assignment**: Update assignment information (userId, userName)
    - **priority**: Update the task priority (numeric value)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports nested objects for assignment
    - Auto-sets timing fields based on status changes

    ### Use Cases
    - Quick status updates during task execution
    - Re-assign tasks to different users
    - Adjust priority based on business needs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (PatchWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PatchWMSTaskResponse200]]
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
    body: PatchWMSTaskBody,
) -> Optional[Union[ErrorResponse, PatchWMSTaskResponse200]]:
    """Partially update task


    ## Patch WMS Task

    Partially update a warehouse task with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **taskStatus**: Update the task status (CREATED, RELEASED, ASSIGNED, IN_PROGRESS, COMPLETED,
    CANCELLED, SUSPENDED)
    - **assignment**: Update assignment information (userId, userName)
    - **priority**: Update the task priority (numeric value)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports nested objects for assignment
    - Auto-sets timing fields based on status changes

    ### Use Cases
    - Quick status updates during task execution
    - Re-assign tasks to different users
    - Adjust priority based on business needs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (PatchWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PatchWMSTaskResponse200]
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
    body: PatchWMSTaskBody,
) -> Response[Union[ErrorResponse, PatchWMSTaskResponse200]]:
    """Partially update task


    ## Patch WMS Task

    Partially update a warehouse task with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **taskStatus**: Update the task status (CREATED, RELEASED, ASSIGNED, IN_PROGRESS, COMPLETED,
    CANCELLED, SUSPENDED)
    - **assignment**: Update assignment information (userId, userName)
    - **priority**: Update the task priority (numeric value)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports nested objects for assignment
    - Auto-sets timing fields based on status changes

    ### Use Cases
    - Quick status updates during task execution
    - Re-assign tasks to different users
    - Adjust priority based on business needs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (PatchWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, PatchWMSTaskResponse200]]
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
    body: PatchWMSTaskBody,
) -> Optional[Union[ErrorResponse, PatchWMSTaskResponse200]]:
    """Partially update task


    ## Patch WMS Task

    Partially update a warehouse task with only the specified fields. This is useful for updating
    specific properties without affecting other fields.

    ### Allowed Fields
    - **taskStatus**: Update the task status (CREATED, RELEASED, ASSIGNED, IN_PROGRESS, COMPLETED,
    CANCELLED, SUSPENDED)
    - **assignment**: Update assignment information (userId, userName)
    - **priority**: Update the task priority (numeric value)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports nested objects for assignment
    - Auto-sets timing fields based on status changes

    ### Use Cases
    - Quick status updates during task execution
    - Re-assign tasks to different users
    - Adjust priority based on business needs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (PatchWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, PatchWMSTaskResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
