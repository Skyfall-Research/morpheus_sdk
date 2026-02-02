from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_daily_metrics_body import CreateWMSDailyMetricsBody
from ...models.create_wms_daily_metrics_response_201 import CreateWMSDailyMetricsResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSDailyMetricsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/daily-metrics",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSDailyMetricsResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]:
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
    body: CreateWMSDailyMetricsBody,
) -> Response[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]:
    """Create new daily metrics record


    ## Create WMS Daily Metrics

    Create a new daily metrics record for comprehensive warehouse performance tracking and operational
    analysis.

    ### Features
    - **Comprehensive Metrics**: Track inbound, putaway, picking, packing, shipping, labor, inventory,
    and quality metrics
    - **Multi-Zone Support**: Record metrics by specific warehouse zones for detailed analysis
    - **Shift-Based Tracking**: Support multiple shifts with independent metrics
    - **Performance Monitoring**: Real-time operational performance measurement
    - **Quality Tracking**: Monitor errors, accuracy, and quality metrics
    - **Labor Analytics**: Track productivity, utilization, and efficiency metrics
    - **Custom Fields**: Support warehouse-specific operational metrics

    ### Metric Categories
    - **Inbound**: Purchase orders received, units processed, receiving rates
    - **Putaway**: Tasks completed, pallets processed, productivity rates
    - **Picking**: Orders fulfilled, pick accuracy, productivity metrics
    - **Packing**: Orders packed, packaging rates, efficiency metrics
    - **Shipping**: Shipments created, carrier dispatch, package volumes
    - **Labor**: Worker counts, hours tracked, utilization percentages
    - **Inventory**: On-hand units, inventory values, turnover rates
    - **Quality**: Error tracking, damage reports, returns processed

    ### Business Rules
    - metricId is auto-generated with unique identifier if not provided
    - warehouseId and date are required for metrics recording
    - Duplicate prevention for same date/warehouse/shift/zone combination
    - All numeric metrics are optional to support partial data collection
    - Custom fields support warehouse-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDailyMetricsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSDailyMetricsBody,
) -> Optional[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]:
    """Create new daily metrics record


    ## Create WMS Daily Metrics

    Create a new daily metrics record for comprehensive warehouse performance tracking and operational
    analysis.

    ### Features
    - **Comprehensive Metrics**: Track inbound, putaway, picking, packing, shipping, labor, inventory,
    and quality metrics
    - **Multi-Zone Support**: Record metrics by specific warehouse zones for detailed analysis
    - **Shift-Based Tracking**: Support multiple shifts with independent metrics
    - **Performance Monitoring**: Real-time operational performance measurement
    - **Quality Tracking**: Monitor errors, accuracy, and quality metrics
    - **Labor Analytics**: Track productivity, utilization, and efficiency metrics
    - **Custom Fields**: Support warehouse-specific operational metrics

    ### Metric Categories
    - **Inbound**: Purchase orders received, units processed, receiving rates
    - **Putaway**: Tasks completed, pallets processed, productivity rates
    - **Picking**: Orders fulfilled, pick accuracy, productivity metrics
    - **Packing**: Orders packed, packaging rates, efficiency metrics
    - **Shipping**: Shipments created, carrier dispatch, package volumes
    - **Labor**: Worker counts, hours tracked, utilization percentages
    - **Inventory**: On-hand units, inventory values, turnover rates
    - **Quality**: Error tracking, damage reports, returns processed

    ### Business Rules
    - metricId is auto-generated with unique identifier if not provided
    - warehouseId and date are required for metrics recording
    - Duplicate prevention for same date/warehouse/shift/zone combination
    - All numeric metrics are optional to support partial data collection
    - Custom fields support warehouse-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDailyMetricsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSDailyMetricsResponse201, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSDailyMetricsBody,
) -> Response[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]:
    """Create new daily metrics record


    ## Create WMS Daily Metrics

    Create a new daily metrics record for comprehensive warehouse performance tracking and operational
    analysis.

    ### Features
    - **Comprehensive Metrics**: Track inbound, putaway, picking, packing, shipping, labor, inventory,
    and quality metrics
    - **Multi-Zone Support**: Record metrics by specific warehouse zones for detailed analysis
    - **Shift-Based Tracking**: Support multiple shifts with independent metrics
    - **Performance Monitoring**: Real-time operational performance measurement
    - **Quality Tracking**: Monitor errors, accuracy, and quality metrics
    - **Labor Analytics**: Track productivity, utilization, and efficiency metrics
    - **Custom Fields**: Support warehouse-specific operational metrics

    ### Metric Categories
    - **Inbound**: Purchase orders received, units processed, receiving rates
    - **Putaway**: Tasks completed, pallets processed, productivity rates
    - **Picking**: Orders fulfilled, pick accuracy, productivity metrics
    - **Packing**: Orders packed, packaging rates, efficiency metrics
    - **Shipping**: Shipments created, carrier dispatch, package volumes
    - **Labor**: Worker counts, hours tracked, utilization percentages
    - **Inventory**: On-hand units, inventory values, turnover rates
    - **Quality**: Error tracking, damage reports, returns processed

    ### Business Rules
    - metricId is auto-generated with unique identifier if not provided
    - warehouseId and date are required for metrics recording
    - Duplicate prevention for same date/warehouse/shift/zone combination
    - All numeric metrics are optional to support partial data collection
    - Custom fields support warehouse-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDailyMetricsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWMSDailyMetricsBody,
) -> Optional[Union[CreateWMSDailyMetricsResponse201, ErrorResponse]]:
    """Create new daily metrics record


    ## Create WMS Daily Metrics

    Create a new daily metrics record for comprehensive warehouse performance tracking and operational
    analysis.

    ### Features
    - **Comprehensive Metrics**: Track inbound, putaway, picking, packing, shipping, labor, inventory,
    and quality metrics
    - **Multi-Zone Support**: Record metrics by specific warehouse zones for detailed analysis
    - **Shift-Based Tracking**: Support multiple shifts with independent metrics
    - **Performance Monitoring**: Real-time operational performance measurement
    - **Quality Tracking**: Monitor errors, accuracy, and quality metrics
    - **Labor Analytics**: Track productivity, utilization, and efficiency metrics
    - **Custom Fields**: Support warehouse-specific operational metrics

    ### Metric Categories
    - **Inbound**: Purchase orders received, units processed, receiving rates
    - **Putaway**: Tasks completed, pallets processed, productivity rates
    - **Picking**: Orders fulfilled, pick accuracy, productivity metrics
    - **Packing**: Orders packed, packaging rates, efficiency metrics
    - **Shipping**: Shipments created, carrier dispatch, package volumes
    - **Labor**: Worker counts, hours tracked, utilization percentages
    - **Inventory**: On-hand units, inventory values, turnover rates
    - **Quality**: Error tracking, damage reports, returns processed

    ### Business Rules
    - metricId is auto-generated with unique identifier if not provided
    - warehouseId and date are required for metrics recording
    - Duplicate prevention for same date/warehouse/shift/zone combination
    - All numeric metrics are optional to support partial data collection
    - Custom fields support warehouse-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDailyMetricsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSDailyMetricsResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
