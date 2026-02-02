import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_available_dock_doors_door_type import GetWMSAvailableDockDoorsDoorType
from ...models.get_wms_available_dock_doors_response_200 import GetWMSAvailableDockDoorsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: str,
    door_type: GetWMSAvailableDockDoorsDoorType,
    zone_id: Union[Unset, str] = UNSET,
    max_trailer_length: Union[Unset, float] = UNSET,
    leveling_dock: Union[Unset, bool] = UNSET,
    restraint_system: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_door_type = door_type.value
    params["doorType"] = json_door_type

    params["zoneId"] = zone_id

    params["maxTrailerLength"] = max_trailer_length

    params["levelingDock"] = leveling_dock

    params["restraintSystem"] = restraint_system

    json_start_time: Union[Unset, str] = UNSET
    if not isinstance(start_time, Unset):
        json_start_time = start_time.isoformat()
    params["startTime"] = json_start_time

    json_end_time: Union[Unset, str] = UNSET
    if not isinstance(end_time, Unset):
        json_end_time = end_time.isoformat()
    params["endTime"] = json_end_time

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/dock-doors/available",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSAvailableDockDoorsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]:
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
    warehouse_id: str,
    door_type: GetWMSAvailableDockDoorsDoorType,
    zone_id: Union[Unset, str] = UNSET,
    max_trailer_length: Union[Unset, float] = UNSET,
    leveling_dock: Union[Unset, bool] = UNSET,
    restraint_system: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]:
    """Get available dock doors


    ## Get Available WMS Dock Doors

    Retrieve dock doors available for appointment scheduling with advanced filtering by capabilities,
    location, and time slots for optimal assignment coordination.

    ### Features
    - **Availability Filtering**: Find doors with AVAILABLE status for immediate scheduling
    - **Capability Matching**: Filter by trailer length, leveling dock, and restraint systems
    - **Time Slot Validation**: Check availability for specific time periods
    - **Zone-Based Search**: Locate doors within specific warehouse zones
    - **Equipment Requirements**: Match doors with required equipment and capabilities
    - **Real-Time Status**: Current availability based on active appointments

    ### Business Logic
    - warehouseId and doorType are required for warehouse-scoped searches
    - Availability determined by AVAILABLE status and no conflicting appointments
    - Time slot filtering validates against current appointment schedules
    - Capability filters ensure doors meet trailer and equipment requirements
    - Zone filtering supports location-based optimization within warehouses
    - Returns doors immediately ready for appointment assignment

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)
    - **doorType**: Required - Type of door operations (INBOUND, OUTBOUND, CROSS_DOCK)

    ### Query Parameters
    - **zoneId**: Optional - Filter by specific zone within warehouse
    - **maxTrailerLength**: Optional - Minimum trailer length capability required
    - **levelingDock**: Optional - Require leveling dock capability
    - **restraintSystem**: Optional - Require trailer restraint system
    - **startTime**: Optional - Availability window start time (ISO 8601)
    - **endTime**: Optional - Availability window end time (ISO 8601)

    ### Use Cases
    - **Appointment Scheduling**: Find suitable doors for incoming trailer appointments
    - **Capability Matching**: Locate doors with specific equipment requirements
    - **Time Management**: Check door availability for specific time periods
    - **Operational Planning**: Identify available capacity for scheduling optimization
    - **Resource Allocation**: Match doors to trailer requirements for efficient operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (GetWMSAvailableDockDoorsDoorType):  Example: INBOUND.
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.
        max_trailer_length (Union[Unset, float]):  Example: 53.
        leveling_dock (Union[Unset, bool]):  Example: True.
        restraint_system (Union[Unset, bool]):  Example: True.
        start_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T09:00:00Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T17:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        door_type=door_type,
        zone_id=zone_id,
        max_trailer_length=max_trailer_length,
        leveling_dock=leveling_dock,
        restraint_system=restraint_system,
        start_time=start_time,
        end_time=end_time,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    door_type: GetWMSAvailableDockDoorsDoorType,
    zone_id: Union[Unset, str] = UNSET,
    max_trailer_length: Union[Unset, float] = UNSET,
    leveling_dock: Union[Unset, bool] = UNSET,
    restraint_system: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]:
    """Get available dock doors


    ## Get Available WMS Dock Doors

    Retrieve dock doors available for appointment scheduling with advanced filtering by capabilities,
    location, and time slots for optimal assignment coordination.

    ### Features
    - **Availability Filtering**: Find doors with AVAILABLE status for immediate scheduling
    - **Capability Matching**: Filter by trailer length, leveling dock, and restraint systems
    - **Time Slot Validation**: Check availability for specific time periods
    - **Zone-Based Search**: Locate doors within specific warehouse zones
    - **Equipment Requirements**: Match doors with required equipment and capabilities
    - **Real-Time Status**: Current availability based on active appointments

    ### Business Logic
    - warehouseId and doorType are required for warehouse-scoped searches
    - Availability determined by AVAILABLE status and no conflicting appointments
    - Time slot filtering validates against current appointment schedules
    - Capability filters ensure doors meet trailer and equipment requirements
    - Zone filtering supports location-based optimization within warehouses
    - Returns doors immediately ready for appointment assignment

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)
    - **doorType**: Required - Type of door operations (INBOUND, OUTBOUND, CROSS_DOCK)

    ### Query Parameters
    - **zoneId**: Optional - Filter by specific zone within warehouse
    - **maxTrailerLength**: Optional - Minimum trailer length capability required
    - **levelingDock**: Optional - Require leveling dock capability
    - **restraintSystem**: Optional - Require trailer restraint system
    - **startTime**: Optional - Availability window start time (ISO 8601)
    - **endTime**: Optional - Availability window end time (ISO 8601)

    ### Use Cases
    - **Appointment Scheduling**: Find suitable doors for incoming trailer appointments
    - **Capability Matching**: Locate doors with specific equipment requirements
    - **Time Management**: Check door availability for specific time periods
    - **Operational Planning**: Identify available capacity for scheduling optimization
    - **Resource Allocation**: Match doors to trailer requirements for efficient operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (GetWMSAvailableDockDoorsDoorType):  Example: INBOUND.
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.
        max_trailer_length (Union[Unset, float]):  Example: 53.
        leveling_dock (Union[Unset, bool]):  Example: True.
        restraint_system (Union[Unset, bool]):  Example: True.
        start_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T09:00:00Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T17:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        door_type=door_type,
        zone_id=zone_id,
        max_trailer_length=max_trailer_length,
        leveling_dock=leveling_dock,
        restraint_system=restraint_system,
        start_time=start_time,
        end_time=end_time,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    door_type: GetWMSAvailableDockDoorsDoorType,
    zone_id: Union[Unset, str] = UNSET,
    max_trailer_length: Union[Unset, float] = UNSET,
    leveling_dock: Union[Unset, bool] = UNSET,
    restraint_system: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]:
    """Get available dock doors


    ## Get Available WMS Dock Doors

    Retrieve dock doors available for appointment scheduling with advanced filtering by capabilities,
    location, and time slots for optimal assignment coordination.

    ### Features
    - **Availability Filtering**: Find doors with AVAILABLE status for immediate scheduling
    - **Capability Matching**: Filter by trailer length, leveling dock, and restraint systems
    - **Time Slot Validation**: Check availability for specific time periods
    - **Zone-Based Search**: Locate doors within specific warehouse zones
    - **Equipment Requirements**: Match doors with required equipment and capabilities
    - **Real-Time Status**: Current availability based on active appointments

    ### Business Logic
    - warehouseId and doorType are required for warehouse-scoped searches
    - Availability determined by AVAILABLE status and no conflicting appointments
    - Time slot filtering validates against current appointment schedules
    - Capability filters ensure doors meet trailer and equipment requirements
    - Zone filtering supports location-based optimization within warehouses
    - Returns doors immediately ready for appointment assignment

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)
    - **doorType**: Required - Type of door operations (INBOUND, OUTBOUND, CROSS_DOCK)

    ### Query Parameters
    - **zoneId**: Optional - Filter by specific zone within warehouse
    - **maxTrailerLength**: Optional - Minimum trailer length capability required
    - **levelingDock**: Optional - Require leveling dock capability
    - **restraintSystem**: Optional - Require trailer restraint system
    - **startTime**: Optional - Availability window start time (ISO 8601)
    - **endTime**: Optional - Availability window end time (ISO 8601)

    ### Use Cases
    - **Appointment Scheduling**: Find suitable doors for incoming trailer appointments
    - **Capability Matching**: Locate doors with specific equipment requirements
    - **Time Management**: Check door availability for specific time periods
    - **Operational Planning**: Identify available capacity for scheduling optimization
    - **Resource Allocation**: Match doors to trailer requirements for efficient operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (GetWMSAvailableDockDoorsDoorType):  Example: INBOUND.
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.
        max_trailer_length (Union[Unset, float]):  Example: 53.
        leveling_dock (Union[Unset, bool]):  Example: True.
        restraint_system (Union[Unset, bool]):  Example: True.
        start_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T09:00:00Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T17:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        door_type=door_type,
        zone_id=zone_id,
        max_trailer_length=max_trailer_length,
        leveling_dock=leveling_dock,
        restraint_system=restraint_system,
        start_time=start_time,
        end_time=end_time,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    door_type: GetWMSAvailableDockDoorsDoorType,
    zone_id: Union[Unset, str] = UNSET,
    max_trailer_length: Union[Unset, float] = UNSET,
    leveling_dock: Union[Unset, bool] = UNSET,
    restraint_system: Union[Unset, bool] = UNSET,
    start_time: Union[Unset, datetime.datetime] = UNSET,
    end_time: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]]:
    """Get available dock doors


    ## Get Available WMS Dock Doors

    Retrieve dock doors available for appointment scheduling with advanced filtering by capabilities,
    location, and time slots for optimal assignment coordination.

    ### Features
    - **Availability Filtering**: Find doors with AVAILABLE status for immediate scheduling
    - **Capability Matching**: Filter by trailer length, leveling dock, and restraint systems
    - **Time Slot Validation**: Check availability for specific time periods
    - **Zone-Based Search**: Locate doors within specific warehouse zones
    - **Equipment Requirements**: Match doors with required equipment and capabilities
    - **Real-Time Status**: Current availability based on active appointments

    ### Business Logic
    - warehouseId and doorType are required for warehouse-scoped searches
    - Availability determined by AVAILABLE status and no conflicting appointments
    - Time slot filtering validates against current appointment schedules
    - Capability filters ensure doors meet trailer and equipment requirements
    - Zone filtering supports location-based optimization within warehouses
    - Returns doors immediately ready for appointment assignment

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)
    - **doorType**: Required - Type of door operations (INBOUND, OUTBOUND, CROSS_DOCK)

    ### Query Parameters
    - **zoneId**: Optional - Filter by specific zone within warehouse
    - **maxTrailerLength**: Optional - Minimum trailer length capability required
    - **levelingDock**: Optional - Require leveling dock capability
    - **restraintSystem**: Optional - Require trailer restraint system
    - **startTime**: Optional - Availability window start time (ISO 8601)
    - **endTime**: Optional - Availability window end time (ISO 8601)

    ### Use Cases
    - **Appointment Scheduling**: Find suitable doors for incoming trailer appointments
    - **Capability Matching**: Locate doors with specific equipment requirements
    - **Time Management**: Check door availability for specific time periods
    - **Operational Planning**: Identify available capacity for scheduling optimization
    - **Resource Allocation**: Match doors to trailer requirements for efficient operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (GetWMSAvailableDockDoorsDoorType):  Example: INBOUND.
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.
        max_trailer_length (Union[Unset, float]):  Example: 53.
        leveling_dock (Union[Unset, bool]):  Example: True.
        restraint_system (Union[Unset, bool]):  Example: True.
        start_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T09:00:00Z.
        end_time (Union[Unset, datetime.datetime]):  Example: 2024-11-27T17:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSAvailableDockDoorsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            door_type=door_type,
            zone_id=zone_id,
            max_trailer_length=max_trailer_length,
            leveling_dock=leveling_dock,
            restraint_system=restraint_system,
            start_time=start_time,
            end_time=end_time,
        )
    ).parsed
