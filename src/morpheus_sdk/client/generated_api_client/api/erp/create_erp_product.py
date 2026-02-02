from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_erp_product_body import CreateERPProductBody
from ...models.create_erp_product_response_201 import CreateERPProductResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateERPProductBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/products",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateERPProductResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateERPProductResponse201.from_dict(response.json())

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
) -> Response[Union[CreateERPProductResponse201, ErrorResponse]]:
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
    body: CreateERPProductBody,
) -> Response[Union[CreateERPProductResponse201, ErrorResponse]]:
    """Create new ERP product


    Create a new ERP product record with comprehensive product information and operational
    configuration.

    **Core Features**:
    - **Product Registration**: Complete product setup with identification, pricing, and inventory
    details
    - **Auto-Generated IDs**: Automatic productId generation via generateIdByService
    - **Multi-Standard Support**: UPC and EAN barcode support for retail integration
    - **Inventory Management**: Configurable inventory tracking with dimensions and weight
    - **Pricing Configuration**: Currency-based pricing with cost tracking

    **Use Cases**:
    - **Product Catalog Setup**: Create comprehensive product catalogs for ERP integration
    - **Inventory Management**: Register products for warehouse and inventory tracking
    - **Pricing Management**: Set up product pricing for sales and financial operations
    - **Retail Integration**: Support retail operations with barcode and SKU management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPProductResponse201, ErrorResponse]]
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
    body: CreateERPProductBody,
) -> Optional[Union[CreateERPProductResponse201, ErrorResponse]]:
    """Create new ERP product


    Create a new ERP product record with comprehensive product information and operational
    configuration.

    **Core Features**:
    - **Product Registration**: Complete product setup with identification, pricing, and inventory
    details
    - **Auto-Generated IDs**: Automatic productId generation via generateIdByService
    - **Multi-Standard Support**: UPC and EAN barcode support for retail integration
    - **Inventory Management**: Configurable inventory tracking with dimensions and weight
    - **Pricing Configuration**: Currency-based pricing with cost tracking

    **Use Cases**:
    - **Product Catalog Setup**: Create comprehensive product catalogs for ERP integration
    - **Inventory Management**: Register products for warehouse and inventory tracking
    - **Pricing Management**: Set up product pricing for sales and financial operations
    - **Retail Integration**: Support retail operations with barcode and SKU management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPProductResponse201, ErrorResponse]
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
    body: CreateERPProductBody,
) -> Response[Union[CreateERPProductResponse201, ErrorResponse]]:
    """Create new ERP product


    Create a new ERP product record with comprehensive product information and operational
    configuration.

    **Core Features**:
    - **Product Registration**: Complete product setup with identification, pricing, and inventory
    details
    - **Auto-Generated IDs**: Automatic productId generation via generateIdByService
    - **Multi-Standard Support**: UPC and EAN barcode support for retail integration
    - **Inventory Management**: Configurable inventory tracking with dimensions and weight
    - **Pricing Configuration**: Currency-based pricing with cost tracking

    **Use Cases**:
    - **Product Catalog Setup**: Create comprehensive product catalogs for ERP integration
    - **Inventory Management**: Register products for warehouse and inventory tracking
    - **Pricing Management**: Set up product pricing for sales and financial operations
    - **Retail Integration**: Support retail operations with barcode and SKU management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPProductResponse201, ErrorResponse]]
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
    body: CreateERPProductBody,
) -> Optional[Union[CreateERPProductResponse201, ErrorResponse]]:
    """Create new ERP product


    Create a new ERP product record with comprehensive product information and operational
    configuration.

    **Core Features**:
    - **Product Registration**: Complete product setup with identification, pricing, and inventory
    details
    - **Auto-Generated IDs**: Automatic productId generation via generateIdByService
    - **Multi-Standard Support**: UPC and EAN barcode support for retail integration
    - **Inventory Management**: Configurable inventory tracking with dimensions and weight
    - **Pricing Configuration**: Currency-based pricing with cost tracking

    **Use Cases**:
    - **Product Catalog Setup**: Create comprehensive product catalogs for ERP integration
    - **Inventory Management**: Register products for warehouse and inventory tracking
    - **Pricing Management**: Set up product pricing for sales and financial operations
    - **Retail Integration**: Support retail operations with barcode and SKU management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPProductResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
