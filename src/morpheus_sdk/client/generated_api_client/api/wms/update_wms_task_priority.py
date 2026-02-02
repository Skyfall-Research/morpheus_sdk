from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_task_priority_body import UpdateWMSTaskPriorityBody
from ...models.update_wms_task_priority_response_200 import UpdateWMSTaskPriorityResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    task_id: str,
    *,
    body: UpdateWMSTaskPriorityBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/tasks/{task_id}/priority",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSTaskPriorityResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]:
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
    body: UpdateWMSTaskPriorityBody,
) -> Response[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]:
    """Update task priority


    ## Update WMS Task Priority

    Update the priority level of a task to change its processing order in the work queue.

    ### Features
    - **Priority Management**: Change task priority for execution sequencing
    - **Numeric Priority**: Higher numbers indicate higher priority
    - **Real-time Update**: Immediately affects task queue ordering

    ### Priority Guidelines
    - **1-10**: Low priority, process when capacity allows
    - **11-50**: Normal priority, standard processing
    - **51-90**: High priority, expedited processing
    - **91-100**: Critical priority, immediate attention required

    ### Use Cases
    - **Rush Orders**: Elevate priority for urgent customer orders
    - **SLA Management**: Prioritize tasks approaching deadlines
    - **Resource Optimization**: Balance workload across priority levels


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (UpdateWMSTaskPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]
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
    body: UpdateWMSTaskPriorityBody,
) -> Optional[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]:
    """Update task priority


    ## Update WMS Task Priority

    Update the priority level of a task to change its processing order in the work queue.

    ### Features
    - **Priority Management**: Change task priority for execution sequencing
    - **Numeric Priority**: Higher numbers indicate higher priority
    - **Real-time Update**: Immediately affects task queue ordering

    ### Priority Guidelines
    - **1-10**: Low priority, process when capacity allows
    - **11-50**: Normal priority, standard processing
    - **51-90**: High priority, expedited processing
    - **91-100**: Critical priority, immediate attention required

    ### Use Cases
    - **Rush Orders**: Elevate priority for urgent customer orders
    - **SLA Management**: Prioritize tasks approaching deadlines
    - **Resource Optimization**: Balance workload across priority levels


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (UpdateWMSTaskPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]
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
    body: UpdateWMSTaskPriorityBody,
) -> Response[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]:
    """Update task priority


    ## Update WMS Task Priority

    Update the priority level of a task to change its processing order in the work queue.

    ### Features
    - **Priority Management**: Change task priority for execution sequencing
    - **Numeric Priority**: Higher numbers indicate higher priority
    - **Real-time Update**: Immediately affects task queue ordering

    ### Priority Guidelines
    - **1-10**: Low priority, process when capacity allows
    - **11-50**: Normal priority, standard processing
    - **51-90**: High priority, expedited processing
    - **91-100**: Critical priority, immediate attention required

    ### Use Cases
    - **Rush Orders**: Elevate priority for urgent customer orders
    - **SLA Management**: Prioritize tasks approaching deadlines
    - **Resource Optimization**: Balance workload across priority levels


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (UpdateWMSTaskPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]
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
    body: UpdateWMSTaskPriorityBody,
) -> Optional[Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]]:
    """Update task priority


    ## Update WMS Task Priority

    Update the priority level of a task to change its processing order in the work queue.

    ### Features
    - **Priority Management**: Change task priority for execution sequencing
    - **Numeric Priority**: Higher numbers indicate higher priority
    - **Real-time Update**: Immediately affects task queue ordering

    ### Priority Guidelines
    - **1-10**: Low priority, process when capacity allows
    - **11-50**: Normal priority, standard processing
    - **51-90**: High priority, expedited processing
    - **91-100**: Critical priority, immediate attention required

    ### Use Cases
    - **Rush Orders**: Elevate priority for urgent customer orders
    - **SLA Management**: Prioritize tasks approaching deadlines
    - **Resource Optimization**: Balance workload across priority levels


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        task_id (str):  Example: wms_task_674565c1234567890abcdef.
        body (UpdateWMSTaskPriorityBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSTaskPriorityResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
