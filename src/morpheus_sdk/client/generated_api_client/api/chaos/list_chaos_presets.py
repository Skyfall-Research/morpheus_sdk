from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_chaos_presets_response_200 import ListChaosPresetsResponse200
from ...models.list_chaos_presets_response_500 import ListChaosPresetsResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chaos/presets",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]:
    if response.status_code == 200:
        response_200 = ListChaosPresetsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ListChaosPresetsResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]:
    """List all chaos presets

     Retrieve a list of all available chaos presets with their metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]:
    """List all chaos presets

     Retrieve a list of all available chaos presets with their metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]:
    """List all chaos presets

     Retrieve a list of all available chaos presets with their metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]]:
    """List all chaos presets

     Retrieve a list of all available chaos presets with their metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ListChaosPresetsResponse200, ListChaosPresetsResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
