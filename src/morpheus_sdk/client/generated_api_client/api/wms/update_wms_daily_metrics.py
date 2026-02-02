from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_daily_metrics_body import UpdateWMSDailyMetricsBody
from ...models.update_wms_daily_metrics_response_200 import UpdateWMSDailyMetricsResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    metrics_id: str,
    *,
    body: UpdateWMSDailyMetricsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/daily-metrics/{metrics_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSDailyMetricsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    metrics_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDailyMetricsBody,
) -> Response[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]:
    """Update daily metrics record


    ## Update WMS Daily Metrics

    Update an existing daily metrics record with new or corrected data to maintain accurate operational
    performance tracking.

    ### Features
    - **Partial Updates**: Support partial field updates without affecting other data
    - **Data Correction**: Enable correction of recorded metrics data
    - **Real-time Updates**: Update metrics as operations progress throughout the day
    - **Flexible Modification**: Update any combination of metric categories
    - **Audit Trail**: Maintain update history through audit plugin
    - **Validation**: Ensure data integrity during update operations

    ### Update Categories
    - **Inbound Metrics**: Update receiving and inbound processing data
    - **Putaway Metrics**: Modify putaway operation performance data
    - **Picking Metrics**: Update picking operation metrics and accuracy
    - **Packing Metrics**: Modify packing operation performance data
    - **Shipping Metrics**: Update shipping and dispatch metrics
    - **Labor Metrics**: Modify workforce and labor utilization data
    - **Inventory Metrics**: Update inventory levels and turnover data
    - **Quality Metrics**: Modify error rates and quality tracking data

    ### Business Rules
    - metricsId must reference an existing metrics record
    - Only provided fields are updated (partial update support)
    - Core identifiers (warehouseId, date, metricId) cannot be modified
    - Custom fields support flexible warehouse-specific updates
    - Audit trail automatically tracks all modifications


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.
        body (UpdateWMSDailyMetricsBody): Partial metrics data for updating specific fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        metrics_id=metrics_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    metrics_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDailyMetricsBody,
) -> Optional[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]:
    """Update daily metrics record


    ## Update WMS Daily Metrics

    Update an existing daily metrics record with new or corrected data to maintain accurate operational
    performance tracking.

    ### Features
    - **Partial Updates**: Support partial field updates without affecting other data
    - **Data Correction**: Enable correction of recorded metrics data
    - **Real-time Updates**: Update metrics as operations progress throughout the day
    - **Flexible Modification**: Update any combination of metric categories
    - **Audit Trail**: Maintain update history through audit plugin
    - **Validation**: Ensure data integrity during update operations

    ### Update Categories
    - **Inbound Metrics**: Update receiving and inbound processing data
    - **Putaway Metrics**: Modify putaway operation performance data
    - **Picking Metrics**: Update picking operation metrics and accuracy
    - **Packing Metrics**: Modify packing operation performance data
    - **Shipping Metrics**: Update shipping and dispatch metrics
    - **Labor Metrics**: Modify workforce and labor utilization data
    - **Inventory Metrics**: Update inventory levels and turnover data
    - **Quality Metrics**: Modify error rates and quality tracking data

    ### Business Rules
    - metricsId must reference an existing metrics record
    - Only provided fields are updated (partial update support)
    - Core identifiers (warehouseId, date, metricId) cannot be modified
    - Custom fields support flexible warehouse-specific updates
    - Audit trail automatically tracks all modifications


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.
        body (UpdateWMSDailyMetricsBody): Partial metrics data for updating specific fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        metrics_id=metrics_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    metrics_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDailyMetricsBody,
) -> Response[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]:
    """Update daily metrics record


    ## Update WMS Daily Metrics

    Update an existing daily metrics record with new or corrected data to maintain accurate operational
    performance tracking.

    ### Features
    - **Partial Updates**: Support partial field updates without affecting other data
    - **Data Correction**: Enable correction of recorded metrics data
    - **Real-time Updates**: Update metrics as operations progress throughout the day
    - **Flexible Modification**: Update any combination of metric categories
    - **Audit Trail**: Maintain update history through audit plugin
    - **Validation**: Ensure data integrity during update operations

    ### Update Categories
    - **Inbound Metrics**: Update receiving and inbound processing data
    - **Putaway Metrics**: Modify putaway operation performance data
    - **Picking Metrics**: Update picking operation metrics and accuracy
    - **Packing Metrics**: Modify packing operation performance data
    - **Shipping Metrics**: Update shipping and dispatch metrics
    - **Labor Metrics**: Modify workforce and labor utilization data
    - **Inventory Metrics**: Update inventory levels and turnover data
    - **Quality Metrics**: Modify error rates and quality tracking data

    ### Business Rules
    - metricsId must reference an existing metrics record
    - Only provided fields are updated (partial update support)
    - Core identifiers (warehouseId, date, metricId) cannot be modified
    - Custom fields support flexible warehouse-specific updates
    - Audit trail automatically tracks all modifications


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.
        body (UpdateWMSDailyMetricsBody): Partial metrics data for updating specific fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        metrics_id=metrics_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    metrics_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSDailyMetricsBody,
) -> Optional[Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]]:
    """Update daily metrics record


    ## Update WMS Daily Metrics

    Update an existing daily metrics record with new or corrected data to maintain accurate operational
    performance tracking.

    ### Features
    - **Partial Updates**: Support partial field updates without affecting other data
    - **Data Correction**: Enable correction of recorded metrics data
    - **Real-time Updates**: Update metrics as operations progress throughout the day
    - **Flexible Modification**: Update any combination of metric categories
    - **Audit Trail**: Maintain update history through audit plugin
    - **Validation**: Ensure data integrity during update operations

    ### Update Categories
    - **Inbound Metrics**: Update receiving and inbound processing data
    - **Putaway Metrics**: Modify putaway operation performance data
    - **Picking Metrics**: Update picking operation metrics and accuracy
    - **Packing Metrics**: Modify packing operation performance data
    - **Shipping Metrics**: Update shipping and dispatch metrics
    - **Labor Metrics**: Modify workforce and labor utilization data
    - **Inventory Metrics**: Update inventory levels and turnover data
    - **Quality Metrics**: Modify error rates and quality tracking data

    ### Business Rules
    - metricsId must reference an existing metrics record
    - Only provided fields are updated (partial update support)
    - Core identifiers (warehouseId, date, metricId) cannot be modified
    - Custom fields support flexible warehouse-specific updates
    - Audit trail automatically tracks all modifications


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.
        body (UpdateWMSDailyMetricsBody): Partial metrics data for updating specific fields

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSDailyMetricsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            metrics_id=metrics_id,
            client=client,
            body=body,
        )
    ).parsed
