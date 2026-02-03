import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_tickets_impact import GetTicketsImpact
from ...models.get_tickets_priority import GetTicketsPriority
from ...models.get_tickets_response_200 import GetTicketsResponse200
from ...models.get_tickets_status import GetTicketsStatus
from ...models.get_tickets_urgency import GetTicketsUrgency
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: Union[Unset, GetTicketsStatus] = UNSET,
    priority: Union[Unset, GetTicketsPriority] = UNSET,
    impact: Union[Unset, GetTicketsImpact] = UNSET,
    urgency: Union[Unset, GetTicketsUrgency] = UNSET,
    department: Union[Unset, str] = UNSET,
    assigned_to: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    json_priority: Union[Unset, str] = UNSET
    if not isinstance(priority, Unset):
        json_priority = priority.value

    params["priority"] = json_priority

    json_impact: Union[Unset, str] = UNSET
    if not isinstance(impact, Unset):
        json_impact = impact.value

    params["impact"] = json_impact

    json_urgency: Union[Unset, str] = UNSET
    if not isinstance(urgency, Unset):
        json_urgency = urgency.value

    params["urgency"] = json_urgency

    params["department"] = department

    params["assignedTo"] = assigned_to

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
        "url": f"/{world_id}/tickets",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetTicketsResponse200]:
    if response.status_code == 200:
        response_200 = GetTicketsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetTicketsResponse200]:
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
    status: Union[Unset, GetTicketsStatus] = UNSET,
    priority: Union[Unset, GetTicketsPriority] = UNSET,
    impact: Union[Unset, GetTicketsImpact] = UNSET,
    urgency: Union[Unset, GetTicketsUrgency] = UNSET,
    department: Union[Unset, str] = UNSET,
    assigned_to: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GetTicketsResponse200]:
    """Get tickets for a world with filtering and pagination


    ## Retrieve ITSM Tickets

    Get paginated ITSM tickets for managing incidents, service requests, problems, and change requests
    within a specific world environment.

    ### Features
    - **Multiple Ticket Types**: Support for incidents, service requests, problems, and change requests
    - **Advanced Filtering**: Filter by status, priority, impact, urgency, department, assignee, and
    date ranges
    - **Cursor-Based Pagination**: Efficient pagination for large ticket volumes

    ### Ticket Types
    - **incident**: Unplanned interruption to service
    - **service_request**: Request for something to be provided
    - **problem**: Root cause of one or more incidents
    - **change**: Addition, modification or removal of service

    ### Status Workflow
    - **new** → **open** → **in_progress** → **resolved** → **closed**
    - **on_hold** can be set from any active status


    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        status (Union[Unset, GetTicketsStatus]):  Example: open.
        priority (Union[Unset, GetTicketsPriority]):  Example: high.
        impact (Union[Unset, GetTicketsImpact]):  Example: medium.
        urgency (Union[Unset, GetTicketsUrgency]):  Example: high.
        department (Union[Unset, str]):  Example: IT Support.
        assigned_to (Union[Unset, str]):  Example: user_john_doe.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTicketsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        priority=priority,
        impact=impact,
        urgency=urgency,
        department=department,
        assigned_to=assigned_to,
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
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetTicketsStatus] = UNSET,
    priority: Union[Unset, GetTicketsPriority] = UNSET,
    impact: Union[Unset, GetTicketsImpact] = UNSET,
    urgency: Union[Unset, GetTicketsUrgency] = UNSET,
    department: Union[Unset, str] = UNSET,
    assigned_to: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GetTicketsResponse200]:
    """Get tickets for a world with filtering and pagination


    ## Retrieve ITSM Tickets

    Get paginated ITSM tickets for managing incidents, service requests, problems, and change requests
    within a specific world environment.

    ### Features
    - **Multiple Ticket Types**: Support for incidents, service requests, problems, and change requests
    - **Advanced Filtering**: Filter by status, priority, impact, urgency, department, assignee, and
    date ranges
    - **Cursor-Based Pagination**: Efficient pagination for large ticket volumes

    ### Ticket Types
    - **incident**: Unplanned interruption to service
    - **service_request**: Request for something to be provided
    - **problem**: Root cause of one or more incidents
    - **change**: Addition, modification or removal of service

    ### Status Workflow
    - **new** → **open** → **in_progress** → **resolved** → **closed**
    - **on_hold** can be set from any active status


    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        status (Union[Unset, GetTicketsStatus]):  Example: open.
        priority (Union[Unset, GetTicketsPriority]):  Example: high.
        impact (Union[Unset, GetTicketsImpact]):  Example: medium.
        urgency (Union[Unset, GetTicketsUrgency]):  Example: high.
        department (Union[Unset, str]):  Example: IT Support.
        assigned_to (Union[Unset, str]):  Example: user_john_doe.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTicketsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        priority=priority,
        impact=impact,
        urgency=urgency,
        department=department,
        assigned_to=assigned_to,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetTicketsStatus] = UNSET,
    priority: Union[Unset, GetTicketsPriority] = UNSET,
    impact: Union[Unset, GetTicketsImpact] = UNSET,
    urgency: Union[Unset, GetTicketsUrgency] = UNSET,
    department: Union[Unset, str] = UNSET,
    assigned_to: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Response[GetTicketsResponse200]:
    """Get tickets for a world with filtering and pagination


    ## Retrieve ITSM Tickets

    Get paginated ITSM tickets for managing incidents, service requests, problems, and change requests
    within a specific world environment.

    ### Features
    - **Multiple Ticket Types**: Support for incidents, service requests, problems, and change requests
    - **Advanced Filtering**: Filter by status, priority, impact, urgency, department, assignee, and
    date ranges
    - **Cursor-Based Pagination**: Efficient pagination for large ticket volumes

    ### Ticket Types
    - **incident**: Unplanned interruption to service
    - **service_request**: Request for something to be provided
    - **problem**: Root cause of one or more incidents
    - **change**: Addition, modification or removal of service

    ### Status Workflow
    - **new** → **open** → **in_progress** → **resolved** → **closed**
    - **on_hold** can be set from any active status


    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        status (Union[Unset, GetTicketsStatus]):  Example: open.
        priority (Union[Unset, GetTicketsPriority]):  Example: high.
        impact (Union[Unset, GetTicketsImpact]):  Example: medium.
        urgency (Union[Unset, GetTicketsUrgency]):  Example: high.
        department (Union[Unset, str]):  Example: IT Support.
        assigned_to (Union[Unset, str]):  Example: user_john_doe.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetTicketsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        priority=priority,
        impact=impact,
        urgency=urgency,
        department=department,
        assigned_to=assigned_to,
        date_start=date_start,
        date_end=date_end,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: Union[Unset, GetTicketsStatus] = UNSET,
    priority: Union[Unset, GetTicketsPriority] = UNSET,
    impact: Union[Unset, GetTicketsImpact] = UNSET,
    urgency: Union[Unset, GetTicketsUrgency] = UNSET,
    department: Union[Unset, str] = UNSET,
    assigned_to: Union[Unset, str] = UNSET,
    date_start: Union[Unset, datetime.datetime] = UNSET,
    date_end: Union[Unset, datetime.datetime] = UNSET,
    limit: Union[Unset, int] = 100,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[GetTicketsResponse200]:
    """Get tickets for a world with filtering and pagination


    ## Retrieve ITSM Tickets

    Get paginated ITSM tickets for managing incidents, service requests, problems, and change requests
    within a specific world environment.

    ### Features
    - **Multiple Ticket Types**: Support for incidents, service requests, problems, and change requests
    - **Advanced Filtering**: Filter by status, priority, impact, urgency, department, assignee, and
    date ranges
    - **Cursor-Based Pagination**: Efficient pagination for large ticket volumes

    ### Ticket Types
    - **incident**: Unplanned interruption to service
    - **service_request**: Request for something to be provided
    - **problem**: Root cause of one or more incidents
    - **change**: Addition, modification or removal of service

    ### Status Workflow
    - **new** → **open** → **in_progress** → **resolved** → **closed**
    - **on_hold** can be set from any active status


    Args:
        world_id (str):  Example: 550e8400-e29b-41d4-a716-446655440000.
        status (Union[Unset, GetTicketsStatus]):  Example: open.
        priority (Union[Unset, GetTicketsPriority]):  Example: high.
        impact (Union[Unset, GetTicketsImpact]):  Example: medium.
        urgency (Union[Unset, GetTicketsUrgency]):  Example: high.
        department (Union[Unset, str]):  Example: IT Support.
        assigned_to (Union[Unset, str]):  Example: user_john_doe.
        date_start (Union[Unset, datetime.datetime]):  Example: 2024-01-15T00:00:00.000Z.
        date_end (Union[Unset, datetime.datetime]):  Example: 2024-01-16T23:59:59.999Z.
        limit (Union[Unset, int]):  Default: 100. Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetTicketsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            priority=priority,
            impact=impact,
            urgency=urgency,
            department=department,
            assigned_to=assigned_to,
            date_start=date_start,
            date_end=date_end,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
