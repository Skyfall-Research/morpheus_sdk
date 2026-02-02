import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_cycle_counts_by_warehouse_count_type_item import GetWMSCycleCountsByWarehouseCountTypeItem
from ...models.get_wms_cycle_counts_by_warehouse_response_200 import GetWMSCycleCountsByWarehouseResponse200
from ...models.get_wms_cycle_counts_by_warehouse_status_item import GetWMSCycleCountsByWarehouseStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    status: Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    json_count_type: Union[Unset, list[str]] = UNSET
    if not isinstance(count_type, Unset):
        json_count_type = []
        for count_type_item_data in count_type:
            count_type_item = count_type_item_data.value
            json_count_type.append(count_type_item)

    params["countType"] = json_count_type

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/cycle-counts/warehouse/{warehouse_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSCycleCountsByWarehouseResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]:
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
    status: Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]:
    """Get cycle counts by warehouse


    ## Get WMS Cycle Counts by Warehouse

    Retrieve all cycle counts for a specific warehouse with comprehensive filtering capabilities for
    warehouse-focused operational management.

    ### Features
    - **Warehouse-Scoped Retrieval**: Get all cycle counts for specific warehouse facility
    - **Status Filtering**: Filter by count status for workflow management
    - **Type-Based Filtering**: Filter by count types for methodology-specific views
    - **Date Range Filtering**: Filter by scheduled dates for time-based analysis
    - **Complete Count Details**: Returns full cycle count information including results
    - **Operational Context**: Warehouse-focused view for facility management

    ### Query Parameters
    - **status**: Optional - Filter by count status (supports multiple values)
    - **countType**: Optional - Filter by count types (supports multiple values)
    - **dateStart**: Optional - Start date for scheduled date filtering
    - **dateEnd**: Optional - End date for scheduled date filtering

    ### Business Logic
    - warehouseId from path parameter scopes all results to specific warehouse
    - All filter parameters support array syntax for multiple values
    - Date filtering applies to scheduled date field
    - Results include complete count details with assignments and results
    - Sorted by scheduled date and creation time for operational relevance

    ### Use Cases
    - **Warehouse Management**: Manage all cycle counts within specific warehouse
    - **Operational Planning**: Plan warehouse counting operations and resources
    - **Performance Monitoring**: Monitor warehouse counting performance and accuracy
    - **Historical Analysis**: Analyze warehouse counting history and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        status (Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]]):  Example:
            ['SCHEDULED', 'IN_PROGRESS'].
        count_type (Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]]):  Example:
            ['ABC', 'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        status=status,
        count_type=count_type,
        date_start=date_start,
        date_end=date_end,
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
    status: Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]:
    """Get cycle counts by warehouse


    ## Get WMS Cycle Counts by Warehouse

    Retrieve all cycle counts for a specific warehouse with comprehensive filtering capabilities for
    warehouse-focused operational management.

    ### Features
    - **Warehouse-Scoped Retrieval**: Get all cycle counts for specific warehouse facility
    - **Status Filtering**: Filter by count status for workflow management
    - **Type-Based Filtering**: Filter by count types for methodology-specific views
    - **Date Range Filtering**: Filter by scheduled dates for time-based analysis
    - **Complete Count Details**: Returns full cycle count information including results
    - **Operational Context**: Warehouse-focused view for facility management

    ### Query Parameters
    - **status**: Optional - Filter by count status (supports multiple values)
    - **countType**: Optional - Filter by count types (supports multiple values)
    - **dateStart**: Optional - Start date for scheduled date filtering
    - **dateEnd**: Optional - End date for scheduled date filtering

    ### Business Logic
    - warehouseId from path parameter scopes all results to specific warehouse
    - All filter parameters support array syntax for multiple values
    - Date filtering applies to scheduled date field
    - Results include complete count details with assignments and results
    - Sorted by scheduled date and creation time for operational relevance

    ### Use Cases
    - **Warehouse Management**: Manage all cycle counts within specific warehouse
    - **Operational Planning**: Plan warehouse counting operations and resources
    - **Performance Monitoring**: Monitor warehouse counting performance and accuracy
    - **Historical Analysis**: Analyze warehouse counting history and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        status (Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]]):  Example:
            ['SCHEDULED', 'IN_PROGRESS'].
        count_type (Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]]):  Example:
            ['ABC', 'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        status=status,
        count_type=count_type,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]:
    """Get cycle counts by warehouse


    ## Get WMS Cycle Counts by Warehouse

    Retrieve all cycle counts for a specific warehouse with comprehensive filtering capabilities for
    warehouse-focused operational management.

    ### Features
    - **Warehouse-Scoped Retrieval**: Get all cycle counts for specific warehouse facility
    - **Status Filtering**: Filter by count status for workflow management
    - **Type-Based Filtering**: Filter by count types for methodology-specific views
    - **Date Range Filtering**: Filter by scheduled dates for time-based analysis
    - **Complete Count Details**: Returns full cycle count information including results
    - **Operational Context**: Warehouse-focused view for facility management

    ### Query Parameters
    - **status**: Optional - Filter by count status (supports multiple values)
    - **countType**: Optional - Filter by count types (supports multiple values)
    - **dateStart**: Optional - Start date for scheduled date filtering
    - **dateEnd**: Optional - End date for scheduled date filtering

    ### Business Logic
    - warehouseId from path parameter scopes all results to specific warehouse
    - All filter parameters support array syntax for multiple values
    - Date filtering applies to scheduled date field
    - Results include complete count details with assignments and results
    - Sorted by scheduled date and creation time for operational relevance

    ### Use Cases
    - **Warehouse Management**: Manage all cycle counts within specific warehouse
    - **Operational Planning**: Plan warehouse counting operations and resources
    - **Performance Monitoring**: Monitor warehouse counting performance and accuracy
    - **Historical Analysis**: Analyze warehouse counting history and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        status (Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]]):  Example:
            ['SCHEDULED', 'IN_PROGRESS'].
        count_type (Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]]):  Example:
            ['ABC', 'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        status=status,
        count_type=count_type,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]]:
    """Get cycle counts by warehouse


    ## Get WMS Cycle Counts by Warehouse

    Retrieve all cycle counts for a specific warehouse with comprehensive filtering capabilities for
    warehouse-focused operational management.

    ### Features
    - **Warehouse-Scoped Retrieval**: Get all cycle counts for specific warehouse facility
    - **Status Filtering**: Filter by count status for workflow management
    - **Type-Based Filtering**: Filter by count types for methodology-specific views
    - **Date Range Filtering**: Filter by scheduled dates for time-based analysis
    - **Complete Count Details**: Returns full cycle count information including results
    - **Operational Context**: Warehouse-focused view for facility management

    ### Query Parameters
    - **status**: Optional - Filter by count status (supports multiple values)
    - **countType**: Optional - Filter by count types (supports multiple values)
    - **dateStart**: Optional - Start date for scheduled date filtering
    - **dateEnd**: Optional - End date for scheduled date filtering

    ### Business Logic
    - warehouseId from path parameter scopes all results to specific warehouse
    - All filter parameters support array syntax for multiple values
    - Date filtering applies to scheduled date field
    - Results include complete count details with assignments and results
    - Sorted by scheduled date and creation time for operational relevance

    ### Use Cases
    - **Warehouse Management**: Manage all cycle counts within specific warehouse
    - **Operational Planning**: Plan warehouse counting operations and resources
    - **Performance Monitoring**: Monitor warehouse counting performance and accuracy
    - **Historical Analysis**: Analyze warehouse counting history and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        status (Union[Unset, list[GetWMSCycleCountsByWarehouseStatusItem]]):  Example:
            ['SCHEDULED', 'IN_PROGRESS'].
        count_type (Union[Unset, list[GetWMSCycleCountsByWarehouseCountTypeItem]]):  Example:
            ['ABC', 'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountsByWarehouseResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            status=status,
            count_type=count_type,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
