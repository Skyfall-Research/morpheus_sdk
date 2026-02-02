from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.start_tms_trailer_unloading_response_200 import StartTMSTrailerUnloadingResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/start-unloading",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]:
    if response.status_code == 200:
        response_200 = StartTMSTrailerUnloadingResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]:
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
) -> Response[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]:
    """Start trailer unloading process


    ## Start TMS Trailer Unloading

    Initiate the formal unloading process for a trailer assigned to a dock door with comprehensive
    workflow integration and resource coordination.

    ### Features
    - **Process Initiation**: Begin formal unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from AT_DOCK to UNLOADING
    - **Time Tracking**: Automatically record unloading start time for performance metrics
    - **Resource Coordination**: Signal dock crew assignment and equipment allocation
    - **Workflow Integration**: Enable real-time progress tracking and completion monitoring
    - **Safety Protocols**: Ensure proper safety procedures are followed before starting

    ### Unloading Process Workflow
    1. **Pre-Start Verification**: Confirm trailer is properly positioned at dock (AT_DOCK status)
    2. **Safety Check**: Verify dock crew safety protocols and equipment readiness
    3. **Resource Assignment**: Confirm dock crew availability and equipment allocation
    4. **Process Initiation**: Start formal unloading operations
    5. **Status Update**: Update trailer status to UNLOADING automatically
    6. **Time Logging**: Record start time for performance tracking and analytics
    7. **Progress Enablement**: Enable real-time progress monitoring and completion workflow

    ### Business Rules
    - **Status Requirement**: Trailer must be in AT_DOCK status to start unloading
    - **Dock Assignment**: Valid dock door assignment is required
    - **Automatic Timestamping**: System automatically records start time
    - **Single Operation**: Only one trailer can be unloading per dock at a time
    - **Workflow Progression**: Starting unloading enables completion tracking workflow
    - **Safety Compliance**: Must meet safety requirements before operations begin

    ### No Request Body Required
    - System automatically captures start time and updates status
    - All required information derived from current trailer state

    ### Use Cases
    - **Operations Management**: Track unloading operations across facility
    - **Performance Analytics**: Measure unloading start times and efficiency
    - **Resource Planning**: Coordinate dock crew and equipment assignments
    - **Safety Compliance**: Ensure proper operational procedures are followed


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        trailer_id=trailer_id,
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
) -> Optional[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]:
    """Start trailer unloading process


    ## Start TMS Trailer Unloading

    Initiate the formal unloading process for a trailer assigned to a dock door with comprehensive
    workflow integration and resource coordination.

    ### Features
    - **Process Initiation**: Begin formal unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from AT_DOCK to UNLOADING
    - **Time Tracking**: Automatically record unloading start time for performance metrics
    - **Resource Coordination**: Signal dock crew assignment and equipment allocation
    - **Workflow Integration**: Enable real-time progress tracking and completion monitoring
    - **Safety Protocols**: Ensure proper safety procedures are followed before starting

    ### Unloading Process Workflow
    1. **Pre-Start Verification**: Confirm trailer is properly positioned at dock (AT_DOCK status)
    2. **Safety Check**: Verify dock crew safety protocols and equipment readiness
    3. **Resource Assignment**: Confirm dock crew availability and equipment allocation
    4. **Process Initiation**: Start formal unloading operations
    5. **Status Update**: Update trailer status to UNLOADING automatically
    6. **Time Logging**: Record start time for performance tracking and analytics
    7. **Progress Enablement**: Enable real-time progress monitoring and completion workflow

    ### Business Rules
    - **Status Requirement**: Trailer must be in AT_DOCK status to start unloading
    - **Dock Assignment**: Valid dock door assignment is required
    - **Automatic Timestamping**: System automatically records start time
    - **Single Operation**: Only one trailer can be unloading per dock at a time
    - **Workflow Progression**: Starting unloading enables completion tracking workflow
    - **Safety Compliance**: Must meet safety requirements before operations begin

    ### No Request Body Required
    - System automatically captures start time and updates status
    - All required information derived from current trailer state

    ### Use Cases
    - **Operations Management**: Track unloading operations across facility
    - **Performance Analytics**: Measure unloading start times and efficiency
    - **Resource Planning**: Coordinate dock crew and equipment assignments
    - **Safety Compliance**: Ensure proper operational procedures are followed


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        trailer_id=trailer_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]:
    """Start trailer unloading process


    ## Start TMS Trailer Unloading

    Initiate the formal unloading process for a trailer assigned to a dock door with comprehensive
    workflow integration and resource coordination.

    ### Features
    - **Process Initiation**: Begin formal unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from AT_DOCK to UNLOADING
    - **Time Tracking**: Automatically record unloading start time for performance metrics
    - **Resource Coordination**: Signal dock crew assignment and equipment allocation
    - **Workflow Integration**: Enable real-time progress tracking and completion monitoring
    - **Safety Protocols**: Ensure proper safety procedures are followed before starting

    ### Unloading Process Workflow
    1. **Pre-Start Verification**: Confirm trailer is properly positioned at dock (AT_DOCK status)
    2. **Safety Check**: Verify dock crew safety protocols and equipment readiness
    3. **Resource Assignment**: Confirm dock crew availability and equipment allocation
    4. **Process Initiation**: Start formal unloading operations
    5. **Status Update**: Update trailer status to UNLOADING automatically
    6. **Time Logging**: Record start time for performance tracking and analytics
    7. **Progress Enablement**: Enable real-time progress monitoring and completion workflow

    ### Business Rules
    - **Status Requirement**: Trailer must be in AT_DOCK status to start unloading
    - **Dock Assignment**: Valid dock door assignment is required
    - **Automatic Timestamping**: System automatically records start time
    - **Single Operation**: Only one trailer can be unloading per dock at a time
    - **Workflow Progression**: Starting unloading enables completion tracking workflow
    - **Safety Compliance**: Must meet safety requirements before operations begin

    ### No Request Body Required
    - System automatically captures start time and updates status
    - All required information derived from current trailer state

    ### Use Cases
    - **Operations Management**: Track unloading operations across facility
    - **Performance Analytics**: Measure unloading start times and efficiency
    - **Resource Planning**: Coordinate dock crew and equipment assignments
    - **Safety Compliance**: Ensure proper operational procedures are followed


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        trailer_id=trailer_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]]:
    """Start trailer unloading process


    ## Start TMS Trailer Unloading

    Initiate the formal unloading process for a trailer assigned to a dock door with comprehensive
    workflow integration and resource coordination.

    ### Features
    - **Process Initiation**: Begin formal unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from AT_DOCK to UNLOADING
    - **Time Tracking**: Automatically record unloading start time for performance metrics
    - **Resource Coordination**: Signal dock crew assignment and equipment allocation
    - **Workflow Integration**: Enable real-time progress tracking and completion monitoring
    - **Safety Protocols**: Ensure proper safety procedures are followed before starting

    ### Unloading Process Workflow
    1. **Pre-Start Verification**: Confirm trailer is properly positioned at dock (AT_DOCK status)
    2. **Safety Check**: Verify dock crew safety protocols and equipment readiness
    3. **Resource Assignment**: Confirm dock crew availability and equipment allocation
    4. **Process Initiation**: Start formal unloading operations
    5. **Status Update**: Update trailer status to UNLOADING automatically
    6. **Time Logging**: Record start time for performance tracking and analytics
    7. **Progress Enablement**: Enable real-time progress monitoring and completion workflow

    ### Business Rules
    - **Status Requirement**: Trailer must be in AT_DOCK status to start unloading
    - **Dock Assignment**: Valid dock door assignment is required
    - **Automatic Timestamping**: System automatically records start time
    - **Single Operation**: Only one trailer can be unloading per dock at a time
    - **Workflow Progression**: Starting unloading enables completion tracking workflow
    - **Safety Compliance**: Must meet safety requirements before operations begin

    ### No Request Body Required
    - System automatically captures start time and updates status
    - All required information derived from current trailer state

    ### Use Cases
    - **Operations Management**: Track unloading operations across facility
    - **Performance Analytics**: Measure unloading start times and efficiency
    - **Resource Planning**: Coordinate dock crew and equipment assignments
    - **Safety Compliance**: Ensure proper operational procedures are followed


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, StartTMSTrailerUnloadingResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
        )
    ).parsed
