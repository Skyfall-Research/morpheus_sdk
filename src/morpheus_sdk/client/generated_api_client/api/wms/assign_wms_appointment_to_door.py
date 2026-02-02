from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.assign_wms_appointment_to_door_body import AssignWMSAppointmentToDoorBody
from ...models.assign_wms_appointment_to_door_response_200 import AssignWMSAppointmentToDoorResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    door_id: str,
    *,
    body: AssignWMSAppointmentToDoorBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/dock-doors/{door_id}/assign",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AssignWMSAppointmentToDoorResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 422:
        response_422 = ErrorResponse.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignWMSAppointmentToDoorBody,
) -> Response[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]:
    """Assign appointment to dock door


    ## Assign Appointment to WMS Dock Door

    Assign a trailer appointment to an available dock door, automatically updating door status and
    establishing operational schedule coordination.

    ### Features
    - **Appointment Assignment**: Assign scheduled appointments to available dock doors
    - **Automatic Status Management**: Changes door status from AVAILABLE to OCCUPIED
    - **Schedule Coordination**: Validates appointment timing and door availability
    - **Carrier Integration**: Links carrier and trailer information to door operations
    - **Time Management**: Tracks start time and expected completion for scheduling
    - **Conflict Prevention**: Ensures doors are available before assignment

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Door must be in AVAILABLE status for assignment (enforced at repository level)
    - appointmentId is required and must be unique within appointment system
    - Assignment automatically changes door status to OCCUPIED
    - Previous appointment data is cleared before new assignment
    - Start time and expected end time establish operational schedule

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **appointmentId**: Required - Unique appointment identifier from scheduling system
    - **carrier**: Required - Carrier company name or identifier
    - **trailerNumber**: Required - Trailer identification number
    - **startTime**: Required - Scheduled appointment start time
    - **expectedEndTime**: Required - Expected completion time for planning

    ### Business Rules
    - Door must be AVAILABLE for new appointments
    - Concurrent appointments on same door are prevented
    - Assignment coordinates with TMS trailer management
    - Time windows support operational planning and resource allocation

    ### Use Cases
    - **Appointment Scheduling**: Assign confirmed appointments to available dock doors
    - **Operational Coordination**: Link trailers with specific dock facilities
    - **Resource Management**: Optimize dock door utilization through strategic assignment
    - **Schedule Optimization**: Coordinate appointment timing with dock availability
    - **Carrier Services**: Provide carriers with specific dock assignments for deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (AssignWMSAppointmentToDoorBody):  Example: {'appointmentId':
            'tms_appointment_674565c1234567890abcdef', 'carrier': 'Swift Transportation',
            'trailerNumber': 'TRL-98765', 'startTime': '2024-11-27T09:00:00Z', 'expectedEndTime':
            '2024-11-27T13:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        door_id=door_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignWMSAppointmentToDoorBody,
) -> Optional[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]:
    """Assign appointment to dock door


    ## Assign Appointment to WMS Dock Door

    Assign a trailer appointment to an available dock door, automatically updating door status and
    establishing operational schedule coordination.

    ### Features
    - **Appointment Assignment**: Assign scheduled appointments to available dock doors
    - **Automatic Status Management**: Changes door status from AVAILABLE to OCCUPIED
    - **Schedule Coordination**: Validates appointment timing and door availability
    - **Carrier Integration**: Links carrier and trailer information to door operations
    - **Time Management**: Tracks start time and expected completion for scheduling
    - **Conflict Prevention**: Ensures doors are available before assignment

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Door must be in AVAILABLE status for assignment (enforced at repository level)
    - appointmentId is required and must be unique within appointment system
    - Assignment automatically changes door status to OCCUPIED
    - Previous appointment data is cleared before new assignment
    - Start time and expected end time establish operational schedule

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **appointmentId**: Required - Unique appointment identifier from scheduling system
    - **carrier**: Required - Carrier company name or identifier
    - **trailerNumber**: Required - Trailer identification number
    - **startTime**: Required - Scheduled appointment start time
    - **expectedEndTime**: Required - Expected completion time for planning

    ### Business Rules
    - Door must be AVAILABLE for new appointments
    - Concurrent appointments on same door are prevented
    - Assignment coordinates with TMS trailer management
    - Time windows support operational planning and resource allocation

    ### Use Cases
    - **Appointment Scheduling**: Assign confirmed appointments to available dock doors
    - **Operational Coordination**: Link trailers with specific dock facilities
    - **Resource Management**: Optimize dock door utilization through strategic assignment
    - **Schedule Optimization**: Coordinate appointment timing with dock availability
    - **Carrier Services**: Provide carriers with specific dock assignments for deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (AssignWMSAppointmentToDoorBody):  Example: {'appointmentId':
            'tms_appointment_674565c1234567890abcdef', 'carrier': 'Swift Transportation',
            'trailerNumber': 'TRL-98765', 'startTime': '2024-11-27T09:00:00Z', 'expectedEndTime':
            '2024-11-27T13:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        door_id=door_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignWMSAppointmentToDoorBody,
) -> Response[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]:
    """Assign appointment to dock door


    ## Assign Appointment to WMS Dock Door

    Assign a trailer appointment to an available dock door, automatically updating door status and
    establishing operational schedule coordination.

    ### Features
    - **Appointment Assignment**: Assign scheduled appointments to available dock doors
    - **Automatic Status Management**: Changes door status from AVAILABLE to OCCUPIED
    - **Schedule Coordination**: Validates appointment timing and door availability
    - **Carrier Integration**: Links carrier and trailer information to door operations
    - **Time Management**: Tracks start time and expected completion for scheduling
    - **Conflict Prevention**: Ensures doors are available before assignment

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Door must be in AVAILABLE status for assignment (enforced at repository level)
    - appointmentId is required and must be unique within appointment system
    - Assignment automatically changes door status to OCCUPIED
    - Previous appointment data is cleared before new assignment
    - Start time and expected end time establish operational schedule

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **appointmentId**: Required - Unique appointment identifier from scheduling system
    - **carrier**: Required - Carrier company name or identifier
    - **trailerNumber**: Required - Trailer identification number
    - **startTime**: Required - Scheduled appointment start time
    - **expectedEndTime**: Required - Expected completion time for planning

    ### Business Rules
    - Door must be AVAILABLE for new appointments
    - Concurrent appointments on same door are prevented
    - Assignment coordinates with TMS trailer management
    - Time windows support operational planning and resource allocation

    ### Use Cases
    - **Appointment Scheduling**: Assign confirmed appointments to available dock doors
    - **Operational Coordination**: Link trailers with specific dock facilities
    - **Resource Management**: Optimize dock door utilization through strategic assignment
    - **Schedule Optimization**: Coordinate appointment timing with dock availability
    - **Carrier Services**: Provide carriers with specific dock assignments for deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (AssignWMSAppointmentToDoorBody):  Example: {'appointmentId':
            'tms_appointment_674565c1234567890abcdef', 'carrier': 'Swift Transportation',
            'trailerNumber': 'TRL-98765', 'startTime': '2024-11-27T09:00:00Z', 'expectedEndTime':
            '2024-11-27T13:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        door_id=door_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    door_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AssignWMSAppointmentToDoorBody,
) -> Optional[Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]]:
    """Assign appointment to dock door


    ## Assign Appointment to WMS Dock Door

    Assign a trailer appointment to an available dock door, automatically updating door status and
    establishing operational schedule coordination.

    ### Features
    - **Appointment Assignment**: Assign scheduled appointments to available dock doors
    - **Automatic Status Management**: Changes door status from AVAILABLE to OCCUPIED
    - **Schedule Coordination**: Validates appointment timing and door availability
    - **Carrier Integration**: Links carrier and trailer information to door operations
    - **Time Management**: Tracks start time and expected completion for scheduling
    - **Conflict Prevention**: Ensures doors are available before assignment

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Door must be in AVAILABLE status for assignment (enforced at repository level)
    - appointmentId is required and must be unique within appointment system
    - Assignment automatically changes door status to OCCUPIED
    - Previous appointment data is cleared before new assignment
    - Start time and expected end time establish operational schedule

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **appointmentId**: Required - Unique appointment identifier from scheduling system
    - **carrier**: Required - Carrier company name or identifier
    - **trailerNumber**: Required - Trailer identification number
    - **startTime**: Required - Scheduled appointment start time
    - **expectedEndTime**: Required - Expected completion time for planning

    ### Business Rules
    - Door must be AVAILABLE for new appointments
    - Concurrent appointments on same door are prevented
    - Assignment coordinates with TMS trailer management
    - Time windows support operational planning and resource allocation

    ### Use Cases
    - **Appointment Scheduling**: Assign confirmed appointments to available dock doors
    - **Operational Coordination**: Link trailers with specific dock facilities
    - **Resource Management**: Optimize dock door utilization through strategic assignment
    - **Schedule Optimization**: Coordinate appointment timing with dock availability
    - **Carrier Services**: Provide carriers with specific dock assignments for deliveries


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (AssignWMSAppointmentToDoorBody):  Example: {'appointmentId':
            'tms_appointment_674565c1234567890abcdef', 'carrier': 'Swift Transportation',
            'trailerNumber': 'TRL-98765', 'startTime': '2024-11-27T09:00:00Z', 'expectedEndTime':
            '2024-11-27T13:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AssignWMSAppointmentToDoorResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            door_id=door_id,
            client=client,
            body=body,
        )
    ).parsed
