from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_zones_by_type_response_200 import GetZonesByTypeResponse200
from ...models.get_zones_by_type_zone_type import GetZonesByTypeZoneType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    zone_type: GetZonesByTypeZoneType,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/zones/type/{zone_type}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetZonesByTypeResponse200]:
    if response.status_code == 200:
        response_200 = GetZonesByTypeResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetZonesByTypeResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    zone_type: GetZonesByTypeZoneType,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Response[GetZonesByTypeResponse200]:
    """Get zones by type


    Retrieve zones filtered by specific zone type across warehouse environments.

    **Core Features**:
    - **Type Filtering**: Get all zones of specific operational type
    - **Cross-Warehouse Search**: Optional warehouse filtering for targeted results
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Operational Planning**: Find all zones for specific operational activities
    - **Resource Allocation**: Identify zones available for particular functions
    - **Capacity Planning**: Assess type-specific storage capabilities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_type (GetZonesByTypeZoneType):  Example: PICKING.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetZonesByTypeResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_type=zone_type,
        warehouse_id=warehouse_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    zone_type: GetZonesByTypeZoneType,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Optional[GetZonesByTypeResponse200]:
    """Get zones by type


    Retrieve zones filtered by specific zone type across warehouse environments.

    **Core Features**:
    - **Type Filtering**: Get all zones of specific operational type
    - **Cross-Warehouse Search**: Optional warehouse filtering for targeted results
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Operational Planning**: Find all zones for specific operational activities
    - **Resource Allocation**: Identify zones available for particular functions
    - **Capacity Planning**: Assess type-specific storage capabilities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_type (GetZonesByTypeZoneType):  Example: PICKING.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetZonesByTypeResponse200
    """

    return sync_detailed(
        world_id=world_id,
        zone_type=zone_type,
        client=client,
        warehouse_id=warehouse_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    zone_type: GetZonesByTypeZoneType,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Response[GetZonesByTypeResponse200]:
    """Get zones by type


    Retrieve zones filtered by specific zone type across warehouse environments.

    **Core Features**:
    - **Type Filtering**: Get all zones of specific operational type
    - **Cross-Warehouse Search**: Optional warehouse filtering for targeted results
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Operational Planning**: Find all zones for specific operational activities
    - **Resource Allocation**: Identify zones available for particular functions
    - **Capacity Planning**: Assess type-specific storage capabilities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_type (GetZonesByTypeZoneType):  Example: PICKING.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetZonesByTypeResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_type=zone_type,
        warehouse_id=warehouse_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    zone_type: GetZonesByTypeZoneType,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
) -> Optional[GetZonesByTypeResponse200]:
    """Get zones by type


    Retrieve zones filtered by specific zone type across warehouse environments.

    **Core Features**:
    - **Type Filtering**: Get all zones of specific operational type
    - **Cross-Warehouse Search**: Optional warehouse filtering for targeted results
    - **Paginated Results**: Efficient handling of large zone datasets

    **Use Cases**:
    - **Operational Planning**: Find all zones for specific operational activities
    - **Resource Allocation**: Identify zones available for particular functions
    - **Capacity Planning**: Assess type-specific storage capabilities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_type (GetZonesByTypeZoneType):  Example: PICKING.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetZonesByTypeResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            zone_type=zone_type,
            client=client,
            warehouse_id=warehouse_id,
        )
    ).parsed
