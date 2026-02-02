import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_transactions_by_type_response_200 import GetTransactionsByTypeResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["partnerId"] = partner_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/finance/stats/by-type",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTransactionsByTypeResponse200]:
    if response.status_code == 200:
        response_200 = GetTransactionsByTypeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTransactionsByTypeResponse200]:
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
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
) -> Response[GetTransactionsByTypeResponse200]:
    """Get transaction statistics by type


    Retrieve transaction statistics aggregated by transaction type for financial analysis and reporting.

    **Core Features**:
    - **Type-Based Analytics**: Statistics grouped by payment_in and payment_out transaction types
    - **Volume and Value Metrics**: Count and total amount for each transaction type
    - **Date Range Filtering**: Analyze type-based patterns over specific time periods
    - **Partner Filtering**: Focus type analysis on specific business partners

    **Use Cases**:
    - **Cash Flow Analysis**: Understand incoming vs outgoing payment patterns
    - **Financial Planning**: Analyze transaction type distributions for budgeting
    - **Performance Metrics**: Track payment processing volumes by type
    - **Trend Analysis**: Identify patterns in payment types over time

    **Statistics Include**:
    - **count**: Number of transactions for each type
    - **totalAmount**: Total monetary value for each type


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByTypeResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        partner_id=partner_id,
        date_start=date_start,
        date_end=date_end,
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
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
) -> Optional[GetTransactionsByTypeResponse200]:
    """Get transaction statistics by type


    Retrieve transaction statistics aggregated by transaction type for financial analysis and reporting.

    **Core Features**:
    - **Type-Based Analytics**: Statistics grouped by payment_in and payment_out transaction types
    - **Volume and Value Metrics**: Count and total amount for each transaction type
    - **Date Range Filtering**: Analyze type-based patterns over specific time periods
    - **Partner Filtering**: Focus type analysis on specific business partners

    **Use Cases**:
    - **Cash Flow Analysis**: Understand incoming vs outgoing payment patterns
    - **Financial Planning**: Analyze transaction type distributions for budgeting
    - **Performance Metrics**: Track payment processing volumes by type
    - **Trend Analysis**: Identify patterns in payment types over time

    **Statistics Include**:
    - **count**: Number of transactions for each type
    - **totalAmount**: Total monetary value for each type


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByTypeResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        partner_id=partner_id,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
) -> Response[GetTransactionsByTypeResponse200]:
    """Get transaction statistics by type


    Retrieve transaction statistics aggregated by transaction type for financial analysis and reporting.

    **Core Features**:
    - **Type-Based Analytics**: Statistics grouped by payment_in and payment_out transaction types
    - **Volume and Value Metrics**: Count and total amount for each transaction type
    - **Date Range Filtering**: Analyze type-based patterns over specific time periods
    - **Partner Filtering**: Focus type analysis on specific business partners

    **Use Cases**:
    - **Cash Flow Analysis**: Understand incoming vs outgoing payment patterns
    - **Financial Planning**: Analyze transaction type distributions for budgeting
    - **Performance Metrics**: Track payment processing volumes by type
    - **Trend Analysis**: Identify patterns in payment types over time

    **Statistics Include**:
    - **count**: Number of transactions for each type
    - **totalAmount**: Total monetary value for each type


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTransactionsByTypeResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        partner_id=partner_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
) -> Optional[GetTransactionsByTypeResponse200]:
    """Get transaction statistics by type


    Retrieve transaction statistics aggregated by transaction type for financial analysis and reporting.

    **Core Features**:
    - **Type-Based Analytics**: Statistics grouped by payment_in and payment_out transaction types
    - **Volume and Value Metrics**: Count and total amount for each transaction type
    - **Date Range Filtering**: Analyze type-based patterns over specific time periods
    - **Partner Filtering**: Focus type analysis on specific business partners

    **Use Cases**:
    - **Cash Flow Analysis**: Understand incoming vs outgoing payment patterns
    - **Financial Planning**: Analyze transaction type distributions for budgeting
    - **Performance Metrics**: Track payment processing volumes by type
    - **Trend Analysis**: Identify patterns in payment types over time

    **Statistics Include**:
    - **count**: Number of transactions for each type
    - **totalAmount**: Total monetary value for each type


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTransactionsByTypeResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            partner_id=partner_id,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
