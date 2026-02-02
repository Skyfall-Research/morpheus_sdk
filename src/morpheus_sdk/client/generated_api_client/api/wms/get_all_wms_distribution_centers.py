from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_all_wms_distribution_centers_dc_type_item import GetAllWMSDistributionCentersDcTypeItem
from ...models.get_all_wms_distribution_centers_operational_status_item import (
    GetAllWMSDistributionCentersOperationalStatusItem,
)
from ...models.get_all_wms_distribution_centers_response_200 import GetAllWMSDistributionCentersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]] = UNSET,
    operational_status: Union[Unset, list[GetAllWMSDistributionCentersOperationalStatusItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_dc_type: Union[Unset, list[str]] = UNSET
    if not isinstance(dc_type, Unset):
        json_dc_type = []
        for dc_type_item_data in dc_type:
            dc_type_item = dc_type_item_data.value
            json_dc_type.append(dc_type_item)

    params["dcType"] = json_dc_type

    json_operational_status: Union[Unset, list[str]] = UNSET
    if not isinstance(operational_status, Unset):
        json_operational_status = []
        for operational_status_item_data in operational_status:
            operational_status_item = operational_status_item_data.value
            json_operational_status.append(operational_status_item)

    params["operationalStatus"] = json_operational_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/distribution-centers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]:
    if response.status_code == 200:
        response_200 = GetAllWMSDistributionCentersResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]:
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
    dc_type: Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]] = UNSET,
    operational_status: Union[Unset, list[GetAllWMSDistributionCentersOperationalStatusItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]:
    """Get all distribution centers with filtering


    ## Get All WMS Distribution Centers

    Retrieve all distribution centers within a world with comprehensive filtering options for facility
    management and operational oversight.

    ### Features
    - **Comprehensive Listing**: Retrieve all distribution centers across warehouses
    - **Warehouse Filtering**: Filter by specific warehouse for facility-specific queries
    - **Type-Based Filtering**: Filter by distribution center types for operational categorization
    - **Status Filtering**: Filter by operational status for active facility management
    - **Multi-Filter Support**: Combine filters for precise facility selection
    - **Sorted Results**: Results sorted alphabetically by DC name for consistent ordering

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **dcType**: Optional - Array of DC types for type-based filtering
    - **operationalStatus**: Optional - Array of operational statuses for status-based filtering

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Multiple values for dcType and operationalStatus supported as arrays
    - Results include complete facility information for comprehensive management
    - Sorted alphabetically by dcName for consistent presentation
    - Cross-warehouse querying supported when warehouseId not specified

    ### Use Cases
    - **Facility Management**: Overview of all facilities across operations
    - **Warehouse Coordination**: Facility listing for specific warehouse operations
    - **Status Monitoring**: Active facility monitoring and status tracking
    - **Type-Based Operations**: Operations specific to facility types
    - **Multi-Facility Planning**: Planning across multiple distribution centers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]]):  Example:
            ['FULFILLMENT', 'CROSS_DOCK'].
        operational_status (Union[Unset,
            list[GetAllWMSDistributionCentersOperationalStatusItem]]):  Example: ['ACTIVE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        dc_type=dc_type,
        operational_status=operational_status,
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
    dc_type: Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]] = UNSET,
    operational_status: Union[Unset, list[GetAllWMSDistributionCentersOperationalStatusItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]:
    """Get all distribution centers with filtering


    ## Get All WMS Distribution Centers

    Retrieve all distribution centers within a world with comprehensive filtering options for facility
    management and operational oversight.

    ### Features
    - **Comprehensive Listing**: Retrieve all distribution centers across warehouses
    - **Warehouse Filtering**: Filter by specific warehouse for facility-specific queries
    - **Type-Based Filtering**: Filter by distribution center types for operational categorization
    - **Status Filtering**: Filter by operational status for active facility management
    - **Multi-Filter Support**: Combine filters for precise facility selection
    - **Sorted Results**: Results sorted alphabetically by DC name for consistent ordering

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **dcType**: Optional - Array of DC types for type-based filtering
    - **operationalStatus**: Optional - Array of operational statuses for status-based filtering

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Multiple values for dcType and operationalStatus supported as arrays
    - Results include complete facility information for comprehensive management
    - Sorted alphabetically by dcName for consistent presentation
    - Cross-warehouse querying supported when warehouseId not specified

    ### Use Cases
    - **Facility Management**: Overview of all facilities across operations
    - **Warehouse Coordination**: Facility listing for specific warehouse operations
    - **Status Monitoring**: Active facility monitoring and status tracking
    - **Type-Based Operations**: Operations specific to facility types
    - **Multi-Facility Planning**: Planning across multiple distribution centers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]]):  Example:
            ['FULFILLMENT', 'CROSS_DOCK'].
        operational_status (Union[Unset,
            list[GetAllWMSDistributionCentersOperationalStatusItem]]):  Example: ['ACTIVE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        dc_type=dc_type,
        operational_status=operational_status,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]] = UNSET,
    operational_status: Union[Unset, list[GetAllWMSDistributionCentersOperationalStatusItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]:
    """Get all distribution centers with filtering


    ## Get All WMS Distribution Centers

    Retrieve all distribution centers within a world with comprehensive filtering options for facility
    management and operational oversight.

    ### Features
    - **Comprehensive Listing**: Retrieve all distribution centers across warehouses
    - **Warehouse Filtering**: Filter by specific warehouse for facility-specific queries
    - **Type-Based Filtering**: Filter by distribution center types for operational categorization
    - **Status Filtering**: Filter by operational status for active facility management
    - **Multi-Filter Support**: Combine filters for precise facility selection
    - **Sorted Results**: Results sorted alphabetically by DC name for consistent ordering

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **dcType**: Optional - Array of DC types for type-based filtering
    - **operationalStatus**: Optional - Array of operational statuses for status-based filtering

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Multiple values for dcType and operationalStatus supported as arrays
    - Results include complete facility information for comprehensive management
    - Sorted alphabetically by dcName for consistent presentation
    - Cross-warehouse querying supported when warehouseId not specified

    ### Use Cases
    - **Facility Management**: Overview of all facilities across operations
    - **Warehouse Coordination**: Facility listing for specific warehouse operations
    - **Status Monitoring**: Active facility monitoring and status tracking
    - **Type-Based Operations**: Operations specific to facility types
    - **Multi-Facility Planning**: Planning across multiple distribution centers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]]):  Example:
            ['FULFILLMENT', 'CROSS_DOCK'].
        operational_status (Union[Unset,
            list[GetAllWMSDistributionCentersOperationalStatusItem]]):  Example: ['ACTIVE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        dc_type=dc_type,
        operational_status=operational_status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]] = UNSET,
    operational_status: Union[Unset, list[GetAllWMSDistributionCentersOperationalStatusItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]]:
    """Get all distribution centers with filtering


    ## Get All WMS Distribution Centers

    Retrieve all distribution centers within a world with comprehensive filtering options for facility
    management and operational oversight.

    ### Features
    - **Comprehensive Listing**: Retrieve all distribution centers across warehouses
    - **Warehouse Filtering**: Filter by specific warehouse for facility-specific queries
    - **Type-Based Filtering**: Filter by distribution center types for operational categorization
    - **Status Filtering**: Filter by operational status for active facility management
    - **Multi-Filter Support**: Combine filters for precise facility selection
    - **Sorted Results**: Results sorted alphabetically by DC name for consistent ordering

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **dcType**: Optional - Array of DC types for type-based filtering
    - **operationalStatus**: Optional - Array of operational statuses for status-based filtering

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Multiple values for dcType and operationalStatus supported as arrays
    - Results include complete facility information for comprehensive management
    - Sorted alphabetically by dcName for consistent presentation
    - Cross-warehouse querying supported when warehouseId not specified

    ### Use Cases
    - **Facility Management**: Overview of all facilities across operations
    - **Warehouse Coordination**: Facility listing for specific warehouse operations
    - **Status Monitoring**: Active facility monitoring and status tracking
    - **Type-Based Operations**: Operations specific to facility types
    - **Multi-Facility Planning**: Planning across multiple distribution centers


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetAllWMSDistributionCentersDcTypeItem]]):  Example:
            ['FULFILLMENT', 'CROSS_DOCK'].
        operational_status (Union[Unset,
            list[GetAllWMSDistributionCentersOperationalStatusItem]]):  Example: ['ACTIVE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAllWMSDistributionCentersResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            dc_type=dc_type,
            operational_status=operational_status,
        )
    ).parsed
