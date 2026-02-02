import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_inbound_orders_expected_today_response_200 import GetWMSInboundOrdersExpectedTodayResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    warehouse_id: str,
    target_date: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["warehouseId"] = warehouse_id

    json_target_date: Union[Unset, str] = UNSET
    if not isinstance(target_date, Unset):
        json_target_date = target_date.isoformat()
    params["targetDate"] = json_target_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/inbound-orders/expected-today",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSInboundOrdersExpectedTodayResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]:
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
    warehouse_id: str,
    target_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]:
    """Get orders expected today


    ## Get WMS Inbound Orders Expected Today

    Retrieve inbound orders scheduled for delivery today or a specific target date, supporting daily
    receiving planning and resource allocation.

    ### Features
    - **Daily Planning**: Focus on today's expected deliveries for receiving operations
    - **Flexible Date**: Support for custom target dates beyond today
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused planning
    - **Status Filtering**: Only active orders (SCHEDULED, IN_TRANSIT, ARRIVED) included
    - **Priority Sorting**: Results sorted by delivery time and priority for workflow optimization

    ### Business Logic
    - targetDate defaults to current date if not specified
    - Filters orders with expectedDeliveryDate falling within the target date (start to end of day)
    - Only includes orders with active statuses (SCHEDULED, IN_TRANSIT, ARRIVED)
    - Results sorted by expectedDeliveryDate and priority for operational efficiency
    - Supports daily receiving planning and resource allocation workflows

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **targetDate**: Optional - Specific date for expected deliveries (ISO 8601) - defaults to today

    ### Use Cases
    - **Daily Operations**: Plan receiving activities for today's expected deliveries
    - **Resource Planning**: Allocate staff and equipment based on expected arrivals
    - **Dock Scheduling**: Coordinate dock door assignments with expected deliveries
    - **Vendor Coordination**: Communicate with vendors about today's expected deliveries
    - **Performance Monitoring**: Track on-time delivery performance against schedules


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        target_date (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        target_date=target_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    target_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]:
    """Get orders expected today


    ## Get WMS Inbound Orders Expected Today

    Retrieve inbound orders scheduled for delivery today or a specific target date, supporting daily
    receiving planning and resource allocation.

    ### Features
    - **Daily Planning**: Focus on today's expected deliveries for receiving operations
    - **Flexible Date**: Support for custom target dates beyond today
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused planning
    - **Status Filtering**: Only active orders (SCHEDULED, IN_TRANSIT, ARRIVED) included
    - **Priority Sorting**: Results sorted by delivery time and priority for workflow optimization

    ### Business Logic
    - targetDate defaults to current date if not specified
    - Filters orders with expectedDeliveryDate falling within the target date (start to end of day)
    - Only includes orders with active statuses (SCHEDULED, IN_TRANSIT, ARRIVED)
    - Results sorted by expectedDeliveryDate and priority for operational efficiency
    - Supports daily receiving planning and resource allocation workflows

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **targetDate**: Optional - Specific date for expected deliveries (ISO 8601) - defaults to today

    ### Use Cases
    - **Daily Operations**: Plan receiving activities for today's expected deliveries
    - **Resource Planning**: Allocate staff and equipment based on expected arrivals
    - **Dock Scheduling**: Coordinate dock door assignments with expected deliveries
    - **Vendor Coordination**: Communicate with vendors about today's expected deliveries
    - **Performance Monitoring**: Track on-time delivery performance against schedules


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        target_date (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        warehouse_id=warehouse_id,
        target_date=target_date,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    target_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]:
    """Get orders expected today


    ## Get WMS Inbound Orders Expected Today

    Retrieve inbound orders scheduled for delivery today or a specific target date, supporting daily
    receiving planning and resource allocation.

    ### Features
    - **Daily Planning**: Focus on today's expected deliveries for receiving operations
    - **Flexible Date**: Support for custom target dates beyond today
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused planning
    - **Status Filtering**: Only active orders (SCHEDULED, IN_TRANSIT, ARRIVED) included
    - **Priority Sorting**: Results sorted by delivery time and priority for workflow optimization

    ### Business Logic
    - targetDate defaults to current date if not specified
    - Filters orders with expectedDeliveryDate falling within the target date (start to end of day)
    - Only includes orders with active statuses (SCHEDULED, IN_TRANSIT, ARRIVED)
    - Results sorted by expectedDeliveryDate and priority for operational efficiency
    - Supports daily receiving planning and resource allocation workflows

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **targetDate**: Optional - Specific date for expected deliveries (ISO 8601) - defaults to today

    ### Use Cases
    - **Daily Operations**: Plan receiving activities for today's expected deliveries
    - **Resource Planning**: Allocate staff and equipment based on expected arrivals
    - **Dock Scheduling**: Coordinate dock door assignments with expected deliveries
    - **Vendor Coordination**: Communicate with vendors about today's expected deliveries
    - **Performance Monitoring**: Track on-time delivery performance against schedules


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        target_date (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        target_date=target_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    warehouse_id: str,
    target_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]]:
    """Get orders expected today


    ## Get WMS Inbound Orders Expected Today

    Retrieve inbound orders scheduled for delivery today or a specific target date, supporting daily
    receiving planning and resource allocation.

    ### Features
    - **Daily Planning**: Focus on today's expected deliveries for receiving operations
    - **Flexible Date**: Support for custom target dates beyond today
    - **Warehouse Scoping**: Filter by specific warehouse for facility-focused planning
    - **Status Filtering**: Only active orders (SCHEDULED, IN_TRANSIT, ARRIVED) included
    - **Priority Sorting**: Results sorted by delivery time and priority for workflow optimization

    ### Business Logic
    - targetDate defaults to current date if not specified
    - Filters orders with expectedDeliveryDate falling within the target date (start to end of day)
    - Only includes orders with active statuses (SCHEDULED, IN_TRANSIT, ARRIVED)
    - Results sorted by expectedDeliveryDate and priority for operational efficiency
    - Supports daily receiving planning and resource allocation workflows

    ### Path Parameters
    - **warehouseId**: Required - Unique identifier for the warehouse (in route context)

    ### Query Parameters
    - **targetDate**: Optional - Specific date for expected deliveries (ISO 8601) - defaults to today

    ### Use Cases
    - **Daily Operations**: Plan receiving activities for today's expected deliveries
    - **Resource Planning**: Allocate staff and equipment based on expected arrivals
    - **Dock Scheduling**: Coordinate dock door assignments with expected deliveries
    - **Vendor Coordination**: Communicate with vendors about today's expected deliveries
    - **Performance Monitoring**: Track on-time delivery performance against schedules


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: wms_warehouse_674565c1234567890abcdef.
        target_date (Union[Unset, datetime.datetime]):  Example: 2024-11-27T00:00:00Z.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSInboundOrdersExpectedTodayResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            warehouse_id=warehouse_id,
            target_date=target_date,
        )
    ).parsed
