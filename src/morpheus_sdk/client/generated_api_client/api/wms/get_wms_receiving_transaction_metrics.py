import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_receiving_transaction_metrics_response_200 import GetWMSReceivingTransactionMetricsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    params["userId"] = user_id

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
        "url": f"/{world_id}/wms/receiving-transactions/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSReceivingTransactionMetricsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]:
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
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]:
    """Get receiving transaction metrics


    ## Get WMS Receiving Transaction Metrics

    Generate comprehensive metrics and analytics for receiving transaction performance analysis.

    ### Features
    - **Performance Analytics**: Transaction completion rates, processing times, and accuracy metrics
    - **User Performance**: Individual user performance tracking and comparison
    - **Daily Volume Analysis**: Daily transaction volumes and trends
    - **Accuracy Tracking**: Receiving accuracy percentages and discrepancy analysis
    - **Temporal Filtering**: Date range analysis for trend identification
    - **Multi-Dimensional Analysis**: Warehouse and user-specific metrics

    ### Metrics Included
    - **Transaction Volumes**: Total, completed, and pending transaction counts
    - **Accuracy Metrics**: Receiving accuracy percentages and discrepancy tracking
    - **Processing Times**: Average processing times and efficiency indicators
    - **User Performance**: Individual user statistics and performance comparison
    - **Daily Trends**: Daily transaction volumes and accuracy trends
    - **Discrepancy Analysis**: Items received vs expected variance tracking

    ### Query Parameters
    - **warehouseId**: Optional - Scope metrics to specific warehouse
    - **userId**: Optional - Focus on specific user performance
    - **dateStart/dateEnd**: Optional - Time range for metric calculation

    ### Business Logic
    - Metrics calculated from completed and approved transactions
    - Processing time calculated from creation to completion timestamp
    - Accuracy based on received vs expected quantity comparisons
    - User performance aggregated across all transactions in period
    - Daily volume trends show transaction distribution patterns

    **CRITICAL NOTE**: Metrics queries use 'transactionId' field references in aggregations.

    ### Use Cases
    - **Performance Dashboard**: Real-time receiving operation insights
    - **User Management**: Identify training needs and top performers
    - **Process Optimization**: Identify bottlenecks and improvement opportunities
    - **Executive Reporting**: High-level receiving performance summaries
    - **Trend Analysis**: Long-term performance trend identification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        user_id=user_id,
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
    warehouse_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]:
    """Get receiving transaction metrics


    ## Get WMS Receiving Transaction Metrics

    Generate comprehensive metrics and analytics for receiving transaction performance analysis.

    ### Features
    - **Performance Analytics**: Transaction completion rates, processing times, and accuracy metrics
    - **User Performance**: Individual user performance tracking and comparison
    - **Daily Volume Analysis**: Daily transaction volumes and trends
    - **Accuracy Tracking**: Receiving accuracy percentages and discrepancy analysis
    - **Temporal Filtering**: Date range analysis for trend identification
    - **Multi-Dimensional Analysis**: Warehouse and user-specific metrics

    ### Metrics Included
    - **Transaction Volumes**: Total, completed, and pending transaction counts
    - **Accuracy Metrics**: Receiving accuracy percentages and discrepancy tracking
    - **Processing Times**: Average processing times and efficiency indicators
    - **User Performance**: Individual user statistics and performance comparison
    - **Daily Trends**: Daily transaction volumes and accuracy trends
    - **Discrepancy Analysis**: Items received vs expected variance tracking

    ### Query Parameters
    - **warehouseId**: Optional - Scope metrics to specific warehouse
    - **userId**: Optional - Focus on specific user performance
    - **dateStart/dateEnd**: Optional - Time range for metric calculation

    ### Business Logic
    - Metrics calculated from completed and approved transactions
    - Processing time calculated from creation to completion timestamp
    - Accuracy based on received vs expected quantity comparisons
    - User performance aggregated across all transactions in period
    - Daily volume trends show transaction distribution patterns

    **CRITICAL NOTE**: Metrics queries use 'transactionId' field references in aggregations.

    ### Use Cases
    - **Performance Dashboard**: Real-time receiving operation insights
    - **User Management**: Identify training needs and top performers
    - **Process Optimization**: Identify bottlenecks and improvement opportunities
    - **Executive Reporting**: High-level receiving performance summaries
    - **Trend Analysis**: Long-term performance trend identification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        user_id=user_id,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]:
    """Get receiving transaction metrics


    ## Get WMS Receiving Transaction Metrics

    Generate comprehensive metrics and analytics for receiving transaction performance analysis.

    ### Features
    - **Performance Analytics**: Transaction completion rates, processing times, and accuracy metrics
    - **User Performance**: Individual user performance tracking and comparison
    - **Daily Volume Analysis**: Daily transaction volumes and trends
    - **Accuracy Tracking**: Receiving accuracy percentages and discrepancy analysis
    - **Temporal Filtering**: Date range analysis for trend identification
    - **Multi-Dimensional Analysis**: Warehouse and user-specific metrics

    ### Metrics Included
    - **Transaction Volumes**: Total, completed, and pending transaction counts
    - **Accuracy Metrics**: Receiving accuracy percentages and discrepancy tracking
    - **Processing Times**: Average processing times and efficiency indicators
    - **User Performance**: Individual user statistics and performance comparison
    - **Daily Trends**: Daily transaction volumes and accuracy trends
    - **Discrepancy Analysis**: Items received vs expected variance tracking

    ### Query Parameters
    - **warehouseId**: Optional - Scope metrics to specific warehouse
    - **userId**: Optional - Focus on specific user performance
    - **dateStart/dateEnd**: Optional - Time range for metric calculation

    ### Business Logic
    - Metrics calculated from completed and approved transactions
    - Processing time calculated from creation to completion timestamp
    - Accuracy based on received vs expected quantity comparisons
    - User performance aggregated across all transactions in period
    - Daily volume trends show transaction distribution patterns

    **CRITICAL NOTE**: Metrics queries use 'transactionId' field references in aggregations.

    ### Use Cases
    - **Performance Dashboard**: Real-time receiving operation insights
    - **User Management**: Identify training needs and top performers
    - **Process Optimization**: Identify bottlenecks and improvement opportunities
    - **Executive Reporting**: High-level receiving performance summaries
    - **Trend Analysis**: Long-term performance trend identification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        user_id=user_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]]:
    """Get receiving transaction metrics


    ## Get WMS Receiving Transaction Metrics

    Generate comprehensive metrics and analytics for receiving transaction performance analysis.

    ### Features
    - **Performance Analytics**: Transaction completion rates, processing times, and accuracy metrics
    - **User Performance**: Individual user performance tracking and comparison
    - **Daily Volume Analysis**: Daily transaction volumes and trends
    - **Accuracy Tracking**: Receiving accuracy percentages and discrepancy analysis
    - **Temporal Filtering**: Date range analysis for trend identification
    - **Multi-Dimensional Analysis**: Warehouse and user-specific metrics

    ### Metrics Included
    - **Transaction Volumes**: Total, completed, and pending transaction counts
    - **Accuracy Metrics**: Receiving accuracy percentages and discrepancy tracking
    - **Processing Times**: Average processing times and efficiency indicators
    - **User Performance**: Individual user statistics and performance comparison
    - **Daily Trends**: Daily transaction volumes and accuracy trends
    - **Discrepancy Analysis**: Items received vs expected variance tracking

    ### Query Parameters
    - **warehouseId**: Optional - Scope metrics to specific warehouse
    - **userId**: Optional - Focus on specific user performance
    - **dateStart/dateEnd**: Optional - Time range for metric calculation

    ### Business Logic
    - Metrics calculated from completed and approved transactions
    - Processing time calculated from creation to completion timestamp
    - Accuracy based on received vs expected quantity comparisons
    - User performance aggregated across all transactions in period
    - Daily volume trends show transaction distribution patterns

    **CRITICAL NOTE**: Metrics queries use 'transactionId' field references in aggregations.

    ### Use Cases
    - **Performance Dashboard**: Real-time receiving operation insights
    - **User Management**: Identify training needs and top performers
    - **Process Optimization**: Identify bottlenecks and improvement opportunities
    - **Executive Reporting**: High-level receiving performance summaries
    - **Trend Analysis**: Long-term performance trend identification


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSReceivingTransactionMetricsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            user_id=user_id,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
