from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.clear_wms_appointment_from_door_body import ClearWMSAppointmentFromDoorBody
from ...models.clear_wms_appointment_from_door_response_200 import ClearWMSAppointmentFromDoorResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    door_id: str,
    *,
    body: ClearWMSAppointmentFromDoorBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/dock-doors/{door_id}/clear",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = ClearWMSAppointmentFromDoorResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]:
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
    body: ClearWMSAppointmentFromDoorBody,
) -> Response[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]:
    """Clear appointment from dock door


    ## Clear Appointment from WMS Dock Door

    Clear the current appointment from a dock door upon completion or cancellation, returning the door
    to available status for new scheduling.

    ### Features
    - **Appointment Completion**: Clear completed appointments from dock doors
    - **Status Reset**: Automatically returns door status to AVAILABLE
    - **Completion Notes**: Optional notes for appointment closure documentation
    - **History Tracking**: Maintains completion timestamps and notes for audit
    - **Resource Liberation**: Frees dock door for new appointment scheduling

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Clears currentAppointment object and resets door status to AVAILABLE
    - Optional completionNotes captured for operational documentation
    - lastAppointmentNotes and lastAppointmentCompleted fields updated for history
    - Door becomes immediately available for new appointment assignment

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **completionNotes**: Optional - Notes about appointment completion or issues

    ### Business Rules
    - Clearing appointment makes door immediately available for new scheduling
    - Completion notes provide operational feedback for continuous improvement
    - Historical appointment data preserved for reporting and analysis
    - Timestamp tracking enables utilization and efficiency metrics

    ### Use Cases
    - **Appointment Completion**: Mark appointments as completed and free dock doors
    - **Operational Documentation**: Record completion notes for process improvement
    - **Schedule Management**: Clear doors for immediate reassignment
    - **Resource Optimization**: Maximize dock door utilization through quick turnaround
    - **Quality Control**: Document any issues or observations during appointment completion


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (ClearWMSAppointmentFromDoorBody):  Example: {'completionNotes': 'Unloading completed
            successfully. Minor delay due to trailer seal issues.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]
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
    body: ClearWMSAppointmentFromDoorBody,
) -> Optional[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]:
    """Clear appointment from dock door


    ## Clear Appointment from WMS Dock Door

    Clear the current appointment from a dock door upon completion or cancellation, returning the door
    to available status for new scheduling.

    ### Features
    - **Appointment Completion**: Clear completed appointments from dock doors
    - **Status Reset**: Automatically returns door status to AVAILABLE
    - **Completion Notes**: Optional notes for appointment closure documentation
    - **History Tracking**: Maintains completion timestamps and notes for audit
    - **Resource Liberation**: Frees dock door for new appointment scheduling

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Clears currentAppointment object and resets door status to AVAILABLE
    - Optional completionNotes captured for operational documentation
    - lastAppointmentNotes and lastAppointmentCompleted fields updated for history
    - Door becomes immediately available for new appointment assignment

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **completionNotes**: Optional - Notes about appointment completion or issues

    ### Business Rules
    - Clearing appointment makes door immediately available for new scheduling
    - Completion notes provide operational feedback for continuous improvement
    - Historical appointment data preserved for reporting and analysis
    - Timestamp tracking enables utilization and efficiency metrics

    ### Use Cases
    - **Appointment Completion**: Mark appointments as completed and free dock doors
    - **Operational Documentation**: Record completion notes for process improvement
    - **Schedule Management**: Clear doors for immediate reassignment
    - **Resource Optimization**: Maximize dock door utilization through quick turnaround
    - **Quality Control**: Document any issues or observations during appointment completion


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (ClearWMSAppointmentFromDoorBody):  Example: {'completionNotes': 'Unloading completed
            successfully. Minor delay due to trailer seal issues.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]
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
    body: ClearWMSAppointmentFromDoorBody,
) -> Response[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]:
    """Clear appointment from dock door


    ## Clear Appointment from WMS Dock Door

    Clear the current appointment from a dock door upon completion or cancellation, returning the door
    to available status for new scheduling.

    ### Features
    - **Appointment Completion**: Clear completed appointments from dock doors
    - **Status Reset**: Automatically returns door status to AVAILABLE
    - **Completion Notes**: Optional notes for appointment closure documentation
    - **History Tracking**: Maintains completion timestamps and notes for audit
    - **Resource Liberation**: Frees dock door for new appointment scheduling

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Clears currentAppointment object and resets door status to AVAILABLE
    - Optional completionNotes captured for operational documentation
    - lastAppointmentNotes and lastAppointmentCompleted fields updated for history
    - Door becomes immediately available for new appointment assignment

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **completionNotes**: Optional - Notes about appointment completion or issues

    ### Business Rules
    - Clearing appointment makes door immediately available for new scheduling
    - Completion notes provide operational feedback for continuous improvement
    - Historical appointment data preserved for reporting and analysis
    - Timestamp tracking enables utilization and efficiency metrics

    ### Use Cases
    - **Appointment Completion**: Mark appointments as completed and free dock doors
    - **Operational Documentation**: Record completion notes for process improvement
    - **Schedule Management**: Clear doors for immediate reassignment
    - **Resource Optimization**: Maximize dock door utilization through quick turnaround
    - **Quality Control**: Document any issues or observations during appointment completion


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (ClearWMSAppointmentFromDoorBody):  Example: {'completionNotes': 'Unloading completed
            successfully. Minor delay due to trailer seal issues.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]
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
    body: ClearWMSAppointmentFromDoorBody,
) -> Optional[Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]]:
    """Clear appointment from dock door


    ## Clear Appointment from WMS Dock Door

    Clear the current appointment from a dock door upon completion or cancellation, returning the door
    to available status for new scheduling.

    ### Features
    - **Appointment Completion**: Clear completed appointments from dock doors
    - **Status Reset**: Automatically returns door status to AVAILABLE
    - **Completion Notes**: Optional notes for appointment closure documentation
    - **History Tracking**: Maintains completion timestamps and notes for audit
    - **Resource Liberation**: Frees dock door for new appointment scheduling

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - Clears currentAppointment object and resets door status to AVAILABLE
    - Optional completionNotes captured for operational documentation
    - lastAppointmentNotes and lastAppointmentCompleted fields updated for history
    - Door becomes immediately available for new appointment assignment

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door

    ### Request Body Fields
    - **completionNotes**: Optional - Notes about appointment completion or issues

    ### Business Rules
    - Clearing appointment makes door immediately available for new scheduling
    - Completion notes provide operational feedback for continuous improvement
    - Historical appointment data preserved for reporting and analysis
    - Timestamp tracking enables utilization and efficiency metrics

    ### Use Cases
    - **Appointment Completion**: Mark appointments as completed and free dock doors
    - **Operational Documentation**: Record completion notes for process improvement
    - **Schedule Management**: Clear doors for immediate reassignment
    - **Resource Optimization**: Maximize dock door utilization through quick turnaround
    - **Quality Control**: Document any issues or observations during appointment completion


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        body (ClearWMSAppointmentFromDoorBody):  Example: {'completionNotes': 'Unloading completed
            successfully. Minor delay due to trailer seal issues.'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ClearWMSAppointmentFromDoorResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            door_id=door_id,
            client=client,
            body=body,
        )
    ).parsed
