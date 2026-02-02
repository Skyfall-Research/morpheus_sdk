from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.update_od_body import UpdateODBody
from ...models.update_od_response_200 import UpdateODResponse200
from ...types import Response


def _get_kwargs(
    world_id: UUID,
    od_id: str,
    *,
    body: UpdateODBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/od/descriptors/{od_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[UpdateODResponse200]:
    if response.status_code == 200:
        response_200 = UpdateODResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[UpdateODResponse200]:
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
    body: UpdateODBody,
) -> Response[UpdateODResponse200]:
    """Update an Operational Descriptor

    Args:
        world_id (UUID):
        od_id (str):
        body (UpdateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateODResponse200]
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
    body: UpdateODBody,
) -> Optional[UpdateODResponse200]:
    """Update an Operational Descriptor

    Args:
        world_id (UUID):
        od_id (str):
        body (UpdateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateODResponse200
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
    body: UpdateODBody,
) -> Response[UpdateODResponse200]:
    """Update an Operational Descriptor

    Args:
        world_id (UUID):
        od_id (str):
        body (UpdateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[UpdateODResponse200]
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
    body: UpdateODBody,
) -> Optional[UpdateODResponse200]:
    """Update an Operational Descriptor

    Args:
        world_id (UUID):
        od_id (str):
        body (UpdateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        UpdateODResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            od_id=od_id,
            client=client,
            body=body,
        )
    ).parsed
