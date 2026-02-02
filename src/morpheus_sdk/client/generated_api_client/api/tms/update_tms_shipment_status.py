from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_tms_shipment_status_body import UpdateTMSShipmentStatusBody
from ...models.update_tms_shipment_status_response_200 import UpdateTMSShipmentStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: UpdateTMSShipmentStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateTMSShipmentStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]:
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
    body: UpdateTMSShipmentStatusBody,
) -> Response[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]:
    """Update shipment status


    ## Update Shipment Status

    Update the current status of a shipment with optional contextual information.

    ### Features
    - **Status Management**: Update to any valid shipment status
    - **Context Information**: Optional location, notes, and source tracking
    - **Audit Trail**: Complete audit trail of all status changes
    - **Automatic Events**: Creates status change events automatically

    ### Valid Status Values
    - **PLANNED**: Initial shipment planning
    - **TENDERED**: Shipment offered to carrier
    - **ACCEPTED**: Carrier accepted shipment
    - **PICKED_UP**: Cargo collected from origin
    - **IN_TRANSIT**: Shipment in transit
    - **OUT_FOR_DELIVERY**: Final delivery stage
    - **DELIVERED**: Successfully delivered
    - **CANCELLED**: Shipment cancelled
    - **DELAYED**: Experiencing delays
    - **EXCEPTION**: Exception occurred

    ### Status Transitions
    While any status can be set, typical flow:
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → OUT_FOR_DELIVERY → DELIVERED


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]
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
    body: UpdateTMSShipmentStatusBody,
) -> Optional[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]:
    """Update shipment status


    ## Update Shipment Status

    Update the current status of a shipment with optional contextual information.

    ### Features
    - **Status Management**: Update to any valid shipment status
    - **Context Information**: Optional location, notes, and source tracking
    - **Audit Trail**: Complete audit trail of all status changes
    - **Automatic Events**: Creates status change events automatically

    ### Valid Status Values
    - **PLANNED**: Initial shipment planning
    - **TENDERED**: Shipment offered to carrier
    - **ACCEPTED**: Carrier accepted shipment
    - **PICKED_UP**: Cargo collected from origin
    - **IN_TRANSIT**: Shipment in transit
    - **OUT_FOR_DELIVERY**: Final delivery stage
    - **DELIVERED**: Successfully delivered
    - **CANCELLED**: Shipment cancelled
    - **DELAYED**: Experiencing delays
    - **EXCEPTION**: Exception occurred

    ### Status Transitions
    While any status can be set, typical flow:
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → OUT_FOR_DELIVERY → DELIVERED


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]
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
    body: UpdateTMSShipmentStatusBody,
) -> Response[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]:
    """Update shipment status


    ## Update Shipment Status

    Update the current status of a shipment with optional contextual information.

    ### Features
    - **Status Management**: Update to any valid shipment status
    - **Context Information**: Optional location, notes, and source tracking
    - **Audit Trail**: Complete audit trail of all status changes
    - **Automatic Events**: Creates status change events automatically

    ### Valid Status Values
    - **PLANNED**: Initial shipment planning
    - **TENDERED**: Shipment offered to carrier
    - **ACCEPTED**: Carrier accepted shipment
    - **PICKED_UP**: Cargo collected from origin
    - **IN_TRANSIT**: Shipment in transit
    - **OUT_FOR_DELIVERY**: Final delivery stage
    - **DELIVERED**: Successfully delivered
    - **CANCELLED**: Shipment cancelled
    - **DELAYED**: Experiencing delays
    - **EXCEPTION**: Exception occurred

    ### Status Transitions
    While any status can be set, typical flow:
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → OUT_FOR_DELIVERY → DELIVERED


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]
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
    body: UpdateTMSShipmentStatusBody,
) -> Optional[Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]]:
    """Update shipment status


    ## Update Shipment Status

    Update the current status of a shipment with optional contextual information.

    ### Features
    - **Status Management**: Update to any valid shipment status
    - **Context Information**: Optional location, notes, and source tracking
    - **Audit Trail**: Complete audit trail of all status changes
    - **Automatic Events**: Creates status change events automatically

    ### Valid Status Values
    - **PLANNED**: Initial shipment planning
    - **TENDERED**: Shipment offered to carrier
    - **ACCEPTED**: Carrier accepted shipment
    - **PICKED_UP**: Cargo collected from origin
    - **IN_TRANSIT**: Shipment in transit
    - **OUT_FOR_DELIVERY**: Final delivery stage
    - **DELIVERED**: Successfully delivered
    - **CANCELLED**: Shipment cancelled
    - **DELAYED**: Experiencing delays
    - **EXCEPTION**: Exception occurred

    ### Status Transitions
    While any status can be set, typical flow:
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → OUT_FOR_DELIVERY → DELIVERED


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (UpdateTMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateTMSShipmentStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
