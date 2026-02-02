import datetime
from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_logs_level import GetLogsLevel
from ...models.get_logs_response_200 import GetLogsResponse200
from ...models.get_logs_service_type import GetLogsServiceType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: UUID,
    *,
    service_type: Union[Unset, GetLogsServiceType] = UNSET,
    level: Union[Unset, GetLogsLevel] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_service_type: Union[Unset, str] = UNSET
    if not isinstance(service_type, Unset):
        json_service_type = service_type.value

    params["serviceType"] = json_service_type

    json_level: Union[Unset, str] = UNSET
    if not isinstance(level, Unset):
        json_level = level.value

    params["level"] = json_level

    params["searchText"] = search_text

    json_date_start: Union[Unset, str] = UNSET
    if not isinstance(date_start, Unset):
        json_date_start = date_start.isoformat()
    params["dateStart"] = json_date_start

    json_date_end: Union[Unset, str] = UNSET
    if not isinstance(date_end, Unset):
        json_date_end = date_end.isoformat()
    params["dateEnd"] = json_date_end

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetLogsResponse200]]:
    if response.status_code == 200:
        response_200 = GetLogsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetLogsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, GetLogsServiceType] = UNSET,
    level: Union[Unset, GetLogsLevel] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetLogsResponse200]]:
    """Get operational logs for a world


    ## Retrieve Operational Logs

    Get paginated operational logs for monitoring and debugging system activities within a specific
    world.

    ### Features
    - **Multi-Service Coverage**: Tracks activities across EDI, ERP, AS2, translation, validation,
    gateway, and infrastructure services
    - **Advanced Filtering**: Filter by service type, log level, entities, transactions, and time ranges
    - **Full-Text Search**: Search within log messages for specific content
    - **Cursor-Based Pagination**: Efficient pagination for large log volumes
    - **Real-Time Monitoring**: Access to the most recent system events

    ### Common Use Cases
    - Debugging integration issues between services
    - Monitoring system performance and health
    - Tracking transaction flows across services
    - Error analysis and troubleshooting
    - Real-time operational monitoring


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        service_type (Union[Unset, GetLogsServiceType]):  Example: edi.
        level (Union[Unset, GetLogsLevel]):  Example: error.
        search_text (Union[Unset, str]):  Example: purchase order validation.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetLogsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        service_type=service_type,
        level=level,
        search_text=search_text,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, GetLogsServiceType] = UNSET,
    level: Union[Unset, GetLogsLevel] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetLogsResponse200]]:
    """Get operational logs for a world


    ## Retrieve Operational Logs

    Get paginated operational logs for monitoring and debugging system activities within a specific
    world.

    ### Features
    - **Multi-Service Coverage**: Tracks activities across EDI, ERP, AS2, translation, validation,
    gateway, and infrastructure services
    - **Advanced Filtering**: Filter by service type, log level, entities, transactions, and time ranges
    - **Full-Text Search**: Search within log messages for specific content
    - **Cursor-Based Pagination**: Efficient pagination for large log volumes
    - **Real-Time Monitoring**: Access to the most recent system events

    ### Common Use Cases
    - Debugging integration issues between services
    - Monitoring system performance and health
    - Tracking transaction flows across services
    - Error analysis and troubleshooting
    - Real-time operational monitoring


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        service_type (Union[Unset, GetLogsServiceType]):  Example: edi.
        level (Union[Unset, GetLogsLevel]):  Example: error.
        search_text (Union[Unset, str]):  Example: purchase order validation.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetLogsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        service_type=service_type,
        level=level,
        search_text=search_text,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, GetLogsServiceType] = UNSET,
    level: Union[Unset, GetLogsLevel] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetLogsResponse200]]:
    """Get operational logs for a world


    ## Retrieve Operational Logs

    Get paginated operational logs for monitoring and debugging system activities within a specific
    world.

    ### Features
    - **Multi-Service Coverage**: Tracks activities across EDI, ERP, AS2, translation, validation,
    gateway, and infrastructure services
    - **Advanced Filtering**: Filter by service type, log level, entities, transactions, and time ranges
    - **Full-Text Search**: Search within log messages for specific content
    - **Cursor-Based Pagination**: Efficient pagination for large log volumes
    - **Real-Time Monitoring**: Access to the most recent system events

    ### Common Use Cases
    - Debugging integration issues between services
    - Monitoring system performance and health
    - Tracking transaction flows across services
    - Error analysis and troubleshooting
    - Real-time operational monitoring


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        service_type (Union[Unset, GetLogsServiceType]):  Example: edi.
        level (Union[Unset, GetLogsLevel]):  Example: error.
        search_text (Union[Unset, str]):  Example: purchase order validation.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetLogsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        service_type=service_type,
        level=level,
        search_text=search_text,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    service_type: Union[Unset, GetLogsServiceType] = UNSET,
    level: Union[Unset, GetLogsLevel] = UNSET,
    search_text: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetLogsResponse200]]:
    """Get operational logs for a world


    ## Retrieve Operational Logs

    Get paginated operational logs for monitoring and debugging system activities within a specific
    world.

    ### Features
    - **Multi-Service Coverage**: Tracks activities across EDI, ERP, AS2, translation, validation,
    gateway, and infrastructure services
    - **Advanced Filtering**: Filter by service type, log level, entities, transactions, and time ranges
    - **Full-Text Search**: Search within log messages for specific content
    - **Cursor-Based Pagination**: Efficient pagination for large log volumes
    - **Real-Time Monitoring**: Access to the most recent system events

    ### Common Use Cases
    - Debugging integration issues between services
    - Monitoring system performance and health
    - Tracking transaction flows across services
    - Error analysis and troubleshooting
    - Real-time operational monitoring


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        service_type (Union[Unset, GetLogsServiceType]):  Example: edi.
        level (Union[Unset, GetLogsLevel]):  Example: error.
        search_text (Union[Unset, str]):  Example: purchase order validation.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetLogsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            service_type=service_type,
            level=level,
            search_text=search_text,
            date_start=date_start,
            date_end=date_end,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
