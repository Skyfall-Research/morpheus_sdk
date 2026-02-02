from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_shipment_by_id_response_200 import GetTMSShipmentByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/shipments/{shipment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSShipmentByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]:
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
) -> Response[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]:
    """Get shipment by ID with events


    ## Get TMS Shipment Details

    Retrieve comprehensive shipment information including all related status events and tracking
    history.

    ### Features
    - **Complete Shipment Data**: All shipment fields including cargo, routing, and costs
    - **Event History**: Full chronological history of status changes and updates
    - **Location Tracking**: Current and historical location data
    - **Delay Information**: Any delays and their impact on delivery

    ### Response Includes
    - Shipment details with current status
    - Related status events ordered by timestamp
    - Current location and tracking information
    - Carrier and routing details


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
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
) -> Optional[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]:
    """Get shipment by ID with events


    ## Get TMS Shipment Details

    Retrieve comprehensive shipment information including all related status events and tracking
    history.

    ### Features
    - **Complete Shipment Data**: All shipment fields including cargo, routing, and costs
    - **Event History**: Full chronological history of status changes and updates
    - **Location Tracking**: Current and historical location data
    - **Delay Information**: Any delays and their impact on delivery

    ### Response Includes
    - Shipment details with current status
    - Related status events ordered by timestamp
    - Current location and tracking information
    - Carrier and routing details


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSShipmentByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        shipment_id=shipment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]:
    """Get shipment by ID with events


    ## Get TMS Shipment Details

    Retrieve comprehensive shipment information including all related status events and tracking
    history.

    ### Features
    - **Complete Shipment Data**: All shipment fields including cargo, routing, and costs
    - **Event History**: Full chronological history of status changes and updates
    - **Location Tracking**: Current and historical location data
    - **Delay Information**: Any delays and their impact on delivery

    ### Response Includes
    - Shipment details with current status
    - Related status events ordered by timestamp
    - Current location and tracking information
    - Carrier and routing details


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetTMSShipmentByIdResponse200]]:
    """Get shipment by ID with events


    ## Get TMS Shipment Details

    Retrieve comprehensive shipment information including all related status events and tracking
    history.

    ### Features
    - **Complete Shipment Data**: All shipment fields including cargo, routing, and costs
    - **Event History**: Full chronological history of status changes and updates
    - **Location Tracking**: Current and historical location data
    - **Delay Information**: Any delays and their impact on delivery

    ### Response Includes
    - Shipment details with current status
    - Related status events ordered by timestamp
    - Current location and tracking information
    - Carrier and routing details


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSShipmentByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
        )
    ).parsed
