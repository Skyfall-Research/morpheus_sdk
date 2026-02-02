import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_financial_summary_response_200 import GetFinancialSummaryResponse200
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
        "url": f"/{world_id}/finance/summary",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetFinancialSummaryResponse200]:
    if response.status_code == 200:
        response_200 = GetFinancialSummaryResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetFinancialSummaryResponse200]:
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
) -> Response[GetFinancialSummaryResponse200]:
    """Get financial summary


    Retrieve comprehensive financial summary with incoming, outgoing, and net balance calculations.

    **Core Features**:
    - **Financial Overview**: Complete financial position with incoming, outgoing, and net balance
    - **Transaction Metrics**: Transaction count and average transaction amounts
    - **Partner Filtering**: Focus summary on specific business partners
    - **Date Range Analysis**: Analyze financial position for specific time periods

    **Use Cases**:
    - **Financial Position**: Get current financial standing and cash flow position
    - **Management Reporting**: Generate executive summaries for financial review
    - **Cash Flow Analysis**: Understand cash inflows, outflows, and net position
    - **Performance Metrics**: Track average transaction values and volumes

    **Summary Calculations**:
    - **totalIncoming**: Sum of all payment_in transactions
    - **totalOutgoing**: Sum of all payment_out transactions
    - **netBalance**: Difference between incoming and outgoing (incoming - outgoing)
    - **avgTransactionAmount**: Average amount across all transactions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFinancialSummaryResponse200]
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
) -> Optional[GetFinancialSummaryResponse200]:
    """Get financial summary


    Retrieve comprehensive financial summary with incoming, outgoing, and net balance calculations.

    **Core Features**:
    - **Financial Overview**: Complete financial position with incoming, outgoing, and net balance
    - **Transaction Metrics**: Transaction count and average transaction amounts
    - **Partner Filtering**: Focus summary on specific business partners
    - **Date Range Analysis**: Analyze financial position for specific time periods

    **Use Cases**:
    - **Financial Position**: Get current financial standing and cash flow position
    - **Management Reporting**: Generate executive summaries for financial review
    - **Cash Flow Analysis**: Understand cash inflows, outflows, and net position
    - **Performance Metrics**: Track average transaction values and volumes

    **Summary Calculations**:
    - **totalIncoming**: Sum of all payment_in transactions
    - **totalOutgoing**: Sum of all payment_out transactions
    - **netBalance**: Difference between incoming and outgoing (incoming - outgoing)
    - **avgTransactionAmount**: Average amount across all transactions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFinancialSummaryResponse200
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
) -> Response[GetFinancialSummaryResponse200]:
    """Get financial summary


    Retrieve comprehensive financial summary with incoming, outgoing, and net balance calculations.

    **Core Features**:
    - **Financial Overview**: Complete financial position with incoming, outgoing, and net balance
    - **Transaction Metrics**: Transaction count and average transaction amounts
    - **Partner Filtering**: Focus summary on specific business partners
    - **Date Range Analysis**: Analyze financial position for specific time periods

    **Use Cases**:
    - **Financial Position**: Get current financial standing and cash flow position
    - **Management Reporting**: Generate executive summaries for financial review
    - **Cash Flow Analysis**: Understand cash inflows, outflows, and net position
    - **Performance Metrics**: Track average transaction values and volumes

    **Summary Calculations**:
    - **totalIncoming**: Sum of all payment_in transactions
    - **totalOutgoing**: Sum of all payment_out transactions
    - **netBalance**: Difference between incoming and outgoing (incoming - outgoing)
    - **avgTransactionAmount**: Average amount across all transactions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetFinancialSummaryResponse200]
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
) -> Optional[GetFinancialSummaryResponse200]:
    """Get financial summary


    Retrieve comprehensive financial summary with incoming, outgoing, and net balance calculations.

    **Core Features**:
    - **Financial Overview**: Complete financial position with incoming, outgoing, and net balance
    - **Transaction Metrics**: Transaction count and average transaction amounts
    - **Partner Filtering**: Focus summary on specific business partners
    - **Date Range Analysis**: Analyze financial position for specific time periods

    **Use Cases**:
    - **Financial Position**: Get current financial standing and cash flow position
    - **Management Reporting**: Generate executive summaries for financial review
    - **Cash Flow Analysis**: Understand cash inflows, outflows, and net position
    - **Performance Metrics**: Track average transaction values and volumes

    **Summary Calculations**:
    - **totalIncoming**: Sum of all payment_in transactions
    - **totalOutgoing**: Sum of all payment_out transactions
    - **netBalance**: Difference between incoming and outgoing (incoming - outgoing)
    - **avgTransactionAmount**: Average amount across all transactions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439013.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetFinancialSummaryResponse200
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
