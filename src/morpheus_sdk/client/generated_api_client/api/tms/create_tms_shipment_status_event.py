from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tms_shipment_status_event_response_201 import CreateTMSShipmentStatusEventResponse201
from ...models.error_response import ErrorResponse
from ...models.tms_shipment_status_event_input import TMSShipmentStatusEventInput
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: TMSShipmentStatusEventInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateTMSShipmentStatusEventResponse201.from_dict(response.json())

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
) -> Response[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]:
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
    body: TMSShipmentStatusEventInput,
) -> Response[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]:
    """Create shipment status event


    ## Create Shipment Status Event

    Create a new status event for shipment tracking and audit trail purposes.

    ### Features
    - **Event Types**: Support for various event types including status changes, location updates, ETAs,
    delays, exceptions, and milestones
    - **Flexible Data**: Contextual information based on event type
    - **Audit Trail**: Complete event history for compliance and tracking
    - **Event Sources**: Track source of events (API, EDI, Manual, GPS, Carrier Portal)

    ### Event Types
    - **STATUS_CHANGE**: Shipment status transitions
    - **LOCATION_UPDATE**: GPS or location changes
    - **ETA_UPDATE**: Estimated time of arrival updates
    - **DELAY**: Delay notifications and impacts
    - **EXCEPTION**: Exception handling and resolution
    - **MILESTONE**: Important shipment milestones

    ### Event Context
    Different event types support different contextual data:
    - Status changes: previous/new status
    - Location updates: coordinates and location details
    - ETA updates: previous/new ETA and delay calculations
    - Exceptions: severity, description, and resolution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TMSShipmentStatusEventInput): Input data for creating a shipment status event

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]
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
    body: TMSShipmentStatusEventInput,
) -> Optional[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]:
    """Create shipment status event


    ## Create Shipment Status Event

    Create a new status event for shipment tracking and audit trail purposes.

    ### Features
    - **Event Types**: Support for various event types including status changes, location updates, ETAs,
    delays, exceptions, and milestones
    - **Flexible Data**: Contextual information based on event type
    - **Audit Trail**: Complete event history for compliance and tracking
    - **Event Sources**: Track source of events (API, EDI, Manual, GPS, Carrier Portal)

    ### Event Types
    - **STATUS_CHANGE**: Shipment status transitions
    - **LOCATION_UPDATE**: GPS or location changes
    - **ETA_UPDATE**: Estimated time of arrival updates
    - **DELAY**: Delay notifications and impacts
    - **EXCEPTION**: Exception handling and resolution
    - **MILESTONE**: Important shipment milestones

    ### Event Context
    Different event types support different contextual data:
    - Status changes: previous/new status
    - Location updates: coordinates and location details
    - ETA updates: previous/new ETA and delay calculations
    - Exceptions: severity, description, and resolution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TMSShipmentStatusEventInput): Input data for creating a shipment status event

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]
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
    body: TMSShipmentStatusEventInput,
) -> Response[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]:
    """Create shipment status event


    ## Create Shipment Status Event

    Create a new status event for shipment tracking and audit trail purposes.

    ### Features
    - **Event Types**: Support for various event types including status changes, location updates, ETAs,
    delays, exceptions, and milestones
    - **Flexible Data**: Contextual information based on event type
    - **Audit Trail**: Complete event history for compliance and tracking
    - **Event Sources**: Track source of events (API, EDI, Manual, GPS, Carrier Portal)

    ### Event Types
    - **STATUS_CHANGE**: Shipment status transitions
    - **LOCATION_UPDATE**: GPS or location changes
    - **ETA_UPDATE**: Estimated time of arrival updates
    - **DELAY**: Delay notifications and impacts
    - **EXCEPTION**: Exception handling and resolution
    - **MILESTONE**: Important shipment milestones

    ### Event Context
    Different event types support different contextual data:
    - Status changes: previous/new status
    - Location updates: coordinates and location details
    - ETA updates: previous/new ETA and delay calculations
    - Exceptions: severity, description, and resolution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TMSShipmentStatusEventInput): Input data for creating a shipment status event

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]
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
    body: TMSShipmentStatusEventInput,
) -> Optional[Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]]:
    """Create shipment status event


    ## Create Shipment Status Event

    Create a new status event for shipment tracking and audit trail purposes.

    ### Features
    - **Event Types**: Support for various event types including status changes, location updates, ETAs,
    delays, exceptions, and milestones
    - **Flexible Data**: Contextual information based on event type
    - **Audit Trail**: Complete event history for compliance and tracking
    - **Event Sources**: Track source of events (API, EDI, Manual, GPS, Carrier Portal)

    ### Event Types
    - **STATUS_CHANGE**: Shipment status transitions
    - **LOCATION_UPDATE**: GPS or location changes
    - **ETA_UPDATE**: Estimated time of arrival updates
    - **DELAY**: Delay notifications and impacts
    - **EXCEPTION**: Exception handling and resolution
    - **MILESTONE**: Important shipment milestones

    ### Event Context
    Different event types support different contextual data:
    - Status changes: previous/new status
    - Location updates: coordinates and location details
    - ETA updates: previous/new ETA and delay calculations
    - Exceptions: severity, description, and resolution


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TMSShipmentStatusEventInput): Input data for creating a shipment status event

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTMSShipmentStatusEventResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
