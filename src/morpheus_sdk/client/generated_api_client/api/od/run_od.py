from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.run_od_od_name import RunOdOdName
from ...models.run_od_response_200 import RunOdResponse200
from ...types import UNSET, Response


def _get_kwargs(
    world_id: UUID,
    *,
    od_name: RunOdOdName,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_od_name = od_name.value
    params["odName"] = json_od_name

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/od",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RunOdResponse200]:
    if response.status_code == 200:
        response_200 = RunOdResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RunOdResponse200]:
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
    od_name: RunOdOdName,
) -> Response[RunOdResponse200]:
    """Run a simple OD workflow (Demo)

     Executes a predefined demo workflow (simple-edi or simple-wms). This is a legacy endpoint for demo
    purposes.

    Args:
        world_id (UUID):
        od_name (RunOdOdName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RunOdResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_name=od_name,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    od_name: RunOdOdName,
) -> Optional[RunOdResponse200]:
    """Run a simple OD workflow (Demo)

     Executes a predefined demo workflow (simple-edi or simple-wms). This is a legacy endpoint for demo
    purposes.

    Args:
        world_id (UUID):
        od_name (RunOdOdName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RunOdResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        od_name=od_name,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    od_name: RunOdOdName,
) -> Response[RunOdResponse200]:
    """Run a simple OD workflow (Demo)

     Executes a predefined demo workflow (simple-edi or simple-wms). This is a legacy endpoint for demo
    purposes.

    Args:
        world_id (UUID):
        od_name (RunOdOdName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RunOdResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_name=od_name,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    od_name: RunOdOdName,
) -> Optional[RunOdResponse200]:
    """Run a simple OD workflow (Demo)

     Executes a predefined demo workflow (simple-edi or simple-wms). This is a legacy endpoint for demo
    purposes.

    Args:
        world_id (UUID):
        od_name (RunOdOdName):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RunOdResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            od_name=od_name,
        )
    ).parsed
