import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_finance_transactions_response_200 import GetAllFinanceTransactionsResponse200
from ...models.get_all_finance_transactions_source_type import GetAllFinanceTransactionsSourceType
from ...models.get_all_finance_transactions_type import GetAllFinanceTransactionsType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    partner_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, GetAllFinanceTransactionsType] = UNSET,
    source_type: Union[Unset, GetAllFinanceTransactionsSourceType] = UNSET,
    source_id: Union[Unset, str] = UNSET,
    amount_min: Union[Unset, float] = UNSET,
    amount_max: Union[Unset, float] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["partnerId"] = partner_id

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    json_source_type: Union[Unset, str] = UNSET
    if not isinstance(source_type, Unset):
        json_source_type = source_type.value

    params["sourceType"] = json_source_type

    params["sourceId"] = source_id

    params["amountMin"] = amount_min

    params["amountMax"] = amount_max

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["search"] = search

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/finance/transactions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllFinanceTransactionsResponse200]:
    if response.status_code == 200:
        response_200 = GetAllFinanceTransactionsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllFinanceTransactionsResponse200]:
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
    type_: Union[Unset, GetAllFinanceTransactionsType] = UNSET,
    source_type: Union[Unset, GetAllFinanceTransactionsSourceType] = UNSET,
    source_id: Union[Unset, str] = UNSET,
    amount_min: Union[Unset, float] = UNSET,
    amount_max: Union[Unset, float] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[GetAllFinanceTransactionsResponse200]:
    """Get all finance transactions


    Retrieve all finance transactions with comprehensive filtering capabilities for financial analysis
    and reporting.

    **Core Features**:
    - **Advanced Filtering**: Filter by partner, transaction type, source type, amount ranges, and date
    ranges
    - **Full-Text Search**: Search within transaction metadata for flexible querying
    - **Paginated Results**: Cursor-based pagination for efficient data retrieval
    - **Financial Analytics**: Support for business intelligence and reporting needs

    **Use Cases**:
    - **Financial Reporting**: Generate comprehensive transaction reports with filtering
    - **Cash Flow Analysis**: Track payment patterns and transaction volumes
    - **Partner Analytics**: Analyze transaction history by business partner
    - **Audit Trails**: Review transaction history for compliance and auditing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        type_ (Union[Unset, GetAllFinanceTransactionsType]):  Example: payment_in.
        source_type (Union[Unset, GetAllFinanceTransactionsSourceType]):  Example: invoice.
        source_id (Union[Unset, str]):  Example: INV_507f1f77bcf86cd799439014.
        amount_min (Union[Unset, float]):  Example: 100.
        amount_max (Union[Unset, float]):  Example: 5000.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        search (Union[Unset, str]):  Example: ACH payment.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439015.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllFinanceTransactionsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        partner_id=partner_id,
        type_=type_,
        source_type=source_type,
        source_id=source_id,
        amount_min=amount_min,
        amount_max=amount_max,
        date_start=date_start,
        date_end=date_end,
        search=search,
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
    partner_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, GetAllFinanceTransactionsType] = UNSET,
    source_type: Union[Unset, GetAllFinanceTransactionsSourceType] = UNSET,
    source_id: Union[Unset, str] = UNSET,
    amount_min: Union[Unset, float] = UNSET,
    amount_max: Union[Unset, float] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[GetAllFinanceTransactionsResponse200]:
    """Get all finance transactions


    Retrieve all finance transactions with comprehensive filtering capabilities for financial analysis
    and reporting.

    **Core Features**:
    - **Advanced Filtering**: Filter by partner, transaction type, source type, amount ranges, and date
    ranges
    - **Full-Text Search**: Search within transaction metadata for flexible querying
    - **Paginated Results**: Cursor-based pagination for efficient data retrieval
    - **Financial Analytics**: Support for business intelligence and reporting needs

    **Use Cases**:
    - **Financial Reporting**: Generate comprehensive transaction reports with filtering
    - **Cash Flow Analysis**: Track payment patterns and transaction volumes
    - **Partner Analytics**: Analyze transaction history by business partner
    - **Audit Trails**: Review transaction history for compliance and auditing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        type_ (Union[Unset, GetAllFinanceTransactionsType]):  Example: payment_in.
        source_type (Union[Unset, GetAllFinanceTransactionsSourceType]):  Example: invoice.
        source_id (Union[Unset, str]):  Example: INV_507f1f77bcf86cd799439014.
        amount_min (Union[Unset, float]):  Example: 100.
        amount_max (Union[Unset, float]):  Example: 5000.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        search (Union[Unset, str]):  Example: ACH payment.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439015.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllFinanceTransactionsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        partner_id=partner_id,
        type_=type_,
        source_type=source_type,
        source_id=source_id,
        amount_min=amount_min,
        amount_max=amount_max,
        date_start=date_start,
        date_end=date_end,
        search=search,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, GetAllFinanceTransactionsType] = UNSET,
    source_type: Union[Unset, GetAllFinanceTransactionsSourceType] = UNSET,
    source_id: Union[Unset, str] = UNSET,
    amount_min: Union[Unset, float] = UNSET,
    amount_max: Union[Unset, float] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[GetAllFinanceTransactionsResponse200]:
    """Get all finance transactions


    Retrieve all finance transactions with comprehensive filtering capabilities for financial analysis
    and reporting.

    **Core Features**:
    - **Advanced Filtering**: Filter by partner, transaction type, source type, amount ranges, and date
    ranges
    - **Full-Text Search**: Search within transaction metadata for flexible querying
    - **Paginated Results**: Cursor-based pagination for efficient data retrieval
    - **Financial Analytics**: Support for business intelligence and reporting needs

    **Use Cases**:
    - **Financial Reporting**: Generate comprehensive transaction reports with filtering
    - **Cash Flow Analysis**: Track payment patterns and transaction volumes
    - **Partner Analytics**: Analyze transaction history by business partner
    - **Audit Trails**: Review transaction history for compliance and auditing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        type_ (Union[Unset, GetAllFinanceTransactionsType]):  Example: payment_in.
        source_type (Union[Unset, GetAllFinanceTransactionsSourceType]):  Example: invoice.
        source_id (Union[Unset, str]):  Example: INV_507f1f77bcf86cd799439014.
        amount_min (Union[Unset, float]):  Example: 100.
        amount_max (Union[Unset, float]):  Example: 5000.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        search (Union[Unset, str]):  Example: ACH payment.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439015.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllFinanceTransactionsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        partner_id=partner_id,
        type_=type_,
        source_type=source_type,
        source_id=source_id,
        amount_min=amount_min,
        amount_max=amount_max,
        date_start=date_start,
        date_end=date_end,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    partner_id: Union[Unset, str] = UNSET,
    type_: Union[Unset, GetAllFinanceTransactionsType] = UNSET,
    source_type: Union[Unset, GetAllFinanceTransactionsSourceType] = UNSET,
    source_id: Union[Unset, str] = UNSET,
    amount_min: Union[Unset, float] = UNSET,
    amount_max: Union[Unset, float] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[GetAllFinanceTransactionsResponse200]:
    """Get all finance transactions


    Retrieve all finance transactions with comprehensive filtering capabilities for financial analysis
    and reporting.

    **Core Features**:
    - **Advanced Filtering**: Filter by partner, transaction type, source type, amount ranges, and date
    ranges
    - **Full-Text Search**: Search within transaction metadata for flexible querying
    - **Paginated Results**: Cursor-based pagination for efficient data retrieval
    - **Financial Analytics**: Support for business intelligence and reporting needs

    **Use Cases**:
    - **Financial Reporting**: Generate comprehensive transaction reports with filtering
    - **Cash Flow Analysis**: Track payment patterns and transaction volumes
    - **Partner Analytics**: Analyze transaction history by business partner
    - **Audit Trails**: Review transaction history for compliance and auditing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        type_ (Union[Unset, GetAllFinanceTransactionsType]):  Example: payment_in.
        source_type (Union[Unset, GetAllFinanceTransactionsSourceType]):  Example: invoice.
        source_id (Union[Unset, str]):  Example: INV_507f1f77bcf86cd799439014.
        amount_min (Union[Unset, float]):  Example: 100.
        amount_max (Union[Unset, float]):  Example: 5000.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        search (Union[Unset, str]):  Example: ACH payment.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439015.
        limit (Union[Unset, int]):  Default: 20. Example: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllFinanceTransactionsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            partner_id=partner_id,
            type_=type_,
            source_type=source_type,
            source_id=source_id,
            amount_min=amount_min,
            amount_max=amount_max,
            date_start=date_start,
            date_end=date_end,
            search=search,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
