from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_inbound_trailer_by_id_response_200 import GetTMSInboundTrailerByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/trailers/{trailer_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSInboundTrailerByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]:
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
) -> Response[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]:
    """Get trailer by ID


    ## Get TMS Trailer by ID

    Retrieve complete trailer information using the unique trailer identifier for detailed operations
    management.

    ### Features
    - **Complete Trailer Profile**: Full trailer details including identification, status, and
    operational data
    - **Carrier Information**: Comprehensive carrier and driver contact details for coordination
    - **Cargo Manifest**: Purchase orders, expected deliveries, and freight specifications
    - **Appointment Details**: Scheduling information, dock assignments, and timing data
    - **Status Tracking**: Current operational status and historical progression
    - **Facility Assignment**: Distribution center and dock door information

    ### Response Data Includes
    - **Identification**: Trailer ID, trailer number, and system identifiers
    - **Status**: Current operational status and last update timestamp
    - **Carrier Details**: Carrier ID, company name, driver name and contact
    - **Appointment Info**: Scheduled/actual arrival/departure, dock assignments
    - **Facility Info**: Distribution center details and address information
    - **Cargo**: Purchase orders, pallet counts, trailer type, seal numbers
    - **Operational Timestamps**: Created, updated, and status change times

    ### Use Cases
    - **Status Verification**: Check current trailer status and location
    - **Driver Coordination**: Access driver contact information for communication
    - **Dock Planning**: Review appointment details for dock scheduling
    - **Cargo Tracking**: Verify expected deliveries and purchase orders
    - **Operational Monitoring**: Track trailer progress through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]
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
) -> Optional[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]:
    """Get trailer by ID


    ## Get TMS Trailer by ID

    Retrieve complete trailer information using the unique trailer identifier for detailed operations
    management.

    ### Features
    - **Complete Trailer Profile**: Full trailer details including identification, status, and
    operational data
    - **Carrier Information**: Comprehensive carrier and driver contact details for coordination
    - **Cargo Manifest**: Purchase orders, expected deliveries, and freight specifications
    - **Appointment Details**: Scheduling information, dock assignments, and timing data
    - **Status Tracking**: Current operational status and historical progression
    - **Facility Assignment**: Distribution center and dock door information

    ### Response Data Includes
    - **Identification**: Trailer ID, trailer number, and system identifiers
    - **Status**: Current operational status and last update timestamp
    - **Carrier Details**: Carrier ID, company name, driver name and contact
    - **Appointment Info**: Scheduled/actual arrival/departure, dock assignments
    - **Facility Info**: Distribution center details and address information
    - **Cargo**: Purchase orders, pallet counts, trailer type, seal numbers
    - **Operational Timestamps**: Created, updated, and status change times

    ### Use Cases
    - **Status Verification**: Check current trailer status and location
    - **Driver Coordination**: Access driver contact information for communication
    - **Dock Planning**: Review appointment details for dock scheduling
    - **Cargo Tracking**: Verify expected deliveries and purchase orders
    - **Operational Monitoring**: Track trailer progress through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]
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
) -> Response[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]:
    """Get trailer by ID


    ## Get TMS Trailer by ID

    Retrieve complete trailer information using the unique trailer identifier for detailed operations
    management.

    ### Features
    - **Complete Trailer Profile**: Full trailer details including identification, status, and
    operational data
    - **Carrier Information**: Comprehensive carrier and driver contact details for coordination
    - **Cargo Manifest**: Purchase orders, expected deliveries, and freight specifications
    - **Appointment Details**: Scheduling information, dock assignments, and timing data
    - **Status Tracking**: Current operational status and historical progression
    - **Facility Assignment**: Distribution center and dock door information

    ### Response Data Includes
    - **Identification**: Trailer ID, trailer number, and system identifiers
    - **Status**: Current operational status and last update timestamp
    - **Carrier Details**: Carrier ID, company name, driver name and contact
    - **Appointment Info**: Scheduled/actual arrival/departure, dock assignments
    - **Facility Info**: Distribution center details and address information
    - **Cargo**: Purchase orders, pallet counts, trailer type, seal numbers
    - **Operational Timestamps**: Created, updated, and status change times

    ### Use Cases
    - **Status Verification**: Check current trailer status and location
    - **Driver Coordination**: Access driver contact information for communication
    - **Dock Planning**: Review appointment details for dock scheduling
    - **Cargo Tracking**: Verify expected deliveries and purchase orders
    - **Operational Monitoring**: Track trailer progress through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]
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
) -> Optional[Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]]:
    """Get trailer by ID


    ## Get TMS Trailer by ID

    Retrieve complete trailer information using the unique trailer identifier for detailed operations
    management.

    ### Features
    - **Complete Trailer Profile**: Full trailer details including identification, status, and
    operational data
    - **Carrier Information**: Comprehensive carrier and driver contact details for coordination
    - **Cargo Manifest**: Purchase orders, expected deliveries, and freight specifications
    - **Appointment Details**: Scheduling information, dock assignments, and timing data
    - **Status Tracking**: Current operational status and historical progression
    - **Facility Assignment**: Distribution center and dock door information

    ### Response Data Includes
    - **Identification**: Trailer ID, trailer number, and system identifiers
    - **Status**: Current operational status and last update timestamp
    - **Carrier Details**: Carrier ID, company name, driver name and contact
    - **Appointment Info**: Scheduled/actual arrival/departure, dock assignments
    - **Facility Info**: Distribution center details and address information
    - **Cargo**: Purchase orders, pallet counts, trailer type, seal numbers
    - **Operational Timestamps**: Created, updated, and status change times

    ### Use Cases
    - **Status Verification**: Check current trailer status and location
    - **Driver Coordination**: Access driver contact information for communication
    - **Dock Planning**: Review appointment details for dock scheduling
    - **Cargo Tracking**: Verify expected deliveries and purchase orders
    - **Operational Monitoring**: Track trailer progress through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSInboundTrailerByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
        )
    ).parsed
