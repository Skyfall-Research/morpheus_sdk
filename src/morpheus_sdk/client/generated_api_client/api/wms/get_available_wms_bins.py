from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_available_wms_bins_bin_type_item import GetAvailableWMSBinsBinTypeItem
from ...models.get_available_wms_bins_response_200 import GetAvailableWMSBinsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    bin_type: Union[Unset, list[GetAvailableWMSBinsBinTypeItem]] = UNSET,
    min_weight: Union[Unset, float] = UNSET,
    min_volume: Union[Unset, float] = UNSET,
    min_pallets: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_zone_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(zone_ids, Unset):
        json_zone_ids = zone_ids

    params["zoneIds"] = json_zone_ids

    json_bin_type: Union[Unset, list[str]] = UNSET
    if not isinstance(bin_type, Unset):
        json_bin_type = []
        for bin_type_item_data in bin_type:
            bin_type_item = bin_type_item_data.value
            json_bin_type.append(bin_type_item)

    params["binType"] = json_bin_type

    params["minWeight"] = min_weight

    params["minVolume"] = min_volume

    params["minPallets"] = min_pallets

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/bins/available",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]:
    if response.status_code == 200:
        response_200 = GetAvailableWMSBinsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]:
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
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    bin_type: Union[Unset, list[GetAvailableWMSBinsBinTypeItem]] = UNSET,
    min_weight: Union[Unset, float] = UNSET,
    min_volume: Union[Unset, float] = UNSET,
    min_pallets: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]:
    """Get available bins with filtering


    ## Get Available WMS Bins

    Retrieve available warehouse bins based on capacity requirements, location filters, and operational
    criteria for inventory placement and picking operations.

    ### Features
    - **Capacity Filtering**: Filter by minimum weight, volume, and pallet requirements
    - **Zone-Based Filtering**: Limit results to specific warehouse zones
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Warehouse Scoping**: Filter by specific warehouse for multi-facility operations
    - **Availability Status**: Only returns bins available for inventory placement
    - **Real-Time Availability**: Current availability based on inventory occupancy

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse
    - **zoneIds**: Optional - Array of zone identifiers to include
    - **binType**: Optional - Array of bin types to filter by
    - **minWeight**: Optional - Minimum weight capacity requirement in pounds
    - **minVolume**: Optional - Minimum volume capacity requirement in cubic feet
    - **minPallets**: Optional - Minimum pallet capacity requirement

    ### Business Logic
    - Returns only bins with status AVAILABLE
    - Excludes bins that are OCCUPIED, RESERVED, DAMAGED, or BLOCKED
    - Capacity filters are cumulative (bin must meet all specified minimums)
    - Zone filtering allows multiple zones for flexible operations
    - Results sorted by zone, aisle, and position for efficient navigation

    ### Use Cases
    - **Inventory Putaway**: Find suitable bins for incoming inventory
    - **Pick Path Optimization**: Locate bins for efficient picking routes
    - **Capacity Planning**: Assess available storage capacity
    - **Slotting Optimization**: Support slotting and re-slotting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_PICK_B'].
        bin_type (Union[Unset, list[GetAvailableWMSBinsBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        min_weight (Union[Unset, float]):  Example: 1000.
        min_volume (Union[Unset, float]):  Example: 25.5.
        min_pallets (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        zone_ids=zone_ids,
        bin_type=bin_type,
        min_weight=min_weight,
        min_volume=min_volume,
        min_pallets=min_pallets,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    bin_type: Union[Unset, list[GetAvailableWMSBinsBinTypeItem]] = UNSET,
    min_weight: Union[Unset, float] = UNSET,
    min_volume: Union[Unset, float] = UNSET,
    min_pallets: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]:
    """Get available bins with filtering


    ## Get Available WMS Bins

    Retrieve available warehouse bins based on capacity requirements, location filters, and operational
    criteria for inventory placement and picking operations.

    ### Features
    - **Capacity Filtering**: Filter by minimum weight, volume, and pallet requirements
    - **Zone-Based Filtering**: Limit results to specific warehouse zones
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Warehouse Scoping**: Filter by specific warehouse for multi-facility operations
    - **Availability Status**: Only returns bins available for inventory placement
    - **Real-Time Availability**: Current availability based on inventory occupancy

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse
    - **zoneIds**: Optional - Array of zone identifiers to include
    - **binType**: Optional - Array of bin types to filter by
    - **minWeight**: Optional - Minimum weight capacity requirement in pounds
    - **minVolume**: Optional - Minimum volume capacity requirement in cubic feet
    - **minPallets**: Optional - Minimum pallet capacity requirement

    ### Business Logic
    - Returns only bins with status AVAILABLE
    - Excludes bins that are OCCUPIED, RESERVED, DAMAGED, or BLOCKED
    - Capacity filters are cumulative (bin must meet all specified minimums)
    - Zone filtering allows multiple zones for flexible operations
    - Results sorted by zone, aisle, and position for efficient navigation

    ### Use Cases
    - **Inventory Putaway**: Find suitable bins for incoming inventory
    - **Pick Path Optimization**: Locate bins for efficient picking routes
    - **Capacity Planning**: Assess available storage capacity
    - **Slotting Optimization**: Support slotting and re-slotting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_PICK_B'].
        bin_type (Union[Unset, list[GetAvailableWMSBinsBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        min_weight (Union[Unset, float]):  Example: 1000.
        min_volume (Union[Unset, float]):  Example: 25.5.
        min_pallets (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAvailableWMSBinsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        zone_ids=zone_ids,
        bin_type=bin_type,
        min_weight=min_weight,
        min_volume=min_volume,
        min_pallets=min_pallets,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    bin_type: Union[Unset, list[GetAvailableWMSBinsBinTypeItem]] = UNSET,
    min_weight: Union[Unset, float] = UNSET,
    min_volume: Union[Unset, float] = UNSET,
    min_pallets: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]:
    """Get available bins with filtering


    ## Get Available WMS Bins

    Retrieve available warehouse bins based on capacity requirements, location filters, and operational
    criteria for inventory placement and picking operations.

    ### Features
    - **Capacity Filtering**: Filter by minimum weight, volume, and pallet requirements
    - **Zone-Based Filtering**: Limit results to specific warehouse zones
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Warehouse Scoping**: Filter by specific warehouse for multi-facility operations
    - **Availability Status**: Only returns bins available for inventory placement
    - **Real-Time Availability**: Current availability based on inventory occupancy

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse
    - **zoneIds**: Optional - Array of zone identifiers to include
    - **binType**: Optional - Array of bin types to filter by
    - **minWeight**: Optional - Minimum weight capacity requirement in pounds
    - **minVolume**: Optional - Minimum volume capacity requirement in cubic feet
    - **minPallets**: Optional - Minimum pallet capacity requirement

    ### Business Logic
    - Returns only bins with status AVAILABLE
    - Excludes bins that are OCCUPIED, RESERVED, DAMAGED, or BLOCKED
    - Capacity filters are cumulative (bin must meet all specified minimums)
    - Zone filtering allows multiple zones for flexible operations
    - Results sorted by zone, aisle, and position for efficient navigation

    ### Use Cases
    - **Inventory Putaway**: Find suitable bins for incoming inventory
    - **Pick Path Optimization**: Locate bins for efficient picking routes
    - **Capacity Planning**: Assess available storage capacity
    - **Slotting Optimization**: Support slotting and re-slotting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_PICK_B'].
        bin_type (Union[Unset, list[GetAvailableWMSBinsBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        min_weight (Union[Unset, float]):  Example: 1000.
        min_volume (Union[Unset, float]):  Example: 25.5.
        min_pallets (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        zone_ids=zone_ids,
        bin_type=bin_type,
        min_weight=min_weight,
        min_volume=min_volume,
        min_pallets=min_pallets,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    bin_type: Union[Unset, list[GetAvailableWMSBinsBinTypeItem]] = UNSET,
    min_weight: Union[Unset, float] = UNSET,
    min_volume: Union[Unset, float] = UNSET,
    min_pallets: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetAvailableWMSBinsResponse200]]:
    """Get available bins with filtering


    ## Get Available WMS Bins

    Retrieve available warehouse bins based on capacity requirements, location filters, and operational
    criteria for inventory placement and picking operations.

    ### Features
    - **Capacity Filtering**: Filter by minimum weight, volume, and pallet requirements
    - **Zone-Based Filtering**: Limit results to specific warehouse zones
    - **Type-Based Filtering**: Filter by bin types for operational compatibility
    - **Warehouse Scoping**: Filter by specific warehouse for multi-facility operations
    - **Availability Status**: Only returns bins available for inventory placement
    - **Real-Time Availability**: Current availability based on inventory occupancy

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse
    - **zoneIds**: Optional - Array of zone identifiers to include
    - **binType**: Optional - Array of bin types to filter by
    - **minWeight**: Optional - Minimum weight capacity requirement in pounds
    - **minVolume**: Optional - Minimum volume capacity requirement in cubic feet
    - **minPallets**: Optional - Minimum pallet capacity requirement

    ### Business Logic
    - Returns only bins with status AVAILABLE
    - Excludes bins that are OCCUPIED, RESERVED, DAMAGED, or BLOCKED
    - Capacity filters are cumulative (bin must meet all specified minimums)
    - Zone filtering allows multiple zones for flexible operations
    - Results sorted by zone, aisle, and position for efficient navigation

    ### Use Cases
    - **Inventory Putaway**: Find suitable bins for incoming inventory
    - **Pick Path Optimization**: Locate bins for efficient picking routes
    - **Capacity Planning**: Assess available storage capacity
    - **Slotting Optimization**: Support slotting and re-slotting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_PICK_B'].
        bin_type (Union[Unset, list[GetAvailableWMSBinsBinTypeItem]]):  Example: ['PICK_FACE',
            'SHELF'].
        min_weight (Union[Unset, float]):  Example: 1000.
        min_volume (Union[Unset, float]):  Example: 25.5.
        min_pallets (Union[Unset, int]):  Example: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAvailableWMSBinsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            zone_ids=zone_ids,
            bin_type=bin_type,
            min_weight=min_weight,
            min_volume=min_volume,
            min_pallets=min_pallets,
        )
    ).parsed
