from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_erp_order_body import CreateERPOrderBody
from ...models.create_erp_order_response_201 import CreateERPOrderResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateERPOrderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/orders",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateERPOrderResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateERPOrderResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateERPOrderResponse201, ErrorResponse]]:
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
    body: CreateERPOrderBody,
) -> Response[Union[CreateERPOrderResponse201, ErrorResponse]]:
    """Create new ERP purchase order


    Create a new ERP purchase order with comprehensive order information and line item details.

    **Core Features**:
    - **Purchase Order Creation**: Complete B2B order setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic orderId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and scheduling
    - **Financial Calculations**: Automatic subtotal, tax, and total calculations
    - **Status Workflow**: Complete order lifecycle management from received to completed

    **Use Cases**:
    - **B2B Commerce**: Create purchase orders for customer and partner transactions
    - **Supply Chain Management**: Order products and materials from suppliers
    - **Financial Management**: Track order values and payment obligations
    - **Inventory Planning**: Generate purchase orders for inventory replenishment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPOrderResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateERPOrderBody,
) -> Optional[Union[CreateERPOrderResponse201, ErrorResponse]]:
    """Create new ERP purchase order


    Create a new ERP purchase order with comprehensive order information and line item details.

    **Core Features**:
    - **Purchase Order Creation**: Complete B2B order setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic orderId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and scheduling
    - **Financial Calculations**: Automatic subtotal, tax, and total calculations
    - **Status Workflow**: Complete order lifecycle management from received to completed

    **Use Cases**:
    - **B2B Commerce**: Create purchase orders for customer and partner transactions
    - **Supply Chain Management**: Order products and materials from suppliers
    - **Financial Management**: Track order values and payment obligations
    - **Inventory Planning**: Generate purchase orders for inventory replenishment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPOrderResponse201, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateERPOrderBody,
) -> Response[Union[CreateERPOrderResponse201, ErrorResponse]]:
    """Create new ERP purchase order


    Create a new ERP purchase order with comprehensive order information and line item details.

    **Core Features**:
    - **Purchase Order Creation**: Complete B2B order setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic orderId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and scheduling
    - **Financial Calculations**: Automatic subtotal, tax, and total calculations
    - **Status Workflow**: Complete order lifecycle management from received to completed

    **Use Cases**:
    - **B2B Commerce**: Create purchase orders for customer and partner transactions
    - **Supply Chain Management**: Order products and materials from suppliers
    - **Financial Management**: Track order values and payment obligations
    - **Inventory Planning**: Generate purchase orders for inventory replenishment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPOrderResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateERPOrderBody,
) -> Optional[Union[CreateERPOrderResponse201, ErrorResponse]]:
    """Create new ERP purchase order


    Create a new ERP purchase order with comprehensive order information and line item details.

    **Core Features**:
    - **Purchase Order Creation**: Complete B2B order setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic orderId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and scheduling
    - **Financial Calculations**: Automatic subtotal, tax, and total calculations
    - **Status Workflow**: Complete order lifecycle management from received to completed

    **Use Cases**:
    - **B2B Commerce**: Create purchase orders for customer and partner transactions
    - **Supply Chain Management**: Order products and materials from suppliers
    - **Financial Management**: Track order values and payment obligations
    - **Inventory Planning**: Generate purchase orders for inventory replenishment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPOrderResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
