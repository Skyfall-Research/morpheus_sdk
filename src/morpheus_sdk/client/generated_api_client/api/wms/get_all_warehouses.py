from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_all_warehouses_response_200 import GetAllWarehousesResponse200
from ...models.get_all_warehouses_status_item import GetAllWarehousesStatusItem
from ...models.get_all_warehouses_warehouse_type_item import GetAllWarehousesWarehouseTypeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_type: Union[Unset, list[GetAllWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetAllWarehousesStatusItem]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

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

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/warehouses",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetAllWarehousesResponse200]:
    if response.status_code == 200:
        response_200 = GetAllWarehousesResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetAllWarehousesResponse200]:
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
    warehouse_type: Union[Unset, list[GetAllWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetAllWarehousesStatusItem]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllWarehousesResponse200]:
    """Get all warehouses


    Retrieve all warehouses with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Complete Listing**: Get all warehouses in world environment
    - **Advanced Filtering**: Filter by type, status, and operational criteria
    - **Paginated Results**: Efficient handling of large warehouse datasets
    - **Cursor-based Pagination**: Optimized performance for large result sets

    **Use Cases**:
    - **Network Overview**: Get complete warehouse network visibility
    - **Operational Filtering**: Find warehouses by operational status or type
    - **Data Management**: Bulk operations and comprehensive reporting
    - **Performance Monitoring**: Track warehouse network performance metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_type (Union[Unset, list[GetAllWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT', '3PL'].
        status (Union[Unset, list[GetAllWarehousesStatusItem]]):  Example: ['ACTIVE'].
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllWarehousesResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_type=warehouse_type,
        status=status,
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
    warehouse_type: Union[Unset, list[GetAllWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetAllWarehousesStatusItem]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllWarehousesResponse200]:
    """Get all warehouses


    Retrieve all warehouses with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Complete Listing**: Get all warehouses in world environment
    - **Advanced Filtering**: Filter by type, status, and operational criteria
    - **Paginated Results**: Efficient handling of large warehouse datasets
    - **Cursor-based Pagination**: Optimized performance for large result sets

    **Use Cases**:
    - **Network Overview**: Get complete warehouse network visibility
    - **Operational Filtering**: Find warehouses by operational status or type
    - **Data Management**: Bulk operations and comprehensive reporting
    - **Performance Monitoring**: Track warehouse network performance metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_type (Union[Unset, list[GetAllWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT', '3PL'].
        status (Union[Unset, list[GetAllWarehousesStatusItem]]):  Example: ['ACTIVE'].
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllWarehousesResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_type=warehouse_type,
        status=status,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_type: Union[Unset, list[GetAllWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetAllWarehousesStatusItem]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetAllWarehousesResponse200]:
    """Get all warehouses


    Retrieve all warehouses with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Complete Listing**: Get all warehouses in world environment
    - **Advanced Filtering**: Filter by type, status, and operational criteria
    - **Paginated Results**: Efficient handling of large warehouse datasets
    - **Cursor-based Pagination**: Optimized performance for large result sets

    **Use Cases**:
    - **Network Overview**: Get complete warehouse network visibility
    - **Operational Filtering**: Find warehouses by operational status or type
    - **Data Management**: Bulk operations and comprehensive reporting
    - **Performance Monitoring**: Track warehouse network performance metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_type (Union[Unset, list[GetAllWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT', '3PL'].
        status (Union[Unset, list[GetAllWarehousesStatusItem]]):  Example: ['ACTIVE'].
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetAllWarehousesResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_type=warehouse_type,
        status=status,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_type: Union[Unset, list[GetAllWarehousesWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetAllWarehousesStatusItem]] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetAllWarehousesResponse200]:
    """Get all warehouses


    Retrieve all warehouses with comprehensive filtering and pagination capabilities.

    **Core Features**:
    - **Complete Listing**: Get all warehouses in world environment
    - **Advanced Filtering**: Filter by type, status, and operational criteria
    - **Paginated Results**: Efficient handling of large warehouse datasets
    - **Cursor-based Pagination**: Optimized performance for large result sets

    **Use Cases**:
    - **Network Overview**: Get complete warehouse network visibility
    - **Operational Filtering**: Find warehouses by operational status or type
    - **Data Management**: Bulk operations and comprehensive reporting
    - **Performance Monitoring**: Track warehouse network performance metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_type (Union[Unset, list[GetAllWarehousesWarehouseTypeItem]]):  Example:
            ['FULFILLMENT', '3PL'].
        status (Union[Unset, list[GetAllWarehousesStatusItem]]):  Example: ['ACTIVE'].
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439012.
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetAllWarehousesResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_type=warehouse_type,
            status=status,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
