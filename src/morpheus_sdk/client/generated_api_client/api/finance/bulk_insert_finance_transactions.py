from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.bulk_insert_finance_transactions_body import BulkInsertFinanceTransactionsBody
from ...models.bulk_insert_finance_transactions_response_201 import BulkInsertFinanceTransactionsResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: BulkInsertFinanceTransactionsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/finance/transactions/bulk",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = BulkInsertFinanceTransactionsResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]:
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
    body: BulkInsertFinanceTransactionsBody,
) -> Response[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]:
    """Bulk insert finance transactions


    Bulk insert multiple finance transactions for efficient batch processing and data migration.

    **Core Features**:
    - **Batch Processing**: Insert multiple transactions in a single operation for performance
    - **Validation**: Each transaction validated according to business rules
    - **Auto-Generated IDs**: Automatic transactionId generation for transactions without IDs
    - **Atomic Operation**: Entire batch processed as single database operation
    - **Detailed Results**: Returns count of successfully inserted transactions

    **Use Cases**:
    - **Data Migration**: Import financial data from external systems
    - **Batch Processing**: Process large volumes of transactions efficiently
    - **Integration**: Synchronize data from accounting systems
    - **Historical Import**: Load transaction history for new implementations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkInsertFinanceTransactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]
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
    body: BulkInsertFinanceTransactionsBody,
) -> Optional[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]:
    """Bulk insert finance transactions


    Bulk insert multiple finance transactions for efficient batch processing and data migration.

    **Core Features**:
    - **Batch Processing**: Insert multiple transactions in a single operation for performance
    - **Validation**: Each transaction validated according to business rules
    - **Auto-Generated IDs**: Automatic transactionId generation for transactions without IDs
    - **Atomic Operation**: Entire batch processed as single database operation
    - **Detailed Results**: Returns count of successfully inserted transactions

    **Use Cases**:
    - **Data Migration**: Import financial data from external systems
    - **Batch Processing**: Process large volumes of transactions efficiently
    - **Integration**: Synchronize data from accounting systems
    - **Historical Import**: Load transaction history for new implementations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkInsertFinanceTransactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]
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
    body: BulkInsertFinanceTransactionsBody,
) -> Response[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]:
    """Bulk insert finance transactions


    Bulk insert multiple finance transactions for efficient batch processing and data migration.

    **Core Features**:
    - **Batch Processing**: Insert multiple transactions in a single operation for performance
    - **Validation**: Each transaction validated according to business rules
    - **Auto-Generated IDs**: Automatic transactionId generation for transactions without IDs
    - **Atomic Operation**: Entire batch processed as single database operation
    - **Detailed Results**: Returns count of successfully inserted transactions

    **Use Cases**:
    - **Data Migration**: Import financial data from external systems
    - **Batch Processing**: Process large volumes of transactions efficiently
    - **Integration**: Synchronize data from accounting systems
    - **Historical Import**: Load transaction history for new implementations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkInsertFinanceTransactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]
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
    body: BulkInsertFinanceTransactionsBody,
) -> Optional[Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]]:
    """Bulk insert finance transactions


    Bulk insert multiple finance transactions for efficient batch processing and data migration.

    **Core Features**:
    - **Batch Processing**: Insert multiple transactions in a single operation for performance
    - **Validation**: Each transaction validated according to business rules
    - **Auto-Generated IDs**: Automatic transactionId generation for transactions without IDs
    - **Atomic Operation**: Entire batch processed as single database operation
    - **Detailed Results**: Returns count of successfully inserted transactions

    **Use Cases**:
    - **Data Migration**: Import financial data from external systems
    - **Batch Processing**: Process large volumes of transactions efficiently
    - **Integration**: Synchronize data from accounting systems
    - **Historical Import**: Load transaction history for new implementations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (BulkInsertFinanceTransactionsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BulkInsertFinanceTransactionsResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
