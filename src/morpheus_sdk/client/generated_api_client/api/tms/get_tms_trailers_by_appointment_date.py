import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_trailers_by_appointment_date_response_200 import GetTMSTrailersByAppointmentDateResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    dc_id: str,
    appointment_date: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["dcId"] = dc_id

    json_appointment_date: Union[Unset, str] = UNSET
    if not isinstance(appointment_date, Unset):
        json_appointment_date = appointment_date.isoformat()
    params["appointmentDate"] = json_appointment_date

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/trailers/appointments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSTrailersByAppointmentDateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]:
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
    dc_id: str,
    appointment_date: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]:
    """Get trailers by appointment date


    ## Get Trailers by Appointment Date

    Retrieve all trailers scheduled for appointments on a specific date at a distribution center,
    organized by appointment time for daily operations planning.

    ### Features
    - **Daily Scheduling View**: Complete view of all trailers for specific appointment dates
    - **Facility-Specific Filtering**: Results filtered by distribution center identifier
    - **Chronological Organization**: Results automatically ordered by scheduled arrival time
    - **Date Flexibility**: Defaults to current date if appointmentDate not specified
    - **Operational Planning**: Support daily dock scheduling and resource allocation
    - **Efficient Pagination**: Handle large appointment volumes with cursor-based pagination

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific results
    - **appointmentDate**: Optional - Target appointment date (defaults to current date)
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient data retrieval

    ### Business Logic
    - Filters trailers by scheduledArrival date matching the requested appointment date
    - Results include all trailer statuses for comprehensive daily view
    - Appointments are sorted chronologically by scheduled arrival time
    - Supports same-day, future date, and historical date queries
    - Returns complete trailer details including status, carrier, and cargo information

    ### Use Cases
    - **Daily Operations**: Comprehensive daily dock scheduling and coordination
    - **Driver Coordination**: Communicate with drivers for scheduled appointments
    - **Capacity Planning**: Analyze and plan daily dock resource allocation
    - **Real-time Monitoring**: Track appointment progress throughout the day
    - **Operations Dashboard**: Display daily appointment schedules and status
    - **Historical Analysis**: Review past appointment performance and patterns


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        appointment_date (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
        appointment_date=appointment_date,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dc_id: str,
    appointment_date: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]:
    """Get trailers by appointment date


    ## Get Trailers by Appointment Date

    Retrieve all trailers scheduled for appointments on a specific date at a distribution center,
    organized by appointment time for daily operations planning.

    ### Features
    - **Daily Scheduling View**: Complete view of all trailers for specific appointment dates
    - **Facility-Specific Filtering**: Results filtered by distribution center identifier
    - **Chronological Organization**: Results automatically ordered by scheduled arrival time
    - **Date Flexibility**: Defaults to current date if appointmentDate not specified
    - **Operational Planning**: Support daily dock scheduling and resource allocation
    - **Efficient Pagination**: Handle large appointment volumes with cursor-based pagination

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific results
    - **appointmentDate**: Optional - Target appointment date (defaults to current date)
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient data retrieval

    ### Business Logic
    - Filters trailers by scheduledArrival date matching the requested appointment date
    - Results include all trailer statuses for comprehensive daily view
    - Appointments are sorted chronologically by scheduled arrival time
    - Supports same-day, future date, and historical date queries
    - Returns complete trailer details including status, carrier, and cargo information

    ### Use Cases
    - **Daily Operations**: Comprehensive daily dock scheduling and coordination
    - **Driver Coordination**: Communicate with drivers for scheduled appointments
    - **Capacity Planning**: Analyze and plan daily dock resource allocation
    - **Real-time Monitoring**: Track appointment progress throughout the day
    - **Operations Dashboard**: Display daily appointment schedules and status
    - **Historical Analysis**: Review past appointment performance and patterns


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        appointment_date (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        dc_id=dc_id,
        appointment_date=appointment_date,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dc_id: str,
    appointment_date: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]:
    """Get trailers by appointment date


    ## Get Trailers by Appointment Date

    Retrieve all trailers scheduled for appointments on a specific date at a distribution center,
    organized by appointment time for daily operations planning.

    ### Features
    - **Daily Scheduling View**: Complete view of all trailers for specific appointment dates
    - **Facility-Specific Filtering**: Results filtered by distribution center identifier
    - **Chronological Organization**: Results automatically ordered by scheduled arrival time
    - **Date Flexibility**: Defaults to current date if appointmentDate not specified
    - **Operational Planning**: Support daily dock scheduling and resource allocation
    - **Efficient Pagination**: Handle large appointment volumes with cursor-based pagination

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific results
    - **appointmentDate**: Optional - Target appointment date (defaults to current date)
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient data retrieval

    ### Business Logic
    - Filters trailers by scheduledArrival date matching the requested appointment date
    - Results include all trailer statuses for comprehensive daily view
    - Appointments are sorted chronologically by scheduled arrival time
    - Supports same-day, future date, and historical date queries
    - Returns complete trailer details including status, carrier, and cargo information

    ### Use Cases
    - **Daily Operations**: Comprehensive daily dock scheduling and coordination
    - **Driver Coordination**: Communicate with drivers for scheduled appointments
    - **Capacity Planning**: Analyze and plan daily dock resource allocation
    - **Real-time Monitoring**: Track appointment progress throughout the day
    - **Operations Dashboard**: Display daily appointment schedules and status
    - **Historical Analysis**: Review past appointment performance and patterns


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        appointment_date (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
        appointment_date=appointment_date,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dc_id: str,
    appointment_date: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]]:
    """Get trailers by appointment date


    ## Get Trailers by Appointment Date

    Retrieve all trailers scheduled for appointments on a specific date at a distribution center,
    organized by appointment time for daily operations planning.

    ### Features
    - **Daily Scheduling View**: Complete view of all trailers for specific appointment dates
    - **Facility-Specific Filtering**: Results filtered by distribution center identifier
    - **Chronological Organization**: Results automatically ordered by scheduled arrival time
    - **Date Flexibility**: Defaults to current date if appointmentDate not specified
    - **Operational Planning**: Support daily dock scheduling and resource allocation
    - **Efficient Pagination**: Handle large appointment volumes with cursor-based pagination

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific results
    - **appointmentDate**: Optional - Target appointment date (defaults to current date)
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient data retrieval

    ### Business Logic
    - Filters trailers by scheduledArrival date matching the requested appointment date
    - Results include all trailer statuses for comprehensive daily view
    - Appointments are sorted chronologically by scheduled arrival time
    - Supports same-day, future date, and historical date queries
    - Returns complete trailer details including status, carrier, and cargo information

    ### Use Cases
    - **Daily Operations**: Comprehensive daily dock scheduling and coordination
    - **Driver Coordination**: Communicate with drivers for scheduled appointments
    - **Capacity Planning**: Analyze and plan daily dock resource allocation
    - **Real-time Monitoring**: Track appointment progress throughout the day
    - **Operations Dashboard**: Display daily appointment schedules and status
    - **Historical Analysis**: Review past appointment performance and patterns


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        appointment_date (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSTrailersByAppointmentDateResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            dc_id=dc_id,
            appointment_date=appointment_date,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
