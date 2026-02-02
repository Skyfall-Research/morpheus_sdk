from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_product_body import UpdateERPProductBody
from ...models.update_erp_product_response_200 import UpdateERPProductResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    product_id: str,
    *,
    body: UpdateERPProductBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/products/{product_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPProductResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPProductResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPProductResponse200]]:
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
    body: UpdateERPProductBody,
) -> Response[Union[ErrorResponse, UpdateERPProductResponse200]]:
    """Update ERP product


    Update ERP product information with partial data for product catalog maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific product fields without replacing entire record
    - **Pricing Management**: Modify pricing and cost information
    - **Inventory Configuration**: Update inventory tracking and specifications
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Price Updates**: Modify product pricing and cost information
    - **Specification Changes**: Update product dimensions, weight, and descriptions
    - **Status Management**: Change product status for lifecycle management
    - **Catalog Maintenance**: Update product information for catalog management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.
        body (UpdateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPProductResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        product_id=product_id,
        body=body,
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
    body: UpdateERPProductBody,
) -> Optional[Union[ErrorResponse, UpdateERPProductResponse200]]:
    """Update ERP product


    Update ERP product information with partial data for product catalog maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific product fields without replacing entire record
    - **Pricing Management**: Modify pricing and cost information
    - **Inventory Configuration**: Update inventory tracking and specifications
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Price Updates**: Modify product pricing and cost information
    - **Specification Changes**: Update product dimensions, weight, and descriptions
    - **Status Management**: Change product status for lifecycle management
    - **Catalog Maintenance**: Update product information for catalog management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.
        body (UpdateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPProductResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        product_id=product_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPProductBody,
) -> Response[Union[ErrorResponse, UpdateERPProductResponse200]]:
    """Update ERP product


    Update ERP product information with partial data for product catalog maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific product fields without replacing entire record
    - **Pricing Management**: Modify pricing and cost information
    - **Inventory Configuration**: Update inventory tracking and specifications
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Price Updates**: Modify product pricing and cost information
    - **Specification Changes**: Update product dimensions, weight, and descriptions
    - **Status Management**: Change product status for lifecycle management
    - **Catalog Maintenance**: Update product information for catalog management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.
        body (UpdateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPProductResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        product_id=product_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    product_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPProductBody,
) -> Optional[Union[ErrorResponse, UpdateERPProductResponse200]]:
    """Update ERP product


    Update ERP product information with partial data for product catalog maintenance.

    **Core Features**:
    - **Partial Updates**: Update specific product fields without replacing entire record
    - **Pricing Management**: Modify pricing and cost information
    - **Inventory Configuration**: Update inventory tracking and specifications
    - **Validation**: Ensures data consistency and business rule compliance

    **Use Cases**:
    - **Price Updates**: Modify product pricing and cost information
    - **Specification Changes**: Update product dimensions, weight, and descriptions
    - **Status Management**: Change product status for lifecycle management
    - **Catalog Maintenance**: Update product information for catalog management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        product_id (str):  Example: PROD_507f1f77bcf86cd799439012.
        body (UpdateERPProductBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPProductResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            product_id=product_id,
            client=client,
            body=body,
        )
    ).parsed
