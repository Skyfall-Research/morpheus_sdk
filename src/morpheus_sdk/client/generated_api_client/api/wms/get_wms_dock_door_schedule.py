import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_dock_door_schedule_response_200 import GetWMSDockDoorScheduleResponse200
from ...types import UNSET, Response


def _get_kwargs(
    world_id: str,
    *,
    dock_door_id: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["dockDoorId"] = dock_door_id

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/dock-doors/schedule",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDockDoorScheduleResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dock_door_id: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]:
    """Get dock door schedule


    ## Get WMS Dock Door Schedule

    Retrieve appointment schedule for a specific dock door within a date range, providing comprehensive
    scheduling information for operational coordination.

    ### Features
    - **Schedule Visibility**: Complete appointment schedule for specified dock door
    - **Date Range Filtering**: Appointments within specified time periods
    - **Appointment Details**: Carrier, trailer, timing, and status information
    - **Operational Coordination**: Support for appointment management and resource planning
    - **Schedule Conflicts**: Identify potential scheduling conflicts and overlaps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - from and to parameters define the schedule query date range
    - Returns appointments with start times falling within the specified range
    - Includes appointment type classification and current status
    - Handles cases where doors have no appointments (empty array)
    - Future implementation will support complex appointment scheduling systems

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door (in route context)

    ### Query Parameters
    - **from**: Required - Schedule start date and time (ISO 8601)
    - **to**: Required - Schedule end date and time (ISO 8601)

    ### Response Fields
    - **appointmentId**: Unique appointment identifier for tracking
    - **carrierName**: Carrier company responsible for the appointment
    - **trailerNumber**: Trailer identification for operational coordination
    - **scheduledArrival**: Planned arrival time for resource preparation
    - **appointmentType**: Classification of appointment (SCHEDULED, EMERGENCY, etc.)
    - **status**: Current appointment status for operational awareness

    ### Use Cases
    - **Schedule Management**: View comprehensive appointment schedules for planning
    - **Resource Coordination**: Prepare resources based on scheduled appointments
    - **Conflict Resolution**: Identify and resolve scheduling conflicts
    - **Operational Planning**: Coordinate warehouse activities with appointment timing
    - **Performance Monitoring**: Track appointment adherence and operational efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dock_door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        from_ (datetime.datetime):  Example: 2024-11-27T00:00:00Z.
        to (datetime.datetime):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dock_door_id=dock_door_id,
        from_=from_,
        to=to,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dock_door_id: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Optional[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]:
    """Get dock door schedule


    ## Get WMS Dock Door Schedule

    Retrieve appointment schedule for a specific dock door within a date range, providing comprehensive
    scheduling information for operational coordination.

    ### Features
    - **Schedule Visibility**: Complete appointment schedule for specified dock door
    - **Date Range Filtering**: Appointments within specified time periods
    - **Appointment Details**: Carrier, trailer, timing, and status information
    - **Operational Coordination**: Support for appointment management and resource planning
    - **Schedule Conflicts**: Identify potential scheduling conflicts and overlaps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - from and to parameters define the schedule query date range
    - Returns appointments with start times falling within the specified range
    - Includes appointment type classification and current status
    - Handles cases where doors have no appointments (empty array)
    - Future implementation will support complex appointment scheduling systems

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door (in route context)

    ### Query Parameters
    - **from**: Required - Schedule start date and time (ISO 8601)
    - **to**: Required - Schedule end date and time (ISO 8601)

    ### Response Fields
    - **appointmentId**: Unique appointment identifier for tracking
    - **carrierName**: Carrier company responsible for the appointment
    - **trailerNumber**: Trailer identification for operational coordination
    - **scheduledArrival**: Planned arrival time for resource preparation
    - **appointmentType**: Classification of appointment (SCHEDULED, EMERGENCY, etc.)
    - **status**: Current appointment status for operational awareness

    ### Use Cases
    - **Schedule Management**: View comprehensive appointment schedules for planning
    - **Resource Coordination**: Prepare resources based on scheduled appointments
    - **Conflict Resolution**: Identify and resolve scheduling conflicts
    - **Operational Planning**: Coordinate warehouse activities with appointment timing
    - **Performance Monitoring**: Track appointment adherence and operational efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dock_door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        from_ (datetime.datetime):  Example: 2024-11-27T00:00:00Z.
        to (datetime.datetime):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        dock_door_id=dock_door_id,
        from_=from_,
        to=to,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dock_door_id: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Response[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]:
    """Get dock door schedule


    ## Get WMS Dock Door Schedule

    Retrieve appointment schedule for a specific dock door within a date range, providing comprehensive
    scheduling information for operational coordination.

    ### Features
    - **Schedule Visibility**: Complete appointment schedule for specified dock door
    - **Date Range Filtering**: Appointments within specified time periods
    - **Appointment Details**: Carrier, trailer, timing, and status information
    - **Operational Coordination**: Support for appointment management and resource planning
    - **Schedule Conflicts**: Identify potential scheduling conflicts and overlaps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - from and to parameters define the schedule query date range
    - Returns appointments with start times falling within the specified range
    - Includes appointment type classification and current status
    - Handles cases where doors have no appointments (empty array)
    - Future implementation will support complex appointment scheduling systems

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door (in route context)

    ### Query Parameters
    - **from**: Required - Schedule start date and time (ISO 8601)
    - **to**: Required - Schedule end date and time (ISO 8601)

    ### Response Fields
    - **appointmentId**: Unique appointment identifier for tracking
    - **carrierName**: Carrier company responsible for the appointment
    - **trailerNumber**: Trailer identification for operational coordination
    - **scheduledArrival**: Planned arrival time for resource preparation
    - **appointmentType**: Classification of appointment (SCHEDULED, EMERGENCY, etc.)
    - **status**: Current appointment status for operational awareness

    ### Use Cases
    - **Schedule Management**: View comprehensive appointment schedules for planning
    - **Resource Coordination**: Prepare resources based on scheduled appointments
    - **Conflict Resolution**: Identify and resolve scheduling conflicts
    - **Operational Planning**: Coordinate warehouse activities with appointment timing
    - **Performance Monitoring**: Track appointment adherence and operational efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dock_door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        from_ (datetime.datetime):  Example: 2024-11-27T00:00:00Z.
        to (datetime.datetime):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dock_door_id=dock_door_id,
        from_=from_,
        to=to,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dock_door_id: str,
    from_: datetime.datetime,
    to: datetime.datetime,
) -> Optional[Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]]:
    """Get dock door schedule


    ## Get WMS Dock Door Schedule

    Retrieve appointment schedule for a specific dock door within a date range, providing comprehensive
    scheduling information for operational coordination.

    ### Features
    - **Schedule Visibility**: Complete appointment schedule for specified dock door
    - **Date Range Filtering**: Appointments within specified time periods
    - **Appointment Details**: Carrier, trailer, timing, and status information
    - **Operational Coordination**: Support for appointment management and resource planning
    - **Schedule Conflicts**: Identify potential scheduling conflicts and overlaps

    ### Business Logic
    - doorId must reference an existing dock door within the world
    - from and to parameters define the schedule query date range
    - Returns appointments with start times falling within the specified range
    - Includes appointment type classification and current status
    - Handles cases where doors have no appointments (empty array)
    - Future implementation will support complex appointment scheduling systems

    ### Path Parameters
    - **doorId**: Required - Unique identifier for the dock door (in route context)

    ### Query Parameters
    - **from**: Required - Schedule start date and time (ISO 8601)
    - **to**: Required - Schedule end date and time (ISO 8601)

    ### Response Fields
    - **appointmentId**: Unique appointment identifier for tracking
    - **carrierName**: Carrier company responsible for the appointment
    - **trailerNumber**: Trailer identification for operational coordination
    - **scheduledArrival**: Planned arrival time for resource preparation
    - **appointmentType**: Classification of appointment (SCHEDULED, EMERGENCY, etc.)
    - **status**: Current appointment status for operational awareness

    ### Use Cases
    - **Schedule Management**: View comprehensive appointment schedules for planning
    - **Resource Coordination**: Prepare resources based on scheduled appointments
    - **Conflict Resolution**: Identify and resolve scheduling conflicts
    - **Operational Planning**: Coordinate warehouse activities with appointment timing
    - **Performance Monitoring**: Track appointment adherence and operational efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dock_door_id (str):  Example: wms_dock-door_674565c1234567890abcdef.
        from_ (datetime.datetime):  Example: 2024-11-27T00:00:00Z.
        to (datetime.datetime):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorScheduleResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            dock_door_id=dock_door_id,
            from_=from_,
            to=to,
        )
    ).parsed
