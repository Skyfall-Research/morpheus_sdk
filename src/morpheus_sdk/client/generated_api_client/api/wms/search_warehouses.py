from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.search_warehouses_response_200 import SearchWarehousesResponse200
from ...models.search_warehouses_status_item import SearchWarehousesStatusItem
from ...models.search_warehouses_warehouse_type_item import SearchWarehousesWarehouseTypeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    q: str,
    warehouse_type: Union[Unset, list[SearchWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[SearchWarehousesStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q

    json_warehouse_type: Union[Unset, list[str]] = UNSET
    if not isinstance(warehouse_type, Unset):
        json_warehouse_type = []
        for warehouse_type_item_data in warehouse_type:
            warehouse_type_item = warehouse_type_item_data.value
            json_warehouse_type.append(warehouse_type_item)

    params["warehouseType"] = json_warehouse_type

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/warehouses/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, SearchWarehousesResponse200]]:
    if response.status_code == 200:
        response_200 = SearchWarehousesResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, SearchWarehousesResponse200]]:
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
    q: str,
    warehouse_type: Union[Unset, list[SearchWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[SearchWarehousesStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, SearchWarehousesResponse200]]:
    """Search warehouses


    Search warehouses by name and other criteria with flexible filtering capabilities.

    **Core Features**:
    - **Text Search**: Search warehouses by name using flexible text matching
    - **Advanced Filtering**: Filter results by type and status
    - **Flexible Matching**: Support for partial name matches and text search
    - **Operational Filtering**: Combine text search with type and status filters

    **Use Cases**:
    - **Facility Discovery**: Find warehouses by name or partial name
    - **Dynamic Filtering**: Interactive warehouse search and filtering
    - **Integration Support**: API-based warehouse lookup for external systems
    - **User Interfaces**: Support for warehouse selection and discovery


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        q (str):  Example: Atlanta.
        warehouse_type (Union[Unset, list[SearchWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[SearchWarehousesStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SearchWarehousesResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        q=q,
        warehouse_type=warehouse_type,
        status=status,
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
    q: str,
    warehouse_type: Union[Unset, list[SearchWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[SearchWarehousesStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, SearchWarehousesResponse200]]:
    """Search warehouses


    Search warehouses by name and other criteria with flexible filtering capabilities.

    **Core Features**:
    - **Text Search**: Search warehouses by name using flexible text matching
    - **Advanced Filtering**: Filter results by type and status
    - **Flexible Matching**: Support for partial name matches and text search
    - **Operational Filtering**: Combine text search with type and status filters

    **Use Cases**:
    - **Facility Discovery**: Find warehouses by name or partial name
    - **Dynamic Filtering**: Interactive warehouse search and filtering
    - **Integration Support**: API-based warehouse lookup for external systems
    - **User Interfaces**: Support for warehouse selection and discovery


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        q (str):  Example: Atlanta.
        warehouse_type (Union[Unset, list[SearchWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[SearchWarehousesStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SearchWarehousesResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        q=q,
        warehouse_type=warehouse_type,
        status=status,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    warehouse_type: Union[Unset, list[SearchWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[SearchWarehousesStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[Union[ErrorResponse, SearchWarehousesResponse200]]:
    """Search warehouses


    Search warehouses by name and other criteria with flexible filtering capabilities.

    **Core Features**:
    - **Text Search**: Search warehouses by name using flexible text matching
    - **Advanced Filtering**: Filter results by type and status
    - **Flexible Matching**: Support for partial name matches and text search
    - **Operational Filtering**: Combine text search with type and status filters

    **Use Cases**:
    - **Facility Discovery**: Find warehouses by name or partial name
    - **Dynamic Filtering**: Interactive warehouse search and filtering
    - **Integration Support**: API-based warehouse lookup for external systems
    - **User Interfaces**: Support for warehouse selection and discovery


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        q (str):  Example: Atlanta.
        warehouse_type (Union[Unset, list[SearchWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[SearchWarehousesStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, SearchWarehousesResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        q=q,
        warehouse_type=warehouse_type,
        status=status,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    q: str,
    warehouse_type: Union[Unset, list[SearchWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[SearchWarehousesStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[Union[ErrorResponse, SearchWarehousesResponse200]]:
    """Search warehouses


    Search warehouses by name and other criteria with flexible filtering capabilities.

    **Core Features**:
    - **Text Search**: Search warehouses by name using flexible text matching
    - **Advanced Filtering**: Filter results by type and status
    - **Flexible Matching**: Support for partial name matches and text search
    - **Operational Filtering**: Combine text search with type and status filters

    **Use Cases**:
    - **Facility Discovery**: Find warehouses by name or partial name
    - **Dynamic Filtering**: Interactive warehouse search and filtering
    - **Integration Support**: API-based warehouse lookup for external systems
    - **User Interfaces**: Support for warehouse selection and discovery


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        q (str):  Example: Atlanta.
        warehouse_type (Union[Unset, list[SearchWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[SearchWarehousesStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, SearchWarehousesResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            q=q,
            warehouse_type=warehouse_type,
            status=status,
            limit=limit,
        )
    ).parsed
