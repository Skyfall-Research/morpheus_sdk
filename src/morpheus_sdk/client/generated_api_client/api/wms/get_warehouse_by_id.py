from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_warehouse_by_id_response_200 import GetWarehouseByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/warehouses/{warehouse_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWarehouseByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWarehouseByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWarehouseByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWarehouseByIdResponse200]]:
    """Get warehouse by ID


    Retrieve warehouse by unique warehouse identifier for direct facility access and management.

    **Core Features**:
    - **Direct Access**: Get warehouse by unique warehouseId
    - **Complete Data**: Returns full warehouse configuration including address
    - **Fast Lookup**: Optimized query using indexed warehouseId field
    - **Reference Resolution**: Resolve warehouse references from other operations

    **Use Cases**:
    - **Facility Details**: Get complete warehouse information for management
    - **Reference Lookup**: Resolve warehouse references from orders and operations
    - **Configuration Review**: Access warehouse settings for updates
    - **Integration Support**: Direct API access for external systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWarehouseByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWarehouseByIdResponse200]]:
    """Get warehouse by ID


    Retrieve warehouse by unique warehouse identifier for direct facility access and management.

    **Core Features**:
    - **Direct Access**: Get warehouse by unique warehouseId
    - **Complete Data**: Returns full warehouse configuration including address
    - **Fast Lookup**: Optimized query using indexed warehouseId field
    - **Reference Resolution**: Resolve warehouse references from other operations

    **Use Cases**:
    - **Facility Details**: Get complete warehouse information for management
    - **Reference Lookup**: Resolve warehouse references from orders and operations
    - **Configuration Review**: Access warehouse settings for updates
    - **Integration Support**: Direct API access for external systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWarehouseByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWarehouseByIdResponse200]]:
    """Get warehouse by ID


    Retrieve warehouse by unique warehouse identifier for direct facility access and management.

    **Core Features**:
    - **Direct Access**: Get warehouse by unique warehouseId
    - **Complete Data**: Returns full warehouse configuration including address
    - **Fast Lookup**: Optimized query using indexed warehouseId field
    - **Reference Resolution**: Resolve warehouse references from other operations

    **Use Cases**:
    - **Facility Details**: Get complete warehouse information for management
    - **Reference Lookup**: Resolve warehouse references from orders and operations
    - **Configuration Review**: Access warehouse settings for updates
    - **Integration Support**: Direct API access for external systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWarehouseByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWarehouseByIdResponse200]]:
    """Get warehouse by ID


    Retrieve warehouse by unique warehouse identifier for direct facility access and management.

    **Core Features**:
    - **Direct Access**: Get warehouse by unique warehouseId
    - **Complete Data**: Returns full warehouse configuration including address
    - **Fast Lookup**: Optimized query using indexed warehouseId field
    - **Reference Resolution**: Resolve warehouse references from other operations

    **Use Cases**:
    - **Facility Details**: Get complete warehouse information for management
    - **Reference Lookup**: Resolve warehouse references from orders and operations
    - **Configuration Review**: Access warehouse settings for updates
    - **Integration Support**: Direct API access for external systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWarehouseByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
        )
    ).parsed
