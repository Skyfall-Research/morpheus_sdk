from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_product_by_id_response_200 import GetERPProductByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    product_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/products/{product_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPProductByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPProductByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetERPProductByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPProductByIdResponse200]]:
    """Get ERP product by ID


    Retrieve specific ERP product by product identifier for detailed product information access.

    **Core Features**:
    - **Direct Access**: Get product by unique productId identifier
    - **Complete Profile**: Returns full product data including pricing and specifications
    - **Fast Lookup**: Optimized query using indexed productId field
    - **Product Intelligence**: Access comprehensive product data for business operations

    **Use Cases**:
    - **Product Details**: Get complete product information for catalog operations
    - **Inventory Reference**: Resolve product references from inventory and orders
    - **Pricing Lookup**: Access current product pricing for sales operations
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPProductByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        product_id=product_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPProductByIdResponse200]]:
    """Get ERP product by ID


    Retrieve specific ERP product by product identifier for detailed product information access.

    **Core Features**:
    - **Direct Access**: Get product by unique productId identifier
    - **Complete Profile**: Returns full product data including pricing and specifications
    - **Fast Lookup**: Optimized query using indexed productId field
    - **Product Intelligence**: Access comprehensive product data for business operations

    **Use Cases**:
    - **Product Details**: Get complete product information for catalog operations
    - **Inventory Reference**: Resolve product references from inventory and orders
    - **Pricing Lookup**: Access current product pricing for sales operations
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPProductByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        product_id=product_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPProductByIdResponse200]]:
    """Get ERP product by ID


    Retrieve specific ERP product by product identifier for detailed product information access.

    **Core Features**:
    - **Direct Access**: Get product by unique productId identifier
    - **Complete Profile**: Returns full product data including pricing and specifications
    - **Fast Lookup**: Optimized query using indexed productId field
    - **Product Intelligence**: Access comprehensive product data for business operations

    **Use Cases**:
    - **Product Details**: Get complete product information for catalog operations
    - **Inventory Reference**: Resolve product references from inventory and orders
    - **Pricing Lookup**: Access current product pricing for sales operations
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPProductByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        product_id=product_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPProductByIdResponse200]]:
    """Get ERP product by ID


    Retrieve specific ERP product by product identifier for detailed product information access.

    **Core Features**:
    - **Direct Access**: Get product by unique productId identifier
    - **Complete Profile**: Returns full product data including pricing and specifications
    - **Fast Lookup**: Optimized query using indexed productId field
    - **Product Intelligence**: Access comprehensive product data for business operations

    **Use Cases**:
    - **Product Details**: Get complete product information for catalog operations
    - **Inventory Reference**: Resolve product references from inventory and orders
    - **Pricing Lookup**: Access current product pricing for sales operations
    - **Integration Support**: Direct API access for external system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPProductByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            product_id=product_id,
            client=client,
        )
    ).parsed
