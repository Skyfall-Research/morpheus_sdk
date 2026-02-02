from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.list_worlds_response_200 import ListWorldsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    is_default: Union[Unset, bool] = UNSET,
    mpc_company: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["is_default"] = is_default

    params["mpcCompany"] = mpc_company

    params["search"] = search

    params["cursor"] = cursor

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/world",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ListWorldsResponse200]]:
    if response.status_code == 200:
        response_200 = ListWorldsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, ListWorldsResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    is_default: Union[Unset, bool] = UNSET,
    mpc_company: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[Union[ErrorResponse, ListWorldsResponse200]]:
    """List all worlds with filtering and pagination


    ## List All Worlds

    Retrieve a paginated list of all world environments with optional filtering capabilities.

    ### Features
    - **Pagination**: Cursor-based pagination for efficient data retrieval
    - **Search**: Text search across world names
    - **Default Filter**: Filter for default worlds
    - **Company Filter**: Filter by associated MPC company

    ### Use Cases
    - Admin dashboard world management
    - World selection interfaces
    - System monitoring and analytics
    - Multi-tenant environment oversight
    - Default world identification

    ### Pagination
    Uses cursor-based pagination for optimal performance:
    - **cursor**: Use the _id from the last item in the previous page
    - **limit**: Control the number of results per page (max 20)
    - **nextCursor**: Provided in response for subsequent pages


    Args:
        is_default (Union[Unset, bool]):  Example: True.
        mpc_company (Union[Unset, str]):  Example: company_skyfall_123.
        search (Union[Unset, str]):  Example: production.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListWorldsResponse200]]
    """

    kwargs = _get_kwargs(
        is_default=is_default,
        mpc_company=mpc_company,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    is_default: Union[Unset, bool] = UNSET,
    mpc_company: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[ErrorResponse, ListWorldsResponse200]]:
    """List all worlds with filtering and pagination


    ## List All Worlds

    Retrieve a paginated list of all world environments with optional filtering capabilities.

    ### Features
    - **Pagination**: Cursor-based pagination for efficient data retrieval
    - **Search**: Text search across world names
    - **Default Filter**: Filter for default worlds
    - **Company Filter**: Filter by associated MPC company

    ### Use Cases
    - Admin dashboard world management
    - World selection interfaces
    - System monitoring and analytics
    - Multi-tenant environment oversight
    - Default world identification

    ### Pagination
    Uses cursor-based pagination for optimal performance:
    - **cursor**: Use the _id from the last item in the previous page
    - **limit**: Control the number of results per page (max 20)
    - **nextCursor**: Provided in response for subsequent pages


    Args:
        is_default (Union[Unset, bool]):  Example: True.
        mpc_company (Union[Unset, str]):  Example: company_skyfall_123.
        search (Union[Unset, str]):  Example: production.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListWorldsResponse200]
    """

    return sync_detailed(
        client=client,
        is_default=is_default,
        mpc_company=mpc_company,
        search=search,
        cursor=cursor,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    is_default: Union[Unset, bool] = UNSET,
    mpc_company: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Response[Union[ErrorResponse, ListWorldsResponse200]]:
    """List all worlds with filtering and pagination


    ## List All Worlds

    Retrieve a paginated list of all world environments with optional filtering capabilities.

    ### Features
    - **Pagination**: Cursor-based pagination for efficient data retrieval
    - **Search**: Text search across world names
    - **Default Filter**: Filter for default worlds
    - **Company Filter**: Filter by associated MPC company

    ### Use Cases
    - Admin dashboard world management
    - World selection interfaces
    - System monitoring and analytics
    - Multi-tenant environment oversight
    - Default world identification

    ### Pagination
    Uses cursor-based pagination for optimal performance:
    - **cursor**: Use the _id from the last item in the previous page
    - **limit**: Control the number of results per page (max 20)
    - **nextCursor**: Provided in response for subsequent pages


    Args:
        is_default (Union[Unset, bool]):  Example: True.
        mpc_company (Union[Unset, str]):  Example: company_skyfall_123.
        search (Union[Unset, str]):  Example: production.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ListWorldsResponse200]]
    """

    kwargs = _get_kwargs(
        is_default=is_default,
        mpc_company=mpc_company,
        search=search,
        cursor=cursor,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    is_default: Union[Unset, bool] = UNSET,
    mpc_company: Union[Unset, str] = UNSET,
    search: Union[Unset, str] = UNSET,
    cursor: Union[Unset, str] = UNSET,
    limit: Union[Unset, int] = 20,
) -> Optional[Union[ErrorResponse, ListWorldsResponse200]]:
    """List all worlds with filtering and pagination


    ## List All Worlds

    Retrieve a paginated list of all world environments with optional filtering capabilities.

    ### Features
    - **Pagination**: Cursor-based pagination for efficient data retrieval
    - **Search**: Text search across world names
    - **Default Filter**: Filter for default worlds
    - **Company Filter**: Filter by associated MPC company

    ### Use Cases
    - Admin dashboard world management
    - World selection interfaces
    - System monitoring and analytics
    - Multi-tenant environment oversight
    - Default world identification

    ### Pagination
    Uses cursor-based pagination for optimal performance:
    - **cursor**: Use the _id from the last item in the previous page
    - **limit**: Control the number of results per page (max 20)
    - **nextCursor**: Provided in response for subsequent pages


    Args:
        is_default (Union[Unset, bool]):  Example: True.
        mpc_company (Union[Unset, str]):  Example: company_skyfall_123.
        search (Union[Unset, str]):  Example: production.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Default: 20. Example: 10.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ListWorldsResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            is_default=is_default,
            mpc_company=mpc_company,
            search=search,
            cursor=cursor,
            limit=limit,
        )
    ).parsed
