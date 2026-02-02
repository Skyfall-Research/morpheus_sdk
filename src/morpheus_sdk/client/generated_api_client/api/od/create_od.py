from http import HTTPStatus
from typing import Any, Optional, Union
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_od_body import CreateODBody
from ...models.create_od_response_201 import CreateODResponse201
from ...models.create_od_response_207 import CreateODResponse207
from ...types import Response


def _get_kwargs(
    world_id: UUID,
    *,
    body: CreateODBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/od/descriptors",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateODResponse201, CreateODResponse207]]:
    if response.status_code == 201:
        response_201 = CreateODResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 207:
        response_207 = CreateODResponse207.from_dict(response.json())

        return response_207

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateODResponse201, CreateODResponse207]]:
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
    body: CreateODBody,
) -> Response[Union[CreateODResponse201, CreateODResponse207]]:
    """Create a new Operational Descriptor


    ## Create Operational Descriptor

    Create a new Operational Descriptor (OD) definition in the specified world. The OD defines a
    workflow with steps, inputs, and execution policies.

    ### Features
    - **Schema Validation**: Validates the OD structure against the strict OD schema
    - **Immediate Scheduling**: Optionally schedule the OD for execution upon creation
    - **World Isolation**: ODs are scoped to a specific world environment

    ### OD Structure
    - **id**: Unique identifier for the OD
    - **name**: Human-readable name
    - **type**: Type of OD (standard, background_job, workflow)
    - **steps**: Array of execution steps (MCP tools, scripts, etc.)
    - **runPolicy**: Configuration for execution behavior (idempotency, retries)


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (CreateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateODResponse201, CreateODResponse207]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateODBody,
) -> Optional[Union[CreateODResponse201, CreateODResponse207]]:
    """Create a new Operational Descriptor


    ## Create Operational Descriptor

    Create a new Operational Descriptor (OD) definition in the specified world. The OD defines a
    workflow with steps, inputs, and execution policies.

    ### Features
    - **Schema Validation**: Validates the OD structure against the strict OD schema
    - **Immediate Scheduling**: Optionally schedule the OD for execution upon creation
    - **World Isolation**: ODs are scoped to a specific world environment

    ### OD Structure
    - **id**: Unique identifier for the OD
    - **name**: Human-readable name
    - **type**: Type of OD (standard, background_job, workflow)
    - **steps**: Array of execution steps (MCP tools, scripts, etc.)
    - **runPolicy**: Configuration for execution behavior (idempotency, retries)


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (CreateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateODResponse201, CreateODResponse207]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateODBody,
) -> Response[Union[CreateODResponse201, CreateODResponse207]]:
    """Create a new Operational Descriptor


    ## Create Operational Descriptor

    Create a new Operational Descriptor (OD) definition in the specified world. The OD defines a
    workflow with steps, inputs, and execution policies.

    ### Features
    - **Schema Validation**: Validates the OD structure against the strict OD schema
    - **Immediate Scheduling**: Optionally schedule the OD for execution upon creation
    - **World Isolation**: ODs are scoped to a specific world environment

    ### OD Structure
    - **id**: Unique identifier for the OD
    - **name**: Human-readable name
    - **type**: Type of OD (standard, background_job, workflow)
    - **steps**: Array of execution steps (MCP tools, scripts, etc.)
    - **runPolicy**: Configuration for execution behavior (idempotency, retries)


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (CreateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateODResponse201, CreateODResponse207]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: UUID,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateODBody,
) -> Optional[Union[CreateODResponse201, CreateODResponse207]]:
    """Create a new Operational Descriptor


    ## Create Operational Descriptor

    Create a new Operational Descriptor (OD) definition in the specified world. The OD defines a
    workflow with steps, inputs, and execution policies.

    ### Features
    - **Schema Validation**: Validates the OD structure against the strict OD schema
    - **Immediate Scheduling**: Optionally schedule the OD for execution upon creation
    - **World Isolation**: ODs are scoped to a specific world environment

    ### OD Structure
    - **id**: Unique identifier for the OD
    - **name**: Human-readable name
    - **type**: Type of OD (standard, background_job, workflow)
    - **steps**: Array of execution steps (MCP tools, scripts, etc.)
    - **runPolicy**: Configuration for execution behavior (idempotency, retries)


    Args:
        world_id (UUID):  Example: 550e8400-e29b-41d4-a716-446655440000.
        body (CreateODBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateODResponse201, CreateODResponse207]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
