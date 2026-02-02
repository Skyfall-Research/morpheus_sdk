import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_erp_orders_response_200 import GetAllERPOrdersResponse200
from ...models.get_all_erp_orders_status import GetAllERPOrdersStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, GetAllERPOrdersStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    orderdate_start: Union[Unset, datetime.date] = UNSET,
    orderdate_end: Union[Unset, datetime.date] = UNSET,
    requesteddate_start: Union[Unset, datetime.date] = UNSET,
    requesteddate_end: Union[Unset, datetime.date] = UNSET,
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

    params["orderId"] = order_id

    json_orderdate_start: Union[Unset, str] = UNSET
    if not isinstance(orderdate_start, Unset):
        json_orderdate_start = orderdate_start.isoformat()
    params["orderdateStart"] = json_orderdate_start

    json_orderdate_end: Union[Unset, str] = UNSET
    if not isinstance(orderdate_end, Unset):
        json_orderdate_end = orderdate_end.isoformat()
    params["orderdateEnd"] = json_orderdate_end

    json_requesteddate_start: Union[Unset, str] = UNSET
    if not isinstance(requesteddate_start, Unset):
        json_requesteddate_start = requesteddate_start.isoformat()
    params["requesteddateStart"] = json_requesteddate_start

    json_requesteddate_end: Union[Unset, str] = UNSET
    if not isinstance(requesteddate_end, Unset):
        json_requesteddate_end = requesteddate_end.isoformat()
    params["requesteddateEnd"] = json_requesteddate_end

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllERPOrdersResponse200]:
    if response.status_code == 200:
        response_200 = GetAllERPOrdersResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllERPOrdersResponse200]:
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
    status: Union[Unset, GetAllERPOrdersStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    orderdate_start: Union[Unset, datetime.date] = UNSET,
    orderdate_end: Union[Unset, datetime.date] = UNSET,
    requesteddate_start: Union[Unset, datetime.date] = UNSET,
    requesteddate_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPOrdersResponse200]:
    """Get all ERP orders


    Retrieve all ERP orders with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, order date ranges
    - **Date Range Support**: Filter orders by order date and requested date ranges
    - **Customer/Partner Filtering**: Search orders by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Order Data**: Returns full order profiles with line items

    **Use Cases**:
    - **Order Management**: Browse and manage customer orders
    - **Financial Reporting**: Filter orders by date ranges for financial analysis
    - **Customer Service**: Search orders by customer for support inquiries
    - **Business Intelligence**: Analyze order patterns and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPOrdersStatus]):  Example: IN_PROGRESS.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439014.
        order_id (Union[Unset, str]):  Example: ORDER_507f1f77bcf86cd799439012.
        orderdate_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        orderdate_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        requesteddate_start (Union[Unset, datetime.date]):  Example: 2024-01-15.
        requesteddate_end (Union[Unset, datetime.date]):  Example: 2024-02-15.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPOrdersResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        order_id=order_id,
        orderdate_start=orderdate_start,
        orderdate_end=orderdate_end,
        requesteddate_start=requesteddate_start,
        requesteddate_end=requesteddate_end,
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
    status: Union[Unset, GetAllERPOrdersStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    orderdate_start: Union[Unset, datetime.date] = UNSET,
    orderdate_end: Union[Unset, datetime.date] = UNSET,
    requesteddate_start: Union[Unset, datetime.date] = UNSET,
    requesteddate_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPOrdersResponse200]:
    """Get all ERP orders


    Retrieve all ERP orders with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, order date ranges
    - **Date Range Support**: Filter orders by order date and requested date ranges
    - **Customer/Partner Filtering**: Search orders by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Order Data**: Returns full order profiles with line items

    **Use Cases**:
    - **Order Management**: Browse and manage customer orders
    - **Financial Reporting**: Filter orders by date ranges for financial analysis
    - **Customer Service**: Search orders by customer for support inquiries
    - **Business Intelligence**: Analyze order patterns and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPOrdersStatus]):  Example: IN_PROGRESS.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439014.
        order_id (Union[Unset, str]):  Example: ORDER_507f1f77bcf86cd799439012.
        orderdate_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        orderdate_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        requesteddate_start (Union[Unset, datetime.date]):  Example: 2024-01-15.
        requesteddate_end (Union[Unset, datetime.date]):  Example: 2024-02-15.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPOrdersResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        order_id=order_id,
        orderdate_start=orderdate_start,
        orderdate_end=orderdate_end,
        requesteddate_start=requesteddate_start,
        requesteddate_end=requesteddate_end,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPOrdersStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    orderdate_start: Union[Unset, datetime.date] = UNSET,
    orderdate_end: Union[Unset, datetime.date] = UNSET,
    requesteddate_start: Union[Unset, datetime.date] = UNSET,
    requesteddate_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPOrdersResponse200]:
    """Get all ERP orders


    Retrieve all ERP orders with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, order date ranges
    - **Date Range Support**: Filter orders by order date and requested date ranges
    - **Customer/Partner Filtering**: Search orders by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Order Data**: Returns full order profiles with line items

    **Use Cases**:
    - **Order Management**: Browse and manage customer orders
    - **Financial Reporting**: Filter orders by date ranges for financial analysis
    - **Customer Service**: Search orders by customer for support inquiries
    - **Business Intelligence**: Analyze order patterns and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPOrdersStatus]):  Example: IN_PROGRESS.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439014.
        order_id (Union[Unset, str]):  Example: ORDER_507f1f77bcf86cd799439012.
        orderdate_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        orderdate_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        requesteddate_start (Union[Unset, datetime.date]):  Example: 2024-01-15.
        requesteddate_end (Union[Unset, datetime.date]):  Example: 2024-02-15.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPOrdersResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        customer_id=customer_id,
        partner_id=partner_id,
        order_id=order_id,
        orderdate_start=orderdate_start,
        orderdate_end=orderdate_end,
        requesteddate_start=requesteddate_start,
        requesteddate_end=requesteddate_end,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPOrdersStatus] = UNSET,
    customer_id: Union[Unset, str] = UNSET,
    partner_id: Union[Unset, str] = UNSET,
    order_id: Union[Unset, str] = UNSET,
    orderdate_start: Union[Unset, datetime.date] = UNSET,
    orderdate_end: Union[Unset, datetime.date] = UNSET,
    requesteddate_start: Union[Unset, datetime.date] = UNSET,
    requesteddate_end: Union[Unset, datetime.date] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPOrdersResponse200]:
    """Get all ERP orders


    Retrieve all ERP orders with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, customer, partner, order date ranges
    - **Date Range Support**: Filter orders by order date and requested date ranges
    - **Customer/Partner Filtering**: Search orders by business relationships
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Order Data**: Returns full order profiles with line items

    **Use Cases**:
    - **Order Management**: Browse and manage customer orders
    - **Financial Reporting**: Filter orders by date ranges for financial analysis
    - **Customer Service**: Search orders by customer for support inquiries
    - **Business Intelligence**: Analyze order patterns and trends


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPOrdersStatus]):  Example: IN_PROGRESS.
        customer_id (Union[Unset, str]):  Example: CUST_507f1f77bcf86cd799439013.
        partner_id (Union[Unset, str]):  Example: PARTNER_507f1f77bcf86cd799439014.
        order_id (Union[Unset, str]):  Example: ORDER_507f1f77bcf86cd799439012.
        orderdate_start (Union[Unset, datetime.date]):  Example: 2024-01-01.
        orderdate_end (Union[Unset, datetime.date]):  Example: 2024-01-31.
        requesteddate_start (Union[Unset, datetime.date]):  Example: 2024-01-15.
        requesteddate_end (Union[Unset, datetime.date]):  Example: 2024-02-15.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPOrdersResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            customer_id=customer_id,
            partner_id=partner_id,
            order_id=order_id,
            orderdate_start=orderdate_start,
            orderdate_end=orderdate_end,
            requesteddate_start=requesteddate_start,
            requesteddate_end=requesteddate_end,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
