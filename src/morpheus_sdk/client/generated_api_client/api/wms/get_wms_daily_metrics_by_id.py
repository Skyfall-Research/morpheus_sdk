from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_daily_metrics_by_id_response_200 import GetWMSDailyMetricsByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    metrics_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/daily-metrics/{metrics_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDailyMetricsByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]:
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
) -> Response[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]:
    """Get daily metrics by ID


    ## Get WMS Daily Metrics by ID

    Retrieve a specific daily metrics record using its unique identifier for detailed analysis and data
    access.

    ### Features
    - **Direct Access**: Retrieve metrics using unique metric identifier
    - **Complete Data**: Full metrics record with all operational categories
    - **Single Record Focus**: Detailed view of specific day's performance
    - **Cross-Reference Support**: Support for metric ID-based references
    - **Audit Trail Support**: Enable audit trail and historical reference tracking

    ### Path Parameters
    - **metricsId**: Required - Unique identifier for the specific metrics record

    ### Business Logic
    - metricsId must be a valid, existing metrics record identifier
    - Returns complete metrics record with all categories and fields
    - Includes metadata like creation and update timestamps
    - Null response if metrics record is not found
    - Full data structure for comprehensive analysis

    ### Use Cases
    - **Detailed Analysis**: Deep dive into specific day's performance
    - **Data Verification**: Verify specific metrics data for accuracy
    - **Cross-Reference**: Reference specific metrics from other systems
    - **Historical Review**: Review historical performance data
    - **Audit Support**: Support audit trail and compliance requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        metrics_id=metrics_id,
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
) -> Optional[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]:
    """Get daily metrics by ID


    ## Get WMS Daily Metrics by ID

    Retrieve a specific daily metrics record using its unique identifier for detailed analysis and data
    access.

    ### Features
    - **Direct Access**: Retrieve metrics using unique metric identifier
    - **Complete Data**: Full metrics record with all operational categories
    - **Single Record Focus**: Detailed view of specific day's performance
    - **Cross-Reference Support**: Support for metric ID-based references
    - **Audit Trail Support**: Enable audit trail and historical reference tracking

    ### Path Parameters
    - **metricsId**: Required - Unique identifier for the specific metrics record

    ### Business Logic
    - metricsId must be a valid, existing metrics record identifier
    - Returns complete metrics record with all categories and fields
    - Includes metadata like creation and update timestamps
    - Null response if metrics record is not found
    - Full data structure for comprehensive analysis

    ### Use Cases
    - **Detailed Analysis**: Deep dive into specific day's performance
    - **Data Verification**: Verify specific metrics data for accuracy
    - **Cross-Reference**: Reference specific metrics from other systems
    - **Historical Review**: Review historical performance data
    - **Audit Support**: Support audit trail and compliance requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        metrics_id=metrics_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    metrics_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]:
    """Get daily metrics by ID


    ## Get WMS Daily Metrics by ID

    Retrieve a specific daily metrics record using its unique identifier for detailed analysis and data
    access.

    ### Features
    - **Direct Access**: Retrieve metrics using unique metric identifier
    - **Complete Data**: Full metrics record with all operational categories
    - **Single Record Focus**: Detailed view of specific day's performance
    - **Cross-Reference Support**: Support for metric ID-based references
    - **Audit Trail Support**: Enable audit trail and historical reference tracking

    ### Path Parameters
    - **metricsId**: Required - Unique identifier for the specific metrics record

    ### Business Logic
    - metricsId must be a valid, existing metrics record identifier
    - Returns complete metrics record with all categories and fields
    - Includes metadata like creation and update timestamps
    - Null response if metrics record is not found
    - Full data structure for comprehensive analysis

    ### Use Cases
    - **Detailed Analysis**: Deep dive into specific day's performance
    - **Data Verification**: Verify specific metrics data for accuracy
    - **Cross-Reference**: Reference specific metrics from other systems
    - **Historical Review**: Review historical performance data
    - **Audit Support**: Support audit trail and compliance requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        metrics_id=metrics_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    metrics_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]]:
    """Get daily metrics by ID


    ## Get WMS Daily Metrics by ID

    Retrieve a specific daily metrics record using its unique identifier for detailed analysis and data
    access.

    ### Features
    - **Direct Access**: Retrieve metrics using unique metric identifier
    - **Complete Data**: Full metrics record with all operational categories
    - **Single Record Focus**: Detailed view of specific day's performance
    - **Cross-Reference Support**: Support for metric ID-based references
    - **Audit Trail Support**: Enable audit trail and historical reference tracking

    ### Path Parameters
    - **metricsId**: Required - Unique identifier for the specific metrics record

    ### Business Logic
    - metricsId must be a valid, existing metrics record identifier
    - Returns complete metrics record with all categories and fields
    - Includes metadata like creation and update timestamps
    - Null response if metrics record is not found
    - Full data structure for comprehensive analysis

    ### Use Cases
    - **Detailed Analysis**: Deep dive into specific day's performance
    - **Data Verification**: Verify specific metrics data for accuracy
    - **Cross-Reference**: Reference specific metrics from other systems
    - **Historical Review**: Review historical performance data
    - **Audit Support**: Support audit trail and compliance requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        metrics_id (str):  Example: wms_daily-metrics_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDailyMetricsByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            metrics_id=metrics_id,
            client=client,
        )
    ).parsed
