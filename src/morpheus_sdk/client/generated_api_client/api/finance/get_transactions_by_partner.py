import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_transactions_by_partner_response_200 import GetTransactionsByPartnerResponse200
from ...models.get_transactions_by_partner_type import GetTransactionsByPartnerType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    type_: Union[Unset, GetTransactionsByPartnerType] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = 100,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

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
        "url": f"/{world_id}/finance/stats/by-partner",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTransactionsByPartnerResponse200]:
    if response.status_code == 200:
        response_200 = GetTransactionsByPartnerResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTransactionsByPartnerResponse200]:
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
    type_: Union[Unset, GetTransactionsByPartnerType] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[GetTransactionsByPartnerResponse200]:
    """Get transaction statistics by partner


    Retrieve transaction statistics aggregated by business partner for relationship analysis and
    reporting.

    **Core Features**:
    - **Partner-Based Analytics**: Statistics grouped by business partner for relationship insights
    - **Comprehensive Metrics**: Count, total amount, and average amount per partner
    - **Transaction Type Filtering**: Focus analysis on specific transaction types
    (payment_in/payment_out)
    - **Date Range Analysis**: Analyze partner relationships over specific time periods
    - **Result Limiting**: Configurable result limits with safety caps to prevent abuse

    **Use Cases**:
    - **Partner Performance**: Analyze transaction volumes and values by business partner
    - **Relationship Management**: Understand financial relationships with key partners
    - **Credit Analysis**: Evaluate partner payment patterns and transaction history
    - **Business Intelligence**: Identify top partners by transaction volume and value

    **Statistics Include**:
    - **partnerId**: Business partner identifier
    - **count**: Number of transactions with the partner
    - **totalAmount**: Total transaction value with the partner
    - **avgAmount**: Average transaction amount with the partner


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetTransactionsByPartnerType]):  Example: payment_in.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        limit (Union[Unset, int]):  Default: 100. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByPartnerResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        type_=type_,
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
    type_: Union[Unset, GetTransactionsByPartnerType] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[GetTransactionsByPartnerResponse200]:
    """Get transaction statistics by partner


    Retrieve transaction statistics aggregated by business partner for relationship analysis and
    reporting.

    **Core Features**:
    - **Partner-Based Analytics**: Statistics grouped by business partner for relationship insights
    - **Comprehensive Metrics**: Count, total amount, and average amount per partner
    - **Transaction Type Filtering**: Focus analysis on specific transaction types
    (payment_in/payment_out)
    - **Date Range Analysis**: Analyze partner relationships over specific time periods
    - **Result Limiting**: Configurable result limits with safety caps to prevent abuse

    **Use Cases**:
    - **Partner Performance**: Analyze transaction volumes and values by business partner
    - **Relationship Management**: Understand financial relationships with key partners
    - **Credit Analysis**: Evaluate partner payment patterns and transaction history
    - **Business Intelligence**: Identify top partners by transaction volume and value

    **Statistics Include**:
    - **partnerId**: Business partner identifier
    - **count**: Number of transactions with the partner
    - **totalAmount**: Total transaction value with the partner
    - **avgAmount**: Average transaction amount with the partner


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetTransactionsByPartnerType]):  Example: payment_in.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        limit (Union[Unset, int]):  Default: 100. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByPartnerResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        type_=type_,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, GetTransactionsByPartnerType] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Response[GetTransactionsByPartnerResponse200]:
    """Get transaction statistics by partner


    Retrieve transaction statistics aggregated by business partner for relationship analysis and
    reporting.

    **Core Features**:
    - **Partner-Based Analytics**: Statistics grouped by business partner for relationship insights
    - **Comprehensive Metrics**: Count, total amount, and average amount per partner
    - **Transaction Type Filtering**: Focus analysis on specific transaction types
    (payment_in/payment_out)
    - **Date Range Analysis**: Analyze partner relationships over specific time periods
    - **Result Limiting**: Configurable result limits with safety caps to prevent abuse

    **Use Cases**:
    - **Partner Performance**: Analyze transaction volumes and values by business partner
    - **Relationship Management**: Understand financial relationships with key partners
    - **Credit Analysis**: Evaluate partner payment patterns and transaction history
    - **Business Intelligence**: Identify top partners by transaction volume and value

    **Statistics Include**:
    - **partnerId**: Business partner identifier
    - **count**: Number of transactions with the partner
    - **totalAmount**: Total transaction value with the partner
    - **avgAmount**: Average transaction amount with the partner


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetTransactionsByPartnerType]):  Example: payment_in.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        limit (Union[Unset, int]):  Default: 100. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByPartnerResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        type_=type_,
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
    type_: Union[Unset, GetTransactionsByPartnerType] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    limit: Union[Unset, int] = 100,
) -> Optional[GetTransactionsByPartnerResponse200]:
    """Get transaction statistics by partner


    Retrieve transaction statistics aggregated by business partner for relationship analysis and
    reporting.

    **Core Features**:
    - **Partner-Based Analytics**: Statistics grouped by business partner for relationship insights
    - **Comprehensive Metrics**: Count, total amount, and average amount per partner
    - **Transaction Type Filtering**: Focus analysis on specific transaction types
    (payment_in/payment_out)
    - **Date Range Analysis**: Analyze partner relationships over specific time periods
    - **Result Limiting**: Configurable result limits with safety caps to prevent abuse

    **Use Cases**:
    - **Partner Performance**: Analyze transaction volumes and values by business partner
    - **Relationship Management**: Understand financial relationships with key partners
    - **Credit Analysis**: Evaluate partner payment patterns and transaction history
    - **Business Intelligence**: Identify top partners by transaction volume and value

    **Statistics Include**:
    - **partnerId**: Business partner identifier
    - **count**: Number of transactions with the partner
    - **totalAmount**: Total transaction value with the partner
    - **avgAmount**: Average transaction amount with the partner


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetTransactionsByPartnerType]):  Example: payment_in.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        limit (Union[Unset, int]):  Default: 100. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByPartnerResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            type_=type_,
            date_start=date_start,
            date_end=date_end,
            limit=limit,
        )
    ).parsed
