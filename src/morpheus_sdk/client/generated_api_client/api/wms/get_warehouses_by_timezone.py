from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_warehouses_by_timezone_response_200 import GetWarehousesByTimezoneResponse200
from ...models.get_warehouses_by_timezone_status_item import GetWarehousesByTimezoneStatusItem
from ...models.get_warehouses_by_timezone_warehouse_type_item import GetWarehousesByTimezoneWarehouseTypeItem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    timezone: str,
    *,
    warehouse_type: Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetWarehousesByTimezoneStatusItem]] = UNSET,
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

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/warehouses/timezone/{timezone}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWarehousesByTimezoneResponse200]:
    if response.status_code == 200:
        response_200 = GetWarehousesByTimezoneResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWarehousesByTimezoneResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    timezone: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_type: Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetWarehousesByTimezoneStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetWarehousesByTimezoneResponse200]:
    """Get warehouses by timezone


    Retrieve warehouses filtered by timezone for regional operational planning and coordination.

    **Core Features**:
    - **Timezone Filtering**: Get warehouses in specific IANA timezone
    - **Regional Planning**: Support for timezone-based operational coordination
    - **Advanced Filtering**: Additional filtering by type and status
    - **Operational Coordination**: Enable timezone-aware warehouse operations

    **Use Cases**:
    - **Regional Operations**: Coordinate operations within specific timezones
    - **Shift Planning**: Plan warehouse operations by timezone alignment
    - **Multi-regional Management**: Manage warehouse networks across timezones
    - **Operational Scheduling**: Schedule activities based on warehouse timezones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        timezone (str):  Example: America/New_York.
        warehouse_type (Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[GetWarehousesByTimezoneStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWarehousesByTimezoneResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        timezone=timezone,
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
    timezone: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_type: Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetWarehousesByTimezoneStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetWarehousesByTimezoneResponse200]:
    """Get warehouses by timezone


    Retrieve warehouses filtered by timezone for regional operational planning and coordination.

    **Core Features**:
    - **Timezone Filtering**: Get warehouses in specific IANA timezone
    - **Regional Planning**: Support for timezone-based operational coordination
    - **Advanced Filtering**: Additional filtering by type and status
    - **Operational Coordination**: Enable timezone-aware warehouse operations

    **Use Cases**:
    - **Regional Operations**: Coordinate operations within specific timezones
    - **Shift Planning**: Plan warehouse operations by timezone alignment
    - **Multi-regional Management**: Manage warehouse networks across timezones
    - **Operational Scheduling**: Schedule activities based on warehouse timezones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        timezone (str):  Example: America/New_York.
        warehouse_type (Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[GetWarehousesByTimezoneStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWarehousesByTimezoneResponse200
    """

    return sync_detailed(
        world_id=world_id,
        timezone=timezone,
        client=client,
        warehouse_type=warehouse_type,
        status=status,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    timezone: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_type: Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetWarehousesByTimezoneStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetWarehousesByTimezoneResponse200]:
    """Get warehouses by timezone


    Retrieve warehouses filtered by timezone for regional operational planning and coordination.

    **Core Features**:
    - **Timezone Filtering**: Get warehouses in specific IANA timezone
    - **Regional Planning**: Support for timezone-based operational coordination
    - **Advanced Filtering**: Additional filtering by type and status
    - **Operational Coordination**: Enable timezone-aware warehouse operations

    **Use Cases**:
    - **Regional Operations**: Coordinate operations within specific timezones
    - **Shift Planning**: Plan warehouse operations by timezone alignment
    - **Multi-regional Management**: Manage warehouse networks across timezones
    - **Operational Scheduling**: Schedule activities based on warehouse timezones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        timezone (str):  Example: America/New_York.
        warehouse_type (Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[GetWarehousesByTimezoneStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWarehousesByTimezoneResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        timezone=timezone,
        warehouse_type=warehouse_type,
        status=status,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    timezone: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_type: Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]] = UNSET,
    status: Union[Unset, list[GetWarehousesByTimezoneStatusItem]] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetWarehousesByTimezoneResponse200]:
    """Get warehouses by timezone


    Retrieve warehouses filtered by timezone for regional operational planning and coordination.

    **Core Features**:
    - **Timezone Filtering**: Get warehouses in specific IANA timezone
    - **Regional Planning**: Support for timezone-based operational coordination
    - **Advanced Filtering**: Additional filtering by type and status
    - **Operational Coordination**: Enable timezone-aware warehouse operations

    **Use Cases**:
    - **Regional Operations**: Coordinate operations within specific timezones
    - **Shift Planning**: Plan warehouse operations by timezone alignment
    - **Multi-regional Management**: Manage warehouse networks across timezones
    - **Operational Scheduling**: Schedule activities based on warehouse timezones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        timezone (str):  Example: America/New_York.
        warehouse_type (Union[Unset, list[GetWarehousesByTimezoneWarehouseTypeItem]]):  Example:
            ['FULFILLMENT'].
        status (Union[Unset, list[GetWarehousesByTimezoneStatusItem]]):  Example: ['ACTIVE'].
        limit (Union[Unset, int]):  Default: 50. Example: 25.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWarehousesByTimezoneResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            timezone=timezone,
            client=client,
            warehouse_type=warehouse_type,
            status=status,
            limit=limit,
        )
    ).parsed
