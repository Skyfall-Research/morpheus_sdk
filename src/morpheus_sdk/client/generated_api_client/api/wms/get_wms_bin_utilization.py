import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_bin_utilization_response_200 import GetWMSBinUtilizationResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    zone_ids: Union[Unset, list[str]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_zone_ids: Union[Unset, list[str]] = UNSET
    if not isinstance(zone_ids, Unset):
        json_zone_ids = zone_ids

    params["zoneIds"] = json_zone_ids

    params["warehouseId"] = warehouse_id

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/bins/utilization",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSBinUtilizationResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]:
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
    zone_ids: Union[Unset, list[str]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]:
    """Get bin utilization metrics


    ## Get WMS Bin Utilization Metrics

    Retrieve comprehensive bin utilization metrics and analytics for warehouse capacity planning,
    performance monitoring, and operational optimization.

    ### Features
    - **Utilization Analytics**: Calculate space utilization percentages across bins
    - **Zone-Based Analysis**: Analyze utilization by specific warehouse zones
    - **Capacity Planning**: Support capacity planning with current and projected utilization
    - **Performance Monitoring**: Track utilization trends for operational efficiency
    - **Warehouse Scoping**: Filter analysis by specific warehouse facilities

    ### Metrics Included
    - **Space Utilization**: Percentage of capacity utilized by weight, volume, and count
    - **Bin Status Distribution**: Count of bins by operational status
    - **Zone Performance**: Utilization metrics aggregated by zone
    - **Capacity Analysis**: Available vs. utilized capacity across dimensions
    - **Efficiency Indicators**: Operational efficiency metrics and trends

    ### Query Parameters
    - **zoneIds**: Optional - Filter analysis to specific zones (supports multiple)
    - **warehouseId**: Optional - Scope analysis to specific warehouse
    - **dateStart**: Optional - Start date for historical analysis
    - **dateEnd**: Optional - End date for historical analysis

    ### Business Logic
    - Calculates real-time utilization based on current inventory
    - Excludes DAMAGED and BLOCKED bins from available capacity
    - Provides both absolute and percentage utilization metrics
    - Aggregates data by zone and warehouse for hierarchical analysis

    ### Use Cases
    - **Capacity Planning**: Assess current capacity utilization for expansion planning
    - **Performance Monitoring**: Track warehouse operational efficiency
    - **Zone Optimization**: Identify underutilized or overcapacity zones
    - **Resource Allocation**: Optimize bin allocation and slotting strategies
    - **Operational Reporting**: Generate utilization reports for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_RESERVE_B'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_ids=zone_ids,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_ids: Union[Unset, list[str]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]:
    """Get bin utilization metrics


    ## Get WMS Bin Utilization Metrics

    Retrieve comprehensive bin utilization metrics and analytics for warehouse capacity planning,
    performance monitoring, and operational optimization.

    ### Features
    - **Utilization Analytics**: Calculate space utilization percentages across bins
    - **Zone-Based Analysis**: Analyze utilization by specific warehouse zones
    - **Capacity Planning**: Support capacity planning with current and projected utilization
    - **Performance Monitoring**: Track utilization trends for operational efficiency
    - **Warehouse Scoping**: Filter analysis by specific warehouse facilities

    ### Metrics Included
    - **Space Utilization**: Percentage of capacity utilized by weight, volume, and count
    - **Bin Status Distribution**: Count of bins by operational status
    - **Zone Performance**: Utilization metrics aggregated by zone
    - **Capacity Analysis**: Available vs. utilized capacity across dimensions
    - **Efficiency Indicators**: Operational efficiency metrics and trends

    ### Query Parameters
    - **zoneIds**: Optional - Filter analysis to specific zones (supports multiple)
    - **warehouseId**: Optional - Scope analysis to specific warehouse
    - **dateStart**: Optional - Start date for historical analysis
    - **dateEnd**: Optional - End date for historical analysis

    ### Business Logic
    - Calculates real-time utilization based on current inventory
    - Excludes DAMAGED and BLOCKED bins from available capacity
    - Provides both absolute and percentage utilization metrics
    - Aggregates data by zone and warehouse for hierarchical analysis

    ### Use Cases
    - **Capacity Planning**: Assess current capacity utilization for expansion planning
    - **Performance Monitoring**: Track warehouse operational efficiency
    - **Zone Optimization**: Identify underutilized or overcapacity zones
    - **Resource Allocation**: Optimize bin allocation and slotting strategies
    - **Operational Reporting**: Generate utilization reports for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_RESERVE_B'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSBinUtilizationResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        zone_ids=zone_ids,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_ids: Union[Unset, list[str]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]:
    """Get bin utilization metrics


    ## Get WMS Bin Utilization Metrics

    Retrieve comprehensive bin utilization metrics and analytics for warehouse capacity planning,
    performance monitoring, and operational optimization.

    ### Features
    - **Utilization Analytics**: Calculate space utilization percentages across bins
    - **Zone-Based Analysis**: Analyze utilization by specific warehouse zones
    - **Capacity Planning**: Support capacity planning with current and projected utilization
    - **Performance Monitoring**: Track utilization trends for operational efficiency
    - **Warehouse Scoping**: Filter analysis by specific warehouse facilities

    ### Metrics Included
    - **Space Utilization**: Percentage of capacity utilized by weight, volume, and count
    - **Bin Status Distribution**: Count of bins by operational status
    - **Zone Performance**: Utilization metrics aggregated by zone
    - **Capacity Analysis**: Available vs. utilized capacity across dimensions
    - **Efficiency Indicators**: Operational efficiency metrics and trends

    ### Query Parameters
    - **zoneIds**: Optional - Filter analysis to specific zones (supports multiple)
    - **warehouseId**: Optional - Scope analysis to specific warehouse
    - **dateStart**: Optional - Start date for historical analysis
    - **dateEnd**: Optional - End date for historical analysis

    ### Business Logic
    - Calculates real-time utilization based on current inventory
    - Excludes DAMAGED and BLOCKED bins from available capacity
    - Provides both absolute and percentage utilization metrics
    - Aggregates data by zone and warehouse for hierarchical analysis

    ### Use Cases
    - **Capacity Planning**: Assess current capacity utilization for expansion planning
    - **Performance Monitoring**: Track warehouse operational efficiency
    - **Zone Optimization**: Identify underutilized or overcapacity zones
    - **Resource Allocation**: Optimize bin allocation and slotting strategies
    - **Operational Reporting**: Generate utilization reports for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_RESERVE_B'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_ids=zone_ids,
        warehouse_id=warehouse_id,
        date_start=date_start,
        date_end=date_end,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    zone_ids: Union[Unset, list[str]] = UNSET,
    warehouse_id: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSBinUtilizationResponse200]]:
    """Get bin utilization metrics


    ## Get WMS Bin Utilization Metrics

    Retrieve comprehensive bin utilization metrics and analytics for warehouse capacity planning,
    performance monitoring, and operational optimization.

    ### Features
    - **Utilization Analytics**: Calculate space utilization percentages across bins
    - **Zone-Based Analysis**: Analyze utilization by specific warehouse zones
    - **Capacity Planning**: Support capacity planning with current and projected utilization
    - **Performance Monitoring**: Track utilization trends for operational efficiency
    - **Warehouse Scoping**: Filter analysis by specific warehouse facilities

    ### Metrics Included
    - **Space Utilization**: Percentage of capacity utilized by weight, volume, and count
    - **Bin Status Distribution**: Count of bins by operational status
    - **Zone Performance**: Utilization metrics aggregated by zone
    - **Capacity Analysis**: Available vs. utilized capacity across dimensions
    - **Efficiency Indicators**: Operational efficiency metrics and trends

    ### Query Parameters
    - **zoneIds**: Optional - Filter analysis to specific zones (supports multiple)
    - **warehouseId**: Optional - Scope analysis to specific warehouse
    - **dateStart**: Optional - Start date for historical analysis
    - **dateEnd**: Optional - End date for historical analysis

    ### Business Logic
    - Calculates real-time utilization based on current inventory
    - Excludes DAMAGED and BLOCKED bins from available capacity
    - Provides both absolute and percentage utilization metrics
    - Aggregates data by zone and warehouse for hierarchical analysis

    ### Use Cases
    - **Capacity Planning**: Assess current capacity utilization for expansion planning
    - **Performance Monitoring**: Track warehouse operational efficiency
    - **Zone Optimization**: Identify underutilized or overcapacity zones
    - **Resource Allocation**: Optimize bin allocation and slotting strategies
    - **Operational Reporting**: Generate utilization reports for management


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_ids (Union[Unset, list[str]]):  Example: ['ZONE_PICK_A', 'ZONE_RESERVE_B'].
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-01T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-31T23:59:59.999Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSBinUtilizationResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            zone_ids=zone_ids,
            warehouse_id=warehouse_id,
            date_start=date_start,
            date_end=date_end,
        )
    ).parsed
