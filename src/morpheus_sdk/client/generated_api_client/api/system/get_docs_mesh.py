from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_docs_mesh_method import GetDocsMeshMethod
from ...models.get_docs_mesh_response_200 import GetDocsMeshResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    service: str,
    action: Union[Unset, str] = UNSET,
    method: Union[Unset, GetDocsMeshMethod] = UNSET,
    include_examples: Union[Unset, bool] = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["service"] = service

    params["action"] = action

    json_method: Union[Unset, str] = UNSET
    if not isinstance(method, Unset):
        json_method = method.value

    params["method"] = json_method

    params["includeExamples"] = include_examples

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/docs/mesh",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetDocsMeshResponse200]:
    if response.status_code == 200:
        response_200 = GetDocsMeshResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetDocsMeshResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    service: str,
    action: Union[Unset, str] = UNSET,
    method: Union[Unset, GetDocsMeshMethod] = UNSET,
    include_examples: Union[Unset, bool] = True,
) -> Response[GetDocsMeshResponse200]:
    """Detailed Service Mesh Documentation


    ### Retrieve Formatted Documentation

    Programmatically access detailed, human-readable documentation for any service in the mesh. This is
    useful for building dynamic help systems or exploring the API capabilities programmatically.

    #### Parameters Guide

    - **service**: The top-level domain (e.g., `wms`, `tms`, `erp`).
    - **action** (Sub-Service): The specific functional area or resource within the service.
        - Example: In `wms`, actions include `inbound-order`, `inventory`, `waves`.
        - Leave empty to see all actions for a service.
    - **method**: Filter by HTTP method to find specific operations (e.g., `post` for creation).

    #### Usage Examples

    **1. Get all documentation for WMS:**
    `GET /docs/mesh?service=wms`

    **2. Get documentation for WMS Inbound Orders (Action/Sub-Service):**
    `GET /docs/mesh?service=wms&action=inbound-order`

    **3. Get only the creation endpoint (POST) for Inbound Orders:**
    `GET /docs/mesh?service=wms&action=inbound-order&method=post`

    **4. Get clean docs without example payloads (for compact view):**
    `GET /docs/mesh?service=wms&action=inbound-order&includeExamples=false`


    Args:
        service (str):  Example: wms.
        action (Union[Unset, str]):  Example: inbound-order.
        method (Union[Unset, GetDocsMeshMethod]):  Example: post.
        include_examples (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDocsMeshResponse200]
    """

    kwargs = _get_kwargs(
        service=service,
        action=action,
        method=method,
        include_examples=include_examples,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    service: str,
    action: Union[Unset, str] = UNSET,
    method: Union[Unset, GetDocsMeshMethod] = UNSET,
    include_examples: Union[Unset, bool] = True,
) -> Optional[GetDocsMeshResponse200]:
    """Detailed Service Mesh Documentation


    ### Retrieve Formatted Documentation

    Programmatically access detailed, human-readable documentation for any service in the mesh. This is
    useful for building dynamic help systems or exploring the API capabilities programmatically.

    #### Parameters Guide

    - **service**: The top-level domain (e.g., `wms`, `tms`, `erp`).
    - **action** (Sub-Service): The specific functional area or resource within the service.
        - Example: In `wms`, actions include `inbound-order`, `inventory`, `waves`.
        - Leave empty to see all actions for a service.
    - **method**: Filter by HTTP method to find specific operations (e.g., `post` for creation).

    #### Usage Examples

    **1. Get all documentation for WMS:**
    `GET /docs/mesh?service=wms`

    **2. Get documentation for WMS Inbound Orders (Action/Sub-Service):**
    `GET /docs/mesh?service=wms&action=inbound-order`

    **3. Get only the creation endpoint (POST) for Inbound Orders:**
    `GET /docs/mesh?service=wms&action=inbound-order&method=post`

    **4. Get clean docs without example payloads (for compact view):**
    `GET /docs/mesh?service=wms&action=inbound-order&includeExamples=false`


    Args:
        service (str):  Example: wms.
        action (Union[Unset, str]):  Example: inbound-order.
        method (Union[Unset, GetDocsMeshMethod]):  Example: post.
        include_examples (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDocsMeshResponse200
    """

    return sync_detailed(
        client=client,
        service=service,
        action=action,
        method=method,
        include_examples=include_examples,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    service: str,
    action: Union[Unset, str] = UNSET,
    method: Union[Unset, GetDocsMeshMethod] = UNSET,
    include_examples: Union[Unset, bool] = True,
) -> Response[GetDocsMeshResponse200]:
    """Detailed Service Mesh Documentation


    ### Retrieve Formatted Documentation

    Programmatically access detailed, human-readable documentation for any service in the mesh. This is
    useful for building dynamic help systems or exploring the API capabilities programmatically.

    #### Parameters Guide

    - **service**: The top-level domain (e.g., `wms`, `tms`, `erp`).
    - **action** (Sub-Service): The specific functional area or resource within the service.
        - Example: In `wms`, actions include `inbound-order`, `inventory`, `waves`.
        - Leave empty to see all actions for a service.
    - **method**: Filter by HTTP method to find specific operations (e.g., `post` for creation).

    #### Usage Examples

    **1. Get all documentation for WMS:**
    `GET /docs/mesh?service=wms`

    **2. Get documentation for WMS Inbound Orders (Action/Sub-Service):**
    `GET /docs/mesh?service=wms&action=inbound-order`

    **3. Get only the creation endpoint (POST) for Inbound Orders:**
    `GET /docs/mesh?service=wms&action=inbound-order&method=post`

    **4. Get clean docs without example payloads (for compact view):**
    `GET /docs/mesh?service=wms&action=inbound-order&includeExamples=false`


    Args:
        service (str):  Example: wms.
        action (Union[Unset, str]):  Example: inbound-order.
        method (Union[Unset, GetDocsMeshMethod]):  Example: post.
        include_examples (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetDocsMeshResponse200]
    """

    kwargs = _get_kwargs(
        service=service,
        action=action,
        method=method,
        include_examples=include_examples,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    service: str,
    action: Union[Unset, str] = UNSET,
    method: Union[Unset, GetDocsMeshMethod] = UNSET,
    include_examples: Union[Unset, bool] = True,
) -> Optional[GetDocsMeshResponse200]:
    """Detailed Service Mesh Documentation


    ### Retrieve Formatted Documentation

    Programmatically access detailed, human-readable documentation for any service in the mesh. This is
    useful for building dynamic help systems or exploring the API capabilities programmatically.

    #### Parameters Guide

    - **service**: The top-level domain (e.g., `wms`, `tms`, `erp`).
    - **action** (Sub-Service): The specific functional area or resource within the service.
        - Example: In `wms`, actions include `inbound-order`, `inventory`, `waves`.
        - Leave empty to see all actions for a service.
    - **method**: Filter by HTTP method to find specific operations (e.g., `post` for creation).

    #### Usage Examples

    **1. Get all documentation for WMS:**
    `GET /docs/mesh?service=wms`

    **2. Get documentation for WMS Inbound Orders (Action/Sub-Service):**
    `GET /docs/mesh?service=wms&action=inbound-order`

    **3. Get only the creation endpoint (POST) for Inbound Orders:**
    `GET /docs/mesh?service=wms&action=inbound-order&method=post`

    **4. Get clean docs without example payloads (for compact view):**
    `GET /docs/mesh?service=wms&action=inbound-order&includeExamples=false`


    Args:
        service (str):  Example: wms.
        action (Union[Unset, str]):  Example: inbound-order.
        method (Union[Unset, GetDocsMeshMethod]):  Example: post.
        include_examples (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetDocsMeshResponse200
    """

    return (
        await asyncio_detailed(
            client=client,
            service=service,
            action=action,
            method=method,
            include_examples=include_examples,
        )
    ).parsed
