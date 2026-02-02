from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_chaos_status_response_200 import GetChaosStatusResponse200
from ...models.get_chaos_status_response_500 import GetChaosStatusResponse500
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/chaos/status",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]:
    if response.status_code == 200:
        response_200 = GetChaosStatusResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = GetChaosStatusResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]:
    """Get chaos system status

     Retrieve the current status of the chaos engineering system, including whether it is enabled and
    statistics about configured policies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]:
    """Get chaos system status

     Retrieve the current status of the chaos engineering system, including whether it is enabled and
    statistics about configured policies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChaosStatusResponse200, GetChaosStatusResponse500]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]:
    """Get chaos system status

     Retrieve the current status of the chaos engineering system, including whether it is enabled and
    statistics about configured policies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetChaosStatusResponse200, GetChaosStatusResponse500]]:
    """Get chaos system status

     Retrieve the current status of the chaos engineering system, including whether it is enabled and
    statistics about configured policies.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetChaosStatusResponse200, GetChaosStatusResponse500]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
