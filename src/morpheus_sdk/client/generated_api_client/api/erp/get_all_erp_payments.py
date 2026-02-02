import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_erp_payments_response_200 import GetAllERPPaymentsResponse200
from ...models.get_all_erp_payments_status import GetAllERPPaymentsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, GetAllERPPaymentsStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
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

    params["productId"] = product_id

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
        "url": f"/{world_id}/erp/payments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllERPPaymentsResponse200]:
    if response.status_code == 200:
        response_200 = GetAllERPPaymentsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllERPPaymentsResponse200]:
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
    status: Union[Unset, GetAllERPPaymentsStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPPaymentsResponse200]:
    """Get all ERP payments


    Retrieve all ERP payments with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and payment date ranges
    - **Date Range Support**: Filter payments by payment date for financial reporting
    - **Customer/Partner Filtering**: Search payments by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Financial Data**: Returns full payment profiles with allocation details

    **Use Cases**:
    - **Accounts Receivable**: Browse and manage customer payments
    - **Financial Reporting**: Filter payments by date ranges for cash flow analysis
    - **Customer Service**: Search payments by customer for account inquiries
    - **Business Intelligence**: Analyze payment patterns and cash collection trends

    **🔴 Critical Filter Bug**: Repository filters by 'productId' using non-existent
    'appliedProducts.productId' field!


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPPaymentsStatus]):  Example: APPLIED.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        product_id (Union[Unset, str]):  Example: PROD_WIDGET_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPPaymentsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        product_id=product_id,
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
    status: Union[Unset, GetAllERPPaymentsStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPPaymentsResponse200]:
    """Get all ERP payments


    Retrieve all ERP payments with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and payment date ranges
    - **Date Range Support**: Filter payments by payment date for financial reporting
    - **Customer/Partner Filtering**: Search payments by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Financial Data**: Returns full payment profiles with allocation details

    **Use Cases**:
    - **Accounts Receivable**: Browse and manage customer payments
    - **Financial Reporting**: Filter payments by date ranges for cash flow analysis
    - **Customer Service**: Search payments by customer for account inquiries
    - **Business Intelligence**: Analyze payment patterns and cash collection trends

    **🔴 Critical Filter Bug**: Repository filters by 'productId' using non-existent
    'appliedProducts.productId' field!


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPPaymentsStatus]):  Example: APPLIED.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        product_id (Union[Unset, str]):  Example: PROD_WIDGET_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPPaymentsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        product_id=product_id,
        date_start=date_start,
        date_end=date_end,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPPaymentsStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPPaymentsResponse200]:
    """Get all ERP payments


    Retrieve all ERP payments with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and payment date ranges
    - **Date Range Support**: Filter payments by payment date for financial reporting
    - **Customer/Partner Filtering**: Search payments by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Financial Data**: Returns full payment profiles with allocation details

    **Use Cases**:
    - **Accounts Receivable**: Browse and manage customer payments
    - **Financial Reporting**: Filter payments by date ranges for cash flow analysis
    - **Customer Service**: Search payments by customer for account inquiries
    - **Business Intelligence**: Analyze payment patterns and cash collection trends

    **🔴 Critical Filter Bug**: Repository filters by 'productId' using non-existent
    'appliedProducts.productId' field!


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPPaymentsStatus]):  Example: APPLIED.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        product_id (Union[Unset, str]):  Example: PROD_WIDGET_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPPaymentsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        product_id=product_id,
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
    status: Union[Unset, GetAllERPPaymentsStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    product_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.date] = UNSET,
    date_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPPaymentsResponse200]:
    """Get all ERP payments


    Retrieve all ERP payments with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, and payment date ranges
    - **Date Range Support**: Filter payments by payment date for financial reporting
    - **Customer/Partner Filtering**: Search payments by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Financial Data**: Returns full payment profiles with allocation details

    **Use Cases**:
    - **Accounts Receivable**: Browse and manage customer payments
    - **Financial Reporting**: Filter payments by date ranges for cash flow analysis
    - **Customer Service**: Search payments by customer for account inquiries
    - **Business Intelligence**: Analyze payment patterns and cash collection trends

    **🔴 Critical Filter Bug**: Repository filters by 'productId' using non-existent
    'appliedProducts.productId' field!


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPPaymentsStatus]):  Example: APPLIED.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439014.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439015.
        product_id (Union[Unset, str]):  Example: PROD_WIDGET_001.
        date_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        date_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPPaymentsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            customer_id=customer_id,
            partner_id=partner_id,
            product_id=product_id,
            date_start=date_start,
            date_end=date_end,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
