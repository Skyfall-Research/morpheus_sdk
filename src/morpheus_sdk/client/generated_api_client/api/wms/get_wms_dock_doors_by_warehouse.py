from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_dock_doors_by_warehouse_door_type_item import GetWMSDockDoorsByWarehouseDoorTypeItem
from ...models.get_wms_dock_doors_by_warehouse_response_200 import GetWMSDockDoorsByWarehouseResponse200
from ...models.get_wms_dock_doors_by_warehouse_status_item import GetWMSDockDoorsByWarehouseStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    door_type: Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]] = UNSET,
    status: Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_door_type: Union[Unset, list[str]] = UNSET
    if not isinstance(door_type, Unset):
        json_door_type = []
        for door_type_item_data in door_type:
            door_type_item = door_type_item_data.value
            json_door_type.append(door_type_item)

    params["doorType"] = json_door_type

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["zoneId"] = zone_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/dock-doors/warehouse/{warehouse_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDockDoorsByWarehouseResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    door_type: Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]] = UNSET,
    status: Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]:
    """Get dock doors by warehouse


    ## Get WMS Dock Doors by Warehouse

    Retrieve filtered list of dock doors within a specific warehouse with advanced filtering
    capabilities for operational management and scheduling optimization.

    ### Features
    - **Warehouse-Scoped**: All dock doors within specified warehouse facility
    - **Multi-Filter Support**: Door type, status, and zone filtering
    - **Pagination Support**: Efficient handling of large door inventories
    - **Real-Time Status**: Current availability and occupancy information
    - **Standards Compliance**: Structured response format for downstream integration

    ### Business Logic
    - warehouseId must reference an existing warehouse
    - Supports multiple filter combinations for precise door selection
    - Returns paginated results with total count and navigation metadata
    - doorType and status support multiple values using array format
    - zoneId filters to specific warehouse zones for operational efficiency
    - Default pagination limit applies if not specified

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse

    ### Query Parameters
    - **doorType**: Optional - Filter by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **status**: Optional - Filter by operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **zoneId**: Optional - Filter by specific zone within warehouse

    ### Use Cases
    - **Capacity Planning**: Assess total dock door capacity by type and availability
    - **Operational Scheduling**: Find available doors for appointment assignment
    - **Maintenance Management**: Identify doors requiring maintenance attention
    - **Zone Management**: Review door distribution across warehouse zones
    - **Status Monitoring**: Monitor real-time dock door utilization


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]]):
        status (Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]]):
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        door_type=door_type,
        status=status,
        zone_id=zone_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    door_type: Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]] = UNSET,
    status: Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]:
    """Get dock doors by warehouse


    ## Get WMS Dock Doors by Warehouse

    Retrieve filtered list of dock doors within a specific warehouse with advanced filtering
    capabilities for operational management and scheduling optimization.

    ### Features
    - **Warehouse-Scoped**: All dock doors within specified warehouse facility
    - **Multi-Filter Support**: Door type, status, and zone filtering
    - **Pagination Support**: Efficient handling of large door inventories
    - **Real-Time Status**: Current availability and occupancy information
    - **Standards Compliance**: Structured response format for downstream integration

    ### Business Logic
    - warehouseId must reference an existing warehouse
    - Supports multiple filter combinations for precise door selection
    - Returns paginated results with total count and navigation metadata
    - doorType and status support multiple values using array format
    - zoneId filters to specific warehouse zones for operational efficiency
    - Default pagination limit applies if not specified

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse

    ### Query Parameters
    - **doorType**: Optional - Filter by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **status**: Optional - Filter by operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **zoneId**: Optional - Filter by specific zone within warehouse

    ### Use Cases
    - **Capacity Planning**: Assess total dock door capacity by type and availability
    - **Operational Scheduling**: Find available doors for appointment assignment
    - **Maintenance Management**: Identify doors requiring maintenance attention
    - **Zone Management**: Review door distribution across warehouse zones
    - **Status Monitoring**: Monitor real-time dock door utilization


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]]):
        status (Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]]):
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        door_type=door_type,
        status=status,
        zone_id=zone_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    door_type: Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]] = UNSET,
    status: Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]:
    """Get dock doors by warehouse


    ## Get WMS Dock Doors by Warehouse

    Retrieve filtered list of dock doors within a specific warehouse with advanced filtering
    capabilities for operational management and scheduling optimization.

    ### Features
    - **Warehouse-Scoped**: All dock doors within specified warehouse facility
    - **Multi-Filter Support**: Door type, status, and zone filtering
    - **Pagination Support**: Efficient handling of large door inventories
    - **Real-Time Status**: Current availability and occupancy information
    - **Standards Compliance**: Structured response format for downstream integration

    ### Business Logic
    - warehouseId must reference an existing warehouse
    - Supports multiple filter combinations for precise door selection
    - Returns paginated results with total count and navigation metadata
    - doorType and status support multiple values using array format
    - zoneId filters to specific warehouse zones for operational efficiency
    - Default pagination limit applies if not specified

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse

    ### Query Parameters
    - **doorType**: Optional - Filter by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **status**: Optional - Filter by operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **zoneId**: Optional - Filter by specific zone within warehouse

    ### Use Cases
    - **Capacity Planning**: Assess total dock door capacity by type and availability
    - **Operational Scheduling**: Find available doors for appointment assignment
    - **Maintenance Management**: Identify doors requiring maintenance attention
    - **Zone Management**: Review door distribution across warehouse zones
    - **Status Monitoring**: Monitor real-time dock door utilization


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]]):
        status (Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]]):
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        door_type=door_type,
        status=status,
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    door_type: Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]] = UNSET,
    status: Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]]:
    """Get dock doors by warehouse


    ## Get WMS Dock Doors by Warehouse

    Retrieve filtered list of dock doors within a specific warehouse with advanced filtering
    capabilities for operational management and scheduling optimization.

    ### Features
    - **Warehouse-Scoped**: All dock doors within specified warehouse facility
    - **Multi-Filter Support**: Door type, status, and zone filtering
    - **Pagination Support**: Efficient handling of large door inventories
    - **Real-Time Status**: Current availability and occupancy information
    - **Standards Compliance**: Structured response format for downstream integration

    ### Business Logic
    - warehouseId must reference an existing warehouse
    - Supports multiple filter combinations for precise door selection
    - Returns paginated results with total count and navigation metadata
    - doorType and status support multiple values using array format
    - zoneId filters to specific warehouse zones for operational efficiency
    - Default pagination limit applies if not specified

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse

    ### Query Parameters
    - **doorType**: Optional - Filter by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **status**: Optional - Filter by operational status (AVAILABLE, OCCUPIED, MAINTENANCE, CLOSED)
    - **zoneId**: Optional - Filter by specific zone within warehouse

    ### Use Cases
    - **Capacity Planning**: Assess total dock door capacity by type and availability
    - **Operational Scheduling**: Find available doors for appointment assignment
    - **Maintenance Management**: Identify doors requiring maintenance attention
    - **Zone Management**: Review door distribution across warehouse zones
    - **Status Monitoring**: Monitor real-time dock door utilization


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorsByWarehouseDoorTypeItem]]):
        status (Union[Unset, list[GetWMSDockDoorsByWarehouseStatusItem]]):
        zone_id (Union[Unset, str]):  Example: wms_zone_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorsByWarehouseResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            door_type=door_type,
            status=status,
            zone_id=zone_id,
        )
    ).parsed
