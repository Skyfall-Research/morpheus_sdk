from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_tms_shipment_location_body import UpdateTMSShipmentLocationBody
from ...models.update_tms_shipment_location_response_200 import UpdateTMSShipmentLocationResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: UpdateTMSShipmentLocationBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/location",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateTMSShipmentLocationResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSShipmentLocationBody,
) -> Response[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]:
    """Update shipment location


    ## Update Shipment Location

    Update the current location of a shipment with GPS coordinates and optional location details.

    ### Features
    - **Real-Time Tracking**: GPS coordinate updates for live tracking
    - **Multiple Sources**: Support for EDI, GPS, Manual, and Carrier Portal updates
    - **Location History**: Maintains complete location tracking history
    - **Automatic Events**: Creates location update events automatically

    ### Data Sources
    - **GPS**: Automatic GPS device updates
    - **EDI**: EDI 214 location status updates
    - **MANUAL**: Manual location entry by operators
    - **CARRIER_PORTAL**: Updates from carrier web portals

    ### Location Accuracy
    - Latitude/longitude coordinates are required
    - Optional city/state for human-readable location
    - Timestamp defaults to current time if not provided


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentLocationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSShipmentLocationBody,
) -> Optional[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]:
    """Update shipment location


    ## Update Shipment Location

    Update the current location of a shipment with GPS coordinates and optional location details.

    ### Features
    - **Real-Time Tracking**: GPS coordinate updates for live tracking
    - **Multiple Sources**: Support for EDI, GPS, Manual, and Carrier Portal updates
    - **Location History**: Maintains complete location tracking history
    - **Automatic Events**: Creates location update events automatically

    ### Data Sources
    - **GPS**: Automatic GPS device updates
    - **EDI**: EDI 214 location status updates
    - **MANUAL**: Manual location entry by operators
    - **CARRIER_PORTAL**: Updates from carrier web portals

    ### Location Accuracy
    - Latitude/longitude coordinates are required
    - Optional city/state for human-readable location
    - Timestamp defaults to current time if not provided


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentLocationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        shipment_id=shipment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSShipmentLocationBody,
) -> Response[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]:
    """Update shipment location


    ## Update Shipment Location

    Update the current location of a shipment with GPS coordinates and optional location details.

    ### Features
    - **Real-Time Tracking**: GPS coordinate updates for live tracking
    - **Multiple Sources**: Support for EDI, GPS, Manual, and Carrier Portal updates
    - **Location History**: Maintains complete location tracking history
    - **Automatic Events**: Creates location update events automatically

    ### Data Sources
    - **GPS**: Automatic GPS device updates
    - **EDI**: EDI 214 location status updates
    - **MANUAL**: Manual location entry by operators
    - **CARRIER_PORTAL**: Updates from carrier web portals

    ### Location Accuracy
    - Latitude/longitude coordinates are required
    - Optional city/state for human-readable location
    - Timestamp defaults to current time if not provided


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentLocationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateTMSShipmentLocationBody,
) -> Optional[Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]]:
    """Update shipment location


    ## Update Shipment Location

    Update the current location of a shipment with GPS coordinates and optional location details.

    ### Features
    - **Real-Time Tracking**: GPS coordinate updates for live tracking
    - **Multiple Sources**: Support for EDI, GPS, Manual, and Carrier Portal updates
    - **Location History**: Maintains complete location tracking history
    - **Automatic Events**: Creates location update events automatically

    ### Data Sources
    - **GPS**: Automatic GPS device updates
    - **EDI**: EDI 214 location status updates
    - **MANUAL**: Manual location entry by operators
    - **CARRIER_PORTAL**: Updates from carrier web portals

    ### Location Accuracy
    - Latitude/longitude coordinates are required
    - Optional city/state for human-readable location
    - Timestamp defaults to current time if not provided


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentLocationBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateTMSShipmentLocationResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
