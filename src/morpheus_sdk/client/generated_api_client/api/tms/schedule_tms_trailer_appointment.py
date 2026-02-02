from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.schedule_tms_trailer_appointment_body import ScheduleTMSTrailerAppointmentBody
from ...models.schedule_tms_trailer_appointment_response_200 import ScheduleTMSTrailerAppointmentResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
    *,
    body: ScheduleTMSTrailerAppointmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/schedule",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]:
    if response.status_code == 200:
        response_200 = ScheduleTMSTrailerAppointmentResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]:
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
    body: ScheduleTMSTrailerAppointmentBody,
) -> Response[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]:
    """Schedule trailer appointment


    ## Schedule TMS Trailer Appointment

    Schedule or reschedule a trailer appointment with dock assignment and timing details.

    ### Features
    - **Appointment Management**: Schedule arrival and departure times
    - **Dock Assignment**: Assign specific dock doors for operations
    - **Facility Coordination**: Link with distribution center operations
    - **Status Update**: Automatically updates trailer status to SCHEDULED
    - **Validation**: Ensures trailer is in valid status for scheduling

    ### Business Rules
    - Trailer must be in SCHEDULED or EN_ROUTE status
    - Scheduled arrival time is required
    - Distribution center ID must be provided
    - Appointment ID is auto-generated if not provided
    - Dock door assignment is optional during scheduling

    ### Workflow Integration
    - Updates trailer status to SCHEDULED
    - Triggers facility notification systems
    - Updates capacity planning calculations
    - Enables driver communication workflows


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (ScheduleTMSTrailerAppointmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]
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
    body: ScheduleTMSTrailerAppointmentBody,
) -> Optional[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]:
    """Schedule trailer appointment


    ## Schedule TMS Trailer Appointment

    Schedule or reschedule a trailer appointment with dock assignment and timing details.

    ### Features
    - **Appointment Management**: Schedule arrival and departure times
    - **Dock Assignment**: Assign specific dock doors for operations
    - **Facility Coordination**: Link with distribution center operations
    - **Status Update**: Automatically updates trailer status to SCHEDULED
    - **Validation**: Ensures trailer is in valid status for scheduling

    ### Business Rules
    - Trailer must be in SCHEDULED or EN_ROUTE status
    - Scheduled arrival time is required
    - Distribution center ID must be provided
    - Appointment ID is auto-generated if not provided
    - Dock door assignment is optional during scheduling

    ### Workflow Integration
    - Updates trailer status to SCHEDULED
    - Triggers facility notification systems
    - Updates capacity planning calculations
    - Enables driver communication workflows


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (ScheduleTMSTrailerAppointmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]
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
    body: ScheduleTMSTrailerAppointmentBody,
) -> Response[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]:
    """Schedule trailer appointment


    ## Schedule TMS Trailer Appointment

    Schedule or reschedule a trailer appointment with dock assignment and timing details.

    ### Features
    - **Appointment Management**: Schedule arrival and departure times
    - **Dock Assignment**: Assign specific dock doors for operations
    - **Facility Coordination**: Link with distribution center operations
    - **Status Update**: Automatically updates trailer status to SCHEDULED
    - **Validation**: Ensures trailer is in valid status for scheduling

    ### Business Rules
    - Trailer must be in SCHEDULED or EN_ROUTE status
    - Scheduled arrival time is required
    - Distribution center ID must be provided
    - Appointment ID is auto-generated if not provided
    - Dock door assignment is optional during scheduling

    ### Workflow Integration
    - Updates trailer status to SCHEDULED
    - Triggers facility notification systems
    - Updates capacity planning calculations
    - Enables driver communication workflows


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (ScheduleTMSTrailerAppointmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]
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
    body: ScheduleTMSTrailerAppointmentBody,
) -> Optional[Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]]:
    """Schedule trailer appointment


    ## Schedule TMS Trailer Appointment

    Schedule or reschedule a trailer appointment with dock assignment and timing details.

    ### Features
    - **Appointment Management**: Schedule arrival and departure times
    - **Dock Assignment**: Assign specific dock doors for operations
    - **Facility Coordination**: Link with distribution center operations
    - **Status Update**: Automatically updates trailer status to SCHEDULED
    - **Validation**: Ensures trailer is in valid status for scheduling

    ### Business Rules
    - Trailer must be in SCHEDULED or EN_ROUTE status
    - Scheduled arrival time is required
    - Distribution center ID must be provided
    - Appointment ID is auto-generated if not provided
    - Dock door assignment is optional during scheduling

    ### Workflow Integration
    - Updates trailer status to SCHEDULED
    - Triggers facility notification systems
    - Updates capacity planning calculations
    - Enables driver communication workflows


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (ScheduleTMSTrailerAppointmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ScheduleTMSTrailerAppointmentResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
            body=body,
        )
    ).parsed
