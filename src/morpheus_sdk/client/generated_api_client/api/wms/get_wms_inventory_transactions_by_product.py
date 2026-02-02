import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_transactions_by_product_response_200 import (
    GetWMSInventoryTransactionsByProductResponse200,
)
from ...models.get_wms_inventory_transactions_by_product_transaction_type_item import (
    GetWMSInventoryTransactionsByProductTransactionTypeItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    product_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByProductTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

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

    params["binId"] = bin_id

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inventory-transactions/product/{product_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryTransactionsByProductResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByProductTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]:
    """Get inventory transactions by product


    ## Get WMS Inventory Transactions by Product

    Retrieve paginated inventory transactions for a specific product with comprehensive filtering
    capabilities.

    ### Features
    - **Product-Specific Filtering**: All transactions for a specific product across warehouses
    - **Advanced Filtering**: Filter by warehouse, transaction type, date range, and bin location
    - **Cursor-Based Pagination**: Efficient pagination for large transaction sets
    - **Multi-Transaction Type**: Support for filtering by multiple transaction types
    - **Bin Movement Tracking**: Filter by specific bin involvement (fromBin or toBin)

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **binId**: Optional - Filter transactions involving specific bin (fromBinId OR toBinId)
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - Cursor-based pagination ensures consistency during concurrent operations
    - binId filter uses OR logic (fromBinId OR toBinId) to capture all bin involvement
    - Date filtering uses transactionDate field for temporal analysis

    ### Use Cases
    - **Product Movement Analysis**: Track all movements for specific products
    - **Inventory Audit**: Review complete transaction history for products
    - **Performance Analysis**: Analyze transaction patterns by product
    - **Compliance Reporting**: Generate product-specific transaction reports
    - **Troubleshooting**: Investigate inventory discrepancies for products


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: prod_12345.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByProductTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        product_id=product_id,
        warehouse_id=warehouse_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        bin_id=bin_id,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByProductTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]:
    """Get inventory transactions by product


    ## Get WMS Inventory Transactions by Product

    Retrieve paginated inventory transactions for a specific product with comprehensive filtering
    capabilities.

    ### Features
    - **Product-Specific Filtering**: All transactions for a specific product across warehouses
    - **Advanced Filtering**: Filter by warehouse, transaction type, date range, and bin location
    - **Cursor-Based Pagination**: Efficient pagination for large transaction sets
    - **Multi-Transaction Type**: Support for filtering by multiple transaction types
    - **Bin Movement Tracking**: Filter by specific bin involvement (fromBin or toBin)

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **binId**: Optional - Filter transactions involving specific bin (fromBinId OR toBinId)
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - Cursor-based pagination ensures consistency during concurrent operations
    - binId filter uses OR logic (fromBinId OR toBinId) to capture all bin involvement
    - Date filtering uses transactionDate field for temporal analysis

    ### Use Cases
    - **Product Movement Analysis**: Track all movements for specific products
    - **Inventory Audit**: Review complete transaction history for products
    - **Performance Analysis**: Analyze transaction patterns by product
    - **Compliance Reporting**: Generate product-specific transaction reports
    - **Troubleshooting**: Investigate inventory discrepancies for products


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: prod_12345.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByProductTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        product_id=product_id,
        client=client,
        warehouse_id=warehouse_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        bin_id=bin_id,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByProductTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]:
    """Get inventory transactions by product


    ## Get WMS Inventory Transactions by Product

    Retrieve paginated inventory transactions for a specific product with comprehensive filtering
    capabilities.

    ### Features
    - **Product-Specific Filtering**: All transactions for a specific product across warehouses
    - **Advanced Filtering**: Filter by warehouse, transaction type, date range, and bin location
    - **Cursor-Based Pagination**: Efficient pagination for large transaction sets
    - **Multi-Transaction Type**: Support for filtering by multiple transaction types
    - **Bin Movement Tracking**: Filter by specific bin involvement (fromBin or toBin)

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **binId**: Optional - Filter transactions involving specific bin (fromBinId OR toBinId)
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - Cursor-based pagination ensures consistency during concurrent operations
    - binId filter uses OR logic (fromBinId OR toBinId) to capture all bin involvement
    - Date filtering uses transactionDate field for temporal analysis

    ### Use Cases
    - **Product Movement Analysis**: Track all movements for specific products
    - **Inventory Audit**: Review complete transaction history for products
    - **Performance Analysis**: Analyze transaction patterns by product
    - **Compliance Reporting**: Generate product-specific transaction reports
    - **Troubleshooting**: Investigate inventory discrepancies for products


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: prod_12345.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByProductTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        product_id=product_id,
        warehouse_id=warehouse_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        bin_id=bin_id,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByProductTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    bin_id: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]]:
    """Get inventory transactions by product


    ## Get WMS Inventory Transactions by Product

    Retrieve paginated inventory transactions for a specific product with comprehensive filtering
    capabilities.

    ### Features
    - **Product-Specific Filtering**: All transactions for a specific product across warehouses
    - **Advanced Filtering**: Filter by warehouse, transaction type, date range, and bin location
    - **Cursor-Based Pagination**: Efficient pagination for large transaction sets
    - **Multi-Transaction Type**: Support for filtering by multiple transaction types
    - **Bin Movement Tracking**: Filter by specific bin involvement (fromBin or toBin)

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **binId**: Optional - Filter transactions involving specific bin (fromBinId OR toBinId)
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page

    ### Business Logic
    - Results ordered by transaction date (newest first)
    - Cursor-based pagination ensures consistency during concurrent operations
    - binId filter uses OR logic (fromBinId OR toBinId) to capture all bin involvement
    - Date filtering uses transactionDate field for temporal analysis

    ### Use Cases
    - **Product Movement Analysis**: Track all movements for specific products
    - **Inventory Audit**: Review complete transaction history for products
    - **Performance Analysis**: Analyze transaction patterns by product
    - **Compliance Reporting**: Generate product-specific transaction reports
    - **Troubleshooting**: Investigate inventory discrepancies for products


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: prod_12345.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByProductTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        bin_id (Union[Unset, str]):  Example: BIN-A-01-01.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionsByProductResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            product_id=product_id,
            client=client,
            warehouse_id=warehouse_id,
            transaction_type=transaction_type,
            date_start=date_start,
            date_end=date_end,
            bin_id=bin_id,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
