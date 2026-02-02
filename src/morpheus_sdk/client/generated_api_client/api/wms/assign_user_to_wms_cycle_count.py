from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_user_to_wms_cycle_count_body import AssignUserToWMSCycleCountBody
from ...models.assign_user_to_wms_cycle_count_response_200 import AssignUserToWMSCycleCountResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    cycle_count_id: str,
    *,
    body: AssignUserToWMSCycleCountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/cycle-counts/{cycle_count_id}/assign",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AssignUserToWMSCycleCountResponse200.from_dict(response.json())

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
) -> Response[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignUserToWMSCycleCountBody,
) -> Response[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]:
    """Assign user to cycle count


    ## Assign User to WMS Cycle Count

    Assign specific users to cycle count tasks with precise bin allocations and assignment tracking for
    efficient count execution.

    ### Features
    - **User Assignment Management**: Assign users to specific cycle count tasks
    - **Bin Allocation**: Specify exact bins assigned to each user for counting
    - **Assignment Tracking**: Track assignment status and progress
    - **Workload Distribution**: Distribute counting workload across available users
    - **Flexible Assignment**: Support individual and bulk user assignments
    - **Status Monitoring**: Monitor assignment completion and progress

    ### Assignment Process
    - **User Identification**: Specify user ID and display name for assignment tracking
    - **Bin Allocation**: Define specific bins assigned to user for counting
    - **Status Initialization**: Set initial assignment status (typically ASSIGNED)
    - **Workflow Integration**: Enable assignment tracking and progress monitoring

    ### Business Rules
    - userId and userName are required for all assignments
    - assignedBins array defines specific bins for user to count
    - Assignment status tracks individual user progress
    - Multiple users can be assigned to single cycle count
    - Bin assignments should not overlap between users for accuracy

    ### Use Cases
    - **Task Distribution**: Distribute cycle count tasks across available personnel
    - **Workload Management**: Balance counting workload for efficient execution
    - **Progress Tracking**: Track individual user progress and completion
    - **Resource Planning**: Plan counting resources and user allocations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AssignUserToWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignUserToWMSCycleCountBody,
) -> Optional[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]:
    """Assign user to cycle count


    ## Assign User to WMS Cycle Count

    Assign specific users to cycle count tasks with precise bin allocations and assignment tracking for
    efficient count execution.

    ### Features
    - **User Assignment Management**: Assign users to specific cycle count tasks
    - **Bin Allocation**: Specify exact bins assigned to each user for counting
    - **Assignment Tracking**: Track assignment status and progress
    - **Workload Distribution**: Distribute counting workload across available users
    - **Flexible Assignment**: Support individual and bulk user assignments
    - **Status Monitoring**: Monitor assignment completion and progress

    ### Assignment Process
    - **User Identification**: Specify user ID and display name for assignment tracking
    - **Bin Allocation**: Define specific bins assigned to user for counting
    - **Status Initialization**: Set initial assignment status (typically ASSIGNED)
    - **Workflow Integration**: Enable assignment tracking and progress monitoring

    ### Business Rules
    - userId and userName are required for all assignments
    - assignedBins array defines specific bins for user to count
    - Assignment status tracks individual user progress
    - Multiple users can be assigned to single cycle count
    - Bin assignments should not overlap between users for accuracy

    ### Use Cases
    - **Task Distribution**: Distribute cycle count tasks across available personnel
    - **Workload Management**: Balance counting workload for efficient execution
    - **Progress Tracking**: Track individual user progress and completion
    - **Resource Planning**: Plan counting resources and user allocations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AssignUserToWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignUserToWMSCycleCountBody,
) -> Response[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]:
    """Assign user to cycle count


    ## Assign User to WMS Cycle Count

    Assign specific users to cycle count tasks with precise bin allocations and assignment tracking for
    efficient count execution.

    ### Features
    - **User Assignment Management**: Assign users to specific cycle count tasks
    - **Bin Allocation**: Specify exact bins assigned to each user for counting
    - **Assignment Tracking**: Track assignment status and progress
    - **Workload Distribution**: Distribute counting workload across available users
    - **Flexible Assignment**: Support individual and bulk user assignments
    - **Status Monitoring**: Monitor assignment completion and progress

    ### Assignment Process
    - **User Identification**: Specify user ID and display name for assignment tracking
    - **Bin Allocation**: Define specific bins assigned to user for counting
    - **Status Initialization**: Set initial assignment status (typically ASSIGNED)
    - **Workflow Integration**: Enable assignment tracking and progress monitoring

    ### Business Rules
    - userId and userName are required for all assignments
    - assignedBins array defines specific bins for user to count
    - Assignment status tracks individual user progress
    - Multiple users can be assigned to single cycle count
    - Bin assignments should not overlap between users for accuracy

    ### Use Cases
    - **Task Distribution**: Distribute cycle count tasks across available personnel
    - **Workload Management**: Balance counting workload for efficient execution
    - **Progress Tracking**: Track individual user progress and completion
    - **Resource Planning**: Plan counting resources and user allocations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AssignUserToWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignUserToWMSCycleCountBody,
) -> Optional[Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]]:
    """Assign user to cycle count


    ## Assign User to WMS Cycle Count

    Assign specific users to cycle count tasks with precise bin allocations and assignment tracking for
    efficient count execution.

    ### Features
    - **User Assignment Management**: Assign users to specific cycle count tasks
    - **Bin Allocation**: Specify exact bins assigned to each user for counting
    - **Assignment Tracking**: Track assignment status and progress
    - **Workload Distribution**: Distribute counting workload across available users
    - **Flexible Assignment**: Support individual and bulk user assignments
    - **Status Monitoring**: Monitor assignment completion and progress

    ### Assignment Process
    - **User Identification**: Specify user ID and display name for assignment tracking
    - **Bin Allocation**: Define specific bins assigned to user for counting
    - **Status Initialization**: Set initial assignment status (typically ASSIGNED)
    - **Workflow Integration**: Enable assignment tracking and progress monitoring

    ### Business Rules
    - userId and userName are required for all assignments
    - assignedBins array defines specific bins for user to count
    - Assignment status tracks individual user progress
    - Multiple users can be assigned to single cycle count
    - Bin assignments should not overlap between users for accuracy

    ### Use Cases
    - **Task Distribution**: Distribute cycle count tasks across available personnel
    - **Workload Management**: Balance counting workload for efficient execution
    - **Progress Tracking**: Track individual user progress and completion
    - **Resource Planning**: Plan counting resources and user allocations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AssignUserToWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignUserToWMSCycleCountResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            cycle_count_id=cycle_count_id,
            client=client,
            body=body,
        )
    ).parsed
