import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_scheduled_wms_cycle_counts_response_200 import GetScheduledWMSCycleCountsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    from_: datetime.datetime,
    to: datetime.datetime,
    warehouse_id: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to = to.isoformat()
    params["to"] = json_to

    params["warehouseId"] = warehouse_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/cycle-counts/scheduled",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]:
    if response.status_code == 200:
        response_200 = GetScheduledWMSCycleCountsResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]:
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
    from_: datetime.datetime,
    to: datetime.datetime,
    warehouse_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]:
    """Get scheduled cycle counts


    ## Get Scheduled WMS Cycle Counts

    Retrieve cycle counts scheduled within a specific date range for operational planning and resource
    allocation.

    ### Features
    - **Date Range Filtering**: Get counts scheduled within specific time periods
    - **Warehouse Scoping**: Optional filtering by specific warehouse facility
    - **Planning Support**: Support daily, weekly, and monthly planning activities
    - **Resource Planning**: Enable resource allocation and scheduling coordination
    - **Operational Visibility**: Provide visibility into upcoming count activities

    ### Query Parameters
    - **from**: Required - Start date for scheduled date range (ISO 8601 format)
    - **to**: Required - End date for scheduled date range (ISO 8601 format)
    - **warehouseId**: Optional - Filter to specific warehouse for facility planning

    ### Business Logic
    - from and to parameters define the scheduled date range for filtering
    - Returns only counts with SCHEDULED status within the date range
    - Optional warehouse filtering for facility-specific planning
    - Results sorted by scheduled date for chronological planning
    - Includes complete count details for planning purposes

    ### Use Cases
    - **Daily Planning**: Plan daily counting activities and resource allocation
    - **Weekly Coordination**: Coordinate weekly counting schedules across facilities
    - **Resource Planning**: Allocate personnel and equipment for scheduled counts
    - **Operational Scheduling**: Schedule and coordinate counting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        from_ (datetime.datetime):  Example: 2024-01-25T00:00:00.000Z.
        to (datetime.datetime):  Example: 2024-01-31T23:59:59.999Z.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        from_=from_,
        to=to,
        warehouse_id=warehouse_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.datetime,
    to: datetime.datetime,
    warehouse_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]:
    """Get scheduled cycle counts


    ## Get Scheduled WMS Cycle Counts

    Retrieve cycle counts scheduled within a specific date range for operational planning and resource
    allocation.

    ### Features
    - **Date Range Filtering**: Get counts scheduled within specific time periods
    - **Warehouse Scoping**: Optional filtering by specific warehouse facility
    - **Planning Support**: Support daily, weekly, and monthly planning activities
    - **Resource Planning**: Enable resource allocation and scheduling coordination
    - **Operational Visibility**: Provide visibility into upcoming count activities

    ### Query Parameters
    - **from**: Required - Start date for scheduled date range (ISO 8601 format)
    - **to**: Required - End date for scheduled date range (ISO 8601 format)
    - **warehouseId**: Optional - Filter to specific warehouse for facility planning

    ### Business Logic
    - from and to parameters define the scheduled date range for filtering
    - Returns only counts with SCHEDULED status within the date range
    - Optional warehouse filtering for facility-specific planning
    - Results sorted by scheduled date for chronological planning
    - Includes complete count details for planning purposes

    ### Use Cases
    - **Daily Planning**: Plan daily counting activities and resource allocation
    - **Weekly Coordination**: Coordinate weekly counting schedules across facilities
    - **Resource Planning**: Allocate personnel and equipment for scheduled counts
    - **Operational Scheduling**: Schedule and coordinate counting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        from_ (datetime.datetime):  Example: 2024-01-25T00:00:00.000Z.
        to (datetime.datetime):  Example: 2024-01-31T23:59:59.999Z.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        from_=from_,
        to=to,
        warehouse_id=warehouse_id,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.datetime,
    to: datetime.datetime,
    warehouse_id: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]:
    """Get scheduled cycle counts


    ## Get Scheduled WMS Cycle Counts

    Retrieve cycle counts scheduled within a specific date range for operational planning and resource
    allocation.

    ### Features
    - **Date Range Filtering**: Get counts scheduled within specific time periods
    - **Warehouse Scoping**: Optional filtering by specific warehouse facility
    - **Planning Support**: Support daily, weekly, and monthly planning activities
    - **Resource Planning**: Enable resource allocation and scheduling coordination
    - **Operational Visibility**: Provide visibility into upcoming count activities

    ### Query Parameters
    - **from**: Required - Start date for scheduled date range (ISO 8601 format)
    - **to**: Required - End date for scheduled date range (ISO 8601 format)
    - **warehouseId**: Optional - Filter to specific warehouse for facility planning

    ### Business Logic
    - from and to parameters define the scheduled date range for filtering
    - Returns only counts with SCHEDULED status within the date range
    - Optional warehouse filtering for facility-specific planning
    - Results sorted by scheduled date for chronological planning
    - Includes complete count details for planning purposes

    ### Use Cases
    - **Daily Planning**: Plan daily counting activities and resource allocation
    - **Weekly Coordination**: Coordinate weekly counting schedules across facilities
    - **Resource Planning**: Allocate personnel and equipment for scheduled counts
    - **Operational Scheduling**: Schedule and coordinate counting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        from_ (datetime.datetime):  Example: 2024-01-25T00:00:00.000Z.
        to (datetime.datetime):  Example: 2024-01-31T23:59:59.999Z.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        from_=from_,
        to=to,
        warehouse_id=warehouse_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    from_: datetime.datetime,
    to: datetime.datetime,
    warehouse_id: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]]:
    """Get scheduled cycle counts


    ## Get Scheduled WMS Cycle Counts

    Retrieve cycle counts scheduled within a specific date range for operational planning and resource
    allocation.

    ### Features
    - **Date Range Filtering**: Get counts scheduled within specific time periods
    - **Warehouse Scoping**: Optional filtering by specific warehouse facility
    - **Planning Support**: Support daily, weekly, and monthly planning activities
    - **Resource Planning**: Enable resource allocation and scheduling coordination
    - **Operational Visibility**: Provide visibility into upcoming count activities

    ### Query Parameters
    - **from**: Required - Start date for scheduled date range (ISO 8601 format)
    - **to**: Required - End date for scheduled date range (ISO 8601 format)
    - **warehouseId**: Optional - Filter to specific warehouse for facility planning

    ### Business Logic
    - from and to parameters define the scheduled date range for filtering
    - Returns only counts with SCHEDULED status within the date range
    - Optional warehouse filtering for facility-specific planning
    - Results sorted by scheduled date for chronological planning
    - Includes complete count details for planning purposes

    ### Use Cases
    - **Daily Planning**: Plan daily counting activities and resource allocation
    - **Weekly Coordination**: Coordinate weekly counting schedules across facilities
    - **Resource Planning**: Allocate personnel and equipment for scheduled counts
    - **Operational Scheduling**: Schedule and coordinate counting operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        from_ (datetime.datetime):  Example: 2024-01-25T00:00:00.000Z.
        to (datetime.datetime):  Example: 2024-01-31T23:59:59.999Z.
        warehouse_id (Union[Unset, str]):  Example: WH_ATL_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetScheduledWMSCycleCountsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            from_=from_,
            to=to,
            warehouse_id=warehouse_id,
        )
    ).parsed
