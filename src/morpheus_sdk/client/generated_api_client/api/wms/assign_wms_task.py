from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_wms_task_body import AssignWMSTaskBody
from ...models.assign_wms_task_response_200 import AssignWMSTaskResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    task_id: str,
    *,
    body: AssignWMSTaskBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/tasks/{task_id}/assign",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssignWMSTaskResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AssignWMSTaskResponse200.from_dict(response.json())

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
) -> Response[Union[AssignWMSTaskResponse200, ErrorResponse]]:
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
    body: AssignWMSTaskBody,
) -> Response[Union[AssignWMSTaskResponse200, ErrorResponse]]:
    """Assign task to user


    ## Assign WMS Task

    Assign a task to a specific user for execution. Updates the task's assigned user information and
    sets the status to ASSIGNED.

    ### Features
    - **User Assignment**: Assign task to specific warehouse worker
    - **Status Update**: Automatically updates task status to ASSIGNED
    - **Audit Trail**: Records assignment timestamp for tracking

    ### Required Fields
    - **userId**: Unique identifier of the user being assigned
    - **userName**: Display name of the user for reporting

    ### Use Cases
    - **Manual Assignment**: Supervisors assign tasks to specific workers
    - **Workload Balancing**: Distribute tasks across available workers
    - **Reassignment**: Transfer task from one worker to another


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (AssignWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignWMSTaskResponse200, ErrorResponse]]
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
    body: AssignWMSTaskBody,
) -> Optional[Union[AssignWMSTaskResponse200, ErrorResponse]]:
    """Assign task to user


    ## Assign WMS Task

    Assign a task to a specific user for execution. Updates the task's assigned user information and
    sets the status to ASSIGNED.

    ### Features
    - **User Assignment**: Assign task to specific warehouse worker
    - **Status Update**: Automatically updates task status to ASSIGNED
    - **Audit Trail**: Records assignment timestamp for tracking

    ### Required Fields
    - **userId**: Unique identifier of the user being assigned
    - **userName**: Display name of the user for reporting

    ### Use Cases
    - **Manual Assignment**: Supervisors assign tasks to specific workers
    - **Workload Balancing**: Distribute tasks across available workers
    - **Reassignment**: Transfer task from one worker to another


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (AssignWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignWMSTaskResponse200, ErrorResponse]
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
    body: AssignWMSTaskBody,
) -> Response[Union[AssignWMSTaskResponse200, ErrorResponse]]:
    """Assign task to user


    ## Assign WMS Task

    Assign a task to a specific user for execution. Updates the task's assigned user information and
    sets the status to ASSIGNED.

    ### Features
    - **User Assignment**: Assign task to specific warehouse worker
    - **Status Update**: Automatically updates task status to ASSIGNED
    - **Audit Trail**: Records assignment timestamp for tracking

    ### Required Fields
    - **userId**: Unique identifier of the user being assigned
    - **userName**: Display name of the user for reporting

    ### Use Cases
    - **Manual Assignment**: Supervisors assign tasks to specific workers
    - **Workload Balancing**: Distribute tasks across available workers
    - **Reassignment**: Transfer task from one worker to another


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (AssignWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignWMSTaskResponse200, ErrorResponse]]
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
    body: AssignWMSTaskBody,
) -> Optional[Union[AssignWMSTaskResponse200, ErrorResponse]]:
    """Assign task to user


    ## Assign WMS Task

    Assign a task to a specific user for execution. Updates the task's assigned user information and
    sets the status to ASSIGNED.

    ### Features
    - **User Assignment**: Assign task to specific warehouse worker
    - **Status Update**: Automatically updates task status to ASSIGNED
    - **Audit Trail**: Records assignment timestamp for tracking

    ### Required Fields
    - **userId**: Unique identifier of the user being assigned
    - **userName**: Display name of the user for reporting

    ### Use Cases
    - **Manual Assignment**: Supervisors assign tasks to specific workers
    - **Workload Balancing**: Distribute tasks across available workers
    - **Reassignment**: Transfer task from one worker to another


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (AssignWMSTaskBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignWMSTaskResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
