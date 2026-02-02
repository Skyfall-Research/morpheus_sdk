import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inventory_transactions_by_bin_response_200 import GetWMSInventoryTransactionsByBinResponse200
from ...models.get_wms_inventory_transactions_by_bin_transaction_type_item import (
    GetWMSInventoryTransactionsByBinTransactionTypeItem,
)
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    bin_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByBinTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    product_id: Union[Unset, str] = UNSET,
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

    params["productId"] = product_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inventory-transactions/bin/{bin_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInventoryTransactionsByBinResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByBinTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    product_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]:
    """Get inventory transactions by bin


    ## Get WMS Inventory Transactions by Bin

    Retrieve all inventory transactions involving a specific bin location, including both inbound and
    outbound movements.

    ### Features
    - **Bin-Centric View**: All transactions where bin is source (fromBinId) or destination (toBinId)
    - **Comprehensive Filtering**: Filter by warehouse, transaction type, date range, and product
    - **Movement Direction Tracking**: See both incoming and outgoing transactions for the bin
    - **Real-Time Analysis**: Current transaction data for operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **productId**: Optional - Filter transactions for specific product

    ### Business Logic
    - Uses OR query logic: (fromBinId = binId OR toBinId = binId)
    - Results ordered by transaction date (newest first)
    - Includes all transaction types that involve the specified bin
    - Date filtering based on transactionDate for temporal analysis

    ### Use Cases
    - **Bin Activity Analysis**: Review all activity for specific storage location
    - **Location Utilization**: Understand bin usage patterns and frequency
    - **Inventory Tracking**: Track product flow through specific locations
    - **Operational Planning**: Optimize bin assignments based on activity
    - **Compliance Audit**: Review all movements involving specific locations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN-A-01-01.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByBinTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        product_id (Union[Unset, str]):  Example: prod_12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        warehouse_id=warehouse_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByBinTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    product_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]:
    """Get inventory transactions by bin


    ## Get WMS Inventory Transactions by Bin

    Retrieve all inventory transactions involving a specific bin location, including both inbound and
    outbound movements.

    ### Features
    - **Bin-Centric View**: All transactions where bin is source (fromBinId) or destination (toBinId)
    - **Comprehensive Filtering**: Filter by warehouse, transaction type, date range, and product
    - **Movement Direction Tracking**: See both incoming and outgoing transactions for the bin
    - **Real-Time Analysis**: Current transaction data for operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **productId**: Optional - Filter transactions for specific product

    ### Business Logic
    - Uses OR query logic: (fromBinId = binId OR toBinId = binId)
    - Results ordered by transaction date (newest first)
    - Includes all transaction types that involve the specified bin
    - Date filtering based on transactionDate for temporal analysis

    ### Use Cases
    - **Bin Activity Analysis**: Review all activity for specific storage location
    - **Location Utilization**: Understand bin usage patterns and frequency
    - **Inventory Tracking**: Track product flow through specific locations
    - **Operational Planning**: Optimize bin assignments based on activity
    - **Compliance Audit**: Review all movements involving specific locations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN-A-01-01.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByBinTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        product_id (Union[Unset, str]):  Example: prod_12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        bin_id=bin_id,
        client=client,
        warehouse_id=warehouse_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        product_id=product_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByBinTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    product_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]:
    """Get inventory transactions by bin


    ## Get WMS Inventory Transactions by Bin

    Retrieve all inventory transactions involving a specific bin location, including both inbound and
    outbound movements.

    ### Features
    - **Bin-Centric View**: All transactions where bin is source (fromBinId) or destination (toBinId)
    - **Comprehensive Filtering**: Filter by warehouse, transaction type, date range, and product
    - **Movement Direction Tracking**: See both incoming and outgoing transactions for the bin
    - **Real-Time Analysis**: Current transaction data for operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **productId**: Optional - Filter transactions for specific product

    ### Business Logic
    - Uses OR query logic: (fromBinId = binId OR toBinId = binId)
    - Results ordered by transaction date (newest first)
    - Includes all transaction types that involve the specified bin
    - Date filtering based on transactionDate for temporal analysis

    ### Use Cases
    - **Bin Activity Analysis**: Review all activity for specific storage location
    - **Location Utilization**: Understand bin usage patterns and frequency
    - **Inventory Tracking**: Track product flow through specific locations
    - **Operational Planning**: Optimize bin assignments based on activity
    - **Compliance Audit**: Review all movements involving specific locations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN-A-01-01.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByBinTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        product_id (Union[Unset, str]):  Example: prod_12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        warehouse_id=warehouse_id,
        transaction_type=transaction_type,
        date_start=date_start,
        date_end=date_end,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    transaction_type: Union[Unset, list[GetWMSInventoryTransactionsByBinTransactionTypeItem]] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    product_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]]:
    """Get inventory transactions by bin


    ## Get WMS Inventory Transactions by Bin

    Retrieve all inventory transactions involving a specific bin location, including both inbound and
    outbound movements.

    ### Features
    - **Bin-Centric View**: All transactions where bin is source (fromBinId) or destination (toBinId)
    - **Comprehensive Filtering**: Filter by warehouse, transaction type, date range, and product
    - **Movement Direction Tracking**: See both incoming and outgoing transactions for the bin
    - **Real-Time Analysis**: Current transaction data for operational decisions

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **transactionType**: Optional - Filter by transaction type (supports arrays)
    - **dateStart/dateEnd**: Optional - Filter by transaction date range
    - **productId**: Optional - Filter transactions for specific product

    ### Business Logic
    - Uses OR query logic: (fromBinId = binId OR toBinId = binId)
    - Results ordered by transaction date (newest first)
    - Includes all transaction types that involve the specified bin
    - Date filtering based on transactionDate for temporal analysis

    ### Use Cases
    - **Bin Activity Analysis**: Review all activity for specific storage location
    - **Location Utilization**: Understand bin usage patterns and frequency
    - **Inventory Tracking**: Track product flow through specific locations
    - **Operational Planning**: Optimize bin assignments based on activity
    - **Compliance Audit**: Review all movements involving specific locations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN-A-01-01.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        transaction_type (Union[Unset,
            list[GetWMSInventoryTransactionsByBinTransactionTypeItem]]):
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        product_id (Union[Unset, str]):  Example: prod_12345.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInventoryTransactionsByBinResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            bin_id=bin_id,
            client=client,
            warehouse_id=warehouse_id,
            transaction_type=transaction_type,
            date_start=date_start,
            date_end=date_end,
            product_id=product_id,
        )
    ).parsed
