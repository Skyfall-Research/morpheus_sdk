from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_order_by_id_response_200 import GetERPOrderByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/orders/{order_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPOrderByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPOrderByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetERPOrderByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPOrderByIdResponse200]]:
    """Get ERP order by ID


    Retrieve specific ERP order by order identifier for detailed order information access.

    **Core Features**:
    - **Direct Access**: Get order by unique orderId identifier
    - **Complete Profile**: Returns full order data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed orderId field
    - **Business Intelligence**: Access comprehensive order data for operations

    **Use Cases**:
    - **Order Details**: Get complete order information for business operations
    - **Customer Service**: Resolve order inquiries using order ID references
    - **Financial Operations**: Access order details for financial processing
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPOrderByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPOrderByIdResponse200]]:
    """Get ERP order by ID


    Retrieve specific ERP order by order identifier for detailed order information access.

    **Core Features**:
    - **Direct Access**: Get order by unique orderId identifier
    - **Complete Profile**: Returns full order data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed orderId field
    - **Business Intelligence**: Access comprehensive order data for operations

    **Use Cases**:
    - **Order Details**: Get complete order information for business operations
    - **Customer Service**: Resolve order inquiries using order ID references
    - **Financial Operations**: Access order details for financial processing
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPOrderByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        order_id=order_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPOrderByIdResponse200]]:
    """Get ERP order by ID


    Retrieve specific ERP order by order identifier for detailed order information access.

    **Core Features**:
    - **Direct Access**: Get order by unique orderId identifier
    - **Complete Profile**: Returns full order data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed orderId field
    - **Business Intelligence**: Access comprehensive order data for operations

    **Use Cases**:
    - **Order Details**: Get complete order information for business operations
    - **Customer Service**: Resolve order inquiries using order ID references
    - **Financial Operations**: Access order details for financial processing
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPOrderByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPOrderByIdResponse200]]:
    """Get ERP order by ID


    Retrieve specific ERP order by order identifier for detailed order information access.

    **Core Features**:
    - **Direct Access**: Get order by unique orderId identifier
    - **Complete Profile**: Returns full order data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed orderId field
    - **Business Intelligence**: Access comprehensive order data for operations

    **Use Cases**:
    - **Order Details**: Get complete order information for business operations
    - **Customer Service**: Resolve order inquiries using order ID references
    - **Financial Operations**: Access order details for financial processing
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPOrderByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
        )
    ).parsed
