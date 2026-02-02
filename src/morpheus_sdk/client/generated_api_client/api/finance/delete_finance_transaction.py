from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_finance_transaction_response_200 import DeleteFinanceTransactionResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    transaction_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/{world_id}/finance/transactions/{transaction_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteFinanceTransactionResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]:
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
) -> Response[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]:
    """Delete finance transaction


    Delete finance transaction record from the system for financial cleanup and data management.

    **Core Features**:
    - **Complete Removal**: Permanently delete transaction record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Confirmation Response**: Clear confirmation of deletion success or failure

    **Use Cases**:
    - **Transaction Cleanup**: Remove erroneous or duplicate transactions
    - **Data Management**: Clean up test or invalid transaction data
    - **System Maintenance**: Remove obsolete transaction records
    - **Compliance**: Transaction deletion per data retention policies

    **Important**: Ensure transaction is not referenced by other financial records before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]:
    """Delete finance transaction


    Delete finance transaction record from the system for financial cleanup and data management.

    **Core Features**:
    - **Complete Removal**: Permanently delete transaction record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Confirmation Response**: Clear confirmation of deletion success or failure

    **Use Cases**:
    - **Transaction Cleanup**: Remove erroneous or duplicate transactions
    - **Data Management**: Clean up test or invalid transaction data
    - **System Maintenance**: Remove obsolete transaction records
    - **Compliance**: Transaction deletion per data retention policies

    **Important**: Ensure transaction is not referenced by other financial records before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteFinanceTransactionResponse200, ErrorResponse]
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
) -> Response[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]:
    """Delete finance transaction


    Delete finance transaction record from the system for financial cleanup and data management.

    **Core Features**:
    - **Complete Removal**: Permanently delete transaction record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Confirmation Response**: Clear confirmation of deletion success or failure

    **Use Cases**:
    - **Transaction Cleanup**: Remove erroneous or duplicate transactions
    - **Data Management**: Clean up test or invalid transaction data
    - **System Maintenance**: Remove obsolete transaction records
    - **Compliance**: Transaction deletion per data retention policies

    **Important**: Ensure transaction is not referenced by other financial records before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteFinanceTransactionResponse200, ErrorResponse]]:
    """Delete finance transaction


    Delete finance transaction record from the system for financial cleanup and data management.

    **Core Features**:
    - **Complete Removal**: Permanently delete transaction record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Confirmation Response**: Clear confirmation of deletion success or failure

    **Use Cases**:
    - **Transaction Cleanup**: Remove erroneous or duplicate transactions
    - **Data Management**: Clean up test or invalid transaction data
    - **System Maintenance**: Remove obsolete transaction records
    - **Compliance**: Transaction deletion per data retention policies

    **Important**: Ensure transaction is not referenced by other financial records before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteFinanceTransactionResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            transaction_id=transaction_id,
            client=client,
        )
    ).parsed
