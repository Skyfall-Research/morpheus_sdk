import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_all_wms_receiving_transactions_response_200 import GetAllWMSReceivingTransactionsResponse200
from ...models.get_all_wms_receiving_transactions_status_item import GetAllWMSReceivingTransactionsStatusItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    inbound_order_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    params["inboundOrderId"] = inbound_order_id

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["userId"] = user_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/receiving-transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]:
    if response.status_code == 200:
        response_200 = GetAllWMSReceivingTransactionsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]:
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
    inbound_order_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]:
    """Get all receiving transactions


    ## Get All WMS Receiving Transactions

    Retrieve a paginated list of receiving transactions with comprehensive filtering capabilities.

    ### Features
    - **Advanced Filtering**: Filter by warehouse, order, status, user, and date ranges
    - **Pagination Support**: Cursor-based pagination for efficient data retrieval
    - **Status Filtering**: Multi-status filtering for workflow management
    - **Date Range Analysis**: Time-based filtering for reporting and analytics
    - **User Tracking**: Filter by specific users for performance analysis

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **inboundOrderId**: Optional - Filter by specific inbound order
    - **status**: Optional - Filter by receiving status (can be array)
    - **userId**: Optional - Filter by user who processed the transaction
    - **dateStart/dateEnd**: Optional - Filter by date range
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page (default: system limit)

    ### Business Logic
    - Results ordered by creation date (newest first)
    - Cursor-based pagination ensures consistent results during concurrent operations
    - Status filtering supports multiple values for workflow analysis
    - Date filtering uses creation timestamp for temporal analysis

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior.

    ### Use Cases
    - **Operational Dashboard**: Real-time view of receiving operations
    - **Performance Analysis**: User and warehouse performance tracking
    - **Status Monitoring**: Track transactions through receiving workflow
    - **Reporting**: Generate receiving transaction reports by various criteria
    - **Audit Trail**: Complete transaction history for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        inbound_order_id (Union[Unset, str]):  Example: wms_inbound-order_674565c1234567890abcdef.
        status (Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]]):
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        inbound_order_id=inbound_order_id,
        status=status,
        user_id=user_id,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
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
    inbound_order_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]:
    """Get all receiving transactions


    ## Get All WMS Receiving Transactions

    Retrieve a paginated list of receiving transactions with comprehensive filtering capabilities.

    ### Features
    - **Advanced Filtering**: Filter by warehouse, order, status, user, and date ranges
    - **Pagination Support**: Cursor-based pagination for efficient data retrieval
    - **Status Filtering**: Multi-status filtering for workflow management
    - **Date Range Analysis**: Time-based filtering for reporting and analytics
    - **User Tracking**: Filter by specific users for performance analysis

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **inboundOrderId**: Optional - Filter by specific inbound order
    - **status**: Optional - Filter by receiving status (can be array)
    - **userId**: Optional - Filter by user who processed the transaction
    - **dateStart/dateEnd**: Optional - Filter by date range
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page (default: system limit)

    ### Business Logic
    - Results ordered by creation date (newest first)
    - Cursor-based pagination ensures consistent results during concurrent operations
    - Status filtering supports multiple values for workflow analysis
    - Date filtering uses creation timestamp for temporal analysis

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior.

    ### Use Cases
    - **Operational Dashboard**: Real-time view of receiving operations
    - **Performance Analysis**: User and warehouse performance tracking
    - **Status Monitoring**: Track transactions through receiving workflow
    - **Reporting**: Generate receiving transaction reports by various criteria
    - **Audit Trail**: Complete transaction history for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        inbound_order_id (Union[Unset, str]):  Example: wms_inbound-order_674565c1234567890abcdef.
        status (Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]]):
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        inbound_order_id=inbound_order_id,
        status=status,
        user_id=user_id,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    inbound_order_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Response[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]:
    """Get all receiving transactions


    ## Get All WMS Receiving Transactions

    Retrieve a paginated list of receiving transactions with comprehensive filtering capabilities.

    ### Features
    - **Advanced Filtering**: Filter by warehouse, order, status, user, and date ranges
    - **Pagination Support**: Cursor-based pagination for efficient data retrieval
    - **Status Filtering**: Multi-status filtering for workflow management
    - **Date Range Analysis**: Time-based filtering for reporting and analytics
    - **User Tracking**: Filter by specific users for performance analysis

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **inboundOrderId**: Optional - Filter by specific inbound order
    - **status**: Optional - Filter by receiving status (can be array)
    - **userId**: Optional - Filter by user who processed the transaction
    - **dateStart/dateEnd**: Optional - Filter by date range
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page (default: system limit)

    ### Business Logic
    - Results ordered by creation date (newest first)
    - Cursor-based pagination ensures consistent results during concurrent operations
    - Status filtering supports multiple values for workflow analysis
    - Date filtering uses creation timestamp for temporal analysis

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior.

    ### Use Cases
    - **Operational Dashboard**: Real-time view of receiving operations
    - **Performance Analysis**: User and warehouse performance tracking
    - **Status Monitoring**: Track transactions through receiving workflow
    - **Reporting**: Generate receiving transaction reports by various criteria
    - **Audit Trail**: Complete transaction history for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        inbound_order_id (Union[Unset, str]):  Example: wms_inbound-order_674565c1234567890abcdef.
        status (Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]]):
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        inbound_order_id=inbound_order_id,
        status=status,
        user_id=user_id,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    inbound_order_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]] = UNSET,
    user_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = UNSET,
) -> Optional[Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]]:
    """Get all receiving transactions


    ## Get All WMS Receiving Transactions

    Retrieve a paginated list of receiving transactions with comprehensive filtering capabilities.

    ### Features
    - **Advanced Filtering**: Filter by warehouse, order, status, user, and date ranges
    - **Pagination Support**: Cursor-based pagination for efficient data retrieval
    - **Status Filtering**: Multi-status filtering for workflow management
    - **Date Range Analysis**: Time-based filtering for reporting and analytics
    - **User Tracking**: Filter by specific users for performance analysis

    ### Query Parameters
    - **warehouseId**: Optional - Filter by specific warehouse facility
    - **inboundOrderId**: Optional - Filter by specific inbound order
    - **status**: Optional - Filter by receiving status (can be array)
    - **userId**: Optional - Filter by user who processed the transaction
    - **dateStart/dateEnd**: Optional - Filter by date range
    - **cursor**: Optional - Pagination cursor for next page
    - **limit**: Optional - Maximum results per page (default: system limit)

    ### Business Logic
    - Results ordered by creation date (newest first)
    - Cursor-based pagination ensures consistent results during concurrent operations
    - Status filtering supports multiple values for workflow analysis
    - Date filtering uses creation timestamp for temporal analysis

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior.

    ### Use Cases
    - **Operational Dashboard**: Real-time view of receiving operations
    - **Performance Analysis**: User and warehouse performance tracking
    - **Status Monitoring**: Track transactions through receiving workflow
    - **Reporting**: Generate receiving transaction reports by various criteria
    - **Audit Trail**: Complete transaction history for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (Union[Unset, str]):  Example: wms_warehouse_674565c1234567890abcdef.
        inbound_order_id (Union[Unset, str]):  Example: wms_inbound-order_674565c1234567890abcdef.
        status (Union[Unset, list[GetAllWMSReceivingTransactionsStatusItem]]):
        user_id (Union[Unset, str]):  Example: user_receiver_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59Z.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetAllWMSReceivingTransactionsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            inbound_order_id=inbound_order_id,
            status=status,
            user_id=user_id,
            date_start=date_start,
            date_end=date_end,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
