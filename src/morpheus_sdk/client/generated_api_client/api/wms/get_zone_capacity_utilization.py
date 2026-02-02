from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_zone_capacity_utilization_response_200 import GetZoneCapacityUtilizationResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    zone_id: str,
    *,
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    zone_type: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_zone_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(zone_ids, Unset):
        json_zone_ids = zone_ids

    params["zoneIds"] = json_zone_ids

    json_zone_type: Union[Unset, list[str]] = UNSET
    if not isinstance(zone_type, Unset):
        json_zone_type = zone_type

    params["zoneType"] = json_zone_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/zones/{zone_id}/capacity-utilization",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetZoneCapacityUtilizationResponse200]:
    if response.status_code == 200:
        response_200 = GetZoneCapacityUtilizationResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetZoneCapacityUtilizationResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    zone_type: Union[Unset, list[str]] = UNSET,
) -> Response[GetZoneCapacityUtilizationResponse200]:
    """Get zone capacity utilization


    ## Get Zone Capacity Utilization

    Get capacity utilization metrics for specific zone(s) including bin counts and capacity
    calculations.

    **Core Features**:
    - **Utilization Metrics**: Calculate used vs total capacity
    - **Bin Statistics**: Count available and occupied bins
    - **Zone Filtering**: Filter by specific zone ID or zone type
    - **Warehouse Scope**: Calculate metrics within specific warehouse

    **Use Cases**:
    - **Capacity Planning**: Identify zones nearing full capacity
    - **Storage Optimization**: Find underutilized zones for consolidation
    - **Operational Reporting**: Track storage efficiency metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZNE_001', 'ZNE_002'].
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetZoneCapacityUtilizationResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        warehouse_id=warehouse_id,
        zone_ids=zone_ids,
        zone_type=zone_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    zone_type: Union[Unset, list[str]] = UNSET,
) -> Optional[GetZoneCapacityUtilizationResponse200]:
    """Get zone capacity utilization


    ## Get Zone Capacity Utilization

    Get capacity utilization metrics for specific zone(s) including bin counts and capacity
    calculations.

    **Core Features**:
    - **Utilization Metrics**: Calculate used vs total capacity
    - **Bin Statistics**: Count available and occupied bins
    - **Zone Filtering**: Filter by specific zone ID or zone type
    - **Warehouse Scope**: Calculate metrics within specific warehouse

    **Use Cases**:
    - **Capacity Planning**: Identify zones nearing full capacity
    - **Storage Optimization**: Find underutilized zones for consolidation
    - **Operational Reporting**: Track storage efficiency metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZNE_001', 'ZNE_002'].
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetZoneCapacityUtilizationResponse200
    """

    return sync_detailed(
        world_id=world_id,
        zone_id=zone_id,
        client=client,
        warehouse_id=warehouse_id,
        zone_ids=zone_ids,
        zone_type=zone_type,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    zone_type: Union[Unset, list[str]] = UNSET,
) -> Response[GetZoneCapacityUtilizationResponse200]:
    """Get zone capacity utilization


    ## Get Zone Capacity Utilization

    Get capacity utilization metrics for specific zone(s) including bin counts and capacity
    calculations.

    **Core Features**:
    - **Utilization Metrics**: Calculate used vs total capacity
    - **Bin Statistics**: Count available and occupied bins
    - **Zone Filtering**: Filter by specific zone ID or zone type
    - **Warehouse Scope**: Calculate metrics within specific warehouse

    **Use Cases**:
    - **Capacity Planning**: Identify zones nearing full capacity
    - **Storage Optimization**: Find underutilized zones for consolidation
    - **Operational Reporting**: Track storage efficiency metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZNE_001', 'ZNE_002'].
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetZoneCapacityUtilizationResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        warehouse_id=warehouse_id,
        zone_ids=zone_ids,
        zone_type=zone_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: Union[Unset, str] = UNSET,
    zone_ids: Union[Unset, list[str]] = UNSET,
    zone_type: Union[Unset, list[str]] = UNSET,
) -> Optional[GetZoneCapacityUtilizationResponse200]:
    """Get zone capacity utilization


    ## Get Zone Capacity Utilization

    Get capacity utilization metrics for specific zone(s) including bin counts and capacity
    calculations.

    **Core Features**:
    - **Utilization Metrics**: Calculate used vs total capacity
    - **Bin Statistics**: Count available and occupied bins
    - **Zone Filtering**: Filter by specific zone ID or zone type
    - **Warehouse Scope**: Calculate metrics within specific warehouse

    **Use Cases**:
    - **Capacity Planning**: Identify zones nearing full capacity
    - **Storage Optimization**: Find underutilized zones for consolidation
    - **Operational Reporting**: Track storage efficiency metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZNE_001', 'ZNE_002'].
        zone_type (Union[Unset, list[str]]):  Example: ['PICKING', 'STORAGE'].

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetZoneCapacityUtilizationResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            zone_id=zone_id,
            client=client,
            warehouse_id=warehouse_id,
            zone_ids=zone_ids,
            zone_type=zone_type,
        )
    ).parsed
