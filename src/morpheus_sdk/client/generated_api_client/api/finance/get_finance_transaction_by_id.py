from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_finance_transaction_by_id_response_200 import GetFinanceTransactionByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    transaction_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/finance/transactions/{transaction_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetFinanceTransactionByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]:
    """Get finance transaction by ID


    Retrieve specific finance transaction by transaction ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get transaction by unique transaction identifier
    - **Complete Profile**: Returns full transaction data including metadata and timestamps
    - **Fast Lookup**: Optimized query using indexed transactionId field
    - **Financial Intelligence**: Access comprehensive transaction data for accounting operations

    **Use Cases**:
    - **Transaction Details**: Get complete transaction information for financial operations
    - **Customer Service**: Resolve payment inquiries using transaction ID references
    - **Accounting Operations**: Access transaction details for ledger and reconciliation
    - **Integration Support**: Direct API access for external financial system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]:
    """Get finance transaction by ID


    Retrieve specific finance transaction by transaction ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get transaction by unique transaction identifier
    - **Complete Profile**: Returns full transaction data including metadata and timestamps
    - **Fast Lookup**: Optimized query using indexed transactionId field
    - **Financial Intelligence**: Access comprehensive transaction data for accounting operations

    **Use Cases**:
    - **Transaction Details**: Get complete transaction information for financial operations
    - **Customer Service**: Resolve payment inquiries using transaction ID references
    - **Accounting Operations**: Access transaction details for ledger and reconciliation
    - **Integration Support**: Direct API access for external financial system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetFinanceTransactionByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        transaction_id=transaction_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]:
    """Get finance transaction by ID


    Retrieve specific finance transaction by transaction ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get transaction by unique transaction identifier
    - **Complete Profile**: Returns full transaction data including metadata and timestamps
    - **Fast Lookup**: Optimized query using indexed transactionId field
    - **Financial Intelligence**: Access comprehensive transaction data for accounting operations

    **Use Cases**:
    - **Transaction Details**: Get complete transaction information for financial operations
    - **Customer Service**: Resolve payment inquiries using transaction ID references
    - **Accounting Operations**: Access transaction details for ledger and reconciliation
    - **Integration Support**: Direct API access for external financial system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetFinanceTransactionByIdResponse200]]:
    """Get finance transaction by ID


    Retrieve specific finance transaction by transaction ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get transaction by unique transaction identifier
    - **Complete Profile**: Returns full transaction data including metadata and timestamps
    - **Fast Lookup**: Optimized query using indexed transactionId field
    - **Financial Intelligence**: Access comprehensive transaction data for accounting operations

    **Use Cases**:
    - **Transaction Details**: Get complete transaction information for financial operations
    - **Customer Service**: Resolve payment inquiries using transaction ID references
    - **Accounting Operations**: Access transaction details for ledger and reconciliation
    - **Integration Support**: Direct API access for external financial system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetFinanceTransactionByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            transaction_id=transaction_id,
            client=client,
        )
    ).parsed
