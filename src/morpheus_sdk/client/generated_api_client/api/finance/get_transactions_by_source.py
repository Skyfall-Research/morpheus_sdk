from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_transactions_by_source_response_200 import GetTransactionsBySourceResponse200
from ...models.get_transactions_by_source_source_type import GetTransactionsBySourceSourceType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    source_type: GetTransactionsBySourceSourceType,
    source_id: str,
    *,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/finance/transactions/source/{source_type}/{source_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTransactionsBySourceResponse200]]:
    if response.status_code == 200:
        response_200 = GetTransactionsBySourceResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetTransactionsBySourceResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    source_type: GetTransactionsBySourceSourceType,
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 20,
) -> Response[Union[ErrorResponse, GetTransactionsBySourceResponse200]]:
    """Get transactions by source document


    Retrieve all finance transactions associated with a specific source document for comprehensive
    financial tracking.

    **Core Features**:
    - **Source Linking**: Get all transactions linked to specific source documents
    - **Multi-Source Support**: Support for invoices, bills, manual entries, interest, and payments
    - **Transaction History**: Complete financial history for source documents
    - **Paginated Results**: Efficient pagination for large transaction volumes

    **Use Cases**:
    - **Document Analysis**: See all financial transactions related to specific documents
    - **Payment Tracking**: Track all payments against invoices or bills
    - **Financial Reconciliation**: Match transactions with source documents
    - **Audit Trails**: Review complete financial activity for specific sources

    **Route Validation**: Both sourceType and sourceId are required path parameters.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        source_type (GetTransactionsBySourceSourceType):  Example: invoice.
        source_id (str):  Example: INV_507f1f77bcf86cd799439014.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTransactionsBySourceResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        source_type=source_type,
        source_id=source_id,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    source_type: GetTransactionsBySourceSourceType,
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 20,
) -> Optional[Union[ErrorResponse, GetTransactionsBySourceResponse200]]:
    """Get transactions by source document


    Retrieve all finance transactions associated with a specific source document for comprehensive
    financial tracking.

    **Core Features**:
    - **Source Linking**: Get all transactions linked to specific source documents
    - **Multi-Source Support**: Support for invoices, bills, manual entries, interest, and payments
    - **Transaction History**: Complete financial history for source documents
    - **Paginated Results**: Efficient pagination for large transaction volumes

    **Use Cases**:
    - **Document Analysis**: See all financial transactions related to specific documents
    - **Payment Tracking**: Track all payments against invoices or bills
    - **Financial Reconciliation**: Match transactions with source documents
    - **Audit Trails**: Review complete financial activity for specific sources

    **Route Validation**: Both sourceType and sourceId are required path parameters.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        source_type (GetTransactionsBySourceSourceType):  Example: invoice.
        source_id (str):  Example: INV_507f1f77bcf86cd799439014.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTransactionsBySourceResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        source_type=source_type,
        source_id=source_id,
        client=client,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    source_type: GetTransactionsBySourceSourceType,
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 20,
) -> Response[Union[ErrorResponse, GetTransactionsBySourceResponse200]]:
    """Get transactions by source document


    Retrieve all finance transactions associated with a specific source document for comprehensive
    financial tracking.

    **Core Features**:
    - **Source Linking**: Get all transactions linked to specific source documents
    - **Multi-Source Support**: Support for invoices, bills, manual entries, interest, and payments
    - **Transaction History**: Complete financial history for source documents
    - **Paginated Results**: Efficient pagination for large transaction volumes

    **Use Cases**:
    - **Document Analysis**: See all financial transactions related to specific documents
    - **Payment Tracking**: Track all payments against invoices or bills
    - **Financial Reconciliation**: Match transactions with source documents
    - **Audit Trails**: Review complete financial activity for specific sources

    **Route Validation**: Both sourceType and sourceId are required path parameters.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        source_type (GetTransactionsBySourceSourceType):  Example: invoice.
        source_id (str):  Example: INV_507f1f77bcf86cd799439014.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTransactionsBySourceResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        source_type=source_type,
        source_id=source_id,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    source_type: GetTransactionsBySourceSourceType,
    source_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 20,
) -> Optional[Union[ErrorResponse, GetTransactionsBySourceResponse200]]:
    """Get transactions by source document


    Retrieve all finance transactions associated with a specific source document for comprehensive
    financial tracking.

    **Core Features**:
    - **Source Linking**: Get all transactions linked to specific source documents
    - **Multi-Source Support**: Support for invoices, bills, manual entries, interest, and payments
    - **Transaction History**: Complete financial history for source documents
    - **Paginated Results**: Efficient pagination for large transaction volumes

    **Use Cases**:
    - **Document Analysis**: See all financial transactions related to specific documents
    - **Payment Tracking**: Track all payments against invoices or bills
    - **Financial Reconciliation**: Match transactions with source documents
    - **Audit Trails**: Review complete financial activity for specific sources

    **Route Validation**: Both sourceType and sourceId are required path parameters.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        source_type (GetTransactionsBySourceSourceType):  Example: invoice.
        source_id (str):  Example: INV_507f1f77bcf86cd799439014.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTransactionsBySourceResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            source_type=source_type,
            source_id=source_id,
            client=client,
            limit=limit,
        )
    ).parsed
