import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_edi_transactions_deprecated_direction import ListEdiTransactionsDeprecatedDirection
from ...models.list_edi_transactions_deprecated_doc_type import ListEdiTransactionsDeprecatedDocType
from ...models.list_edi_transactions_deprecated_response_200 import ListEdiTransactionsDeprecatedResponse200
from ...models.list_edi_transactions_deprecated_status import ListEdiTransactionsDeprecatedStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    partner_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    doc_type: Union[Unset, ListEdiTransactionsDeprecatedDocType] = UNSET,
    direction: Union[Unset, ListEdiTransactionsDeprecatedDirection] = UNSET,
    status: Union[Unset, ListEdiTransactionsDeprecatedStatus] = UNSET,
    flow_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["partnerId"] = partner_id

    params["customerId"] = customer_id

    json_doc_type: Union[Unset, str] = UNSET
    if not isinstance(doc_type, Unset):
        json_doc_type = doc_type.value

    params["docType"] = json_doc_type

    json_direction: Union[Unset, str] = UNSET
    if not isinstance(direction, Unset):
        json_direction = direction.value

    params["direction"] = json_direction

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["flowId"] = flow_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["page"] = page

    params["pageSize"] = page_size

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/edi/deprecated",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]:
    if response.status_code == 200:
        response_200 = ListEdiTransactionsDeprecatedResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]:
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
    partner_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    doc_type: Union[Unset, ListEdiTransactionsDeprecatedDocType] = UNSET,
    direction: Union[Unset, ListEdiTransactionsDeprecatedDirection] = UNSET,
    status: Union[Unset, ListEdiTransactionsDeprecatedStatus] = UNSET,
    flow_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
) -> Response[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]:
    """[DEPRECATED] List EDI transactions with page-based pagination


    ## ⚠️ DEPRECATED - List EDI Transactions (Page-Based Pagination)

    > **WARNING**: This endpoint is deprecated and will be removed in a future version.
    > Please migrate to `GET /{worldId}/edi` which uses cursor-based pagination for better performance
    and scalability.

    ### Deprecation Notice

    This endpoint uses **page-based pagination** (`page` and `pageSize` parameters) which has
    significant performance limitations:

    **Why This Endpoint Is Deprecated:**
    - ❌ **Poor Performance**: Page-based pagination requires database to skip records, causing slow
    queries on large datasets
    - ❌ **Inconsistent Results**: Data changes between page requests can cause missing or duplicate
    records
    - ❌ **Memory Intensive**: Higher memory consumption for offset-based queries
    - ❌ **Scalability Issues**: Performance degrades linearly with page number

    **Migration Path:**
    Use `GET /{worldId}/edi` instead, which provides:
    - ✅ **Cursor-Based Pagination**: Uses `cursor` parameter for efficient, consistent pagination
    - ✅ **Better Performance**: Constant-time pagination regardless of dataset size
    - ✅ **Consistent Results**: Stable pagination even with concurrent data changes
    - ✅ **Lower Memory Usage**: Optimized database queries

    ### Migration Example

    **Old (Deprecated):**
    ```
    GET /{worldId}/edi/deprecated?page=2&pageSize=10
    ```

    **New (Recommended):**
    ```
    GET /{worldId}/edi?limit=10&cursor={nextCursor_from_previous_response}
    ```

    ### Features (Same as Main Endpoint)

    - **Multi-dimensional Filtering**: Partner, customer, document type, direction, status
    - **Advanced Date Filtering**: Precise timestamp-based queries
    - **Real-time Status Tracking**: Monitor transaction processing states
    - **Business Document Correlation**: Track related transactions through flow IDs

    ### EDI Document Types Supported
    - **850**: Purchase Orders
    - **855**: Purchase Order Acknowledgments
    - **856**: Advanced Ship Notices
    - **810**: Invoices
    - **820**: Payment Orders
    - **997**: Functional Acknowledgments
    - **999**: Implementation Acknowledgments

    ### Transaction Processing States
    - **RECEIVED**: Successfully received and parsed
    - **QUEUED**: Validated and queued for processing
    - **PROCESSING**: Currently being processed
    - **DELIVERED**: Successfully processed and delivered
    - **ERRORED**: Processing failed
    - **ARCHIVED**: Completed transactions

    ### Implementation Details

    This endpoint uses the `getEdiTransactionsByPageNumber` repository method which:
    - Uses MongoDB `.skip()` and `.limit()` for pagination
    - Calculates skip offset as: `(page - 1) * pageSize`
    - Sorts by `createdAt` in descending order (newest first)
    - Returns total count via separate `countDocuments()` query
    - Does NOT support cursor-based navigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_WALMART_001.
        customer_id (Union[Unset, str]):  Example: CUSTOMER_AMAZON_123.
        doc_type (Union[Unset, ListEdiTransactionsDeprecatedDocType]):  Example: 810.
        direction (Union[Unset, ListEdiTransactionsDeprecatedDirection]):  Example: INBOUND.
        status (Union[Unset, ListEdiTransactionsDeprecatedStatus]):  Example: ERRORED.
        flow_id (Union[Unset, str]):  Example: FLOW_PO_2024_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-15T23:59:59.999Z.
        page (Union[Unset, int]):  Default: 1. Example: 2.
        page_size (Union[Unset, int]):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        partner_id=partner_id,
        customer_id=customer_id,
        doc_type=doc_type,
        direction=direction,
        status=status,
        flow_id=flow_id,
        date_start=date_start,
        date_end=date_end,
        page=page,
        page_size=page_size,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    doc_type: Union[Unset, ListEdiTransactionsDeprecatedDocType] = UNSET,
    direction: Union[Unset, ListEdiTransactionsDeprecatedDirection] = UNSET,
    status: Union[Unset, ListEdiTransactionsDeprecatedStatus] = UNSET,
    flow_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
) -> Optional[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]:
    """[DEPRECATED] List EDI transactions with page-based pagination


    ## ⚠️ DEPRECATED - List EDI Transactions (Page-Based Pagination)

    > **WARNING**: This endpoint is deprecated and will be removed in a future version.
    > Please migrate to `GET /{worldId}/edi` which uses cursor-based pagination for better performance
    and scalability.

    ### Deprecation Notice

    This endpoint uses **page-based pagination** (`page` and `pageSize` parameters) which has
    significant performance limitations:

    **Why This Endpoint Is Deprecated:**
    - ❌ **Poor Performance**: Page-based pagination requires database to skip records, causing slow
    queries on large datasets
    - ❌ **Inconsistent Results**: Data changes between page requests can cause missing or duplicate
    records
    - ❌ **Memory Intensive**: Higher memory consumption for offset-based queries
    - ❌ **Scalability Issues**: Performance degrades linearly with page number

    **Migration Path:**
    Use `GET /{worldId}/edi` instead, which provides:
    - ✅ **Cursor-Based Pagination**: Uses `cursor` parameter for efficient, consistent pagination
    - ✅ **Better Performance**: Constant-time pagination regardless of dataset size
    - ✅ **Consistent Results**: Stable pagination even with concurrent data changes
    - ✅ **Lower Memory Usage**: Optimized database queries

    ### Migration Example

    **Old (Deprecated):**
    ```
    GET /{worldId}/edi/deprecated?page=2&pageSize=10
    ```

    **New (Recommended):**
    ```
    GET /{worldId}/edi?limit=10&cursor={nextCursor_from_previous_response}
    ```

    ### Features (Same as Main Endpoint)

    - **Multi-dimensional Filtering**: Partner, customer, document type, direction, status
    - **Advanced Date Filtering**: Precise timestamp-based queries
    - **Real-time Status Tracking**: Monitor transaction processing states
    - **Business Document Correlation**: Track related transactions through flow IDs

    ### EDI Document Types Supported
    - **850**: Purchase Orders
    - **855**: Purchase Order Acknowledgments
    - **856**: Advanced Ship Notices
    - **810**: Invoices
    - **820**: Payment Orders
    - **997**: Functional Acknowledgments
    - **999**: Implementation Acknowledgments

    ### Transaction Processing States
    - **RECEIVED**: Successfully received and parsed
    - **QUEUED**: Validated and queued for processing
    - **PROCESSING**: Currently being processed
    - **DELIVERED**: Successfully processed and delivered
    - **ERRORED**: Processing failed
    - **ARCHIVED**: Completed transactions

    ### Implementation Details

    This endpoint uses the `getEdiTransactionsByPageNumber` repository method which:
    - Uses MongoDB `.skip()` and `.limit()` for pagination
    - Calculates skip offset as: `(page - 1) * pageSize`
    - Sorts by `createdAt` in descending order (newest first)
    - Returns total count via separate `countDocuments()` query
    - Does NOT support cursor-based navigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_WALMART_001.
        customer_id (Union[Unset, str]):  Example: CUSTOMER_AMAZON_123.
        doc_type (Union[Unset, ListEdiTransactionsDeprecatedDocType]):  Example: 810.
        direction (Union[Unset, ListEdiTransactionsDeprecatedDirection]):  Example: INBOUND.
        status (Union[Unset, ListEdiTransactionsDeprecatedStatus]):  Example: ERRORED.
        flow_id (Union[Unset, str]):  Example: FLOW_PO_2024_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-15T23:59:59.999Z.
        page (Union[Unset, int]):  Default: 1. Example: 2.
        page_size (Union[Unset, int]):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        partner_id=partner_id,
        customer_id=customer_id,
        doc_type=doc_type,
        direction=direction,
        status=status,
        flow_id=flow_id,
        date_start=date_start,
        date_end=date_end,
        page=page,
        page_size=page_size,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    doc_type: Union[Unset, ListEdiTransactionsDeprecatedDocType] = UNSET,
    direction: Union[Unset, ListEdiTransactionsDeprecatedDirection] = UNSET,
    status: Union[Unset, ListEdiTransactionsDeprecatedStatus] = UNSET,
    flow_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
) -> Response[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]:
    """[DEPRECATED] List EDI transactions with page-based pagination


    ## ⚠️ DEPRECATED - List EDI Transactions (Page-Based Pagination)

    > **WARNING**: This endpoint is deprecated and will be removed in a future version.
    > Please migrate to `GET /{worldId}/edi` which uses cursor-based pagination for better performance
    and scalability.

    ### Deprecation Notice

    This endpoint uses **page-based pagination** (`page` and `pageSize` parameters) which has
    significant performance limitations:

    **Why This Endpoint Is Deprecated:**
    - ❌ **Poor Performance**: Page-based pagination requires database to skip records, causing slow
    queries on large datasets
    - ❌ **Inconsistent Results**: Data changes between page requests can cause missing or duplicate
    records
    - ❌ **Memory Intensive**: Higher memory consumption for offset-based queries
    - ❌ **Scalability Issues**: Performance degrades linearly with page number

    **Migration Path:**
    Use `GET /{worldId}/edi` instead, which provides:
    - ✅ **Cursor-Based Pagination**: Uses `cursor` parameter for efficient, consistent pagination
    - ✅ **Better Performance**: Constant-time pagination regardless of dataset size
    - ✅ **Consistent Results**: Stable pagination even with concurrent data changes
    - ✅ **Lower Memory Usage**: Optimized database queries

    ### Migration Example

    **Old (Deprecated):**
    ```
    GET /{worldId}/edi/deprecated?page=2&pageSize=10
    ```

    **New (Recommended):**
    ```
    GET /{worldId}/edi?limit=10&cursor={nextCursor_from_previous_response}
    ```

    ### Features (Same as Main Endpoint)

    - **Multi-dimensional Filtering**: Partner, customer, document type, direction, status
    - **Advanced Date Filtering**: Precise timestamp-based queries
    - **Real-time Status Tracking**: Monitor transaction processing states
    - **Business Document Correlation**: Track related transactions through flow IDs

    ### EDI Document Types Supported
    - **850**: Purchase Orders
    - **855**: Purchase Order Acknowledgments
    - **856**: Advanced Ship Notices
    - **810**: Invoices
    - **820**: Payment Orders
    - **997**: Functional Acknowledgments
    - **999**: Implementation Acknowledgments

    ### Transaction Processing States
    - **RECEIVED**: Successfully received and parsed
    - **QUEUED**: Validated and queued for processing
    - **PROCESSING**: Currently being processed
    - **DELIVERED**: Successfully processed and delivered
    - **ERRORED**: Processing failed
    - **ARCHIVED**: Completed transactions

    ### Implementation Details

    This endpoint uses the `getEdiTransactionsByPageNumber` repository method which:
    - Uses MongoDB `.skip()` and `.limit()` for pagination
    - Calculates skip offset as: `(page - 1) * pageSize`
    - Sorts by `createdAt` in descending order (newest first)
    - Returns total count via separate `countDocuments()` query
    - Does NOT support cursor-based navigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_WALMART_001.
        customer_id (Union[Unset, str]):  Example: CUSTOMER_AMAZON_123.
        doc_type (Union[Unset, ListEdiTransactionsDeprecatedDocType]):  Example: 810.
        direction (Union[Unset, ListEdiTransactionsDeprecatedDirection]):  Example: INBOUND.
        status (Union[Unset, ListEdiTransactionsDeprecatedStatus]):  Example: ERRORED.
        flow_id (Union[Unset, str]):  Example: FLOW_PO_2024_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-15T23:59:59.999Z.
        page (Union[Unset, int]):  Default: 1. Example: 2.
        page_size (Union[Unset, int]):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        partner_id=partner_id,
        customer_id=customer_id,
        doc_type=doc_type,
        direction=direction,
        status=status,
        flow_id=flow_id,
        date_start=date_start,
        date_end=date_end,
        page=page,
        page_size=page_size,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    doc_type: Union[Unset, ListEdiTransactionsDeprecatedDocType] = UNSET,
    direction: Union[Unset, ListEdiTransactionsDeprecatedDirection] = UNSET,
    status: Union[Unset, ListEdiTransactionsDeprecatedStatus] = UNSET,
    flow_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    page: Union[Unset, int] = 1,
    page_size: Union[Unset, int] = 10,
) -> Optional[Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]]:
    """[DEPRECATED] List EDI transactions with page-based pagination


    ## ⚠️ DEPRECATED - List EDI Transactions (Page-Based Pagination)

    > **WARNING**: This endpoint is deprecated and will be removed in a future version.
    > Please migrate to `GET /{worldId}/edi` which uses cursor-based pagination for better performance
    and scalability.

    ### Deprecation Notice

    This endpoint uses **page-based pagination** (`page` and `pageSize` parameters) which has
    significant performance limitations:

    **Why This Endpoint Is Deprecated:**
    - ❌ **Poor Performance**: Page-based pagination requires database to skip records, causing slow
    queries on large datasets
    - ❌ **Inconsistent Results**: Data changes between page requests can cause missing or duplicate
    records
    - ❌ **Memory Intensive**: Higher memory consumption for offset-based queries
    - ❌ **Scalability Issues**: Performance degrades linearly with page number

    **Migration Path:**
    Use `GET /{worldId}/edi` instead, which provides:
    - ✅ **Cursor-Based Pagination**: Uses `cursor` parameter for efficient, consistent pagination
    - ✅ **Better Performance**: Constant-time pagination regardless of dataset size
    - ✅ **Consistent Results**: Stable pagination even with concurrent data changes
    - ✅ **Lower Memory Usage**: Optimized database queries

    ### Migration Example

    **Old (Deprecated):**
    ```
    GET /{worldId}/edi/deprecated?page=2&pageSize=10
    ```

    **New (Recommended):**
    ```
    GET /{worldId}/edi?limit=10&cursor={nextCursor_from_previous_response}
    ```

    ### Features (Same as Main Endpoint)

    - **Multi-dimensional Filtering**: Partner, customer, document type, direction, status
    - **Advanced Date Filtering**: Precise timestamp-based queries
    - **Real-time Status Tracking**: Monitor transaction processing states
    - **Business Document Correlation**: Track related transactions through flow IDs

    ### EDI Document Types Supported
    - **850**: Purchase Orders
    - **855**: Purchase Order Acknowledgments
    - **856**: Advanced Ship Notices
    - **810**: Invoices
    - **820**: Payment Orders
    - **997**: Functional Acknowledgments
    - **999**: Implementation Acknowledgments

    ### Transaction Processing States
    - **RECEIVED**: Successfully received and parsed
    - **QUEUED**: Validated and queued for processing
    - **PROCESSING**: Currently being processed
    - **DELIVERED**: Successfully processed and delivered
    - **ERRORED**: Processing failed
    - **ARCHIVED**: Completed transactions

    ### Implementation Details

    This endpoint uses the `getEdiTransactionsByPageNumber` repository method which:
    - Uses MongoDB `.skip()` and `.limit()` for pagination
    - Calculates skip offset as: `(page - 1) * pageSize`
    - Sorts by `createdAt` in descending order (newest first)
    - Returns total count via separate `countDocuments()` query
    - Does NOT support cursor-based navigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_WALMART_001.
        customer_id (Union[Unset, str]):  Example: CUSTOMER_AMAZON_123.
        doc_type (Union[Unset, ListEdiTransactionsDeprecatedDocType]):  Example: 810.
        direction (Union[Unset, ListEdiTransactionsDeprecatedDirection]):  Example: INBOUND.
        status (Union[Unset, ListEdiTransactionsDeprecatedStatus]):  Example: ERRORED.
        flow_id (Union[Unset, str]):  Example: FLOW_PO_2024_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-15T23:59:59.999Z.
        page (Union[Unset, int]):  Default: 1. Example: 2.
        page_size (Union[Unset, int]):  Default: 10. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListEdiTransactionsDeprecatedResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            partner_id=partner_id,
            customer_id=customer_id,
            doc_type=doc_type,
            direction=direction,
            status=status,
            flow_id=flow_id,
            date_start=date_start,
            date_end=date_end,
            page=page,
            page_size=page_size,
        )
    ).parsed
