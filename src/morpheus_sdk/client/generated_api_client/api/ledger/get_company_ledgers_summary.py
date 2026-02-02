from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_company_ledgers_summary_response_200 import GetCompanyLedgersSummaryResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/ledger/analytics/summary",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetCompanyLedgersSummaryResponse200]:
    if response.status_code == 200:
        response_200 = GetCompanyLedgersSummaryResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetCompanyLedgersSummaryResponse200]:
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
) -> Response[GetCompanyLedgersSummaryResponse200]:
    """Get company ledger analytics summary


    Retrieve comprehensive analytics summary for company ledger with aggregated financial metrics.

    **Core Features**:
    - **Aggregated Metrics**: Total cash, receivables, payables, and net position across all ledgers
    - **Distribution Analytics**: Count of positive vs negative net position ledgers
    - **Financial Intelligence**: Key performance indicators for financial analysis
    - **Business Intelligence**: High-level financial overview for executive dashboards

    **Use Cases**:
    - **Executive Dashboards**: Provide high-level financial metrics for leadership
    - **Financial Reporting**: Generate summary reports for financial analysis
    - **Performance Monitoring**: Track overall financial health and position
    - **Business Intelligence**: Support data-driven financial decision making

    **Analytics Include**:
    - **totalCash**: Aggregate cash position
    - **totalReceivables**: Total outstanding receivables
    - **totalPayables**: Total outstanding payables
    - **totalNetPosition**: Overall net financial position
    - **ledgerCount**: Total number of ledgers
    - **positiveLedgers**: Count of ledgers with positive net position
    - **negativeLedgers**: Count of ledgers with negative net position


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompanyLedgersSummaryResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetCompanyLedgersSummaryResponse200]:
    """Get company ledger analytics summary


    Retrieve comprehensive analytics summary for company ledger with aggregated financial metrics.

    **Core Features**:
    - **Aggregated Metrics**: Total cash, receivables, payables, and net position across all ledgers
    - **Distribution Analytics**: Count of positive vs negative net position ledgers
    - **Financial Intelligence**: Key performance indicators for financial analysis
    - **Business Intelligence**: High-level financial overview for executive dashboards

    **Use Cases**:
    - **Executive Dashboards**: Provide high-level financial metrics for leadership
    - **Financial Reporting**: Generate summary reports for financial analysis
    - **Performance Monitoring**: Track overall financial health and position
    - **Business Intelligence**: Support data-driven financial decision making

    **Analytics Include**:
    - **totalCash**: Aggregate cash position
    - **totalReceivables**: Total outstanding receivables
    - **totalPayables**: Total outstanding payables
    - **totalNetPosition**: Overall net financial position
    - **ledgerCount**: Total number of ledgers
    - **positiveLedgers**: Count of ledgers with positive net position
    - **negativeLedgers**: Count of ledgers with negative net position


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompanyLedgersSummaryResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[GetCompanyLedgersSummaryResponse200]:
    """Get company ledger analytics summary


    Retrieve comprehensive analytics summary for company ledger with aggregated financial metrics.

    **Core Features**:
    - **Aggregated Metrics**: Total cash, receivables, payables, and net position across all ledgers
    - **Distribution Analytics**: Count of positive vs negative net position ledgers
    - **Financial Intelligence**: Key performance indicators for financial analysis
    - **Business Intelligence**: High-level financial overview for executive dashboards

    **Use Cases**:
    - **Executive Dashboards**: Provide high-level financial metrics for leadership
    - **Financial Reporting**: Generate summary reports for financial analysis
    - **Performance Monitoring**: Track overall financial health and position
    - **Business Intelligence**: Support data-driven financial decision making

    **Analytics Include**:
    - **totalCash**: Aggregate cash position
    - **totalReceivables**: Total outstanding receivables
    - **totalPayables**: Total outstanding payables
    - **totalNetPosition**: Overall net financial position
    - **ledgerCount**: Total number of ledgers
    - **positiveLedgers**: Count of ledgers with positive net position
    - **negativeLedgers**: Count of ledgers with negative net position


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetCompanyLedgersSummaryResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[GetCompanyLedgersSummaryResponse200]:
    """Get company ledger analytics summary


    Retrieve comprehensive analytics summary for company ledger with aggregated financial metrics.

    **Core Features**:
    - **Aggregated Metrics**: Total cash, receivables, payables, and net position across all ledgers
    - **Distribution Analytics**: Count of positive vs negative net position ledgers
    - **Financial Intelligence**: Key performance indicators for financial analysis
    - **Business Intelligence**: High-level financial overview for executive dashboards

    **Use Cases**:
    - **Executive Dashboards**: Provide high-level financial metrics for leadership
    - **Financial Reporting**: Generate summary reports for financial analysis
    - **Performance Monitoring**: Track overall financial health and position
    - **Business Intelligence**: Support data-driven financial decision making

    **Analytics Include**:
    - **totalCash**: Aggregate cash position
    - **totalReceivables**: Total outstanding receivables
    - **totalPayables**: Total outstanding payables
    - **totalNetPosition**: Overall net financial position
    - **ledgerCount**: Total number of ledgers
    - **positiveLedgers**: Count of ledgers with positive net position
    - **negativeLedgers**: Count of ledgers with negative net position


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetCompanyLedgersSummaryResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
