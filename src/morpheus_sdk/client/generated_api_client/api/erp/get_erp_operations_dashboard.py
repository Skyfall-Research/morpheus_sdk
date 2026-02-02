from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_operations_dashboard_response_200 import GetERPOperationsDashboardResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/operations-dashboard",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPOperationsDashboardResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]:
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
) -> Response[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]:
    """Get ERP operations dashboard metrics


    Retrieve aggregated metrics for the ERP Command Center dashboard.

    **Core Features**:
    - **Order Metrics**: Purchase orders and sales orders statistics by status, value, and recent
    activity
    - **Invoice Metrics**: Total invoices, outstanding balance, overdue counts, and monthly paid
    - **Company Metrics**: Customer and supplier counts by type and status
    - **Product Metrics**: Active and discontinued product counts

    **Use Cases**:
    - **Executive Dashboard**: High-level KPIs for operations monitoring
    - **Performance Tracking**: Real-time visibility into order and invoice processing
    - **Business Intelligence**: Aggregated data for reporting and analytics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]:
    """Get ERP operations dashboard metrics


    Retrieve aggregated metrics for the ERP Command Center dashboard.

    **Core Features**:
    - **Order Metrics**: Purchase orders and sales orders statistics by status, value, and recent
    activity
    - **Invoice Metrics**: Total invoices, outstanding balance, overdue counts, and monthly paid
    - **Company Metrics**: Customer and supplier counts by type and status
    - **Product Metrics**: Active and discontinued product counts

    **Use Cases**:
    - **Executive Dashboard**: High-level KPIs for operations monitoring
    - **Performance Tracking**: Real-time visibility into order and invoice processing
    - **Business Intelligence**: Aggregated data for reporting and analytics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPOperationsDashboardResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]:
    """Get ERP operations dashboard metrics


    Retrieve aggregated metrics for the ERP Command Center dashboard.

    **Core Features**:
    - **Order Metrics**: Purchase orders and sales orders statistics by status, value, and recent
    activity
    - **Invoice Metrics**: Total invoices, outstanding balance, overdue counts, and monthly paid
    - **Company Metrics**: Customer and supplier counts by type and status
    - **Product Metrics**: Active and discontinued product counts

    **Use Cases**:
    - **Executive Dashboard**: High-level KPIs for operations monitoring
    - **Performance Tracking**: Real-time visibility into order and invoice processing
    - **Business Intelligence**: Aggregated data for reporting and analytics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPOperationsDashboardResponse200]]:
    """Get ERP operations dashboard metrics


    Retrieve aggregated metrics for the ERP Command Center dashboard.

    **Core Features**:
    - **Order Metrics**: Purchase orders and sales orders statistics by status, value, and recent
    activity
    - **Invoice Metrics**: Total invoices, outstanding balance, overdue counts, and monthly paid
    - **Company Metrics**: Customer and supplier counts by type and status
    - **Product Metrics**: Active and discontinued product counts

    **Use Cases**:
    - **Executive Dashboard**: High-level KPIs for operations monitoring
    - **Performance Tracking**: Real-time visibility into order and invoice processing
    - **Business Intelligence**: Aggregated data for reporting and analytics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPOperationsDashboardResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
