from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_tms_trailer_to_dock_body import AssignTMSTrailerToDockBody
from ...models.assign_tms_trailer_to_dock_response_200 import AssignTMSTrailerToDockResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
    *,
    body: AssignTMSTrailerToDockBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/assign-dock",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AssignTMSTrailerToDockResponse200.from_dict(response.json())

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
) -> Response[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignTMSTrailerToDockBody,
) -> Response[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]:
    """Assign trailer to dock door


    ## Assign TMS Trailer to Dock Door

    Assign a checked-in trailer to a specific dock door for unloading operations with comprehensive
    validation and workflow integration.

    ### Features
    - **Dock Door Assignment**: Assign specific dock door based on availability and operational needs
    - **Automatic Status Update**: Updates trailer status from CHECKED_IN to AT_DOCK
    - **Resource Management**: Coordinate dock door availability and prevent conflicts
    - **Operational Flow Integration**: Enable seamless transition to unloading workflow
    - **Real-time Location Tracking**: Update trailer location for operational visibility
    - **Notification System**: Alert operations team and driver of dock assignment

    ### Assignment Process Workflow
    1. **Status Verification**: Confirm trailer is in CHECKED_IN status
    2. **Dock Availability**: Validate requested dock door is available for assignment
    3. **Conflict Prevention**: Ensure no existing trailers assigned to same dock
    4. **Assignment Execution**: Assign trailer to specified dock door
    5. **Status Update**: Update trailer status to AT_DOCK automatically
    6. **Team Notification**: Notify operations team and driver of assignment
    7. **Workflow Enablement**: Enable unloading process workflow and resource preparation

    ### Business Rules
    - **Status Requirement**: Trailer must be in CHECKED_IN status for dock assignment
    - **Dock Availability**: Specified dock door must be available and not occupied
    - **Single Assignment**: Each trailer can only be assigned to one dock at a time
    - **Status Progression**: Assignment automatically advances trailer to AT_DOCK status
    - **Resource Coordination**: Assignment updates dock utilization and capacity planning

    ### Required Information
    - **dockDoor**: Valid dock door identifier (must reference existing dock)

    ### Use Cases
    - **Operations Planning**: Assign trailers to optimize dock utilization
    - **Workflow Management**: Progress trailers through facility operations
    - **Resource Coordination**: Manage dock door assignments and availability
    - **Performance Tracking**: Monitor trailer flow and dock efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AssignTMSTrailerToDockBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        trailer_id=trailer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignTMSTrailerToDockBody,
) -> Optional[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]:
    """Assign trailer to dock door


    ## Assign TMS Trailer to Dock Door

    Assign a checked-in trailer to a specific dock door for unloading operations with comprehensive
    validation and workflow integration.

    ### Features
    - **Dock Door Assignment**: Assign specific dock door based on availability and operational needs
    - **Automatic Status Update**: Updates trailer status from CHECKED_IN to AT_DOCK
    - **Resource Management**: Coordinate dock door availability and prevent conflicts
    - **Operational Flow Integration**: Enable seamless transition to unloading workflow
    - **Real-time Location Tracking**: Update trailer location for operational visibility
    - **Notification System**: Alert operations team and driver of dock assignment

    ### Assignment Process Workflow
    1. **Status Verification**: Confirm trailer is in CHECKED_IN status
    2. **Dock Availability**: Validate requested dock door is available for assignment
    3. **Conflict Prevention**: Ensure no existing trailers assigned to same dock
    4. **Assignment Execution**: Assign trailer to specified dock door
    5. **Status Update**: Update trailer status to AT_DOCK automatically
    6. **Team Notification**: Notify operations team and driver of assignment
    7. **Workflow Enablement**: Enable unloading process workflow and resource preparation

    ### Business Rules
    - **Status Requirement**: Trailer must be in CHECKED_IN status for dock assignment
    - **Dock Availability**: Specified dock door must be available and not occupied
    - **Single Assignment**: Each trailer can only be assigned to one dock at a time
    - **Status Progression**: Assignment automatically advances trailer to AT_DOCK status
    - **Resource Coordination**: Assignment updates dock utilization and capacity planning

    ### Required Information
    - **dockDoor**: Valid dock door identifier (must reference existing dock)

    ### Use Cases
    - **Operations Planning**: Assign trailers to optimize dock utilization
    - **Workflow Management**: Progress trailers through facility operations
    - **Resource Coordination**: Manage dock door assignments and availability
    - **Performance Tracking**: Monitor trailer flow and dock efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AssignTMSTrailerToDockBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignTMSTrailerToDockResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        trailer_id=trailer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignTMSTrailerToDockBody,
) -> Response[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]:
    """Assign trailer to dock door


    ## Assign TMS Trailer to Dock Door

    Assign a checked-in trailer to a specific dock door for unloading operations with comprehensive
    validation and workflow integration.

    ### Features
    - **Dock Door Assignment**: Assign specific dock door based on availability and operational needs
    - **Automatic Status Update**: Updates trailer status from CHECKED_IN to AT_DOCK
    - **Resource Management**: Coordinate dock door availability and prevent conflicts
    - **Operational Flow Integration**: Enable seamless transition to unloading workflow
    - **Real-time Location Tracking**: Update trailer location for operational visibility
    - **Notification System**: Alert operations team and driver of dock assignment

    ### Assignment Process Workflow
    1. **Status Verification**: Confirm trailer is in CHECKED_IN status
    2. **Dock Availability**: Validate requested dock door is available for assignment
    3. **Conflict Prevention**: Ensure no existing trailers assigned to same dock
    4. **Assignment Execution**: Assign trailer to specified dock door
    5. **Status Update**: Update trailer status to AT_DOCK automatically
    6. **Team Notification**: Notify operations team and driver of assignment
    7. **Workflow Enablement**: Enable unloading process workflow and resource preparation

    ### Business Rules
    - **Status Requirement**: Trailer must be in CHECKED_IN status for dock assignment
    - **Dock Availability**: Specified dock door must be available and not occupied
    - **Single Assignment**: Each trailer can only be assigned to one dock at a time
    - **Status Progression**: Assignment automatically advances trailer to AT_DOCK status
    - **Resource Coordination**: Assignment updates dock utilization and capacity planning

    ### Required Information
    - **dockDoor**: Valid dock door identifier (must reference existing dock)

    ### Use Cases
    - **Operations Planning**: Assign trailers to optimize dock utilization
    - **Workflow Management**: Progress trailers through facility operations
    - **Resource Coordination**: Manage dock door assignments and availability
    - **Performance Tracking**: Monitor trailer flow and dock efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AssignTMSTrailerToDockBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        trailer_id=trailer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignTMSTrailerToDockBody,
) -> Optional[Union[AssignTMSTrailerToDockResponse200, ErrorResponse]]:
    """Assign trailer to dock door


    ## Assign TMS Trailer to Dock Door

    Assign a checked-in trailer to a specific dock door for unloading operations with comprehensive
    validation and workflow integration.

    ### Features
    - **Dock Door Assignment**: Assign specific dock door based on availability and operational needs
    - **Automatic Status Update**: Updates trailer status from CHECKED_IN to AT_DOCK
    - **Resource Management**: Coordinate dock door availability and prevent conflicts
    - **Operational Flow Integration**: Enable seamless transition to unloading workflow
    - **Real-time Location Tracking**: Update trailer location for operational visibility
    - **Notification System**: Alert operations team and driver of dock assignment

    ### Assignment Process Workflow
    1. **Status Verification**: Confirm trailer is in CHECKED_IN status
    2. **Dock Availability**: Validate requested dock door is available for assignment
    3. **Conflict Prevention**: Ensure no existing trailers assigned to same dock
    4. **Assignment Execution**: Assign trailer to specified dock door
    5. **Status Update**: Update trailer status to AT_DOCK automatically
    6. **Team Notification**: Notify operations team and driver of assignment
    7. **Workflow Enablement**: Enable unloading process workflow and resource preparation

    ### Business Rules
    - **Status Requirement**: Trailer must be in CHECKED_IN status for dock assignment
    - **Dock Availability**: Specified dock door must be available and not occupied
    - **Single Assignment**: Each trailer can only be assigned to one dock at a time
    - **Status Progression**: Assignment automatically advances trailer to AT_DOCK status
    - **Resource Coordination**: Assignment updates dock utilization and capacity planning

    ### Required Information
    - **dockDoor**: Valid dock door identifier (must reference existing dock)

    ### Use Cases
    - **Operations Planning**: Assign trailers to optimize dock utilization
    - **Workflow Management**: Progress trailers through facility operations
    - **Resource Coordination**: Manage dock door assignments and availability
    - **Performance Tracking**: Monitor trailer flow and dock efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AssignTMSTrailerToDockBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignTMSTrailerToDockResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
            body=body,
        )
    ).parsed
