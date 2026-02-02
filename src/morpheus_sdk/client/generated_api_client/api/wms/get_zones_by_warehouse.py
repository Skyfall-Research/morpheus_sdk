from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_zones_by_warehouse_response_200 import GetZonesByWarehouseResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    zone_type: Union[Unset, list[str]] = UNSET,
    temperature_controlled: Union[Unset, bool] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_zone_type: Union[Unset, list[str]] = UNSET
    if not isinstance(zone_type, Unset):
        json_zone_type = zone_type

    params["zoneType"] = json_zone_type

    params["temperatureControlled"] = temperature_controlled

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/zones/warehouse/{warehouse_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetZonesByWarehouseResponse200]:
    if response.status_code == 200:
        response_200 = GetZonesByWarehouseResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetZonesByWarehouseResponse200]:
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
    zone_type: Union[Unset, list[str]] = UNSET,
    temperature_controlled: Union[Unset, bool] = UNSET,
) -> Response[GetZonesByWarehouseResponse200]:
    """Get zones by warehouse


    Retrieve all zones within a specific warehouse with optional filtering capabilities.

    **Core Features**:
    - **Warehouse Scoping**: Get all zones within specified warehouse
    - **Type Filtering**: Filter by specific zone types
    - **Temperature Filtering**: Filter by temperature control requirements
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Zone Overview**: Get complete zone listing for warehouse management
    - **Type-Specific Operations**: Find zones for specific operational needs
    - **Temperature Management**: Identify climate-controlled storage areas


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].
        temperature_controlled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetZonesByWarehouseResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        zone_type=zone_type,
        temperature_controlled=temperature_controlled,
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
    zone_type: Union[Unset, list[str]] = UNSET,
    temperature_controlled: Union[Unset, bool] = UNSET,
) -> Optional[GetZonesByWarehouseResponse200]:
    """Get zones by warehouse


    Retrieve all zones within a specific warehouse with optional filtering capabilities.

    **Core Features**:
    - **Warehouse Scoping**: Get all zones within specified warehouse
    - **Type Filtering**: Filter by specific zone types
    - **Temperature Filtering**: Filter by temperature control requirements
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Zone Overview**: Get complete zone listing for warehouse management
    - **Type-Specific Operations**: Find zones for specific operational needs
    - **Temperature Management**: Identify climate-controlled storage areas


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].
        temperature_controlled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetZonesByWarehouseResponse200
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        zone_type=zone_type,
        temperature_controlled=temperature_controlled,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_type: Union[Unset, list[str]] = UNSET,
    temperature_controlled: Union[Unset, bool] = UNSET,
) -> Response[GetZonesByWarehouseResponse200]:
    """Get zones by warehouse


    Retrieve all zones within a specific warehouse with optional filtering capabilities.

    **Core Features**:
    - **Warehouse Scoping**: Get all zones within specified warehouse
    - **Type Filtering**: Filter by specific zone types
    - **Temperature Filtering**: Filter by temperature control requirements
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Zone Overview**: Get complete zone listing for warehouse management
    - **Type-Specific Operations**: Find zones for specific operational needs
    - **Temperature Management**: Identify climate-controlled storage areas


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].
        temperature_controlled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetZonesByWarehouseResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        zone_type=zone_type,
        temperature_controlled=temperature_controlled,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_type: Union[Unset, list[str]] = UNSET,
    temperature_controlled: Union[Unset, bool] = UNSET,
) -> Optional[GetZonesByWarehouseResponse200]:
    """Get zones by warehouse


    Retrieve all zones within a specific warehouse with optional filtering capabilities.

    **Core Features**:
    - **Warehouse Scoping**: Get all zones within specified warehouse
    - **Type Filtering**: Filter by specific zone types
    - **Temperature Filtering**: Filter by temperature control requirements
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Zone Overview**: Get complete zone listing for warehouse management
    - **Type-Specific Operations**: Find zones for specific operational needs
    - **Temperature Management**: Identify climate-controlled storage areas


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_ATL_001.
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].
        temperature_controlled (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetZonesByWarehouseResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            zone_type=zone_type,
            temperature_controlled=temperature_controlled,
        )
    ).parsed
