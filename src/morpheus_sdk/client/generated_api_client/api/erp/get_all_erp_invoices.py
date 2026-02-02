import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_erp_invoices_response_200 import GetAllERPInvoicesResponse200
from ...models.get_all_erp_invoices_status import GetAllERPInvoicesStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, GetAllERPInvoicesStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["customerId"] = customer_id

    params["partnerId"] = partner_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/invoices",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllERPInvoicesResponse200]:
    if response.status_code == 200:
        response_200 = GetAllERPInvoicesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllERPInvoicesResponse200]:
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
    status: Union[Unset, GetAllERPInvoicesStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPInvoicesResponse200]:
    """Get all ERP invoices


    Retrieve all ERP invoices with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and date ranges
    - **Date Range Support**: Filter invoices by issue date for financial reporting
    - **Customer/Partner Filtering**: Search invoices by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Financial Data**: Returns complete invoice data with line items and totals

    **Use Cases**:
    - **Accounts Receivable**: Manage outstanding invoices and payments
    - **Financial Reporting**: Filter invoices by date ranges for financial analysis
    - **Customer Service**: Search invoices by customer for support inquiries
    - **Business Intelligence**: Analyze invoice patterns and revenue trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPInvoicesStatus]):  Example: SENT.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPInvoicesResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        date_start=date_start,
        date_end=date_end,
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
    status: Union[Unset, GetAllERPInvoicesStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPInvoicesResponse200]:
    """Get all ERP invoices


    Retrieve all ERP invoices with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and date ranges
    - **Date Range Support**: Filter invoices by issue date for financial reporting
    - **Customer/Partner Filtering**: Search invoices by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Financial Data**: Returns complete invoice data with line items and totals

    **Use Cases**:
    - **Accounts Receivable**: Manage outstanding invoices and payments
    - **Financial Reporting**: Filter invoices by date ranges for financial analysis
    - **Customer Service**: Search invoices by customer for support inquiries
    - **Business Intelligence**: Analyze invoice patterns and revenue trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPInvoicesStatus]):  Example: SENT.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPInvoicesResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPInvoicesStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPInvoicesResponse200]:
    """Get all ERP invoices


    Retrieve all ERP invoices with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and date ranges
    - **Date Range Support**: Filter invoices by issue date for financial reporting
    - **Customer/Partner Filtering**: Search invoices by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Financial Data**: Returns complete invoice data with line items and totals

    **Use Cases**:
    - **Accounts Receivable**: Manage outstanding invoices and payments
    - **Financial Reporting**: Filter invoices by date ranges for financial analysis
    - **Customer Service**: Search invoices by customer for support inquiries
    - **Business Intelligence**: Analyze invoice patterns and revenue trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPInvoicesStatus]):  Example: SENT.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPInvoicesResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPInvoicesStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPInvoicesResponse200]:
    """Get all ERP invoices


    Retrieve all ERP invoices with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and date ranges
    - **Date Range Support**: Filter invoices by issue date for financial reporting
    - **Customer/Partner Filtering**: Search invoices by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Financial Data**: Returns complete invoice data with line items and totals

    **Use Cases**:
    - **Accounts Receivable**: Manage outstanding invoices and payments
    - **Financial Reporting**: Filter invoices by date ranges for financial analysis
    - **Customer Service**: Search invoices by customer for support inquiries
    - **Business Intelligence**: Analyze invoice patterns and revenue trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPInvoicesStatus]):  Example: SENT.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPInvoicesResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            customer_id=customer_id,
            partner_id=partner_id,
            date_start=date_start,
            date_end=date_end,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
