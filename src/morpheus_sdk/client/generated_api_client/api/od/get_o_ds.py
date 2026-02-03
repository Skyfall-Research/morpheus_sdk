from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_o_ds_od_type import GetODsOdType
from ...models.get_o_ds_response_200 import GetODsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    od_type: Union[Unset, GetODsOdType] = UNSET,
    name: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_od_type: Union[Unset, str] = UNSET
    if not isinstance(od_type, Unset):
        json_od_type = od_type.value

    params["odType"] = json_od_type

    params["name"] = name

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/od/descriptors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetODsResponse200]:
    if response.status_code == 200:
        response_200 = GetODsResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetODsResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    od_type: Union[Unset, GetODsOdType] = UNSET,
    name: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetODsResponse200]:
    """List Operational Descriptors


    ## List Operational Descriptors

    Retrieve a paginated list of Operational Descriptors in the specified world.

    ### Features
    - **Filtering**: Filter by OD type and name
    - **Pagination**: Cursor-based pagination for efficient retrieval


    Args:
        world_id (str):
        od_type (Union[Unset, GetODsOdType]):
        name (Union[Unset, str]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetODsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_type=od_type,
        name=name,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    od_type: Union[Unset, GetODsOdType] = UNSET,
    name: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetODsResponse200]:
    """List Operational Descriptors


    ## List Operational Descriptors

    Retrieve a paginated list of Operational Descriptors in the specified world.

    ### Features
    - **Filtering**: Filter by OD type and name
    - **Pagination**: Cursor-based pagination for efficient retrieval


    Args:
        world_id (str):
        od_type (Union[Unset, GetODsOdType]):
        name (Union[Unset, str]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetODsResponse200
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        od_type=od_type,
        name=name,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    od_type: Union[Unset, GetODsOdType] = UNSET,
    name: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Response[GetODsResponse200]:
    """List Operational Descriptors


    ## List Operational Descriptors

    Retrieve a paginated list of Operational Descriptors in the specified world.

    ### Features
    - **Filtering**: Filter by OD type and name
    - **Pagination**: Cursor-based pagination for efficient retrieval


    Args:
        world_id (str):
        od_type (Union[Unset, GetODsOdType]):
        name (Union[Unset, str]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetODsResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_type=od_type,
        name=name,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    od_type: Union[Unset, GetODsOdType] = UNSET,
    name: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 50,
) -> Optional[GetODsResponse200]:
    """List Operational Descriptors


    ## List Operational Descriptors

    Retrieve a paginated list of Operational Descriptors in the specified world.

    ### Features
    - **Filtering**: Filter by OD type and name
    - **Pagination**: Cursor-based pagination for efficient retrieval


    Args:
        world_id (str):
        od_type (Union[Unset, GetODsOdType]):
        name (Union[Unset, str]):
        cursor (Union[Unset, str]):
        limit (Union[Unset, int]):  Default: 50.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetODsResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            od_type=od_type,
            name=name,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
