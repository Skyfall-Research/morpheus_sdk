from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.act_body import ActBody
from ...models.act_response_200 import ActResponse200
from ...types import Response


def _get_kwargs(
    *,
    body: ActBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/world/act",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActResponse200, Any]]:
    if response.status_code == 200:
        response_200 = ActResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ActResponse200, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActBody,
) -> Response[Union[ActResponse200, Any]]:
    """Dynamic internal API call execution


    ## Execute Internal API Call

    Dynamically execute any internal API endpoint via a unified interface. This endpoint acts as a
    loopback proxy, allowing orchestration of complex workflows or testing internal routes.

    ### Features
    - **Dynamic Routing**: Call any internal endpoint by path
    - **Method Support**: Supports all HTTP methods (GET, POST, PUT, DELETE, etc.)
    - **Parameter Substitution**: Automatically substitutes path parameters
    - **Query String Construction**: Automatically builds query strings from objects
    - **Response Forwarding**: Returns the exact response from the internal call

    ### Use Cases
    - **Workflow Orchestration**: Chain multiple internal calls
    - **Testing**: Verify internal endpoints without external clients
    - **Proxying**: Unified access point for internal services


    Args:
        body (ActBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActResponse200, Any]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActBody,
) -> Optional[Union[ActResponse200, Any]]:
    """Dynamic internal API call execution


    ## Execute Internal API Call

    Dynamically execute any internal API endpoint via a unified interface. This endpoint acts as a
    loopback proxy, allowing orchestration of complex workflows or testing internal routes.

    ### Features
    - **Dynamic Routing**: Call any internal endpoint by path
    - **Method Support**: Supports all HTTP methods (GET, POST, PUT, DELETE, etc.)
    - **Parameter Substitution**: Automatically substitutes path parameters
    - **Query String Construction**: Automatically builds query strings from objects
    - **Response Forwarding**: Returns the exact response from the internal call

    ### Use Cases
    - **Workflow Orchestration**: Chain multiple internal calls
    - **Testing**: Verify internal endpoints without external clients
    - **Proxying**: Unified access point for internal services


    Args:
        body (ActBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActResponse200, Any]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActBody,
) -> Response[Union[ActResponse200, Any]]:
    """Dynamic internal API call execution


    ## Execute Internal API Call

    Dynamically execute any internal API endpoint via a unified interface. This endpoint acts as a
    loopback proxy, allowing orchestration of complex workflows or testing internal routes.

    ### Features
    - **Dynamic Routing**: Call any internal endpoint by path
    - **Method Support**: Supports all HTTP methods (GET, POST, PUT, DELETE, etc.)
    - **Parameter Substitution**: Automatically substitutes path parameters
    - **Query String Construction**: Automatically builds query strings from objects
    - **Response Forwarding**: Returns the exact response from the internal call

    ### Use Cases
    - **Workflow Orchestration**: Chain multiple internal calls
    - **Testing**: Verify internal endpoints without external clients
    - **Proxying**: Unified access point for internal services


    Args:
        body (ActBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActResponse200, Any]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActBody,
) -> Optional[Union[ActResponse200, Any]]:
    """Dynamic internal API call execution


    ## Execute Internal API Call

    Dynamically execute any internal API endpoint via a unified interface. This endpoint acts as a
    loopback proxy, allowing orchestration of complex workflows or testing internal routes.

    ### Features
    - **Dynamic Routing**: Call any internal endpoint by path
    - **Method Support**: Supports all HTTP methods (GET, POST, PUT, DELETE, etc.)
    - **Parameter Substitution**: Automatically substitutes path parameters
    - **Query String Construction**: Automatically builds query strings from objects
    - **Response Forwarding**: Returns the exact response from the internal call

    ### Use Cases
    - **Workflow Orchestration**: Chain multiple internal calls
    - **Testing**: Verify internal endpoints without external clients
    - **Proxying**: Unified access point for internal services


    Args:
        body (ActBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActResponse200, Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
