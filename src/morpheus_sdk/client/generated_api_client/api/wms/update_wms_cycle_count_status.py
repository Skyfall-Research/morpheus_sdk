from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_cycle_count_status_body import UpdateWMSCycleCountStatusBody
from ...models.update_wms_cycle_count_status_response_200 import UpdateWMSCycleCountStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    cycle_count_id: str,
    *,
    body: UpdateWMSCycleCountStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/cycle-counts/{cycle_count_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSCycleCountStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]:
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
    body: UpdateWMSCycleCountStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]:
    """Update cycle count status


    ## Update WMS Cycle Count Status

    Update the operational status of a cycle count with comprehensive status transition management and
    audit logging.

    ### Features
    - **Status Transition Management**: Control count status throughout lifecycle
    - **Completion Tracking**: Record completion user and timestamp information
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with user attribution and timestamps
    - **Validation**: Ensure valid status transitions according to business rules
    - **Notification Integration**: Support notification workflows for status changes

    ### Valid Status Transitions
    - **SCHEDULED** → **IN_PROGRESS**: Begin count execution
    - **IN_PROGRESS** → **COMPLETED**: Complete count execution
    - **COMPLETED** → **APPROVED**: Approve count results
    - **COMPLETED** → **REJECTED**: Reject count results for recount
    - **Any Status** → **CANCELLED**: Cancel count operation
    - **REJECTED** → **SCHEDULED**: Reschedule after rejection
    - **APPROVED** → **COMPLETED**: Revert approval (admin only)

    ### Business Rules
    - Status field is required for all updates
    - completedBy is required when transitioning to COMPLETED status
    - Status changes trigger automatic timestamp updates
    - Some transitions may require specific user permissions
    - Status history is maintained for audit compliance

    ### Use Cases
    - **Count Execution**: Update status as count progresses through workflow
    - **Approval Management**: Approve or reject completed count results
    - **Workflow Control**: Manage count lifecycle and progression
    - **Exception Handling**: Handle cancellations and rejections


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (UpdateWMSCycleCountStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]
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
    body: UpdateWMSCycleCountStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]:
    """Update cycle count status


    ## Update WMS Cycle Count Status

    Update the operational status of a cycle count with comprehensive status transition management and
    audit logging.

    ### Features
    - **Status Transition Management**: Control count status throughout lifecycle
    - **Completion Tracking**: Record completion user and timestamp information
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with user attribution and timestamps
    - **Validation**: Ensure valid status transitions according to business rules
    - **Notification Integration**: Support notification workflows for status changes

    ### Valid Status Transitions
    - **SCHEDULED** → **IN_PROGRESS**: Begin count execution
    - **IN_PROGRESS** → **COMPLETED**: Complete count execution
    - **COMPLETED** → **APPROVED**: Approve count results
    - **COMPLETED** → **REJECTED**: Reject count results for recount
    - **Any Status** → **CANCELLED**: Cancel count operation
    - **REJECTED** → **SCHEDULED**: Reschedule after rejection
    - **APPROVED** → **COMPLETED**: Revert approval (admin only)

    ### Business Rules
    - Status field is required for all updates
    - completedBy is required when transitioning to COMPLETED status
    - Status changes trigger automatic timestamp updates
    - Some transitions may require specific user permissions
    - Status history is maintained for audit compliance

    ### Use Cases
    - **Count Execution**: Update status as count progresses through workflow
    - **Approval Management**: Approve or reject completed count results
    - **Workflow Control**: Manage count lifecycle and progression
    - **Exception Handling**: Handle cancellations and rejections


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (UpdateWMSCycleCountStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]
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
    body: UpdateWMSCycleCountStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]:
    """Update cycle count status


    ## Update WMS Cycle Count Status

    Update the operational status of a cycle count with comprehensive status transition management and
    audit logging.

    ### Features
    - **Status Transition Management**: Control count status throughout lifecycle
    - **Completion Tracking**: Record completion user and timestamp information
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with user attribution and timestamps
    - **Validation**: Ensure valid status transitions according to business rules
    - **Notification Integration**: Support notification workflows for status changes

    ### Valid Status Transitions
    - **SCHEDULED** → **IN_PROGRESS**: Begin count execution
    - **IN_PROGRESS** → **COMPLETED**: Complete count execution
    - **COMPLETED** → **APPROVED**: Approve count results
    - **COMPLETED** → **REJECTED**: Reject count results for recount
    - **Any Status** → **CANCELLED**: Cancel count operation
    - **REJECTED** → **SCHEDULED**: Reschedule after rejection
    - **APPROVED** → **COMPLETED**: Revert approval (admin only)

    ### Business Rules
    - Status field is required for all updates
    - completedBy is required when transitioning to COMPLETED status
    - Status changes trigger automatic timestamp updates
    - Some transitions may require specific user permissions
    - Status history is maintained for audit compliance

    ### Use Cases
    - **Count Execution**: Update status as count progresses through workflow
    - **Approval Management**: Approve or reject completed count results
    - **Workflow Control**: Manage count lifecycle and progression
    - **Exception Handling**: Handle cancellations and rejections


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (UpdateWMSCycleCountStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]
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
    body: UpdateWMSCycleCountStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]]:
    """Update cycle count status


    ## Update WMS Cycle Count Status

    Update the operational status of a cycle count with comprehensive status transition management and
    audit logging.

    ### Features
    - **Status Transition Management**: Control count status throughout lifecycle
    - **Completion Tracking**: Record completion user and timestamp information
    - **Workflow Integration**: Trigger downstream processes based on status changes
    - **Audit Trail**: Track all status changes with user attribution and timestamps
    - **Validation**: Ensure valid status transitions according to business rules
    - **Notification Integration**: Support notification workflows for status changes

    ### Valid Status Transitions
    - **SCHEDULED** → **IN_PROGRESS**: Begin count execution
    - **IN_PROGRESS** → **COMPLETED**: Complete count execution
    - **COMPLETED** → **APPROVED**: Approve count results
    - **COMPLETED** → **REJECTED**: Reject count results for recount
    - **Any Status** → **CANCELLED**: Cancel count operation
    - **REJECTED** → **SCHEDULED**: Reschedule after rejection
    - **APPROVED** → **COMPLETED**: Revert approval (admin only)

    ### Business Rules
    - Status field is required for all updates
    - completedBy is required when transitioning to COMPLETED status
    - Status changes trigger automatic timestamp updates
    - Some transitions may require specific user permissions
    - Status history is maintained for audit compliance

    ### Use Cases
    - **Count Execution**: Update status as count progresses through workflow
    - **Approval Management**: Approve or reject completed count results
    - **Workflow Control**: Manage count lifecycle and progression
    - **Exception Handling**: Handle cancellations and rejections


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (UpdateWMSCycleCountStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSCycleCountStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            cycle_count_id=cycle_count_id,
            client=client,
            body=body,
        )
    ).parsed
