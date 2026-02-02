from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_dock_door_body import CreateWMSDockDoorBody
from ...models.create_wms_dock_door_response_201 import CreateWMSDockDoorResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSDockDoorBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/dock-doors",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSDockDoorResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSDockDoorResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSDockDoorResponse201, ErrorResponse]]:
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
    body: CreateWMSDockDoorBody,
) -> Response[Union[CreateWMSDockDoorResponse201, ErrorResponse]]:
    """Create new dock door


    ## Create WMS Dock Door

    Create a new dock door within a warehouse for trailer loading/unloading operations and appointment
    scheduling.

    ### Features
    - **Comprehensive Configuration**: Full facility setup including capabilities, equipment, and safety
    features
    - **Multi-Type Support**: INBOUND, OUTBOUND, or CROSS_DOCK operational modes
    - **Equipment Specifications**: Detailed equipment and capability tracking
    - **Safety Standards**: Emergency stop systems and inspection scheduling
    - **Operating Hours**: Configurable daily operating schedules
    - **Audit Trail**: Automatic creation and modification tracking

    ### Business Logic
    - Validates required fields: warehouseId, doorNumber, and doorType
    - Prevents duplicate door numbers within the same warehouse
    - Auto-generates unique dockDoorId using WMS service prefix
    - Sets default status to AVAILABLE for immediate scheduling
    - Initializes safety equipment defaults (emergency stop and safety lights enabled)
    - Establishes audit trail for all subsequent modifications

    ### Use Cases
    - **Facility Setup**: Initial dock door configuration during warehouse establishment
    - **Capacity Expansion**: Add new dock doors to increase warehouse throughput
    - **Equipment Upgrade**: Create new doors with enhanced capabilities
    - **Cross-Dock Operations**: Establish specialized cross-dock facilities
    - **Safety Compliance**: Ensure proper safety equipment configuration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDockDoorBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'doorNumber': 'DOCK-01', 'doorType': 'INBOUND',
            'zoneId': 'wms_zone_674565c1234567890abcdef', 'capabilities': {'maxTrailerLength': 53,
            'maxTrailerHeight': 13.5, 'levelingDock': True, 'hydraulicLeveler': True,
            'restraintSystem': True, 'weatherSeal': True}, 'equipment': {'forkliftAccess': True,
            'conveyorSystem': False, 'scales': True, 'lightSystem': True}, 'operatingHours':
            {'monday': {'open': '06:00', 'close': '22:00'}, 'tuesday': {'open': '06:00', 'close':
            '22:00'}, 'wednesday': {'open': '06:00', 'close': '22:00'}, 'thursday': {'open': '06:00',
            'close': '22:00'}, 'friday': {'open': '06:00', 'close': '22:00'}, 'saturday': {'open':
            '08:00', 'close': '18:00'}, 'sunday': {'open': '10:00', 'close': '16:00'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSDockDoorResponse201, ErrorResponse]]
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
    body: CreateWMSDockDoorBody,
) -> Optional[Union[CreateWMSDockDoorResponse201, ErrorResponse]]:
    """Create new dock door


    ## Create WMS Dock Door

    Create a new dock door within a warehouse for trailer loading/unloading operations and appointment
    scheduling.

    ### Features
    - **Comprehensive Configuration**: Full facility setup including capabilities, equipment, and safety
    features
    - **Multi-Type Support**: INBOUND, OUTBOUND, or CROSS_DOCK operational modes
    - **Equipment Specifications**: Detailed equipment and capability tracking
    - **Safety Standards**: Emergency stop systems and inspection scheduling
    - **Operating Hours**: Configurable daily operating schedules
    - **Audit Trail**: Automatic creation and modification tracking

    ### Business Logic
    - Validates required fields: warehouseId, doorNumber, and doorType
    - Prevents duplicate door numbers within the same warehouse
    - Auto-generates unique dockDoorId using WMS service prefix
    - Sets default status to AVAILABLE for immediate scheduling
    - Initializes safety equipment defaults (emergency stop and safety lights enabled)
    - Establishes audit trail for all subsequent modifications

    ### Use Cases
    - **Facility Setup**: Initial dock door configuration during warehouse establishment
    - **Capacity Expansion**: Add new dock doors to increase warehouse throughput
    - **Equipment Upgrade**: Create new doors with enhanced capabilities
    - **Cross-Dock Operations**: Establish specialized cross-dock facilities
    - **Safety Compliance**: Ensure proper safety equipment configuration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDockDoorBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'doorNumber': 'DOCK-01', 'doorType': 'INBOUND',
            'zoneId': 'wms_zone_674565c1234567890abcdef', 'capabilities': {'maxTrailerLength': 53,
            'maxTrailerHeight': 13.5, 'levelingDock': True, 'hydraulicLeveler': True,
            'restraintSystem': True, 'weatherSeal': True}, 'equipment': {'forkliftAccess': True,
            'conveyorSystem': False, 'scales': True, 'lightSystem': True}, 'operatingHours':
            {'monday': {'open': '06:00', 'close': '22:00'}, 'tuesday': {'open': '06:00', 'close':
            '22:00'}, 'wednesday': {'open': '06:00', 'close': '22:00'}, 'thursday': {'open': '06:00',
            'close': '22:00'}, 'friday': {'open': '06:00', 'close': '22:00'}, 'saturday': {'open':
            '08:00', 'close': '18:00'}, 'sunday': {'open': '10:00', 'close': '16:00'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSDockDoorResponse201, ErrorResponse]
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
    body: CreateWMSDockDoorBody,
) -> Response[Union[CreateWMSDockDoorResponse201, ErrorResponse]]:
    """Create new dock door


    ## Create WMS Dock Door

    Create a new dock door within a warehouse for trailer loading/unloading operations and appointment
    scheduling.

    ### Features
    - **Comprehensive Configuration**: Full facility setup including capabilities, equipment, and safety
    features
    - **Multi-Type Support**: INBOUND, OUTBOUND, or CROSS_DOCK operational modes
    - **Equipment Specifications**: Detailed equipment and capability tracking
    - **Safety Standards**: Emergency stop systems and inspection scheduling
    - **Operating Hours**: Configurable daily operating schedules
    - **Audit Trail**: Automatic creation and modification tracking

    ### Business Logic
    - Validates required fields: warehouseId, doorNumber, and doorType
    - Prevents duplicate door numbers within the same warehouse
    - Auto-generates unique dockDoorId using WMS service prefix
    - Sets default status to AVAILABLE for immediate scheduling
    - Initializes safety equipment defaults (emergency stop and safety lights enabled)
    - Establishes audit trail for all subsequent modifications

    ### Use Cases
    - **Facility Setup**: Initial dock door configuration during warehouse establishment
    - **Capacity Expansion**: Add new dock doors to increase warehouse throughput
    - **Equipment Upgrade**: Create new doors with enhanced capabilities
    - **Cross-Dock Operations**: Establish specialized cross-dock facilities
    - **Safety Compliance**: Ensure proper safety equipment configuration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDockDoorBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'doorNumber': 'DOCK-01', 'doorType': 'INBOUND',
            'zoneId': 'wms_zone_674565c1234567890abcdef', 'capabilities': {'maxTrailerLength': 53,
            'maxTrailerHeight': 13.5, 'levelingDock': True, 'hydraulicLeveler': True,
            'restraintSystem': True, 'weatherSeal': True}, 'equipment': {'forkliftAccess': True,
            'conveyorSystem': False, 'scales': True, 'lightSystem': True}, 'operatingHours':
            {'monday': {'open': '06:00', 'close': '22:00'}, 'tuesday': {'open': '06:00', 'close':
            '22:00'}, 'wednesday': {'open': '06:00', 'close': '22:00'}, 'thursday': {'open': '06:00',
            'close': '22:00'}, 'friday': {'open': '06:00', 'close': '22:00'}, 'saturday': {'open':
            '08:00', 'close': '18:00'}, 'sunday': {'open': '10:00', 'close': '16:00'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSDockDoorResponse201, ErrorResponse]]
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
    body: CreateWMSDockDoorBody,
) -> Optional[Union[CreateWMSDockDoorResponse201, ErrorResponse]]:
    """Create new dock door


    ## Create WMS Dock Door

    Create a new dock door within a warehouse for trailer loading/unloading operations and appointment
    scheduling.

    ### Features
    - **Comprehensive Configuration**: Full facility setup including capabilities, equipment, and safety
    features
    - **Multi-Type Support**: INBOUND, OUTBOUND, or CROSS_DOCK operational modes
    - **Equipment Specifications**: Detailed equipment and capability tracking
    - **Safety Standards**: Emergency stop systems and inspection scheduling
    - **Operating Hours**: Configurable daily operating schedules
    - **Audit Trail**: Automatic creation and modification tracking

    ### Business Logic
    - Validates required fields: warehouseId, doorNumber, and doorType
    - Prevents duplicate door numbers within the same warehouse
    - Auto-generates unique dockDoorId using WMS service prefix
    - Sets default status to AVAILABLE for immediate scheduling
    - Initializes safety equipment defaults (emergency stop and safety lights enabled)
    - Establishes audit trail for all subsequent modifications

    ### Use Cases
    - **Facility Setup**: Initial dock door configuration during warehouse establishment
    - **Capacity Expansion**: Add new dock doors to increase warehouse throughput
    - **Equipment Upgrade**: Create new doors with enhanced capabilities
    - **Cross-Dock Operations**: Establish specialized cross-dock facilities
    - **Safety Compliance**: Ensure proper safety equipment configuration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDockDoorBody):  Example: {'warehouseId':
            'wms_warehouse_674565c1234567890abcdef', 'doorNumber': 'DOCK-01', 'doorType': 'INBOUND',
            'zoneId': 'wms_zone_674565c1234567890abcdef', 'capabilities': {'maxTrailerLength': 53,
            'maxTrailerHeight': 13.5, 'levelingDock': True, 'hydraulicLeveler': True,
            'restraintSystem': True, 'weatherSeal': True}, 'equipment': {'forkliftAccess': True,
            'conveyorSystem': False, 'scales': True, 'lightSystem': True}, 'operatingHours':
            {'monday': {'open': '06:00', 'close': '22:00'}, 'tuesday': {'open': '06:00', 'close':
            '22:00'}, 'wednesday': {'open': '06:00', 'close': '22:00'}, 'thursday': {'open': '06:00',
            'close': '22:00'}, 'friday': {'open': '06:00', 'close': '22:00'}, 'saturday': {'open':
            '08:00', 'close': '18:00'}, 'sunday': {'open': '10:00', 'close': '16:00'}}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSDockDoorResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
