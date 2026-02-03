from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.execute_od_body import ExecuteODBody
from ...models.execute_od_response_200 import ExecuteODResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    od_id: str,
    *,
    body: ExecuteODBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/od/descriptors/{od_id}/execute",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ExecuteODResponse200]:
    if response.status_code == 200:
        response_200 = ExecuteODResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ExecuteODResponse200]:
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
    body: ExecuteODBody,
) -> Response[ExecuteODResponse200]:
    """Execute an Operational Descriptor

     Triggers the immediate execution of an OD workflow.

    Args:
        world_id (str):
        od_id (str):
        body (ExecuteODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteODResponse200]
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
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteODBody,
) -> Optional[ExecuteODResponse200]:
    """Execute an Operational Descriptor

     Triggers the immediate execution of an OD workflow.

    Args:
        world_id (str):
        od_id (str):
        body (ExecuteODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteODResponse200
    """

    return sync_detailed(
        world_id=world_id,
        od_id=od_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteODBody,
) -> Response[ExecuteODResponse200]:
    """Execute an Operational Descriptor

     Triggers the immediate execution of an OD workflow.

    Args:
        world_id (str):
        od_id (str):
        body (ExecuteODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExecuteODResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    od_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ExecuteODBody,
) -> Optional[ExecuteODResponse200]:
    """Execute an Operational Descriptor

     Triggers the immediate execution of an OD workflow.

    Args:
        world_id (str):
        od_id (str):
        body (ExecuteODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExecuteODResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            od_id=od_id,
            client=client,
            body=body,
        )
    ).parsed
