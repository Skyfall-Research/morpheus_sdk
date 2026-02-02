from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_tms_trailer_status_body import UpdateTMSTrailerStatusBody
from ...models.update_tms_trailer_status_response_200 import UpdateTMSTrailerStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
    *,
    body: UpdateTMSTrailerStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateTMSTrailerStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]:
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
    body: UpdateTMSTrailerStatusBody,
) -> Response[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]:
    """Update trailer status


    ## Update TMS Trailer Status

    Update the operational status of a trailer with comprehensive timing and location data for complete
    lifecycle tracking.

    ### Features
    - **Status Management**: Control trailer operational state throughout the facility workflow
    - **Timing Updates**: Record actual arrival/departure times with precision
    - **Location Tracking**: Update and manage dock door assignments
    - **Workflow Integration**: Automatically trigger downstream facility processes
    - **Audit Trail**: Maintain complete history of all status changes with timestamps
    - **Data Validation**: Ensure status transitions follow business rules

    ### Valid Status Transitions
    - **SCHEDULED** → **EN_ROUTE**: Carrier confirms trailer has departed for facility
    - **EN_ROUTE** → **CHECKED_IN**: Trailer arrives and checks in at facility gate
    - **CHECKED_IN** → **AT_DOCK**: Trailer assigned and positioned at dock door
    - **AT_DOCK** → **UNLOADING**: Begin active unloading operations
    - **UNLOADING** → **UNLOADED**: Complete unloading process
    - **UNLOADED** → **DEPARTED**: Trailer exits facility
    - **Any Status** → **CANCELLED**: Appointment cancelled
    - **Any Status** → **DELAYED**: Delayed arrival reported

    ### Optional Timing Updates
    - **actualArrival**: Record precise arrival time for performance tracking
    - **actualDeparture**: Record departure time for turnaround analysis
    - **estimatedArrival**: Update arrival estimate for planning adjustments
    - **dockDoor**: Assign or reassign dock door for operational flexibility

    ### Business Rules
    - Status field is required for all updates
    - Timing fields must be valid ISO 8601 date-time strings
    - Dock door assignments must reference valid dock identifiers
    - Status transitions are logged for audit compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (UpdateTMSTrailerStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]
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
    body: UpdateTMSTrailerStatusBody,
) -> Optional[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]:
    """Update trailer status


    ## Update TMS Trailer Status

    Update the operational status of a trailer with comprehensive timing and location data for complete
    lifecycle tracking.

    ### Features
    - **Status Management**: Control trailer operational state throughout the facility workflow
    - **Timing Updates**: Record actual arrival/departure times with precision
    - **Location Tracking**: Update and manage dock door assignments
    - **Workflow Integration**: Automatically trigger downstream facility processes
    - **Audit Trail**: Maintain complete history of all status changes with timestamps
    - **Data Validation**: Ensure status transitions follow business rules

    ### Valid Status Transitions
    - **SCHEDULED** → **EN_ROUTE**: Carrier confirms trailer has departed for facility
    - **EN_ROUTE** → **CHECKED_IN**: Trailer arrives and checks in at facility gate
    - **CHECKED_IN** → **AT_DOCK**: Trailer assigned and positioned at dock door
    - **AT_DOCK** → **UNLOADING**: Begin active unloading operations
    - **UNLOADING** → **UNLOADED**: Complete unloading process
    - **UNLOADED** → **DEPARTED**: Trailer exits facility
    - **Any Status** → **CANCELLED**: Appointment cancelled
    - **Any Status** → **DELAYED**: Delayed arrival reported

    ### Optional Timing Updates
    - **actualArrival**: Record precise arrival time for performance tracking
    - **actualDeparture**: Record departure time for turnaround analysis
    - **estimatedArrival**: Update arrival estimate for planning adjustments
    - **dockDoor**: Assign or reassign dock door for operational flexibility

    ### Business Rules
    - Status field is required for all updates
    - Timing fields must be valid ISO 8601 date-time strings
    - Dock door assignments must reference valid dock identifiers
    - Status transitions are logged for audit compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (UpdateTMSTrailerStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]
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
    body: UpdateTMSTrailerStatusBody,
) -> Response[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]:
    """Update trailer status


    ## Update TMS Trailer Status

    Update the operational status of a trailer with comprehensive timing and location data for complete
    lifecycle tracking.

    ### Features
    - **Status Management**: Control trailer operational state throughout the facility workflow
    - **Timing Updates**: Record actual arrival/departure times with precision
    - **Location Tracking**: Update and manage dock door assignments
    - **Workflow Integration**: Automatically trigger downstream facility processes
    - **Audit Trail**: Maintain complete history of all status changes with timestamps
    - **Data Validation**: Ensure status transitions follow business rules

    ### Valid Status Transitions
    - **SCHEDULED** → **EN_ROUTE**: Carrier confirms trailer has departed for facility
    - **EN_ROUTE** → **CHECKED_IN**: Trailer arrives and checks in at facility gate
    - **CHECKED_IN** → **AT_DOCK**: Trailer assigned and positioned at dock door
    - **AT_DOCK** → **UNLOADING**: Begin active unloading operations
    - **UNLOADING** → **UNLOADED**: Complete unloading process
    - **UNLOADED** → **DEPARTED**: Trailer exits facility
    - **Any Status** → **CANCELLED**: Appointment cancelled
    - **Any Status** → **DELAYED**: Delayed arrival reported

    ### Optional Timing Updates
    - **actualArrival**: Record precise arrival time for performance tracking
    - **actualDeparture**: Record departure time for turnaround analysis
    - **estimatedArrival**: Update arrival estimate for planning adjustments
    - **dockDoor**: Assign or reassign dock door for operational flexibility

    ### Business Rules
    - Status field is required for all updates
    - Timing fields must be valid ISO 8601 date-time strings
    - Dock door assignments must reference valid dock identifiers
    - Status transitions are logged for audit compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (UpdateTMSTrailerStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]
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
    body: UpdateTMSTrailerStatusBody,
) -> Optional[Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]]:
    """Update trailer status


    ## Update TMS Trailer Status

    Update the operational status of a trailer with comprehensive timing and location data for complete
    lifecycle tracking.

    ### Features
    - **Status Management**: Control trailer operational state throughout the facility workflow
    - **Timing Updates**: Record actual arrival/departure times with precision
    - **Location Tracking**: Update and manage dock door assignments
    - **Workflow Integration**: Automatically trigger downstream facility processes
    - **Audit Trail**: Maintain complete history of all status changes with timestamps
    - **Data Validation**: Ensure status transitions follow business rules

    ### Valid Status Transitions
    - **SCHEDULED** → **EN_ROUTE**: Carrier confirms trailer has departed for facility
    - **EN_ROUTE** → **CHECKED_IN**: Trailer arrives and checks in at facility gate
    - **CHECKED_IN** → **AT_DOCK**: Trailer assigned and positioned at dock door
    - **AT_DOCK** → **UNLOADING**: Begin active unloading operations
    - **UNLOADING** → **UNLOADED**: Complete unloading process
    - **UNLOADED** → **DEPARTED**: Trailer exits facility
    - **Any Status** → **CANCELLED**: Appointment cancelled
    - **Any Status** → **DELAYED**: Delayed arrival reported

    ### Optional Timing Updates
    - **actualArrival**: Record precise arrival time for performance tracking
    - **actualDeparture**: Record departure time for turnaround analysis
    - **estimatedArrival**: Update arrival estimate for planning adjustments
    - **dockDoor**: Assign or reassign dock door for operational flexibility

    ### Business Rules
    - Status field is required for all updates
    - Timing fields must be valid ISO 8601 date-time strings
    - Dock door assignments must reference valid dock identifiers
    - Status transitions are logged for audit compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (UpdateTMSTrailerStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateTMSTrailerStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
            body=body,
        )
    ).parsed
