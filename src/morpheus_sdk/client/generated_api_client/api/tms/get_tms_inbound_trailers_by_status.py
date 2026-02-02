import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_inbound_trailers_by_status_response_200 import GetTMSInboundTrailersByStatusResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    dc_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params["carrierId"] = carrier_id

    params["dcId"] = dc_id

    json_from_: Union[Unset, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Union[Unset, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/trailers",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSInboundTrailersByStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]:
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
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    dc_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]:
    """Get trailers by status with filtering


    ## Get TMS Trailers by Status

    Retrieve inbound trailers based on their operational status with comprehensive filtering and
    pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using comma-separated list
    - **Date Range Filtering**: Filter by scheduled arrival date ranges for time-based queries
    - **Facility Filtering**: Filter by specific distribution center for location-based operations
    - **Carrier Filtering**: Filter by carrier ID for carrier-specific views
    - **Cursor Pagination**: Efficient pagination handling for large datasets
    - **Sorted Results**: Results automatically ordered by scheduled arrival time
    - **Flexible Queries**: Combine multiple filter parameters for precise results

    ### Available Status Values
    - **SCHEDULED**: Trailer appointment scheduled and confirmed
    - **EN_ROUTE**: In transit to facility (carrier reported)
    - **CHECKED_IN**: Arrived at facility and checked in at gate
    - **AT_DOCK**: Assigned to dock door and positioned for unloading
    - **UNLOADING**: Active unloading process in progress
    - **UNLOADED**: Unloading completed, ready for departure
    - **DEPARTED**: Trailer has left the facility
    - **CANCELLED**: Appointment cancelled by carrier or facility
    - **DELAYED**: Delayed arrival reported with updated ETA

    ### Query Parameters
    - **status**: Required - Single status or comma-separated list of statuses
    - **dcId**: Optional - Distribution center identifier for facility-specific filtering
    - **carrierId**: Optional - Carrier identifier for carrier-specific filtering
    - **startDate**: Optional - Start date for scheduled arrival filtering
    - **endDate**: Optional - End date for scheduled arrival filtering
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling

    ### Use Cases
    - **Dock Scheduling**: View trailers by status for dock assignment planning
    - **Driver Communication**: Find trailers needing driver notifications
    - **Operational Monitoring**: Real-time status tracking and performance monitoring
    - **Analytics & Reporting**: Generate status-based reports and KPI dashboards
    - **Facility Management**: Track trailer flow through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: SCHEDULED,EN_ROUTE,CHECKED_IN.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        dc_id (Union[Unset, str]):  Example: DC_ATL_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-01-20T23:59:59.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        carrier_id=carrier_id,
        dc_id=dc_id,
        from_=from_,
        to=to,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    dc_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]:
    """Get trailers by status with filtering


    ## Get TMS Trailers by Status

    Retrieve inbound trailers based on their operational status with comprehensive filtering and
    pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using comma-separated list
    - **Date Range Filtering**: Filter by scheduled arrival date ranges for time-based queries
    - **Facility Filtering**: Filter by specific distribution center for location-based operations
    - **Carrier Filtering**: Filter by carrier ID for carrier-specific views
    - **Cursor Pagination**: Efficient pagination handling for large datasets
    - **Sorted Results**: Results automatically ordered by scheduled arrival time
    - **Flexible Queries**: Combine multiple filter parameters for precise results

    ### Available Status Values
    - **SCHEDULED**: Trailer appointment scheduled and confirmed
    - **EN_ROUTE**: In transit to facility (carrier reported)
    - **CHECKED_IN**: Arrived at facility and checked in at gate
    - **AT_DOCK**: Assigned to dock door and positioned for unloading
    - **UNLOADING**: Active unloading process in progress
    - **UNLOADED**: Unloading completed, ready for departure
    - **DEPARTED**: Trailer has left the facility
    - **CANCELLED**: Appointment cancelled by carrier or facility
    - **DELAYED**: Delayed arrival reported with updated ETA

    ### Query Parameters
    - **status**: Required - Single status or comma-separated list of statuses
    - **dcId**: Optional - Distribution center identifier for facility-specific filtering
    - **carrierId**: Optional - Carrier identifier for carrier-specific filtering
    - **startDate**: Optional - Start date for scheduled arrival filtering
    - **endDate**: Optional - End date for scheduled arrival filtering
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling

    ### Use Cases
    - **Dock Scheduling**: View trailers by status for dock assignment planning
    - **Driver Communication**: Find trailers needing driver notifications
    - **Operational Monitoring**: Real-time status tracking and performance monitoring
    - **Analytics & Reporting**: Generate status-based reports and KPI dashboards
    - **Facility Management**: Track trailer flow through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: SCHEDULED,EN_ROUTE,CHECKED_IN.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        dc_id (Union[Unset, str]):  Example: DC_ATL_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-01-20T23:59:59.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        carrier_id=carrier_id,
        dc_id=dc_id,
        from_=from_,
        to=to,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    dc_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]:
    """Get trailers by status with filtering


    ## Get TMS Trailers by Status

    Retrieve inbound trailers based on their operational status with comprehensive filtering and
    pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using comma-separated list
    - **Date Range Filtering**: Filter by scheduled arrival date ranges for time-based queries
    - **Facility Filtering**: Filter by specific distribution center for location-based operations
    - **Carrier Filtering**: Filter by carrier ID for carrier-specific views
    - **Cursor Pagination**: Efficient pagination handling for large datasets
    - **Sorted Results**: Results automatically ordered by scheduled arrival time
    - **Flexible Queries**: Combine multiple filter parameters for precise results

    ### Available Status Values
    - **SCHEDULED**: Trailer appointment scheduled and confirmed
    - **EN_ROUTE**: In transit to facility (carrier reported)
    - **CHECKED_IN**: Arrived at facility and checked in at gate
    - **AT_DOCK**: Assigned to dock door and positioned for unloading
    - **UNLOADING**: Active unloading process in progress
    - **UNLOADED**: Unloading completed, ready for departure
    - **DEPARTED**: Trailer has left the facility
    - **CANCELLED**: Appointment cancelled by carrier or facility
    - **DELAYED**: Delayed arrival reported with updated ETA

    ### Query Parameters
    - **status**: Required - Single status or comma-separated list of statuses
    - **dcId**: Optional - Distribution center identifier for facility-specific filtering
    - **carrierId**: Optional - Carrier identifier for carrier-specific filtering
    - **startDate**: Optional - Start date for scheduled arrival filtering
    - **endDate**: Optional - End date for scheduled arrival filtering
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling

    ### Use Cases
    - **Dock Scheduling**: View trailers by status for dock assignment planning
    - **Driver Communication**: Find trailers needing driver notifications
    - **Operational Monitoring**: Real-time status tracking and performance monitoring
    - **Analytics & Reporting**: Generate status-based reports and KPI dashboards
    - **Facility Management**: Track trailer flow through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: SCHEDULED,EN_ROUTE,CHECKED_IN.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        dc_id (Union[Unset, str]):  Example: DC_ATL_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-01-20T23:59:59.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        carrier_id=carrier_id,
        dc_id=dc_id,
        from_=from_,
        to=to,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    dc_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]]:
    """Get trailers by status with filtering


    ## Get TMS Trailers by Status

    Retrieve inbound trailers based on their operational status with comprehensive filtering and
    pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by one or multiple status values using comma-separated list
    - **Date Range Filtering**: Filter by scheduled arrival date ranges for time-based queries
    - **Facility Filtering**: Filter by specific distribution center for location-based operations
    - **Carrier Filtering**: Filter by carrier ID for carrier-specific views
    - **Cursor Pagination**: Efficient pagination handling for large datasets
    - **Sorted Results**: Results automatically ordered by scheduled arrival time
    - **Flexible Queries**: Combine multiple filter parameters for precise results

    ### Available Status Values
    - **SCHEDULED**: Trailer appointment scheduled and confirmed
    - **EN_ROUTE**: In transit to facility (carrier reported)
    - **CHECKED_IN**: Arrived at facility and checked in at gate
    - **AT_DOCK**: Assigned to dock door and positioned for unloading
    - **UNLOADING**: Active unloading process in progress
    - **UNLOADED**: Unloading completed, ready for departure
    - **DEPARTED**: Trailer has left the facility
    - **CANCELLED**: Appointment cancelled by carrier or facility
    - **DELAYED**: Delayed arrival reported with updated ETA

    ### Query Parameters
    - **status**: Required - Single status or comma-separated list of statuses
    - **dcId**: Optional - Distribution center identifier for facility-specific filtering
    - **carrierId**: Optional - Carrier identifier for carrier-specific filtering
    - **startDate**: Optional - Start date for scheduled arrival filtering
    - **endDate**: Optional - End date for scheduled arrival filtering
    - **limit**: Optional - Maximum results per page (default: 50, max: 500)
    - **cursor**: Optional - Pagination cursor for efficient large dataset handling

    ### Use Cases
    - **Dock Scheduling**: View trailers by status for dock assignment planning
    - **Driver Communication**: Find trailers needing driver notifications
    - **Operational Monitoring**: Real-time status tracking and performance monitoring
    - **Analytics & Reporting**: Generate status-based reports and KPI dashboards
    - **Facility Management**: Track trailer flow through facility operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: SCHEDULED,EN_ROUTE,CHECKED_IN.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        dc_id (Union[Unset, str]):  Example: DC_ATL_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-01-20T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-01-20T23:59:59.000Z.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSInboundTrailersByStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            carrier_id=carrier_id,
            dc_id=dc_id,
            from_=from_,
            to=to,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
