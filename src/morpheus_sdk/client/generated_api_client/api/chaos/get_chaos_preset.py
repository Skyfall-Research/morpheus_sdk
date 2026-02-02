from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_chaos_preset_response_200 import GetChaosPresetResponse200
from ...models.get_chaos_preset_response_400 import GetChaosPresetResponse400
from ...models.get_chaos_preset_response_404 import GetChaosPresetResponse404
from ...models.get_chaos_preset_response_500 import GetChaosPresetResponse500
from ...types import Response


def _get_kwargs(
    id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/chaos/presets/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[
    Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
]:
    if response.status_code == 200:
        response_200 = GetChaosPresetResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetChaosPresetResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = GetChaosPresetResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetChaosPresetResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[
    Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
]:
    """Get a specific chaos preset

     Retrieve detailed information about a specific chaos preset by its ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
]:
    """Get a specific chaos preset

     Retrieve detailed information about a specific chaos preset by its ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
    """

    return sync_detailed(
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[
    Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
]:
    """Get a specific chaos preset

     Retrieve detailed information about a specific chaos preset by its ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]]
    """

    kwargs = _get_kwargs(
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[
    Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
]:
    """Get a specific chaos preset

     Retrieve detailed information about a specific chaos preset by its ID.

    Args:
        id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChaosPresetResponse200, GetChaosPresetResponse400, GetChaosPresetResponse404, GetChaosPresetResponse500]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
        )
    ).parsed
