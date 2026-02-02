from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_warehouse_body import CreateWarehouseBody
from ...models.create_warehouse_response_201 import CreateWarehouseResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWarehouseBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/warehouses",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWarehouseResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWarehouseResponse201.from_dict(response.json())

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
) -> Response[Union[CreateWarehouseResponse201, ErrorResponse]]:
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
    body: CreateWarehouseBody,
) -> Response[Union[CreateWarehouseResponse201, ErrorResponse]]:
    """Create new warehouse


    Create a new warehouse facility with comprehensive location and operational configuration.

    **Core Features**:
    - **Facility Setup**: Complete warehouse configuration with address and timezone
    - **Auto-Generated Codes**: Automatic warehouseId and warehouseCode generation from name
    - **Type Classification**: Support for multiple warehouse operational types
    - **Status Management**: Built-in status lifecycle with ACTIVE, DISABLED, ARCHIVED

    **Use Cases**:
    - **Network Expansion**: Add new warehouse facilities to distribution network
    - **Regional Setup**: Configure warehouses for specific geographic regions
    - **Operational Classification**: Define warehouse types for specialized operations
    - **Multi-tenant Support**: Create isolated warehouse environments per world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWarehouseResponse201, ErrorResponse]]
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
    body: CreateWarehouseBody,
) -> Optional[Union[CreateWarehouseResponse201, ErrorResponse]]:
    """Create new warehouse


    Create a new warehouse facility with comprehensive location and operational configuration.

    **Core Features**:
    - **Facility Setup**: Complete warehouse configuration with address and timezone
    - **Auto-Generated Codes**: Automatic warehouseId and warehouseCode generation from name
    - **Type Classification**: Support for multiple warehouse operational types
    - **Status Management**: Built-in status lifecycle with ACTIVE, DISABLED, ARCHIVED

    **Use Cases**:
    - **Network Expansion**: Add new warehouse facilities to distribution network
    - **Regional Setup**: Configure warehouses for specific geographic regions
    - **Operational Classification**: Define warehouse types for specialized operations
    - **Multi-tenant Support**: Create isolated warehouse environments per world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWarehouseResponse201, ErrorResponse]
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
    body: CreateWarehouseBody,
) -> Response[Union[CreateWarehouseResponse201, ErrorResponse]]:
    """Create new warehouse


    Create a new warehouse facility with comprehensive location and operational configuration.

    **Core Features**:
    - **Facility Setup**: Complete warehouse configuration with address and timezone
    - **Auto-Generated Codes**: Automatic warehouseId and warehouseCode generation from name
    - **Type Classification**: Support for multiple warehouse operational types
    - **Status Management**: Built-in status lifecycle with ACTIVE, DISABLED, ARCHIVED

    **Use Cases**:
    - **Network Expansion**: Add new warehouse facilities to distribution network
    - **Regional Setup**: Configure warehouses for specific geographic regions
    - **Operational Classification**: Define warehouse types for specialized operations
    - **Multi-tenant Support**: Create isolated warehouse environments per world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWarehouseResponse201, ErrorResponse]]
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
    body: CreateWarehouseBody,
) -> Optional[Union[CreateWarehouseResponse201, ErrorResponse]]:
    """Create new warehouse


    Create a new warehouse facility with comprehensive location and operational configuration.

    **Core Features**:
    - **Facility Setup**: Complete warehouse configuration with address and timezone
    - **Auto-Generated Codes**: Automatic warehouseId and warehouseCode generation from name
    - **Type Classification**: Support for multiple warehouse operational types
    - **Status Management**: Built-in status lifecycle with ACTIVE, DISABLED, ARCHIVED

    **Use Cases**:
    - **Network Expansion**: Add new warehouse facilities to distribution network
    - **Regional Setup**: Configure warehouses for specific geographic regions
    - **Operational Classification**: Define warehouse types for specialized operations
    - **Multi-tenant Support**: Create isolated warehouse environments per world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWarehouseResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
