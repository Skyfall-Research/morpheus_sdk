import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_available_dock_doors_response_200 import GetTMSAvailableDockDoorsResponse200
from ...types import UNSET, Response


def _get_kwargs(
    world_id: str,
    *,
    dc_id: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["dcId"] = dc_id

    json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/dock-doors/available",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSAvailableDockDoorsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]:
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
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Response[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]:
    """Get available dock doors for time period


    ## Get Available TMS Dock Doors

    Retrieve available dock doors for a specific distribution center and time period to support
    appointment scheduling and dock capacity management.

    ### Features
    - **Real-Time Availability**: Find open dock doors based on current schedules
    - **Time Window Analysis**: Check availability for specific time ranges
    - **Conflict Detection**: Automatically exclude doors occupied by existing appointments
    - **Capacity Planning**: Support resource allocation and scheduling decisions
    - **Standards Compliance**: Returns standardized dock door identifiers

    ### Business Logic
    - Analyzes trailers with status AT_DOCK or UNLOADING within the time window
    - Considers scheduled arrival and departure time overlaps
    - Handles edge cases for appointments without departure times (assumes 8-hour default)
    - Returns dock door identifiers in standard format (DOCK-01 through DOCK-20)
    - Excludes doors with active or overlapping appointments

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific availability
    - **startTime**: Required - Beginning of availability window in ISO 8601 format
    - **endTime**: Required - End of availability window in ISO 8601 format

    ### Use Cases
    - **Appointment Scheduling**: Find available slots during trailer booking
    - **Dock Capacity Management**: Monitor and plan dock utilization
    - **Resource Allocation**: Optimize dock assignments for operational efficiency
    - **Real-time Dashboards**: Display current availability status
    - **Conflict Prevention**: Avoid double-booking dock resources


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        start_time (datetime.datetime):  Example: 2024-01-20T08:00:00.000Z.
        end_time (datetime.datetime):  Example: 2024-01-20T18:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
        start_time=start_time,
        end_time=end_time,
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
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Optional[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]:
    """Get available dock doors for time period


    ## Get Available TMS Dock Doors

    Retrieve available dock doors for a specific distribution center and time period to support
    appointment scheduling and dock capacity management.

    ### Features
    - **Real-Time Availability**: Find open dock doors based on current schedules
    - **Time Window Analysis**: Check availability for specific time ranges
    - **Conflict Detection**: Automatically exclude doors occupied by existing appointments
    - **Capacity Planning**: Support resource allocation and scheduling decisions
    - **Standards Compliance**: Returns standardized dock door identifiers

    ### Business Logic
    - Analyzes trailers with status AT_DOCK or UNLOADING within the time window
    - Considers scheduled arrival and departure time overlaps
    - Handles edge cases for appointments without departure times (assumes 8-hour default)
    - Returns dock door identifiers in standard format (DOCK-01 through DOCK-20)
    - Excludes doors with active or overlapping appointments

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific availability
    - **startTime**: Required - Beginning of availability window in ISO 8601 format
    - **endTime**: Required - End of availability window in ISO 8601 format

    ### Use Cases
    - **Appointment Scheduling**: Find available slots during trailer booking
    - **Dock Capacity Management**: Monitor and plan dock utilization
    - **Resource Allocation**: Optimize dock assignments for operational efficiency
    - **Real-time Dashboards**: Display current availability status
    - **Conflict Prevention**: Avoid double-booking dock resources


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        start_time (datetime.datetime):  Example: 2024-01-20T08:00:00.000Z.
        end_time (datetime.datetime):  Example: 2024-01-20T18:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        dc_id=dc_id,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dc_id: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Response[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]:
    """Get available dock doors for time period


    ## Get Available TMS Dock Doors

    Retrieve available dock doors for a specific distribution center and time period to support
    appointment scheduling and dock capacity management.

    ### Features
    - **Real-Time Availability**: Find open dock doors based on current schedules
    - **Time Window Analysis**: Check availability for specific time ranges
    - **Conflict Detection**: Automatically exclude doors occupied by existing appointments
    - **Capacity Planning**: Support resource allocation and scheduling decisions
    - **Standards Compliance**: Returns standardized dock door identifiers

    ### Business Logic
    - Analyzes trailers with status AT_DOCK or UNLOADING within the time window
    - Considers scheduled arrival and departure time overlaps
    - Handles edge cases for appointments without departure times (assumes 8-hour default)
    - Returns dock door identifiers in standard format (DOCK-01 through DOCK-20)
    - Excludes doors with active or overlapping appointments

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific availability
    - **startTime**: Required - Beginning of availability window in ISO 8601 format
    - **endTime**: Required - End of availability window in ISO 8601 format

    ### Use Cases
    - **Appointment Scheduling**: Find available slots during trailer booking
    - **Dock Capacity Management**: Monitor and plan dock utilization
    - **Resource Allocation**: Optimize dock assignments for operational efficiency
    - **Real-time Dashboards**: Display current availability status
    - **Conflict Prevention**: Avoid double-booking dock resources


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        start_time (datetime.datetime):  Example: 2024-01-20T08:00:00.000Z.
        end_time (datetime.datetime):  Example: 2024-01-20T18:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
        start_time=start_time,
        end_time=end_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    dc_id: str,
    start_time: datetime.datetime,
    end_time: datetime.datetime,
) -> Optional[Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]]:
    """Get available dock doors for time period


    ## Get Available TMS Dock Doors

    Retrieve available dock doors for a specific distribution center and time period to support
    appointment scheduling and dock capacity management.

    ### Features
    - **Real-Time Availability**: Find open dock doors based on current schedules
    - **Time Window Analysis**: Check availability for specific time ranges
    - **Conflict Detection**: Automatically exclude doors occupied by existing appointments
    - **Capacity Planning**: Support resource allocation and scheduling decisions
    - **Standards Compliance**: Returns standardized dock door identifiers

    ### Business Logic
    - Analyzes trailers with status AT_DOCK or UNLOADING within the time window
    - Considers scheduled arrival and departure time overlaps
    - Handles edge cases for appointments without departure times (assumes 8-hour default)
    - Returns dock door identifiers in standard format (DOCK-01 through DOCK-20)
    - Excludes doors with active or overlapping appointments

    ### Query Parameters
    - **dcId**: Required - Distribution center identifier for facility-specific availability
    - **startTime**: Required - Beginning of availability window in ISO 8601 format
    - **endTime**: Required - End of availability window in ISO 8601 format

    ### Use Cases
    - **Appointment Scheduling**: Find available slots during trailer booking
    - **Dock Capacity Management**: Monitor and plan dock utilization
    - **Resource Allocation**: Optimize dock assignments for operational efficiency
    - **Real-time Dashboards**: Display current availability status
    - **Conflict Prevention**: Avoid double-booking dock resources


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: DC_ATL_001.
        start_time (datetime.datetime):  Example: 2024-01-20T08:00:00.000Z.
        end_time (datetime.datetime):  Example: 2024-01-20T18:00:00.000Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSAvailableDockDoorsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            dc_id=dc_id,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
