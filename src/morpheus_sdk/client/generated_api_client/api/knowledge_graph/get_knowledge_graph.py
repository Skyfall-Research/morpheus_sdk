from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_knowledge_graph_response_200 import GetKnowledgeGraphResponse200
from ...models.get_knowledge_graph_response_404 import GetKnowledgeGraphResponse404
from ...models.get_knowledge_graph_response_500 import GetKnowledgeGraphResponse500
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/knowledge-graph",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]:
    if response.status_code == 200:
        response_200 = GetKnowledgeGraphResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = GetKnowledgeGraphResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = GetKnowledgeGraphResponse500.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]:
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
) -> Response[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]:
    """Get knowledge graph for world


    Retrieve the knowledge graph filtered by the world's assigned capabilities. Uses bidirectional BFS
    to capture the complete connected subgraph.

    **Graph Structure**:
    The knowledge graph represents relationships between different entity types in the system:

    - **PERSONA → CAPABILITY**: via `can_perform` edge
    - **CAPABILITY → OD**: via `implemented_by` edge
    - **OD → TOOL**: via `uses` edge
    - **TOOL → SERVICE**: via `exposed_by` edge
    - **TOOL → ENTITY**: via `produces`, `requires`, or `modifies` edges

    **Filtering Behavior**:
    - When the world has assigned capabilities, the graph is automatically filtered to show only
    relevant nodes
    - Uses bidirectional BFS starting from the world's ODs to find all connected nodes
    - Returns `filtered: true` and `seedODs` array when filtering is applied
    - Returns full graph with `filtered: false` and info message when no capabilities are assigned

    **Use Cases**:
    - **Visualization**: Render interactive 2D/3D knowledge graph views
    - **Capability Discovery**: Understand available capabilities and their connections
    - **Impact Analysis**: Identify what entities are affected by running an OD
    - **Dependency Mapping**: Find tool and service dependencies
    - **Lineage Tracking**: Trace entity creation and modification paths


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]:
    """Get knowledge graph for world


    Retrieve the knowledge graph filtered by the world's assigned capabilities. Uses bidirectional BFS
    to capture the complete connected subgraph.

    **Graph Structure**:
    The knowledge graph represents relationships between different entity types in the system:

    - **PERSONA → CAPABILITY**: via `can_perform` edge
    - **CAPABILITY → OD**: via `implemented_by` edge
    - **OD → TOOL**: via `uses` edge
    - **TOOL → SERVICE**: via `exposed_by` edge
    - **TOOL → ENTITY**: via `produces`, `requires`, or `modifies` edges

    **Filtering Behavior**:
    - When the world has assigned capabilities, the graph is automatically filtered to show only
    relevant nodes
    - Uses bidirectional BFS starting from the world's ODs to find all connected nodes
    - Returns `filtered: true` and `seedODs` array when filtering is applied
    - Returns full graph with `filtered: false` and info message when no capabilities are assigned

    **Use Cases**:
    - **Visualization**: Render interactive 2D/3D knowledge graph views
    - **Capability Discovery**: Understand available capabilities and their connections
    - **Impact Analysis**: Identify what entities are affected by running an OD
    - **Dependency Mapping**: Find tool and service dependencies
    - **Lineage Tracking**: Trace entity creation and modification paths


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]:
    """Get knowledge graph for world


    Retrieve the knowledge graph filtered by the world's assigned capabilities. Uses bidirectional BFS
    to capture the complete connected subgraph.

    **Graph Structure**:
    The knowledge graph represents relationships between different entity types in the system:

    - **PERSONA → CAPABILITY**: via `can_perform` edge
    - **CAPABILITY → OD**: via `implemented_by` edge
    - **OD → TOOL**: via `uses` edge
    - **TOOL → SERVICE**: via `exposed_by` edge
    - **TOOL → ENTITY**: via `produces`, `requires`, or `modifies` edges

    **Filtering Behavior**:
    - When the world has assigned capabilities, the graph is automatically filtered to show only
    relevant nodes
    - Uses bidirectional BFS starting from the world's ODs to find all connected nodes
    - Returns `filtered: true` and `seedODs` array when filtering is applied
    - Returns full graph with `filtered: false` and info message when no capabilities are assigned

    **Use Cases**:
    - **Visualization**: Render interactive 2D/3D knowledge graph views
    - **Capability Discovery**: Understand available capabilities and their connections
    - **Impact Analysis**: Identify what entities are affected by running an OD
    - **Dependency Mapping**: Find tool and service dependencies
    - **Lineage Tracking**: Trace entity creation and modification paths


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]]:
    """Get knowledge graph for world


    Retrieve the knowledge graph filtered by the world's assigned capabilities. Uses bidirectional BFS
    to capture the complete connected subgraph.

    **Graph Structure**:
    The knowledge graph represents relationships between different entity types in the system:

    - **PERSONA → CAPABILITY**: via `can_perform` edge
    - **CAPABILITY → OD**: via `implemented_by` edge
    - **OD → TOOL**: via `uses` edge
    - **TOOL → SERVICE**: via `exposed_by` edge
    - **TOOL → ENTITY**: via `produces`, `requires`, or `modifies` edges

    **Filtering Behavior**:
    - When the world has assigned capabilities, the graph is automatically filtered to show only
    relevant nodes
    - Uses bidirectional BFS starting from the world's ODs to find all connected nodes
    - Returns `filtered: true` and `seedODs` array when filtering is applied
    - Returns full graph with `filtered: false` and info message when no capabilities are assigned

    **Use Cases**:
    - **Visualization**: Render interactive 2D/3D knowledge graph views
    - **Capability Discovery**: Understand available capabilities and their connections
    - **Impact Analysis**: Identify what entities are affected by running an OD
    - **Dependency Mapping**: Find tool and service dependencies
    - **Lineage Tracking**: Trace entity creation and modification paths


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[GetKnowledgeGraphResponse200, GetKnowledgeGraphResponse404, GetKnowledgeGraphResponse500]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
