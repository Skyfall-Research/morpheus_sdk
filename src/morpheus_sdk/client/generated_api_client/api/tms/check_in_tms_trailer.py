from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.check_in_tms_trailer_body import CheckInTMSTrailerBody
from ...models.check_in_tms_trailer_response_200 import CheckInTMSTrailerResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
    *,
    body: CheckInTMSTrailerBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/checkin",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CheckInTMSTrailerResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CheckInTMSTrailerResponse200.from_dict(response.json())

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
) -> Response[Union[CheckInTMSTrailerResponse200, ErrorResponse]]:
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
    body: CheckInTMSTrailerBody,
) -> Response[Union[CheckInTMSTrailerResponse200, ErrorResponse]]:
    """Check-in trailer at facility


    ## Check-in TMS Trailer

    Register trailer arrival at the facility and complete the check-in process with comprehensive
    verification and documentation.

    ### Features
    - **Arrival Registration**: Record precise actual arrival time for performance tracking
    - **Driver Verification**: Capture and validate driver information and contact details
    - **Security Compliance**: Record and verify seal numbers and trailer condition
    - **Optional Dock Assignment**: Assign dock door during check-in if available
    - **Automatic Status Update**: Updates trailer status to CHECKED_IN
    - **Notification Integration**: Trigger alerts to operations team and stakeholders

    ### Check-in Process Workflow
    1. **Identity Verification**: Verify trailer number against scheduled appointment
    2. **Arrival Documentation**: Record actual arrival time with timestamp precision
    3. **Driver Information**: Capture driver name and contact information for coordination
    4. **Security Check**: Verify seal integrity and record seal number for compliance
    5. **Dock Assignment**: Optionally assign dock door if available and ready
    6. **Status Update**: Update trailer status and notify relevant teams
    7. **Workflow Trigger**: Enable next phase of facility operations

    ### Required Information
    - **actualArrival**: Precise timestamp when trailer arrived at facility (required)

    ### Optional Information
    - **driverName**: Full name of the driver for contact and coordination
    - **driverPhone**: Driver contact number for communication
    - **sealNumber**: Trailer seal number for security verification and compliance
    - **dockDoor**: Dock door assignment if available during check-in

    ### Business Rules
    - actualArrival timestamp is mandatory for all check-ins
    - Driver information updates carrier records for communication
    - Seal verification supports security and compliance requirements
    - Dock assignment during check-in is optional but recommended for efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CheckInTMSTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CheckInTMSTrailerResponse200, ErrorResponse]]
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
    body: CheckInTMSTrailerBody,
) -> Optional[Union[CheckInTMSTrailerResponse200, ErrorResponse]]:
    """Check-in trailer at facility


    ## Check-in TMS Trailer

    Register trailer arrival at the facility and complete the check-in process with comprehensive
    verification and documentation.

    ### Features
    - **Arrival Registration**: Record precise actual arrival time for performance tracking
    - **Driver Verification**: Capture and validate driver information and contact details
    - **Security Compliance**: Record and verify seal numbers and trailer condition
    - **Optional Dock Assignment**: Assign dock door during check-in if available
    - **Automatic Status Update**: Updates trailer status to CHECKED_IN
    - **Notification Integration**: Trigger alerts to operations team and stakeholders

    ### Check-in Process Workflow
    1. **Identity Verification**: Verify trailer number against scheduled appointment
    2. **Arrival Documentation**: Record actual arrival time with timestamp precision
    3. **Driver Information**: Capture driver name and contact information for coordination
    4. **Security Check**: Verify seal integrity and record seal number for compliance
    5. **Dock Assignment**: Optionally assign dock door if available and ready
    6. **Status Update**: Update trailer status and notify relevant teams
    7. **Workflow Trigger**: Enable next phase of facility operations

    ### Required Information
    - **actualArrival**: Precise timestamp when trailer arrived at facility (required)

    ### Optional Information
    - **driverName**: Full name of the driver for contact and coordination
    - **driverPhone**: Driver contact number for communication
    - **sealNumber**: Trailer seal number for security verification and compliance
    - **dockDoor**: Dock door assignment if available during check-in

    ### Business Rules
    - actualArrival timestamp is mandatory for all check-ins
    - Driver information updates carrier records for communication
    - Seal verification supports security and compliance requirements
    - Dock assignment during check-in is optional but recommended for efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CheckInTMSTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CheckInTMSTrailerResponse200, ErrorResponse]
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
    body: CheckInTMSTrailerBody,
) -> Response[Union[CheckInTMSTrailerResponse200, ErrorResponse]]:
    """Check-in trailer at facility


    ## Check-in TMS Trailer

    Register trailer arrival at the facility and complete the check-in process with comprehensive
    verification and documentation.

    ### Features
    - **Arrival Registration**: Record precise actual arrival time for performance tracking
    - **Driver Verification**: Capture and validate driver information and contact details
    - **Security Compliance**: Record and verify seal numbers and trailer condition
    - **Optional Dock Assignment**: Assign dock door during check-in if available
    - **Automatic Status Update**: Updates trailer status to CHECKED_IN
    - **Notification Integration**: Trigger alerts to operations team and stakeholders

    ### Check-in Process Workflow
    1. **Identity Verification**: Verify trailer number against scheduled appointment
    2. **Arrival Documentation**: Record actual arrival time with timestamp precision
    3. **Driver Information**: Capture driver name and contact information for coordination
    4. **Security Check**: Verify seal integrity and record seal number for compliance
    5. **Dock Assignment**: Optionally assign dock door if available and ready
    6. **Status Update**: Update trailer status and notify relevant teams
    7. **Workflow Trigger**: Enable next phase of facility operations

    ### Required Information
    - **actualArrival**: Precise timestamp when trailer arrived at facility (required)

    ### Optional Information
    - **driverName**: Full name of the driver for contact and coordination
    - **driverPhone**: Driver contact number for communication
    - **sealNumber**: Trailer seal number for security verification and compliance
    - **dockDoor**: Dock door assignment if available during check-in

    ### Business Rules
    - actualArrival timestamp is mandatory for all check-ins
    - Driver information updates carrier records for communication
    - Seal verification supports security and compliance requirements
    - Dock assignment during check-in is optional but recommended for efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CheckInTMSTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CheckInTMSTrailerResponse200, ErrorResponse]]
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
    body: CheckInTMSTrailerBody,
) -> Optional[Union[CheckInTMSTrailerResponse200, ErrorResponse]]:
    """Check-in trailer at facility


    ## Check-in TMS Trailer

    Register trailer arrival at the facility and complete the check-in process with comprehensive
    verification and documentation.

    ### Features
    - **Arrival Registration**: Record precise actual arrival time for performance tracking
    - **Driver Verification**: Capture and validate driver information and contact details
    - **Security Compliance**: Record and verify seal numbers and trailer condition
    - **Optional Dock Assignment**: Assign dock door during check-in if available
    - **Automatic Status Update**: Updates trailer status to CHECKED_IN
    - **Notification Integration**: Trigger alerts to operations team and stakeholders

    ### Check-in Process Workflow
    1. **Identity Verification**: Verify trailer number against scheduled appointment
    2. **Arrival Documentation**: Record actual arrival time with timestamp precision
    3. **Driver Information**: Capture driver name and contact information for coordination
    4. **Security Check**: Verify seal integrity and record seal number for compliance
    5. **Dock Assignment**: Optionally assign dock door if available and ready
    6. **Status Update**: Update trailer status and notify relevant teams
    7. **Workflow Trigger**: Enable next phase of facility operations

    ### Required Information
    - **actualArrival**: Precise timestamp when trailer arrived at facility (required)

    ### Optional Information
    - **driverName**: Full name of the driver for contact and coordination
    - **driverPhone**: Driver contact number for communication
    - **sealNumber**: Trailer seal number for security verification and compliance
    - **dockDoor**: Dock door assignment if available during check-in

    ### Business Rules
    - actualArrival timestamp is mandatory for all check-ins
    - Driver information updates carrier records for communication
    - Seal verification supports security and compliance requirements
    - Dock assignment during check-in is optional but recommended for efficiency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CheckInTMSTrailerBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CheckInTMSTrailerResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
            body=body,
        )
    ).parsed
