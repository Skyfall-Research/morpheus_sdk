import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inbound_order_receiving_metrics_response_200 import GetWMSInboundOrderReceivingMetricsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
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

    params["vendorId"] = vendor_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inbound-orders/metrics",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInboundOrderReceivingMetricsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]:
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
    vendor_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]:
    """Get receiving performance metrics


    ## Get WMS Inbound Order Receiving Metrics

    Retrieve comprehensive receiving performance analytics including order completion rates, timing
    analysis, vendor performance, and operational efficiency metrics.

    ### Features
    - **Performance Analytics**: Complete receiving metrics for operational insight
    - **Vendor Analysis**: Top vendor performance with on-time delivery tracking
    - **Timing Metrics**: Average receiving times and efficiency measurements
    - **Accuracy Tracking**: Receiving accuracy and quality performance indicators
    - **Status Distribution**: Order status breakdown for operational visibility
    - **Historical Analysis**: Date range filtering for trend analysis and reporting

    ### Business Logic
    - Calculates comprehensive receiving metrics across specified filters
    - Vendor performance includes order count, on-time percentage, and total lines
    - Receiving accuracy based on expected vs. received quantities
    - Average receiving time calculated from receivingStarted to receivingCompleted
    - On-time receipts determined by comparing actual vs. expected arrival dates
    - Status distribution provides operational dashboard insights

    ### Query Parameters
    - **warehouseId**: Optional - Filter metrics by specific warehouse facility
    - **dateStart**: Optional - Start date for metrics analysis period
    - **dateEnd**: Optional - End date for metrics analysis period
    - **vendorId**: Optional - Filter metrics for specific vendor analysis

    ### Metrics Included
    - **Total Orders**: Complete count of orders in analysis period
    - **Completion Rate**: Percentage of orders fully received
    - **Average Receiving Time**: Mean time from start to completion of receiving
    - **On-Time Performance**: Ratio of orders received on schedule
    - **Receiving Accuracy**: Quality metric for receiving precision
    - **Status Distribution**: Breakdown of orders by current status
    - **Vendor Rankings**: Top vendors by performance metrics

    ### Use Cases
    - **Performance Monitoring**: Track receiving efficiency and operational performance
    - **Vendor Management**: Evaluate vendor performance for supplier relationship management
    - **Operational Planning**: Use metrics for capacity planning and resource allocation
    - **Quality Management**: Monitor receiving accuracy and identify improvement opportunities
    - **Executive Reporting**: Generate comprehensive receiving performance reports


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        vendor_id=vendor_id,
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
    vendor_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]:
    """Get receiving performance metrics


    ## Get WMS Inbound Order Receiving Metrics

    Retrieve comprehensive receiving performance analytics including order completion rates, timing
    analysis, vendor performance, and operational efficiency metrics.

    ### Features
    - **Performance Analytics**: Complete receiving metrics for operational insight
    - **Vendor Analysis**: Top vendor performance with on-time delivery tracking
    - **Timing Metrics**: Average receiving times and efficiency measurements
    - **Accuracy Tracking**: Receiving accuracy and quality performance indicators
    - **Status Distribution**: Order status breakdown for operational visibility
    - **Historical Analysis**: Date range filtering for trend analysis and reporting

    ### Business Logic
    - Calculates comprehensive receiving metrics across specified filters
    - Vendor performance includes order count, on-time percentage, and total lines
    - Receiving accuracy based on expected vs. received quantities
    - Average receiving time calculated from receivingStarted to receivingCompleted
    - On-time receipts determined by comparing actual vs. expected arrival dates
    - Status distribution provides operational dashboard insights

    ### Query Parameters
    - **warehouseId**: Optional - Filter metrics by specific warehouse facility
    - **dateStart**: Optional - Start date for metrics analysis period
    - **dateEnd**: Optional - End date for metrics analysis period
    - **vendorId**: Optional - Filter metrics for specific vendor analysis

    ### Metrics Included
    - **Total Orders**: Complete count of orders in analysis period
    - **Completion Rate**: Percentage of orders fully received
    - **Average Receiving Time**: Mean time from start to completion of receiving
    - **On-Time Performance**: Ratio of orders received on schedule
    - **Receiving Accuracy**: Quality metric for receiving precision
    - **Status Distribution**: Breakdown of orders by current status
    - **Vendor Rankings**: Top vendors by performance metrics

    ### Use Cases
    - **Performance Monitoring**: Track receiving efficiency and operational performance
    - **Vendor Management**: Evaluate vendor performance for supplier relationship management
    - **Operational Planning**: Use metrics for capacity planning and resource allocation
    - **Quality Management**: Monitor receiving accuracy and identify improvement opportunities
    - **Executive Reporting**: Generate comprehensive receiving performance reports


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        vendor_id=vendor_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    vendor_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]:
    """Get receiving performance metrics


    ## Get WMS Inbound Order Receiving Metrics

    Retrieve comprehensive receiving performance analytics including order completion rates, timing
    analysis, vendor performance, and operational efficiency metrics.

    ### Features
    - **Performance Analytics**: Complete receiving metrics for operational insight
    - **Vendor Analysis**: Top vendor performance with on-time delivery tracking
    - **Timing Metrics**: Average receiving times and efficiency measurements
    - **Accuracy Tracking**: Receiving accuracy and quality performance indicators
    - **Status Distribution**: Order status breakdown for operational visibility
    - **Historical Analysis**: Date range filtering for trend analysis and reporting

    ### Business Logic
    - Calculates comprehensive receiving metrics across specified filters
    - Vendor performance includes order count, on-time percentage, and total lines
    - Receiving accuracy based on expected vs. received quantities
    - Average receiving time calculated from receivingStarted to receivingCompleted
    - On-time receipts determined by comparing actual vs. expected arrival dates
    - Status distribution provides operational dashboard insights

    ### Query Parameters
    - **warehouseId**: Optional - Filter metrics by specific warehouse facility
    - **dateStart**: Optional - Start date for metrics analysis period
    - **dateEnd**: Optional - End date for metrics analysis period
    - **vendorId**: Optional - Filter metrics for specific vendor analysis

    ### Metrics Included
    - **Total Orders**: Complete count of orders in analysis period
    - **Completion Rate**: Percentage of orders fully received
    - **Average Receiving Time**: Mean time from start to completion of receiving
    - **On-Time Performance**: Ratio of orders received on schedule
    - **Receiving Accuracy**: Quality metric for receiving precision
    - **Status Distribution**: Breakdown of orders by current status
    - **Vendor Rankings**: Top vendors by performance metrics

    ### Use Cases
    - **Performance Monitoring**: Track receiving efficiency and operational performance
    - **Vendor Management**: Evaluate vendor performance for supplier relationship management
    - **Operational Planning**: Use metrics for capacity planning and resource allocation
    - **Quality Management**: Monitor receiving accuracy and identify improvement opportunities
    - **Executive Reporting**: Generate comprehensive receiving performance reports


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
        vendor_id=vendor_id,
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
    vendor_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]]:
    """Get receiving performance metrics


    ## Get WMS Inbound Order Receiving Metrics

    Retrieve comprehensive receiving performance analytics including order completion rates, timing
    analysis, vendor performance, and operational efficiency metrics.

    ### Features
    - **Performance Analytics**: Complete receiving metrics for operational insight
    - **Vendor Analysis**: Top vendor performance with on-time delivery tracking
    - **Timing Metrics**: Average receiving times and efficiency measurements
    - **Accuracy Tracking**: Receiving accuracy and quality performance indicators
    - **Status Distribution**: Order status breakdown for operational visibility
    - **Historical Analysis**: Date range filtering for trend analysis and reporting

    ### Business Logic
    - Calculates comprehensive receiving metrics across specified filters
    - Vendor performance includes order count, on-time percentage, and total lines
    - Receiving accuracy based on expected vs. received quantities
    - Average receiving time calculated from receivingStarted to receivingCompleted
    - On-time receipts determined by comparing actual vs. expected arrival dates
    - Status distribution provides operational dashboard insights

    ### Query Parameters
    - **warehouseId**: Optional - Filter metrics by specific warehouse facility
    - **dateStart**: Optional - Start date for metrics analysis period
    - **dateEnd**: Optional - End date for metrics analysis period
    - **vendorId**: Optional - Filter metrics for specific vendor analysis

    ### Metrics Included
    - **Total Orders**: Complete count of orders in analysis period
    - **Completion Rate**: Percentage of orders fully received
    - **Average Receiving Time**: Mean time from start to completion of receiving
    - **On-Time Performance**: Ratio of orders received on schedule
    - **Receiving Accuracy**: Quality metric for receiving precision
    - **Status Distribution**: Breakdown of orders by current status
    - **Vendor Rankings**: Top vendors by performance metrics

    ### Use Cases
    - **Performance Monitoring**: Track receiving efficiency and operational performance
    - **Vendor Management**: Evaluate vendor performance for supplier relationship management
    - **Operational Planning**: Use metrics for capacity planning and resource allocation
    - **Quality Management**: Monitor receiving accuracy and identify improvement opportunities
    - **Executive Reporting**: Generate comprehensive receiving performance reports


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-20T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-27T23:59:59Z.
        vendor_id (Union[Unset, str]):  Example: VND-SWIFT-001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrderReceivingMetricsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
            vendor_id=vendor_id,
        )
    ).parsed
