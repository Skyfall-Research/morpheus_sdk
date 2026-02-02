from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_distribution_centers_by_status_dc_type_item import GetWMSDistributionCentersByStatusDcTypeItem
from ...models.get_wms_distribution_centers_by_status_response_200 import GetWMSDistributionCentersByStatusResponse200
from ...models.get_wms_distribution_centers_by_status_status_item import GetWMSDistributionCentersByStatusStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: list[GetWMSDistributionCentersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = []
    for status_item_data in status:
        status_item = status_item_data.value
        json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

    json_dc_type: Union[Unset, list[str]] = UNSET
    if not isinstance(dc_type, Unset):
        json_dc_type = []
        for dc_type_item_data in dc_type:
            dc_type_item = dc_type_item_data.value
            json_dc_type.append(dc_type_item)

    params["dcType"] = json_dc_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/distribution-centers/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDistributionCentersByStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]:
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
    status: list[GetWMSDistributionCentersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]:
    """Get distribution centers by operational status


    ## Get WMS Distribution Centers by Status

    Retrieve distribution centers filtered by specific operational statuses for targeted facility
    management and operational coordination.

    ### Features
    - **Status-Based Filtering**: Primary filtering by one or more operational statuses
    - **Warehouse Scoping**: Secondary filtering by warehouse for facility-specific queries
    - **Type-Based Refinement**: Additional filtering by DC types for operational categorization
    - **Multi-Status Support**: Query multiple statuses simultaneously for comprehensive oversight
    - **Operational Focus**: Designed for status-driven facility management workflows

    ### Query Parameters
    - **status**: Required - Array of operational statuses for filtering
    - **warehouseId**: Optional - Warehouse identifier for warehouse-specific filtering
    - **dcType**: Optional - Array of DC types for additional type-based filtering

    ### Business Logic
    - status parameter is required and supports multiple values as array
    - Empty status array will return no results (intentional design)
    - warehouseId and dcType provide additional filtering refinement
    - Results sorted alphabetically by DC name for consistent presentation
    - Supports operational workflow patterns for status-specific operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational facilities accepting all operations
    - **INACTIVE**: Temporarily inactive facilities available for activation
    - **MAINTENANCE**: Facilities under maintenance with suspended operations

    ### Use Cases
    - **Active Facility Management**: List all currently active facilities
    - **Maintenance Coordination**: Identify facilities under maintenance
    - **Status Monitoring**: Monitor facility status across operations
    - **Operational Planning**: Plan operations based on facility availability
    - **Multi-Status Queries**: Complex status-based facility selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSDistributionCentersByStatusStatusItem]):  Example: ['ACTIVE',
            'MAINTENANCE'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]]):  Example:
            ['FULFILLMENT'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        dc_type=dc_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSDistributionCentersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]:
    """Get distribution centers by operational status


    ## Get WMS Distribution Centers by Status

    Retrieve distribution centers filtered by specific operational statuses for targeted facility
    management and operational coordination.

    ### Features
    - **Status-Based Filtering**: Primary filtering by one or more operational statuses
    - **Warehouse Scoping**: Secondary filtering by warehouse for facility-specific queries
    - **Type-Based Refinement**: Additional filtering by DC types for operational categorization
    - **Multi-Status Support**: Query multiple statuses simultaneously for comprehensive oversight
    - **Operational Focus**: Designed for status-driven facility management workflows

    ### Query Parameters
    - **status**: Required - Array of operational statuses for filtering
    - **warehouseId**: Optional - Warehouse identifier for warehouse-specific filtering
    - **dcType**: Optional - Array of DC types for additional type-based filtering

    ### Business Logic
    - status parameter is required and supports multiple values as array
    - Empty status array will return no results (intentional design)
    - warehouseId and dcType provide additional filtering refinement
    - Results sorted alphabetically by DC name for consistent presentation
    - Supports operational workflow patterns for status-specific operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational facilities accepting all operations
    - **INACTIVE**: Temporarily inactive facilities available for activation
    - **MAINTENANCE**: Facilities under maintenance with suspended operations

    ### Use Cases
    - **Active Facility Management**: List all currently active facilities
    - **Maintenance Coordination**: Identify facilities under maintenance
    - **Status Monitoring**: Monitor facility status across operations
    - **Operational Planning**: Plan operations based on facility availability
    - **Multi-Status Queries**: Complex status-based facility selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSDistributionCentersByStatusStatusItem]):  Example: ['ACTIVE',
            'MAINTENANCE'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]]):  Example:
            ['FULFILLMENT'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        dc_type=dc_type,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSDistributionCentersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]:
    """Get distribution centers by operational status


    ## Get WMS Distribution Centers by Status

    Retrieve distribution centers filtered by specific operational statuses for targeted facility
    management and operational coordination.

    ### Features
    - **Status-Based Filtering**: Primary filtering by one or more operational statuses
    - **Warehouse Scoping**: Secondary filtering by warehouse for facility-specific queries
    - **Type-Based Refinement**: Additional filtering by DC types for operational categorization
    - **Multi-Status Support**: Query multiple statuses simultaneously for comprehensive oversight
    - **Operational Focus**: Designed for status-driven facility management workflows

    ### Query Parameters
    - **status**: Required - Array of operational statuses for filtering
    - **warehouseId**: Optional - Warehouse identifier for warehouse-specific filtering
    - **dcType**: Optional - Array of DC types for additional type-based filtering

    ### Business Logic
    - status parameter is required and supports multiple values as array
    - Empty status array will return no results (intentional design)
    - warehouseId and dcType provide additional filtering refinement
    - Results sorted alphabetically by DC name for consistent presentation
    - Supports operational workflow patterns for status-specific operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational facilities accepting all operations
    - **INACTIVE**: Temporarily inactive facilities available for activation
    - **MAINTENANCE**: Facilities under maintenance with suspended operations

    ### Use Cases
    - **Active Facility Management**: List all currently active facilities
    - **Maintenance Coordination**: Identify facilities under maintenance
    - **Status Monitoring**: Monitor facility status across operations
    - **Operational Planning**: Plan operations based on facility availability
    - **Multi-Status Queries**: Complex status-based facility selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSDistributionCentersByStatusStatusItem]):  Example: ['ACTIVE',
            'MAINTENANCE'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]]):  Example:
            ['FULFILLMENT'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        dc_type=dc_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSDistributionCentersByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    dc_type: Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]]:
    """Get distribution centers by operational status


    ## Get WMS Distribution Centers by Status

    Retrieve distribution centers filtered by specific operational statuses for targeted facility
    management and operational coordination.

    ### Features
    - **Status-Based Filtering**: Primary filtering by one or more operational statuses
    - **Warehouse Scoping**: Secondary filtering by warehouse for facility-specific queries
    - **Type-Based Refinement**: Additional filtering by DC types for operational categorization
    - **Multi-Status Support**: Query multiple statuses simultaneously for comprehensive oversight
    - **Operational Focus**: Designed for status-driven facility management workflows

    ### Query Parameters
    - **status**: Required - Array of operational statuses for filtering
    - **warehouseId**: Optional - Warehouse identifier for warehouse-specific filtering
    - **dcType**: Optional - Array of DC types for additional type-based filtering

    ### Business Logic
    - status parameter is required and supports multiple values as array
    - Empty status array will return no results (intentional design)
    - warehouseId and dcType provide additional filtering refinement
    - Results sorted alphabetically by DC name for consistent presentation
    - Supports operational workflow patterns for status-specific operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational facilities accepting all operations
    - **INACTIVE**: Temporarily inactive facilities available for activation
    - **MAINTENANCE**: Facilities under maintenance with suspended operations

    ### Use Cases
    - **Active Facility Management**: List all currently active facilities
    - **Maintenance Coordination**: Identify facilities under maintenance
    - **Status Monitoring**: Monitor facility status across operations
    - **Operational Planning**: Plan operations based on facility availability
    - **Multi-Status Queries**: Complex status-based facility selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSDistributionCentersByStatusStatusItem]):  Example: ['ACTIVE',
            'MAINTENANCE'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        dc_type (Union[Unset, list[GetWMSDistributionCentersByStatusDcTypeItem]]):  Example:
            ['FULFILLMENT'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDistributionCentersByStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            dc_type=dc_type,
        )
    ).parsed
