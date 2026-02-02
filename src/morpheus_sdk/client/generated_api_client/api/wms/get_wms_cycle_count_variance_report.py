import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_cycle_count_variance_report_count_type_item import GetWMSCycleCountVarianceReportCountTypeItem
from ...models.get_wms_cycle_count_variance_report_response_200 import GetWMSCycleCountVarianceReportResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]] = UNSET,
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

    json_count_type: Union[Unset, list[str]] = UNSET
    if not isinstance(count_type, Unset):
        json_count_type = []
        for count_type_item_data in count_type:
            count_type_item = count_type_item_data.value
            json_count_type.append(count_type_item)

    params["countType"] = json_count_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/cycle-counts/variance-report",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSCycleCountVarianceReportResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]:
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
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]:
    """Get cycle count variance report


    ## Get WMS Cycle Count Variance Report

    Generate comprehensive variance analysis report for cycle count results with statistical analysis
    and operational insights.

    ### Features
    - **Comprehensive Variance Analysis**: Detailed variance statistics and trends
    - **Multi-Dimensional Filtering**: Filter by warehouse, date range, and count type
    - **Statistical Insights**: Variance percentages, accuracy metrics, and trend analysis
    - **Financial Impact**: Variance value calculations and cost impact analysis
    - **Operational Metrics**: Count accuracy, completion rates, and efficiency indicators
    - **Trend Analysis**: Historical variance patterns and improvement tracking

    ### Report Data Includes
    - **Overall Variance Statistics**: Total variances, accuracy percentages, and trends
    - **Variance Distribution**: Variance patterns by location, product, and user
    - **Financial Impact**: Monetary impact of variances and cost analysis
    - **Accuracy Metrics**: Count accuracy rates and improvement trends
    - **Operational Performance**: Count completion rates and efficiency metrics

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **dateStart**: Optional - Start date for report period
    - **dateEnd**: Optional - End date for report period
    - **countType**: Optional - Filter by count types for methodology analysis

    ### Business Logic
    - Analyzes completed and approved cycle counts for variance calculation
    - Calculates statistical variance metrics and accuracy percentages
    - Includes financial impact analysis based on product costs
    - Provides trending analysis for operational improvement
    - Aggregates results by multiple dimensions for comprehensive insights

    ### Use Cases
    - **Performance Analysis**: Analyze cycle count accuracy and variance trends
    - **Operational Improvement**: Identify areas for counting process improvement
    - **Financial Impact**: Assess monetary impact of inventory variances
    - **Management Reporting**: Generate variance reports for management review


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        count_type (Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]]):  Example:
            ['ABC', 'FULL'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        count_type=count_type,
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
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]:
    """Get cycle count variance report


    ## Get WMS Cycle Count Variance Report

    Generate comprehensive variance analysis report for cycle count results with statistical analysis
    and operational insights.

    ### Features
    - **Comprehensive Variance Analysis**: Detailed variance statistics and trends
    - **Multi-Dimensional Filtering**: Filter by warehouse, date range, and count type
    - **Statistical Insights**: Variance percentages, accuracy metrics, and trend analysis
    - **Financial Impact**: Variance value calculations and cost impact analysis
    - **Operational Metrics**: Count accuracy, completion rates, and efficiency indicators
    - **Trend Analysis**: Historical variance patterns and improvement tracking

    ### Report Data Includes
    - **Overall Variance Statistics**: Total variances, accuracy percentages, and trends
    - **Variance Distribution**: Variance patterns by location, product, and user
    - **Financial Impact**: Monetary impact of variances and cost analysis
    - **Accuracy Metrics**: Count accuracy rates and improvement trends
    - **Operational Performance**: Count completion rates and efficiency metrics

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **dateStart**: Optional - Start date for report period
    - **dateEnd**: Optional - End date for report period
    - **countType**: Optional - Filter by count types for methodology analysis

    ### Business Logic
    - Analyzes completed and approved cycle counts for variance calculation
    - Calculates statistical variance metrics and accuracy percentages
    - Includes financial impact analysis based on product costs
    - Provides trending analysis for operational improvement
    - Aggregates results by multiple dimensions for comprehensive insights

    ### Use Cases
    - **Performance Analysis**: Analyze cycle count accuracy and variance trends
    - **Operational Improvement**: Identify areas for counting process improvement
    - **Financial Impact**: Assess monetary impact of inventory variances
    - **Management Reporting**: Generate variance reports for management review


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        count_type (Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]]):  Example:
            ['ABC', 'FULL'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        count_type=count_type,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]:
    """Get cycle count variance report


    ## Get WMS Cycle Count Variance Report

    Generate comprehensive variance analysis report for cycle count results with statistical analysis
    and operational insights.

    ### Features
    - **Comprehensive Variance Analysis**: Detailed variance statistics and trends
    - **Multi-Dimensional Filtering**: Filter by warehouse, date range, and count type
    - **Statistical Insights**: Variance percentages, accuracy metrics, and trend analysis
    - **Financial Impact**: Variance value calculations and cost impact analysis
    - **Operational Metrics**: Count accuracy, completion rates, and efficiency indicators
    - **Trend Analysis**: Historical variance patterns and improvement tracking

    ### Report Data Includes
    - **Overall Variance Statistics**: Total variances, accuracy percentages, and trends
    - **Variance Distribution**: Variance patterns by location, product, and user
    - **Financial Impact**: Monetary impact of variances and cost analysis
    - **Accuracy Metrics**: Count accuracy rates and improvement trends
    - **Operational Performance**: Count completion rates and efficiency metrics

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **dateStart**: Optional - Start date for report period
    - **dateEnd**: Optional - End date for report period
    - **countType**: Optional - Filter by count types for methodology analysis

    ### Business Logic
    - Analyzes completed and approved cycle counts for variance calculation
    - Calculates statistical variance metrics and accuracy percentages
    - Includes financial impact analysis based on product costs
    - Provides trending analysis for operational improvement
    - Aggregates results by multiple dimensions for comprehensive insights

    ### Use Cases
    - **Performance Analysis**: Analyze cycle count accuracy and variance trends
    - **Operational Improvement**: Identify areas for counting process improvement
    - **Financial Impact**: Assess monetary impact of inventory variances
    - **Management Reporting**: Generate variance reports for management review


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        count_type (Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]]):  Example:
            ['ABC', 'FULL'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        count_type=count_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    count_type: Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]]:
    """Get cycle count variance report


    ## Get WMS Cycle Count Variance Report

    Generate comprehensive variance analysis report for cycle count results with statistical analysis
    and operational insights.

    ### Features
    - **Comprehensive Variance Analysis**: Detailed variance statistics and trends
    - **Multi-Dimensional Filtering**: Filter by warehouse, date range, and count type
    - **Statistical Insights**: Variance percentages, accuracy metrics, and trend analysis
    - **Financial Impact**: Variance value calculations and cost impact analysis
    - **Operational Metrics**: Count accuracy, completion rates, and efficiency indicators
    - **Trend Analysis**: Historical variance patterns and improvement tracking

    ### Report Data Includes
    - **Overall Variance Statistics**: Total variances, accuracy percentages, and trends
    - **Variance Distribution**: Variance patterns by location, product, and user
    - **Financial Impact**: Monetary impact of variances and cost analysis
    - **Accuracy Metrics**: Count accuracy rates and improvement trends
    - **Operational Performance**: Count completion rates and efficiency metrics

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **dateStart**: Optional - Start date for report period
    - **dateEnd**: Optional - End date for report period
    - **countType**: Optional - Filter by count types for methodology analysis

    ### Business Logic
    - Analyzes completed and approved cycle counts for variance calculation
    - Calculates statistical variance metrics and accuracy percentages
    - Includes financial impact analysis based on product costs
    - Provides trending analysis for operational improvement
    - Aggregates results by multiple dimensions for comprehensive insights

    ### Use Cases
    - **Performance Analysis**: Analyze cycle count accuracy and variance trends
    - **Operational Improvement**: Identify areas for counting process improvement
    - **Financial Impact**: Assess monetary impact of inventory variances
    - **Management Reporting**: Generate variance reports for management review


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.
        count_type (Union[Unset, list[GetWMSCycleCountVarianceReportCountTypeItem]]):  Example:
            ['ABC', 'FULL'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountVarianceReportResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            count_type=count_type,
        )
    ).parsed
