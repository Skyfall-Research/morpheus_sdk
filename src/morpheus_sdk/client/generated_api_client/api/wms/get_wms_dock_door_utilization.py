import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_dock_door_utilization_door_type_item import GetWMSDockDoorUtilizationDoorTypeItem
from ...models.get_wms_dock_door_utilization_response_200 import GetWMSDockDoorUtilizationResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: str,
    door_type: Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_door_type: Union[Unset, list[str]] = UNSET
    if not isinstance(door_type, Unset):
        json_door_type = []
        for door_type_item_data in door_type:
            door_type_item = door_type_item_data.value
            json_door_type.append(door_type_item)

    params["doorType"] = json_door_type

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
        "url": f"/{world_id}/wms/dock-doors/utilization",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDockDoorUtilizationResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]:
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
    door_type: Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]:
    """Get dock door utilization metrics


    ## Get WMS Dock Door Utilization Metrics

    Retrieve comprehensive utilization analytics for dock doors within a warehouse, including status
    distribution, type breakdown, and operational efficiency metrics.

    ### Features
    - **Comprehensive Metrics**: Total doors, status distribution, and utilization percentages
    - **Type Analysis**: Breakdown by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **Time-Based Filtering**: Historical utilization analysis for specified date ranges
    - **Operational Insights**: Real-time efficiency and capacity utilization metrics
    - **Performance Tracking**: Monitor dock door productivity and identify optimization opportunities

    ### Business Logic
    - warehouseId scopes utilization analysis to specific facility
    - Status aggregation provides real-time capacity management insights
    - doorType filtering enables type-specific utilization analysis
    - Date range filtering supports historical trend analysis and reporting
    - Utilization percentages calculated as (occupied doors / total doors) * 100
    - Type-specific breakdown enables targeted operational improvements

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **doorType**: Optional - Filter by specific door type(s)
    - **dateStart**: Optional - Start date for historical utilization analysis
    - **dateEnd**: Optional - End date for historical utilization analysis

    ### Business Metrics
    - **Total Doors**: Complete inventory of dock doors in warehouse
    - **Status Distribution**: Count of doors by operational status
    - **Utilization Percentage**: Overall facility dock utilization efficiency
    - **Type Breakdown**: Door type specific utilization and productivity metrics

    ### Use Cases
    - **Capacity Planning**: Assess current dock door utilization for expansion planning
    - **Operational Efficiency**: Monitor real-time dock door productivity
    - **Performance Analysis**: Analyze historical trends and identify improvement opportunities
    - **Resource Optimization**: Balance door assignments across types and zones
    - **Management Reporting**: Generate utilization reports for stakeholder analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        door_type=door_type,
        date_start=date_start,
        date_end=date_end,
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
    door_type: Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]:
    """Get dock door utilization metrics


    ## Get WMS Dock Door Utilization Metrics

    Retrieve comprehensive utilization analytics for dock doors within a warehouse, including status
    distribution, type breakdown, and operational efficiency metrics.

    ### Features
    - **Comprehensive Metrics**: Total doors, status distribution, and utilization percentages
    - **Type Analysis**: Breakdown by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **Time-Based Filtering**: Historical utilization analysis for specified date ranges
    - **Operational Insights**: Real-time efficiency and capacity utilization metrics
    - **Performance Tracking**: Monitor dock door productivity and identify optimization opportunities

    ### Business Logic
    - warehouseId scopes utilization analysis to specific facility
    - Status aggregation provides real-time capacity management insights
    - doorType filtering enables type-specific utilization analysis
    - Date range filtering supports historical trend analysis and reporting
    - Utilization percentages calculated as (occupied doors / total doors) * 100
    - Type-specific breakdown enables targeted operational improvements

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **doorType**: Optional - Filter by specific door type(s)
    - **dateStart**: Optional - Start date for historical utilization analysis
    - **dateEnd**: Optional - End date for historical utilization analysis

    ### Business Metrics
    - **Total Doors**: Complete inventory of dock doors in warehouse
    - **Status Distribution**: Count of doors by operational status
    - **Utilization Percentage**: Overall facility dock utilization efficiency
    - **Type Breakdown**: Door type specific utilization and productivity metrics

    ### Use Cases
    - **Capacity Planning**: Assess current dock door utilization for expansion planning
    - **Operational Efficiency**: Monitor real-time dock door productivity
    - **Performance Analysis**: Analyze historical trends and identify improvement opportunities
    - **Resource Optimization**: Balance door assignments across types and zones
    - **Management Reporting**: Generate utilization reports for stakeholder analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        door_type=door_type,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    door_type: Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]:
    """Get dock door utilization metrics


    ## Get WMS Dock Door Utilization Metrics

    Retrieve comprehensive utilization analytics for dock doors within a warehouse, including status
    distribution, type breakdown, and operational efficiency metrics.

    ### Features
    - **Comprehensive Metrics**: Total doors, status distribution, and utilization percentages
    - **Type Analysis**: Breakdown by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **Time-Based Filtering**: Historical utilization analysis for specified date ranges
    - **Operational Insights**: Real-time efficiency and capacity utilization metrics
    - **Performance Tracking**: Monitor dock door productivity and identify optimization opportunities

    ### Business Logic
    - warehouseId scopes utilization analysis to specific facility
    - Status aggregation provides real-time capacity management insights
    - doorType filtering enables type-specific utilization analysis
    - Date range filtering supports historical trend analysis and reporting
    - Utilization percentages calculated as (occupied doors / total doors) * 100
    - Type-specific breakdown enables targeted operational improvements

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **doorType**: Optional - Filter by specific door type(s)
    - **dateStart**: Optional - Start date for historical utilization analysis
    - **dateEnd**: Optional - End date for historical utilization analysis

    ### Business Metrics
    - **Total Doors**: Complete inventory of dock doors in warehouse
    - **Status Distribution**: Count of doors by operational status
    - **Utilization Percentage**: Overall facility dock utilization efficiency
    - **Type Breakdown**: Door type specific utilization and productivity metrics

    ### Use Cases
    - **Capacity Planning**: Assess current dock door utilization for expansion planning
    - **Operational Efficiency**: Monitor real-time dock door productivity
    - **Performance Analysis**: Analyze historical trends and identify improvement opportunities
    - **Resource Optimization**: Balance door assignments across types and zones
    - **Management Reporting**: Generate utilization reports for stakeholder analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        door_type=door_type,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    door_type: Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]]:
    """Get dock door utilization metrics


    ## Get WMS Dock Door Utilization Metrics

    Retrieve comprehensive utilization analytics for dock doors within a warehouse, including status
    distribution, type breakdown, and operational efficiency metrics.

    ### Features
    - **Comprehensive Metrics**: Total doors, status distribution, and utilization percentages
    - **Type Analysis**: Breakdown by door type (INBOUND, OUTBOUND, CROSS_DOCK)
    - **Time-Based Filtering**: Historical utilization analysis for specified date ranges
    - **Operational Insights**: Real-time efficiency and capacity utilization metrics
    - **Performance Tracking**: Monitor dock door productivity and identify optimization opportunities

    ### Business Logic
    - warehouseId scopes utilization analysis to specific facility
    - Status aggregation provides real-time capacity management insights
    - doorType filtering enables type-specific utilization analysis
    - Date range filtering supports historical trend analysis and reporting
    - Utilization percentages calculated as (occupied doors / total doors) * 100
    - Type-specific breakdown enables targeted operational improvements

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **doorType**: Optional - Filter by specific door type(s)
    - **dateStart**: Optional - Start date for historical utilization analysis
    - **dateEnd**: Optional - End date for historical utilization analysis

    ### Business Metrics
    - **Total Doors**: Complete inventory of dock doors in warehouse
    - **Status Distribution**: Count of doors by operational status
    - **Utilization Percentage**: Overall facility dock utilization efficiency
    - **Type Breakdown**: Door type specific utilization and productivity metrics

    ### Use Cases
    - **Capacity Planning**: Assess current dock door utilization for expansion planning
    - **Operational Efficiency**: Monitor real-time dock door productivity
    - **Performance Analysis**: Analyze historical trends and identify improvement opportunities
    - **Resource Optimization**: Balance door assignments across types and zones
    - **Management Reporting**: Generate utilization reports for stakeholder analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        door_type (Union[Unset, list[GetWMSDockDoorUtilizationDoorTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDockDoorUtilizationResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            door_type=door_type,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
