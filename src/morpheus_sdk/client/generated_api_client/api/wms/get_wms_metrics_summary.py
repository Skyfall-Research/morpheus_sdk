import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_metrics_summary_response_200 import GetWMSMetricsSummaryResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["zoneId"] = zone_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/daily-metrics/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSMetricsSummaryResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSMetricsSummaryResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSMetricsSummaryResponse200]:
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
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSMetricsSummaryResponse200]:
    """Get comprehensive metrics summary


    ## Get WMS Daily Metrics Summary

    Generate a comprehensive summary of warehouse performance metrics with averages, totals, and trend
    analysis for strategic decision-making and operational planning.

    ### Features
    - **Aggregated Analytics**: Calculate average performance metrics across date ranges
    - **Multi-Category Summary**: Comprehensive summary across all operational categories
    - **Trend Analysis**: Historical trend data for performance pattern identification
    - **Flexible Filtering**: Filter by warehouse, date range, and zone for targeted analysis
    - **Performance Benchmarking**: Establish performance baselines and benchmarks
    - **Executive Reporting**: High-level metrics for executive reporting and dashboards

    ### Summary Categories
    - **Inbound Operations**: Average POs received, units processed, productivity rates
    - **Picking Operations**: Average orders shipped, pick accuracy, productivity metrics
    - **Packing Operations**: Average orders packed, packing rates, efficiency metrics
    - **Inventory Management**: Average accuracy and turnover rate metrics
    - **Trend Analysis**: Daily performance trends with key operational indicators

    ### Query Parameters
    - **warehouseId**: Optional - Filter summary by specific warehouse facility
    - **dateStart**: Optional - Start date for summary period
    - **dateEnd**: Optional - End date for summary period
    - **zoneId**: Optional - Filter summary by specific zone

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Date range filtering is inclusive of both start and end dates
    - Warehouse filtering enables facility-specific analysis
    - Zone filtering provides zone-specific performance summaries
    - Averages calculated from actual recorded daily metrics
    - Trend data includes key performance indicators over time

    ### Use Cases
    - **Executive Dashboards**: High-level performance metrics for leadership
    - **Performance Benchmarking**: Establish and track performance standards
    - **Operational Planning**: Use historical data for future planning
    - **Facility Comparisons**: Compare performance across different warehouses
    - **Zone Analysis**: Evaluate zone-specific operational efficiency
    - **Strategic Analysis**: Long-term performance trend analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-11-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-11-27.
        zone_id (Union[Unset, str]):  Example: ZONE_PICK_A.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSMetricsSummaryResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        zone_id=zone_id,
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
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSMetricsSummaryResponse200]:
    """Get comprehensive metrics summary


    ## Get WMS Daily Metrics Summary

    Generate a comprehensive summary of warehouse performance metrics with averages, totals, and trend
    analysis for strategic decision-making and operational planning.

    ### Features
    - **Aggregated Analytics**: Calculate average performance metrics across date ranges
    - **Multi-Category Summary**: Comprehensive summary across all operational categories
    - **Trend Analysis**: Historical trend data for performance pattern identification
    - **Flexible Filtering**: Filter by warehouse, date range, and zone for targeted analysis
    - **Performance Benchmarking**: Establish performance baselines and benchmarks
    - **Executive Reporting**: High-level metrics for executive reporting and dashboards

    ### Summary Categories
    - **Inbound Operations**: Average POs received, units processed, productivity rates
    - **Picking Operations**: Average orders shipped, pick accuracy, productivity metrics
    - **Packing Operations**: Average orders packed, packing rates, efficiency metrics
    - **Inventory Management**: Average accuracy and turnover rate metrics
    - **Trend Analysis**: Daily performance trends with key operational indicators

    ### Query Parameters
    - **warehouseId**: Optional - Filter summary by specific warehouse facility
    - **dateStart**: Optional - Start date for summary period
    - **dateEnd**: Optional - End date for summary period
    - **zoneId**: Optional - Filter summary by specific zone

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Date range filtering is inclusive of both start and end dates
    - Warehouse filtering enables facility-specific analysis
    - Zone filtering provides zone-specific performance summaries
    - Averages calculated from actual recorded daily metrics
    - Trend data includes key performance indicators over time

    ### Use Cases
    - **Executive Dashboards**: High-level performance metrics for leadership
    - **Performance Benchmarking**: Establish and track performance standards
    - **Operational Planning**: Use historical data for future planning
    - **Facility Comparisons**: Compare performance across different warehouses
    - **Zone Analysis**: Evaluate zone-specific operational efficiency
    - **Strategic Analysis**: Long-term performance trend analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-11-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-11-27.
        zone_id (Union[Unset, str]):  Example: ZONE_PICK_A.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSMetricsSummaryResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        zone_id=zone_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Response[GetWMSMetricsSummaryResponse200]:
    """Get comprehensive metrics summary


    ## Get WMS Daily Metrics Summary

    Generate a comprehensive summary of warehouse performance metrics with averages, totals, and trend
    analysis for strategic decision-making and operational planning.

    ### Features
    - **Aggregated Analytics**: Calculate average performance metrics across date ranges
    - **Multi-Category Summary**: Comprehensive summary across all operational categories
    - **Trend Analysis**: Historical trend data for performance pattern identification
    - **Flexible Filtering**: Filter by warehouse, date range, and zone for targeted analysis
    - **Performance Benchmarking**: Establish performance baselines and benchmarks
    - **Executive Reporting**: High-level metrics for executive reporting and dashboards

    ### Summary Categories
    - **Inbound Operations**: Average POs received, units processed, productivity rates
    - **Picking Operations**: Average orders shipped, pick accuracy, productivity metrics
    - **Packing Operations**: Average orders packed, packing rates, efficiency metrics
    - **Inventory Management**: Average accuracy and turnover rate metrics
    - **Trend Analysis**: Daily performance trends with key operational indicators

    ### Query Parameters
    - **warehouseId**: Optional - Filter summary by specific warehouse facility
    - **dateStart**: Optional - Start date for summary period
    - **dateEnd**: Optional - End date for summary period
    - **zoneId**: Optional - Filter summary by specific zone

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Date range filtering is inclusive of both start and end dates
    - Warehouse filtering enables facility-specific analysis
    - Zone filtering provides zone-specific performance summaries
    - Averages calculated from actual recorded daily metrics
    - Trend data includes key performance indicators over time

    ### Use Cases
    - **Executive Dashboards**: High-level performance metrics for leadership
    - **Performance Benchmarking**: Establish and track performance standards
    - **Operational Planning**: Use historical data for future planning
    - **Facility Comparisons**: Compare performance across different warehouses
    - **Zone Analysis**: Evaluate zone-specific operational efficiency
    - **Strategic Analysis**: Long-term performance trend analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-11-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-11-27.
        zone_id (Union[Unset, str]):  Example: ZONE_PICK_A.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSMetricsSummaryResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        zone_id=zone_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    zone_id: Union[Unset, str] = UNSET,
) -> Optional[GetWMSMetricsSummaryResponse200]:
    """Get comprehensive metrics summary


    ## Get WMS Daily Metrics Summary

    Generate a comprehensive summary of warehouse performance metrics with averages, totals, and trend
    analysis for strategic decision-making and operational planning.

    ### Features
    - **Aggregated Analytics**: Calculate average performance metrics across date ranges
    - **Multi-Category Summary**: Comprehensive summary across all operational categories
    - **Trend Analysis**: Historical trend data for performance pattern identification
    - **Flexible Filtering**: Filter by warehouse, date range, and zone for targeted analysis
    - **Performance Benchmarking**: Establish performance baselines and benchmarks
    - **Executive Reporting**: High-level metrics for executive reporting and dashboards

    ### Summary Categories
    - **Inbound Operations**: Average POs received, units processed, productivity rates
    - **Picking Operations**: Average orders shipped, pick accuracy, productivity metrics
    - **Packing Operations**: Average orders packed, packing rates, efficiency metrics
    - **Inventory Management**: Average accuracy and turnover rate metrics
    - **Trend Analysis**: Daily performance trends with key operational indicators

    ### Query Parameters
    - **warehouseId**: Optional - Filter summary by specific warehouse facility
    - **dateStart**: Optional - Start date for summary period
    - **dateEnd**: Optional - End date for summary period
    - **zoneId**: Optional - Filter summary by specific zone

    ### Business Logic
    - All query parameters are optional for maximum flexibility
    - Date range filtering is inclusive of both start and end dates
    - Warehouse filtering enables facility-specific analysis
    - Zone filtering provides zone-specific performance summaries
    - Averages calculated from actual recorded daily metrics
    - Trend data includes key performance indicators over time

    ### Use Cases
    - **Executive Dashboards**: High-level performance metrics for leadership
    - **Performance Benchmarking**: Establish and track performance standards
    - **Operational Planning**: Use historical data for future planning
    - **Facility Comparisons**: Compare performance across different warehouses
    - **Zone Analysis**: Evaluate zone-specific operational efficiency
    - **Strategic Analysis**: Long-term performance trend analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-11-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-11-27.
        zone_id (Union[Unset, str]):  Example: ZONE_PICK_A.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSMetricsSummaryResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            zone_id=zone_id,
        )
    ).parsed
