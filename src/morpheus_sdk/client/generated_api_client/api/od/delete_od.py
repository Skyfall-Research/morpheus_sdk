from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_od_response_200 import DeleteODResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    od_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/{world_id}/od/descriptors/{od_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[DeleteODResponse200]:
    if response.status_code == 200:
        response_200 = DeleteODResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[DeleteODResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteODResponse200]:
    """Delete an Operational Descriptor

     Safely deletes an OD and cancels all associated scheduled jobs.

    Args:
        world_id (str):
        od_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteODResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteODResponse200]:
    """Delete an Operational Descriptor

     Safely deletes an OD and cancels all associated scheduled jobs.

    Args:
        world_id (str):
        od_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteODResponse200
    """

    return sync_detailed(
        world_id=world_id,
        od_id=od_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[DeleteODResponse200]:
    """Delete an Operational Descriptor

     Safely deletes an OD and cancels all associated scheduled jobs.

    Args:
        world_id (str):
        od_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DeleteODResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[DeleteODResponse200]:
    """Delete an Operational Descriptor

     Safely deletes an OD and cancels all associated scheduled jobs.

    Args:
        world_id (str):
        od_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DeleteODResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            od_id=od_id,
            client=client,
        )
    ).parsed
