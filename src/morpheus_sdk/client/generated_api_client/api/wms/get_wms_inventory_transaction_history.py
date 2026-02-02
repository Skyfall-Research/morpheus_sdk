import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_transaction_history_response_200 import GetWMSInventoryTransactionHistoryResponse200
from ...models.get_wms_inventory_transaction_history_transaction_type_item import (
    GetWMSInventoryTransactionHistoryTransactionTypeItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionHistoryTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    params["productId"] = product_id

    params["binId"] = bin_id

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

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inventory-transactions/history",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryTransactionHistoryResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]:
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
    product_id: Union[Unset, str] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionHistoryTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]:
    """Get inventory transaction history


    ## Get WMS Inventory Transaction History

    Retrieve chronological inventory transaction history with comprehensive filtering options for
    operational analysis.

    ### Features
    - **Complete Transaction History**: Chronological view of all inventory transactions
    - **Multi-Dimensional Filtering**: Filter by warehouse, product, bin, transaction type, and date
    range
    - **Operational Analysis**: Support for troubleshooting and audit requirements
    - **Flexible Limiting**: Configurable result limits for performance optimization
    - **Real-Time Data**: Current transaction data for immediate operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **productId**: Optional - Filter transactions for specific product
    - **binId**: Optional - Filter transactions involving specific bin (fromBin OR toBin)
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **limit**: Optional - Maximum number of results (performance control)

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - binId filter uses OR logic for comprehensive bin involvement tracking
    - Date filtering based on transactionDate field
    - Supports multiple transaction type filtering for workflow analysis

    ### Use Cases
    - **Audit Trail**: Complete chronological transaction history
    - **Troubleshooting**: Investigate inventory discrepancies and issues
    - **Performance Analysis**: Analyze transaction patterns and frequencies
    - **Compliance Reporting**: Generate transaction history for regulatory requirements
    - **Operational Review**: Review recent transaction activity for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_id (Union[Unset, str]):  Example: prod_12345.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionHistoryTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        limit (Union[Unset, int]):  Example: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        product_id=product_id,
        bin_id=bin_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
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
    product_id: Union[Unset, str] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionHistoryTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]:
    """Get inventory transaction history


    ## Get WMS Inventory Transaction History

    Retrieve chronological inventory transaction history with comprehensive filtering options for
    operational analysis.

    ### Features
    - **Complete Transaction History**: Chronological view of all inventory transactions
    - **Multi-Dimensional Filtering**: Filter by warehouse, product, bin, transaction type, and date
    range
    - **Operational Analysis**: Support for troubleshooting and audit requirements
    - **Flexible Limiting**: Configurable result limits for performance optimization
    - **Real-Time Data**: Current transaction data for immediate operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **productId**: Optional - Filter transactions for specific product
    - **binId**: Optional - Filter transactions involving specific bin (fromBin OR toBin)
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **limit**: Optional - Maximum number of results (performance control)

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - binId filter uses OR logic for comprehensive bin involvement tracking
    - Date filtering based on transactionDate field
    - Supports multiple transaction type filtering for workflow analysis

    ### Use Cases
    - **Audit Trail**: Complete chronological transaction history
    - **Troubleshooting**: Investigate inventory discrepancies and issues
    - **Performance Analysis**: Analyze transaction patterns and frequencies
    - **Compliance Reporting**: Generate transaction history for regulatory requirements
    - **Operational Review**: Review recent transaction activity for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_id (Union[Unset, str]):  Example: prod_12345.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionHistoryTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        limit (Union[Unset, int]):  Example: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        product_id=product_id,
        bin_id=bin_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionHistoryTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]:
    """Get inventory transaction history


    ## Get WMS Inventory Transaction History

    Retrieve chronological inventory transaction history with comprehensive filtering options for
    operational analysis.

    ### Features
    - **Complete Transaction History**: Chronological view of all inventory transactions
    - **Multi-Dimensional Filtering**: Filter by warehouse, product, bin, transaction type, and date
    range
    - **Operational Analysis**: Support for troubleshooting and audit requirements
    - **Flexible Limiting**: Configurable result limits for performance optimization
    - **Real-Time Data**: Current transaction data for immediate operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **productId**: Optional - Filter transactions for specific product
    - **binId**: Optional - Filter transactions involving specific bin (fromBin OR toBin)
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **limit**: Optional - Maximum number of results (performance control)

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - binId filter uses OR logic for comprehensive bin involvement tracking
    - Date filtering based on transactionDate field
    - Supports multiple transaction type filtering for workflow analysis

    ### Use Cases
    - **Audit Trail**: Complete chronological transaction history
    - **Troubleshooting**: Investigate inventory discrepancies and issues
    - **Performance Analysis**: Analyze transaction patterns and frequencies
    - **Compliance Reporting**: Generate transaction history for regulatory requirements
    - **Operational Review**: Review recent transaction activity for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_id (Union[Unset, str]):  Example: prod_12345.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionHistoryTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        limit (Union[Unset, int]):  Example: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        product_id=product_id,
        bin_id=bin_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionHistoryTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]]:
    """Get inventory transaction history


    ## Get WMS Inventory Transaction History

    Retrieve chronological inventory transaction history with comprehensive filtering options for
    operational analysis.

    ### Features
    - **Complete Transaction History**: Chronological view of all inventory transactions
    - **Multi-Dimensional Filtering**: Filter by warehouse, product, bin, transaction type, and date
    range
    - **Operational Analysis**: Support for troubleshooting and audit requirements
    - **Flexible Limiting**: Configurable result limits for performance optimization
    - **Real-Time Data**: Current transaction data for immediate operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **productId**: Optional - Filter transactions for specific product
    - **binId**: Optional - Filter transactions involving specific bin (fromBin OR toBin)
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **limit**: Optional - Maximum number of results (performance control)

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - binId filter uses OR logic for comprehensive bin involvement tracking
    - Date filtering based on transactionDate field
    - Supports multiple transaction type filtering for workflow analysis

    ### Use Cases
    - **Audit Trail**: Complete chronological transaction history
    - **Troubleshooting**: Investigate inventory discrepancies and issues
    - **Performance Analysis**: Analyze transaction patterns and frequencies
    - **Compliance Reporting**: Generate transaction history for regulatory requirements
    - **Operational Review**: Review recent transaction activity for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        product_id (Union[Unset, str]):  Example: prod_12345.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionHistoryTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        limit (Union[Unset, int]):  Example: 1000.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionHistoryResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            product_id=product_id,
            bin_id=bin_id,
            transaction_type=transaction_type,
            date_start=date_start,
            date_end=date_end,
            limit=limit,
        )
    ).parsed
