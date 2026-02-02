import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_cycle_counts_by_status_count_type_item import GetWMSCycleCountsByStatusCountTypeItem
from ...models.get_wms_cycle_counts_by_status_response_200 import GetWMSCycleCountsByStatusResponse200
from ...models.get_wms_cycle_counts_by_status_status_item import GetWMSCycleCountsByStatusStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: list[GetWMSCycleCountsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status = []
    for status_item_data in status:
        status_item = status_item_data.value
        json_status.append(status_item)

    params["status"] = json_status

    params["warehouseId"] = warehouse_id

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

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/cycle-counts/status",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSCycleCountsByStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]:
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
    status: list[GetWMSCycleCountsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]:
    """Get cycle counts by status with filtering


    ## Get WMS Cycle Counts by Status

    Retrieve cycle counts filtered by status with comprehensive filtering capabilities for operational
    management and monitoring.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using array syntax
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused operations
    - **Count Type Filtering**: Filter by count type for methodology-specific views
    - **Date Range Filtering**: Filter by date ranges for time-based analysis
    - **Cursor Pagination**: Efficient pagination for large datasets with cursor-based navigation
    - **Flexible Queries**: Combine multiple filter parameters for precise result sets

    ### Query Parameters
    - **status**: Required - Single status or array of statuses for filtering
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **countType**: Optional - Filter by count types (supports array of types)
    - **dateStart**: Optional - Start date for scheduled date filtering (ISO 8601 format)
    - **dateEnd**: Optional - End date for scheduled date filtering (ISO 8601 format)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)

    ### Available Status Values
    - **SCHEDULED**: Counts scheduled and ready for execution
    - **IN_PROGRESS**: Counts currently being executed
    - **COMPLETED**: Count execution completed, pending approval
    - **APPROVED**: Count results approved and applied
    - **REJECTED**: Count results rejected, requiring recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Logic
    - Status parameter is required and supports multiple values
    - Date filtering applies to scheduled date field
    - Results sorted by scheduled date and creation time
    - Pagination preserves filter context across page requests
    - Returns complete count details including assignments and progress

    ### Use Cases
    - **Operational Monitoring**: Track counts by status for operational oversight
    - **Workflow Management**: Manage count execution and approval workflows
    - **Performance Analysis**: Analyze count completion rates and timelines
    - **Resource Planning**: Plan resources based on scheduled and in-progress counts


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSCycleCountsByStatusStatusItem]):  Example: ['SCHEDULED',
            'IN_PROGRESS'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        count_type (Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]]):  Example: ['ABC',
            'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        cursor (Union[Unset, str]):  Example: eyJfaWQiOiI2NWE5M2Q4NjQyOWM0YzAwMTNiMWQ4YjUifQ==.
        limit (Union[Unset, int]):  Default: 50. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        count_type=count_type,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSCycleCountsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]:
    """Get cycle counts by status with filtering


    ## Get WMS Cycle Counts by Status

    Retrieve cycle counts filtered by status with comprehensive filtering capabilities for operational
    management and monitoring.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using array syntax
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused operations
    - **Count Type Filtering**: Filter by count type for methodology-specific views
    - **Date Range Filtering**: Filter by date ranges for time-based analysis
    - **Cursor Pagination**: Efficient pagination for large datasets with cursor-based navigation
    - **Flexible Queries**: Combine multiple filter parameters for precise result sets

    ### Query Parameters
    - **status**: Required - Single status or array of statuses for filtering
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **countType**: Optional - Filter by count types (supports array of types)
    - **dateStart**: Optional - Start date for scheduled date filtering (ISO 8601 format)
    - **dateEnd**: Optional - End date for scheduled date filtering (ISO 8601 format)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)

    ### Available Status Values
    - **SCHEDULED**: Counts scheduled and ready for execution
    - **IN_PROGRESS**: Counts currently being executed
    - **COMPLETED**: Count execution completed, pending approval
    - **APPROVED**: Count results approved and applied
    - **REJECTED**: Count results rejected, requiring recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Logic
    - Status parameter is required and supports multiple values
    - Date filtering applies to scheduled date field
    - Results sorted by scheduled date and creation time
    - Pagination preserves filter context across page requests
    - Returns complete count details including assignments and progress

    ### Use Cases
    - **Operational Monitoring**: Track counts by status for operational oversight
    - **Workflow Management**: Manage count execution and approval workflows
    - **Performance Analysis**: Analyze count completion rates and timelines
    - **Resource Planning**: Plan resources based on scheduled and in-progress counts


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSCycleCountsByStatusStatusItem]):  Example: ['SCHEDULED',
            'IN_PROGRESS'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        count_type (Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]]):  Example: ['ABC',
            'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        cursor (Union[Unset, str]):  Example: eyJfaWQiOiI2NWE5M2Q4NjQyOWM0YzAwMTNiMWQ4YjUifQ==.
        limit (Union[Unset, int]):  Default: 50. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        warehouse_id=warehouse_id,
        count_type=count_type,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSCycleCountsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]:
    """Get cycle counts by status with filtering


    ## Get WMS Cycle Counts by Status

    Retrieve cycle counts filtered by status with comprehensive filtering capabilities for operational
    management and monitoring.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using array syntax
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused operations
    - **Count Type Filtering**: Filter by count type for methodology-specific views
    - **Date Range Filtering**: Filter by date ranges for time-based analysis
    - **Cursor Pagination**: Efficient pagination for large datasets with cursor-based navigation
    - **Flexible Queries**: Combine multiple filter parameters for precise result sets

    ### Query Parameters
    - **status**: Required - Single status or array of statuses for filtering
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **countType**: Optional - Filter by count types (supports array of types)
    - **dateStart**: Optional - Start date for scheduled date filtering (ISO 8601 format)
    - **dateEnd**: Optional - End date for scheduled date filtering (ISO 8601 format)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)

    ### Available Status Values
    - **SCHEDULED**: Counts scheduled and ready for execution
    - **IN_PROGRESS**: Counts currently being executed
    - **COMPLETED**: Count execution completed, pending approval
    - **APPROVED**: Count results approved and applied
    - **REJECTED**: Count results rejected, requiring recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Logic
    - Status parameter is required and supports multiple values
    - Date filtering applies to scheduled date field
    - Results sorted by scheduled date and creation time
    - Pagination preserves filter context across page requests
    - Returns complete count details including assignments and progress

    ### Use Cases
    - **Operational Monitoring**: Track counts by status for operational oversight
    - **Workflow Management**: Manage count execution and approval workflows
    - **Performance Analysis**: Analyze count completion rates and timelines
    - **Resource Planning**: Plan resources based on scheduled and in-progress counts


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSCycleCountsByStatusStatusItem]):  Example: ['SCHEDULED',
            'IN_PROGRESS'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        count_type (Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]]):  Example: ['ABC',
            'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        cursor (Union[Unset, str]):  Example: eyJfaWQiOiI2NWE5M2Q4NjQyOWM0YzAwMTNiMWQ4YjUifQ==.
        limit (Union[Unset, int]):  Default: 50. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        warehouse_id=warehouse_id,
        count_type=count_type,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: list[GetWMSCycleCountsByStatusStatusItem],
    warehouse_id: Union[Unset, str] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]]:
    """Get cycle counts by status with filtering


    ## Get WMS Cycle Counts by Status

    Retrieve cycle counts filtered by status with comprehensive filtering capabilities for operational
    management and monitoring.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using array syntax
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused operations
    - **Count Type Filtering**: Filter by count type for methodology-specific views
    - **Date Range Filtering**: Filter by date ranges for time-based analysis
    - **Cursor Pagination**: Efficient pagination for large datasets with cursor-based navigation
    - **Flexible Queries**: Combine multiple filter parameters for precise result sets

    ### Query Parameters
    - **status**: Required - Single status or array of statuses for filtering
    - **warehouseId**: Optional - Filter by specific warehouse identifier
    - **countType**: Optional - Filter by count types (supports array of types)
    - **dateStart**: Optional - Start date for scheduled date filtering (ISO 8601 format)
    - **dateEnd**: Optional - End date for scheduled date filtering (ISO 8601 format)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)

    ### Available Status Values
    - **SCHEDULED**: Counts scheduled and ready for execution
    - **IN_PROGRESS**: Counts currently being executed
    - **COMPLETED**: Count execution completed, pending approval
    - **APPROVED**: Count results approved and applied
    - **REJECTED**: Count results rejected, requiring recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Logic
    - Status parameter is required and supports multiple values
    - Date filtering applies to scheduled date field
    - Results sorted by scheduled date and creation time
    - Pagination preserves filter context across page requests
    - Returns complete count details including assignments and progress

    ### Use Cases
    - **Operational Monitoring**: Track counts by status for operational oversight
    - **Workflow Management**: Manage count execution and approval workflows
    - **Performance Analysis**: Analyze count completion rates and timelines
    - **Resource Planning**: Plan resources based on scheduled and in-progress counts


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (list[GetWMSCycleCountsByStatusStatusItem]):  Example: ['SCHEDULED',
            'IN_PROGRESS'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        count_type (Union[Unset, list[GetWMSCycleCountsByStatusCountTypeItem]]):  Example: ['ABC',
            'DAILY'].
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        cursor (Union[Unset, str]):  Example: eyJfaWQiOiI2NWE5M2Q4NjQyOWM0YzAwMTNiMWQ4YjUifQ==.
        limit (Union[Unset, int]):  Default: 50. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountsByStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            warehouse_id=warehouse_id,
            count_type=count_type,
            date_start=date_start,
            date_end=date_end,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
