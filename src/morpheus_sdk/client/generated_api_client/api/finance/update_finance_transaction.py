from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_finance_transaction_body import UpdateFinanceTransactionBody
from ...models.update_finance_transaction_response_200 import UpdateFinanceTransactionResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    transaction_id: str,
    *,
    body: UpdateFinanceTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/finance/transactions/{transaction_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateFinanceTransactionResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]:
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
    body: UpdateFinanceTransactionBody,
) -> Response[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]:
    """Update finance transaction


    Update finance transaction information with partial data for financial corrections and adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific transaction fields without replacing entire record
    - **Financial Management**: Modify transaction amounts, types, and source associations
    - **Metadata Updates**: Update transaction-specific metadata for enhanced tracking
    - **Validation**: Ensure updated data meets business rules and constraints

    **Use Cases**:
    - **Transaction Corrections**: Modify transaction details per accounting requirements
    - **Amount Adjustments**: Update transaction amounts for corrections or adjustments
    - **Source Updates**: Change source document associations for proper linking
    - **Metadata Enhancement**: Add or update transaction metadata for improved tracking

    **Important**: Core transaction type and source validation rules apply to updates.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.
        body (UpdateFinanceTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
        body=body,
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
    body: UpdateFinanceTransactionBody,
) -> Optional[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]:
    """Update finance transaction


    Update finance transaction information with partial data for financial corrections and adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific transaction fields without replacing entire record
    - **Financial Management**: Modify transaction amounts, types, and source associations
    - **Metadata Updates**: Update transaction-specific metadata for enhanced tracking
    - **Validation**: Ensure updated data meets business rules and constraints

    **Use Cases**:
    - **Transaction Corrections**: Modify transaction details per accounting requirements
    - **Amount Adjustments**: Update transaction amounts for corrections or adjustments
    - **Source Updates**: Change source document associations for proper linking
    - **Metadata Enhancement**: Add or update transaction metadata for improved tracking

    **Important**: Core transaction type and source validation rules apply to updates.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.
        body (UpdateFinanceTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateFinanceTransactionResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        transaction_id=transaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateFinanceTransactionBody,
) -> Response[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]:
    """Update finance transaction


    Update finance transaction information with partial data for financial corrections and adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific transaction fields without replacing entire record
    - **Financial Management**: Modify transaction amounts, types, and source associations
    - **Metadata Updates**: Update transaction-specific metadata for enhanced tracking
    - **Validation**: Ensure updated data meets business rules and constraints

    **Use Cases**:
    - **Transaction Corrections**: Modify transaction details per accounting requirements
    - **Amount Adjustments**: Update transaction amounts for corrections or adjustments
    - **Source Updates**: Change source document associations for proper linking
    - **Metadata Enhancement**: Add or update transaction metadata for improved tracking

    **Important**: Core transaction type and source validation rules apply to updates.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.
        body (UpdateFinanceTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateFinanceTransactionBody,
) -> Optional[Union[ErrorResponse, UpdateFinanceTransactionResponse200]]:
    """Update finance transaction


    Update finance transaction information with partial data for financial corrections and adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific transaction fields without replacing entire record
    - **Financial Management**: Modify transaction amounts, types, and source associations
    - **Metadata Updates**: Update transaction-specific metadata for enhanced tracking
    - **Validation**: Ensure updated data meets business rules and constraints

    **Use Cases**:
    - **Transaction Corrections**: Modify transaction details per accounting requirements
    - **Amount Adjustments**: Update transaction amounts for corrections or adjustments
    - **Source Updates**: Change source document associations for proper linking
    - **Metadata Enhancement**: Add or update transaction metadata for improved tracking

    **Important**: Core transaction type and source validation rules apply to updates.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: TRANS_507f1f77bcf86cd799439012.
        body (UpdateFinanceTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateFinanceTransactionResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
