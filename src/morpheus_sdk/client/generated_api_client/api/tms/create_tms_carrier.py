from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.tms_carrier_input import TMSCarrierInput
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: TMSCarrierInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/carriers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
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
    body: TMSCarrierInput,
) -> Response[ErrorResponse]:
    """Create a new TMS carrier


    ## Create TMS Carrier

    Register a new carrier in the Transportation Management System with complete profile and compliance
    information.

    ### Features
    - **Complete Carrier Profile**: Business details, contact info, and operational capabilities
    - **Compliance Tracking**: DOT numbers, insurance, safety ratings, and certifications
    - **Service Region Management**: Define geographical service areas
    - **Performance Initialization**: Set up performance tracking metrics
    - **Automatic Validation**: Ensure unique carrier IDs and codes

    ### Required Fields
    - carrierCode: Unique business identifier (SCAC or internal code)
    - carrierName: Official business name
    - carrierType: Transportation mode and service type

    ### Carrier Types
    - **LTL**: Less Than Truckload
    - **FTL**: Full Truckload
    - **PARCEL**: Small package delivery
    - **INTERMODAL**: Rail/truck combination
    - **COURIER**: Express/overnight
    - **RAIL**: Rail transportation
    - **AIR**: Air freight
    - **OCEAN**: Ocean/maritime


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSCarrierInput): Input data for creating or updating a TMS carrier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    body: TMSCarrierInput,
) -> Optional[ErrorResponse]:
    """Create a new TMS carrier


    ## Create TMS Carrier

    Register a new carrier in the Transportation Management System with complete profile and compliance
    information.

    ### Features
    - **Complete Carrier Profile**: Business details, contact info, and operational capabilities
    - **Compliance Tracking**: DOT numbers, insurance, safety ratings, and certifications
    - **Service Region Management**: Define geographical service areas
    - **Performance Initialization**: Set up performance tracking metrics
    - **Automatic Validation**: Ensure unique carrier IDs and codes

    ### Required Fields
    - carrierCode: Unique business identifier (SCAC or internal code)
    - carrierName: Official business name
    - carrierType: Transportation mode and service type

    ### Carrier Types
    - **LTL**: Less Than Truckload
    - **FTL**: Full Truckload
    - **PARCEL**: Small package delivery
    - **INTERMODAL**: Rail/truck combination
    - **COURIER**: Express/overnight
    - **RAIL**: Rail transportation
    - **AIR**: Air freight
    - **OCEAN**: Ocean/maritime


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSCarrierInput): Input data for creating or updating a TMS carrier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
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
    body: TMSCarrierInput,
) -> Response[ErrorResponse]:
    """Create a new TMS carrier


    ## Create TMS Carrier

    Register a new carrier in the Transportation Management System with complete profile and compliance
    information.

    ### Features
    - **Complete Carrier Profile**: Business details, contact info, and operational capabilities
    - **Compliance Tracking**: DOT numbers, insurance, safety ratings, and certifications
    - **Service Region Management**: Define geographical service areas
    - **Performance Initialization**: Set up performance tracking metrics
    - **Automatic Validation**: Ensure unique carrier IDs and codes

    ### Required Fields
    - carrierCode: Unique business identifier (SCAC or internal code)
    - carrierName: Official business name
    - carrierType: Transportation mode and service type

    ### Carrier Types
    - **LTL**: Less Than Truckload
    - **FTL**: Full Truckload
    - **PARCEL**: Small package delivery
    - **INTERMODAL**: Rail/truck combination
    - **COURIER**: Express/overnight
    - **RAIL**: Rail transportation
    - **AIR**: Air freight
    - **OCEAN**: Ocean/maritime


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSCarrierInput): Input data for creating or updating a TMS carrier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
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
    body: TMSCarrierInput,
) -> Optional[ErrorResponse]:
    """Create a new TMS carrier


    ## Create TMS Carrier

    Register a new carrier in the Transportation Management System with complete profile and compliance
    information.

    ### Features
    - **Complete Carrier Profile**: Business details, contact info, and operational capabilities
    - **Compliance Tracking**: DOT numbers, insurance, safety ratings, and certifications
    - **Service Region Management**: Define geographical service areas
    - **Performance Initialization**: Set up performance tracking metrics
    - **Automatic Validation**: Ensure unique carrier IDs and codes

    ### Required Fields
    - carrierCode: Unique business identifier (SCAC or internal code)
    - carrierName: Official business name
    - carrierType: Transportation mode and service type

    ### Carrier Types
    - **LTL**: Less Than Truckload
    - **FTL**: Full Truckload
    - **PARCEL**: Small package delivery
    - **INTERMODAL**: Rail/truck combination
    - **COURIER**: Express/overnight
    - **RAIL**: Rail transportation
    - **AIR**: Air freight
    - **OCEAN**: Ocean/maritime


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSCarrierInput): Input data for creating or updating a TMS carrier

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
