from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tms_inbound_trailer_body import CreateTMSInboundTrailerBody
from ...models.create_tms_inbound_trailer_response_201 import CreateTMSInboundTrailerResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateTMSInboundTrailerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateTMSInboundTrailerResponse201.from_dict(response.json())

        return response_201

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
) -> Response[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]:
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
    body: CreateTMSInboundTrailerBody,
) -> Response[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]:
    """Create new inbound trailer


    ## Create TMS Inbound Trailer

    Create a new inbound trailer record for dock appointment scheduling and warehouse operations
    management.

    ### Features
    - **Complete Trailer Profile**: Comprehensive carrier, cargo, and facility information
    - **Appointment Scheduling**: Initial scheduling data with flexible timing options
    - **Status Management**: Automatic status tracking throughout the trailer lifecycle
    - **Cargo Documentation**: Purchase orders, expected freight, and compliance details
    - **Driver Information**: Contact details for communication and coordination

    ### Trailer Lifecycle Status Flow
    1. **SCHEDULED**: Initial creation with appointment details
    2. **EN_ROUTE**: Carrier confirms trailer is in transit to facility
    3. **CHECKED_IN**: Trailer arrives and checks in at facility gate
    4. **AT_DOCK**: Assigned to specific dock door for operations
    5. **UNLOADING**: Active unloading process in progress
    6. **UNLOADED**: Unloading completed, ready for departure
    7. **DEPARTED**: Trailer has left the facility
    8. **CANCELLED**: Appointment cancelled
    9. **DELAYED**: Delayed arrival reported

    ### Required Information
    - **trailerNumber**: Physical trailer identification (license plate/number)
    - **appointmentInfo.scheduledArrival**: Required arrival date and time
    - **facilityInfo.dcId**: Target distribution center identifier

    ### Business Rules
    - trailerId is auto-generated with unique identifier if not provided
    - scheduledArrival is mandatory for all trailer appointments
    - trailerNumber should be unique within the carrier's fleet
    - Status automatically defaults to SCHEDULED upon creation
    - appointmentInfo, facilityInfo, and trailerNumber are required fields
    - carrierInfo and cargo details are optional but recommended for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateTMSInboundTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateTMSInboundTrailerBody,
) -> Optional[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]:
    """Create new inbound trailer


    ## Create TMS Inbound Trailer

    Create a new inbound trailer record for dock appointment scheduling and warehouse operations
    management.

    ### Features
    - **Complete Trailer Profile**: Comprehensive carrier, cargo, and facility information
    - **Appointment Scheduling**: Initial scheduling data with flexible timing options
    - **Status Management**: Automatic status tracking throughout the trailer lifecycle
    - **Cargo Documentation**: Purchase orders, expected freight, and compliance details
    - **Driver Information**: Contact details for communication and coordination

    ### Trailer Lifecycle Status Flow
    1. **SCHEDULED**: Initial creation with appointment details
    2. **EN_ROUTE**: Carrier confirms trailer is in transit to facility
    3. **CHECKED_IN**: Trailer arrives and checks in at facility gate
    4. **AT_DOCK**: Assigned to specific dock door for operations
    5. **UNLOADING**: Active unloading process in progress
    6. **UNLOADED**: Unloading completed, ready for departure
    7. **DEPARTED**: Trailer has left the facility
    8. **CANCELLED**: Appointment cancelled
    9. **DELAYED**: Delayed arrival reported

    ### Required Information
    - **trailerNumber**: Physical trailer identification (license plate/number)
    - **appointmentInfo.scheduledArrival**: Required arrival date and time
    - **facilityInfo.dcId**: Target distribution center identifier

    ### Business Rules
    - trailerId is auto-generated with unique identifier if not provided
    - scheduledArrival is mandatory for all trailer appointments
    - trailerNumber should be unique within the carrier's fleet
    - Status automatically defaults to SCHEDULED upon creation
    - appointmentInfo, facilityInfo, and trailerNumber are required fields
    - carrierInfo and cargo details are optional but recommended for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateTMSInboundTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTMSInboundTrailerResponse201, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateTMSInboundTrailerBody,
) -> Response[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]:
    """Create new inbound trailer


    ## Create TMS Inbound Trailer

    Create a new inbound trailer record for dock appointment scheduling and warehouse operations
    management.

    ### Features
    - **Complete Trailer Profile**: Comprehensive carrier, cargo, and facility information
    - **Appointment Scheduling**: Initial scheduling data with flexible timing options
    - **Status Management**: Automatic status tracking throughout the trailer lifecycle
    - **Cargo Documentation**: Purchase orders, expected freight, and compliance details
    - **Driver Information**: Contact details for communication and coordination

    ### Trailer Lifecycle Status Flow
    1. **SCHEDULED**: Initial creation with appointment details
    2. **EN_ROUTE**: Carrier confirms trailer is in transit to facility
    3. **CHECKED_IN**: Trailer arrives and checks in at facility gate
    4. **AT_DOCK**: Assigned to specific dock door for operations
    5. **UNLOADING**: Active unloading process in progress
    6. **UNLOADED**: Unloading completed, ready for departure
    7. **DEPARTED**: Trailer has left the facility
    8. **CANCELLED**: Appointment cancelled
    9. **DELAYED**: Delayed arrival reported

    ### Required Information
    - **trailerNumber**: Physical trailer identification (license plate/number)
    - **appointmentInfo.scheduledArrival**: Required arrival date and time
    - **facilityInfo.dcId**: Target distribution center identifier

    ### Business Rules
    - trailerId is auto-generated with unique identifier if not provided
    - scheduledArrival is mandatory for all trailer appointments
    - trailerNumber should be unique within the carrier's fleet
    - Status automatically defaults to SCHEDULED upon creation
    - appointmentInfo, facilityInfo, and trailerNumber are required fields
    - carrierInfo and cargo details are optional but recommended for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateTMSInboundTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateTMSInboundTrailerBody,
) -> Optional[Union[CreateTMSInboundTrailerResponse201, ErrorResponse]]:
    """Create new inbound trailer


    ## Create TMS Inbound Trailer

    Create a new inbound trailer record for dock appointment scheduling and warehouse operations
    management.

    ### Features
    - **Complete Trailer Profile**: Comprehensive carrier, cargo, and facility information
    - **Appointment Scheduling**: Initial scheduling data with flexible timing options
    - **Status Management**: Automatic status tracking throughout the trailer lifecycle
    - **Cargo Documentation**: Purchase orders, expected freight, and compliance details
    - **Driver Information**: Contact details for communication and coordination

    ### Trailer Lifecycle Status Flow
    1. **SCHEDULED**: Initial creation with appointment details
    2. **EN_ROUTE**: Carrier confirms trailer is in transit to facility
    3. **CHECKED_IN**: Trailer arrives and checks in at facility gate
    4. **AT_DOCK**: Assigned to specific dock door for operations
    5. **UNLOADING**: Active unloading process in progress
    6. **UNLOADED**: Unloading completed, ready for departure
    7. **DEPARTED**: Trailer has left the facility
    8. **CANCELLED**: Appointment cancelled
    9. **DELAYED**: Delayed arrival reported

    ### Required Information
    - **trailerNumber**: Physical trailer identification (license plate/number)
    - **appointmentInfo.scheduledArrival**: Required arrival date and time
    - **facilityInfo.dcId**: Target distribution center identifier

    ### Business Rules
    - trailerId is auto-generated with unique identifier if not provided
    - scheduledArrival is mandatory for all trailer appointments
    - trailerNumber should be unique within the carrier's fleet
    - Status automatically defaults to SCHEDULED upon creation
    - appointmentInfo, facilityInfo, and trailerNumber are required fields
    - carrierInfo and cargo details are optional but recommended for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateTMSInboundTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTMSInboundTrailerResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
