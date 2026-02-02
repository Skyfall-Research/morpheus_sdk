from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_world_body import CreateWorldBody
from ...models.create_world_response_200 import CreateWorldResponse200
from ...models.error_response import ErrorResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: CreateWorldBody,
    stream: Union[Unset, bool] = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["stream"] = stream

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/world",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWorldResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CreateWorldResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWorldResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWorldBody,
    stream: Union[Unset, bool] = False,
) -> Response[Union[CreateWorldResponse200, ErrorResponse]]:
    """Create a new world environment


    ## Create New World

    Create a new isolated world environment with automatic setup of companies and products.

    ### Features
    - **Isolated Environment**: Each world is completely isolated from others
    - **Auto-Generated Content**: Automatically creates MPC company and NPC companies
    - **Product Catalog**: Auto-generates initial product catalog
    - **Streaming Support**: Optional real-time progress updates via Server-Sent Events
    - **URL Generation**: Automatically generates URL slug from name if not provided
    - **Default Management**: Automatically manages default world status

    ### Auto-Generated Content
    When a world is created, the system automatically generates:
    - **1 MPC Company**: Your main company for this world
    - **5 NPC Companies**: Trading partner companies
    - **20 Products**: Initial product catalog

    ### Streaming Mode
    Set `?stream=true` to receive real-time progress updates:
    - **connected**: Stream connection established
    - **progress**: Step-by-step creation updates
    - **complete**: Final result with all generated data
    - **error**: Any errors during creation

    ### Default World Management
    - Only one world can be default at a time
    - Setting `is_default: true` automatically unsets other defaults
    - Default worlds are used for system-wide operations


    Args:
        stream (Union[Unset, bool]):  Default: False. Example: True.
        body (CreateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWorldResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        stream=stream,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWorldBody,
    stream: Union[Unset, bool] = False,
) -> Optional[Union[CreateWorldResponse200, ErrorResponse]]:
    """Create a new world environment


    ## Create New World

    Create a new isolated world environment with automatic setup of companies and products.

    ### Features
    - **Isolated Environment**: Each world is completely isolated from others
    - **Auto-Generated Content**: Automatically creates MPC company and NPC companies
    - **Product Catalog**: Auto-generates initial product catalog
    - **Streaming Support**: Optional real-time progress updates via Server-Sent Events
    - **URL Generation**: Automatically generates URL slug from name if not provided
    - **Default Management**: Automatically manages default world status

    ### Auto-Generated Content
    When a world is created, the system automatically generates:
    - **1 MPC Company**: Your main company for this world
    - **5 NPC Companies**: Trading partner companies
    - **20 Products**: Initial product catalog

    ### Streaming Mode
    Set `?stream=true` to receive real-time progress updates:
    - **connected**: Stream connection established
    - **progress**: Step-by-step creation updates
    - **complete**: Final result with all generated data
    - **error**: Any errors during creation

    ### Default World Management
    - Only one world can be default at a time
    - Setting `is_default: true` automatically unsets other defaults
    - Default worlds are used for system-wide operations


    Args:
        stream (Union[Unset, bool]):  Default: False. Example: True.
        body (CreateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWorldResponse200, ErrorResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
        stream=stream,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWorldBody,
    stream: Union[Unset, bool] = False,
) -> Response[Union[CreateWorldResponse200, ErrorResponse]]:
    """Create a new world environment


    ## Create New World

    Create a new isolated world environment with automatic setup of companies and products.

    ### Features
    - **Isolated Environment**: Each world is completely isolated from others
    - **Auto-Generated Content**: Automatically creates MPC company and NPC companies
    - **Product Catalog**: Auto-generates initial product catalog
    - **Streaming Support**: Optional real-time progress updates via Server-Sent Events
    - **URL Generation**: Automatically generates URL slug from name if not provided
    - **Default Management**: Automatically manages default world status

    ### Auto-Generated Content
    When a world is created, the system automatically generates:
    - **1 MPC Company**: Your main company for this world
    - **5 NPC Companies**: Trading partner companies
    - **20 Products**: Initial product catalog

    ### Streaming Mode
    Set `?stream=true` to receive real-time progress updates:
    - **connected**: Stream connection established
    - **progress**: Step-by-step creation updates
    - **complete**: Final result with all generated data
    - **error**: Any errors during creation

    ### Default World Management
    - Only one world can be default at a time
    - Setting `is_default: true` automatically unsets other defaults
    - Default worlds are used for system-wide operations


    Args:
        stream (Union[Unset, bool]):  Default: False. Example: True.
        body (CreateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWorldResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
        stream=stream,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateWorldBody,
    stream: Union[Unset, bool] = False,
) -> Optional[Union[CreateWorldResponse200, ErrorResponse]]:
    """Create a new world environment


    ## Create New World

    Create a new isolated world environment with automatic setup of companies and products.

    ### Features
    - **Isolated Environment**: Each world is completely isolated from others
    - **Auto-Generated Content**: Automatically creates MPC company and NPC companies
    - **Product Catalog**: Auto-generates initial product catalog
    - **Streaming Support**: Optional real-time progress updates via Server-Sent Events
    - **URL Generation**: Automatically generates URL slug from name if not provided
    - **Default Management**: Automatically manages default world status

    ### Auto-Generated Content
    When a world is created, the system automatically generates:
    - **1 MPC Company**: Your main company for this world
    - **5 NPC Companies**: Trading partner companies
    - **20 Products**: Initial product catalog

    ### Streaming Mode
    Set `?stream=true` to receive real-time progress updates:
    - **connected**: Stream connection established
    - **progress**: Step-by-step creation updates
    - **complete**: Final result with all generated data
    - **error**: Any errors during creation

    ### Default World Management
    - Only one world can be default at a time
    - Setting `is_default: true` automatically unsets other defaults
    - Default worlds are used for system-wide operations


    Args:
        stream (Union[Unset, bool]):  Default: False. Example: True.
        body (CreateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWorldResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            stream=stream,
        )
    ).parsed
