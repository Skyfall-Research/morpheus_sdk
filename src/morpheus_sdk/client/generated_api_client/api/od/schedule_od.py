from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.schedule_od_body import ScheduleODBody
from ...models.schedule_od_response_201 import ScheduleODResponse201
from ...types import Response


def _get_kwargs(
    world_id: UUID,
    od_id: str,
    *,
    body: ScheduleODBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/od/descriptors/{od_id}/schedule",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ScheduleODResponse201]:
    if response.status_code == 201:
        response_201 = ScheduleODResponse201.from_dict(response.json())

        return response_201

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ScheduleODResponse201]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: UUID,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ScheduleODBody,
) -> Response[ScheduleODResponse201]:
    """Schedule an Operational Descriptor

     Schedule an OD for future execution, either once or recurring.

    Args:
        world_id (UUID):
        od_id (str):
        body (ScheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleODResponse201]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ScheduleODBody,
) -> Optional[ScheduleODResponse201]:
    """Schedule an Operational Descriptor

     Schedule an OD for future execution, either once or recurring.

    Args:
        world_id (UUID):
        od_id (str):
        body (ScheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleODResponse201
    """

    return sync_detailed(
        world_id=world_id,
        od_id=od_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ScheduleODBody,
) -> Response[ScheduleODResponse201]:
    """Schedule an Operational Descriptor

     Schedule an OD for future execution, either once or recurring.

    Args:
        world_id (UUID):
        od_id (str):
        body (ScheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ScheduleODResponse201]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ScheduleODBody,
) -> Optional[ScheduleODResponse201]:
    """Schedule an Operational Descriptor

     Schedule an OD for future execution, either once or recurring.

    Args:
        world_id (UUID):
        od_id (str):
        body (ScheduleODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ScheduleODResponse201
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            od_id=od_id,
            client=client,
            body=body,
        )
    ).parsed
