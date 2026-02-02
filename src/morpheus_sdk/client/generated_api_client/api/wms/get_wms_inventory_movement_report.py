import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_movement_report_response_200 import GetWMSInventoryMovementReportResponse200
from ...models.get_wms_inventory_movement_report_transaction_type_item import (
    GetWMSInventoryMovementReportTransactionTypeItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    product_ids: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_product_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(product_ids, Unset):
        json_product_ids = product_ids

    params["productIds"] = json_product_ids

    json_transaction_type: Union[Unset, list[str]] = UNSET
    if not isinstance(transaction_type, Unset):
        json_transaction_type = []
        for transaction_type_item_data in transaction_type:
            transaction_type_item = transaction_type_item_data.value
            json_transaction_type.append(transaction_type_item)

    params["transactionType"] = json_transaction_type

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
        "url": f"/{world_id}/wms/inventory-transactions/movement-report",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryMovementReportResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]:
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
    product_ids: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]:
    """Get inventory movement report


    ## Get WMS Inventory Movement Report

    Generate comprehensive inventory movement analytics with transaction summaries, top moving products,
    and temporal trends.

    ### Features
    - **Movement Analytics**: Total transactions and quantity summaries by type
    - **Product Performance**: Identify top moving products with transaction volumes
    - **Temporal Trends**: Daily movement patterns and transaction distribution
    - **Multi-Dimensional Filtering**: Filter by warehouse, products, transaction types, and date range
    - **Executive Reporting**: High-level inventory movement insights for management

    ### Report Data Includes
    - **Transaction Summary**: Total transaction counts by type with quantity totals
    - **Top Moving Products**: Products with highest transaction volumes and quantities
    - **Daily Trends**: Day-by-day transaction counts and movement quantities
    - **Movement Patterns**: Identify peak activity periods and seasonal trends

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **productIds**: Optional - Focus report on specific products (supports arrays)
    - **transactionType**: Optional - Filter by specific transaction types
    - **dateStart/dateEnd**: Optional - Time range for movement analysis

    ### Business Logic
    - Aggregates transaction data across all selected criteria
    - Groups results by transaction type, product, and date
    - Calculates movement volumes and transaction frequencies
    - Orders results by transaction volume and activity levels

    ### Use Cases
    - **Executive Dashboard**: High-level inventory movement insights
    - **Operational Planning**: Understand movement patterns for resource allocation
    - **Product Analysis**: Identify fast/slow moving products
    - **Performance Monitoring**: Track warehouse productivity and efficiency
    - **Trend Analysis**: Identify seasonal patterns and growth trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_ids (Union[Unset, list[str]]):
        transaction_type (Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        product_ids=product_ids,
        transaction_type=transaction_type,
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
    product_ids: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]:
    """Get inventory movement report


    ## Get WMS Inventory Movement Report

    Generate comprehensive inventory movement analytics with transaction summaries, top moving products,
    and temporal trends.

    ### Features
    - **Movement Analytics**: Total transactions and quantity summaries by type
    - **Product Performance**: Identify top moving products with transaction volumes
    - **Temporal Trends**: Daily movement patterns and transaction distribution
    - **Multi-Dimensional Filtering**: Filter by warehouse, products, transaction types, and date range
    - **Executive Reporting**: High-level inventory movement insights for management

    ### Report Data Includes
    - **Transaction Summary**: Total transaction counts by type with quantity totals
    - **Top Moving Products**: Products with highest transaction volumes and quantities
    - **Daily Trends**: Day-by-day transaction counts and movement quantities
    - **Movement Patterns**: Identify peak activity periods and seasonal trends

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **productIds**: Optional - Focus report on specific products (supports arrays)
    - **transactionType**: Optional - Filter by specific transaction types
    - **dateStart/dateEnd**: Optional - Time range for movement analysis

    ### Business Logic
    - Aggregates transaction data across all selected criteria
    - Groups results by transaction type, product, and date
    - Calculates movement volumes and transaction frequencies
    - Orders results by transaction volume and activity levels

    ### Use Cases
    - **Executive Dashboard**: High-level inventory movement insights
    - **Operational Planning**: Understand movement patterns for resource allocation
    - **Product Analysis**: Identify fast/slow moving products
    - **Performance Monitoring**: Track warehouse productivity and efficiency
    - **Trend Analysis**: Identify seasonal patterns and growth trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_ids (Union[Unset, list[str]]):
        transaction_type (Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        product_ids=product_ids,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    product_ids: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]:
    """Get inventory movement report


    ## Get WMS Inventory Movement Report

    Generate comprehensive inventory movement analytics with transaction summaries, top moving products,
    and temporal trends.

    ### Features
    - **Movement Analytics**: Total transactions and quantity summaries by type
    - **Product Performance**: Identify top moving products with transaction volumes
    - **Temporal Trends**: Daily movement patterns and transaction distribution
    - **Multi-Dimensional Filtering**: Filter by warehouse, products, transaction types, and date range
    - **Executive Reporting**: High-level inventory movement insights for management

    ### Report Data Includes
    - **Transaction Summary**: Total transaction counts by type with quantity totals
    - **Top Moving Products**: Products with highest transaction volumes and quantities
    - **Daily Trends**: Day-by-day transaction counts and movement quantities
    - **Movement Patterns**: Identify peak activity periods and seasonal trends

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **productIds**: Optional - Focus report on specific products (supports arrays)
    - **transactionType**: Optional - Filter by specific transaction types
    - **dateStart/dateEnd**: Optional - Time range for movement analysis

    ### Business Logic
    - Aggregates transaction data across all selected criteria
    - Groups results by transaction type, product, and date
    - Calculates movement volumes and transaction frequencies
    - Orders results by transaction volume and activity levels

    ### Use Cases
    - **Executive Dashboard**: High-level inventory movement insights
    - **Operational Planning**: Understand movement patterns for resource allocation
    - **Product Analysis**: Identify fast/slow moving products
    - **Performance Monitoring**: Track warehouse productivity and efficiency
    - **Trend Analysis**: Identify seasonal patterns and growth trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_ids (Union[Unset, list[str]]):
        transaction_type (Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        product_ids=product_ids,
        transaction_type=transaction_type,
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
    product_ids: Union[Unset, list[str]] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]]:
    """Get inventory movement report


    ## Get WMS Inventory Movement Report

    Generate comprehensive inventory movement analytics with transaction summaries, top moving products,
    and temporal trends.

    ### Features
    - **Movement Analytics**: Total transactions and quantity summaries by type
    - **Product Performance**: Identify top moving products with transaction volumes
    - **Temporal Trends**: Daily movement patterns and transaction distribution
    - **Multi-Dimensional Filtering**: Filter by warehouse, products, transaction types, and date range
    - **Executive Reporting**: High-level inventory movement insights for management

    ### Report Data Includes
    - **Transaction Summary**: Total transaction counts by type with quantity totals
    - **Top Moving Products**: Products with highest transaction volumes and quantities
    - **Daily Trends**: Day-by-day transaction counts and movement quantities
    - **Movement Patterns**: Identify peak activity periods and seasonal trends

    ### Query Parameters
    - **warehouseId**: Optional - Scope report to specific warehouse
    - **productIds**: Optional - Focus report on specific products (supports arrays)
    - **transactionType**: Optional - Filter by specific transaction types
    - **dateStart/dateEnd**: Optional - Time range for movement analysis

    ### Business Logic
    - Aggregates transaction data across all selected criteria
    - Groups results by transaction type, product, and date
    - Calculates movement volumes and transaction frequencies
    - Orders results by transaction volume and activity levels

    ### Use Cases
    - **Executive Dashboard**: High-level inventory movement insights
    - **Operational Planning**: Understand movement patterns for resource allocation
    - **Product Analysis**: Identify fast/slow moving products
    - **Performance Monitoring**: Track warehouse productivity and efficiency
    - **Trend Analysis**: Identify seasonal patterns and growth trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_ids (Union[Unset, list[str]]):
        transaction_type (Union[Unset, list[GetWMSInventoryMovementReportTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryMovementReportResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            product_ids=product_ids,
            transaction_type=transaction_type,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
