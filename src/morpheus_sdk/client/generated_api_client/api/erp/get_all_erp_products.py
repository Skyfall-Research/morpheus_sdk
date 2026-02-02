from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_erp_products_response_200 import GetAllERPProductsResponse200
from ...models.get_all_erp_products_status import GetAllERPProductsStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, GetAllERPProductsStatus] = UNSET,
    inventory_tracking: Union[Unset, bool] = UNSET,
    min_price: Union[Unset, float] = UNSET,
    max_price: Union[Unset, float] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params["inventoryTracking"] = inventory_tracking

    params["minPrice"] = min_price

    params["maxPrice"] = max_price

    params["searchText"] = search_text

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/products",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllERPProductsResponse200]:
    if response.status_code == 200:
        response_200 = GetAllERPProductsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllERPProductsResponse200]:
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
    status: Union[Unset, GetAllERPProductsStatus] = UNSET,
    inventory_tracking: Union[Unset, bool] = UNSET,
    min_price: Union[Unset, float] = UNSET,
    max_price: Union[Unset, float] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPProductsResponse200]:
    """Get all ERP products


    Retrieve all ERP products with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, inventory tracking, price range, and search text
    - **Text Search**: Search by product name and description
    - **Price Range Filtering**: Filter products within specific price ranges
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Product Data**: Returns full product profiles with pricing and specifications

    **Use Cases**:
    - **Product Catalog Management**: Browse complete product catalogs
    - **Inventory Planning**: Filter products by inventory tracking settings
    - **Pricing Analysis**: Filter products by price ranges for pricing strategies
    - **Search Operations**: Find products by name or description for quick lookup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPProductsStatus]):  Example: ACTIVE.
        inventory_tracking (Union[Unset, bool]):  Example: True.
        min_price (Union[Unset, float]):  Example: 10.
        max_price (Union[Unset, float]):  Example: 500.
        search_text (Union[Unset, str]):  Example: widget.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPProductsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        inventory_tracking=inventory_tracking,
        min_price=min_price,
        max_price=max_price,
        search_text=search_text,
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
    status: Union[Unset, GetAllERPProductsStatus] = UNSET,
    inventory_tracking: Union[Unset, bool] = UNSET,
    min_price: Union[Unset, float] = UNSET,
    max_price: Union[Unset, float] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPProductsResponse200]:
    """Get all ERP products


    Retrieve all ERP products with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, inventory tracking, price range, and search text
    - **Text Search**: Search by product name and description
    - **Price Range Filtering**: Filter products within specific price ranges
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Product Data**: Returns full product profiles with pricing and specifications

    **Use Cases**:
    - **Product Catalog Management**: Browse complete product catalogs
    - **Inventory Planning**: Filter products by inventory tracking settings
    - **Pricing Analysis**: Filter products by price ranges for pricing strategies
    - **Search Operations**: Find products by name or description for quick lookup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPProductsStatus]):  Example: ACTIVE.
        inventory_tracking (Union[Unset, bool]):  Example: True.
        min_price (Union[Unset, float]):  Example: 10.
        max_price (Union[Unset, float]):  Example: 500.
        search_text (Union[Unset, str]):  Example: widget.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPProductsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        inventory_tracking=inventory_tracking,
        min_price=min_price,
        max_price=max_price,
        search_text=search_text,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPProductsStatus] = UNSET,
    inventory_tracking: Union[Unset, bool] = UNSET,
    min_price: Union[Unset, float] = UNSET,
    max_price: Union[Unset, float] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllERPProductsResponse200]:
    """Get all ERP products


    Retrieve all ERP products with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, inventory tracking, price range, and search text
    - **Text Search**: Search by product name and description
    - **Price Range Filtering**: Filter products within specific price ranges
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Product Data**: Returns full product profiles with pricing and specifications

    **Use Cases**:
    - **Product Catalog Management**: Browse complete product catalogs
    - **Inventory Planning**: Filter products by inventory tracking settings
    - **Pricing Analysis**: Filter products by price ranges for pricing strategies
    - **Search Operations**: Find products by name or description for quick lookup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPProductsStatus]):  Example: ACTIVE.
        inventory_tracking (Union[Unset, bool]):  Example: True.
        min_price (Union[Unset, float]):  Example: 10.
        max_price (Union[Unset, float]):  Example: 500.
        search_text (Union[Unset, str]):  Example: widget.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllERPProductsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        inventory_tracking=inventory_tracking,
        min_price=min_price,
        max_price=max_price,
        search_text=search_text,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetAllERPProductsStatus] = UNSET,
    inventory_tracking: Union[Unset, bool] = UNSET,
    min_price: Union[Unset, float] = UNSET,
    max_price: Union[Unset, float] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllERPProductsResponse200]:
    """Get all ERP products


    Retrieve all ERP products with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Advanced Filtering**: Filter by status, inventory tracking, price range, and search text
    - **Text Search**: Search by product name and description
    - **Price Range Filtering**: Filter products within specific price ranges
    - **Paginated Results**: Cursor-based pagination for optimal performance
    - **Complete Product Data**: Returns full product profiles with pricing and specifications

    **Use Cases**:
    - **Product Catalog Management**: Browse complete product catalogs
    - **Inventory Planning**: Filter products by inventory tracking settings
    - **Pricing Analysis**: Filter products by price ranges for pricing strategies
    - **Search Operations**: Find products by name or description for quick lookup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (Union[Unset, GetAllERPProductsStatus]):  Example: ACTIVE.
        inventory_tracking (Union[Unset, bool]):  Example: True.
        min_price (Union[Unset, float]):  Example: 10.
        max_price (Union[Unset, float]):  Example: 500.
        search_text (Union[Unset, str]):  Example: widget.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllERPProductsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            inventory_tracking=inventory_tracking,
            min_price=min_price,
            max_price=max_price,
            search_text=search_text,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
