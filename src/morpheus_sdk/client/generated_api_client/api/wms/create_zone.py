from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_zone_body import CreateZoneBody
from ...models.create_zone_response_201 import CreateZoneResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateZoneBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/zones",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateZoneResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateZoneResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateZoneResponse201, ErrorResponse]]:
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
    body: CreateZoneBody,
) -> Response[Union[CreateZoneResponse201, ErrorResponse]]:
    """Create new warehouse zone


    Create a new warehouse zone with specified configuration and capacity settings.

    **Core Features**:
    - **Zone Organization**: Define zone type, capacity, and temperature controls
    - **Aisle Management**: Configure initial aisle assignments for zone layout
    - **Auto-Generated Codes**: Automatic zoneId and zoneCode generation from zoneName

    **Use Cases**:
    - **Warehouse Setup**: Initial zone configuration during warehouse setup
    - **Zone Expansion**: Add new zones to accommodate growth
    - **Specialized Areas**: Create temperature-controlled or purpose-specific zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateZoneResponse201, ErrorResponse]]
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
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateZoneBody,
) -> Optional[Union[CreateZoneResponse201, ErrorResponse]]:
    """Create new warehouse zone


    Create a new warehouse zone with specified configuration and capacity settings.

    **Core Features**:
    - **Zone Organization**: Define zone type, capacity, and temperature controls
    - **Aisle Management**: Configure initial aisle assignments for zone layout
    - **Auto-Generated Codes**: Automatic zoneId and zoneCode generation from zoneName

    **Use Cases**:
    - **Warehouse Setup**: Initial zone configuration during warehouse setup
    - **Zone Expansion**: Add new zones to accommodate growth
    - **Specialized Areas**: Create temperature-controlled or purpose-specific zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateZoneResponse201, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateZoneBody,
) -> Response[Union[CreateZoneResponse201, ErrorResponse]]:
    """Create new warehouse zone


    Create a new warehouse zone with specified configuration and capacity settings.

    **Core Features**:
    - **Zone Organization**: Define zone type, capacity, and temperature controls
    - **Aisle Management**: Configure initial aisle assignments for zone layout
    - **Auto-Generated Codes**: Automatic zoneId and zoneCode generation from zoneName

    **Use Cases**:
    - **Warehouse Setup**: Initial zone configuration during warehouse setup
    - **Zone Expansion**: Add new zones to accommodate growth
    - **Specialized Areas**: Create temperature-controlled or purpose-specific zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateZoneResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: CreateZoneBody,
) -> Optional[Union[CreateZoneResponse201, ErrorResponse]]:
    """Create new warehouse zone


    Create a new warehouse zone with specified configuration and capacity settings.

    **Core Features**:
    - **Zone Organization**: Define zone type, capacity, and temperature controls
    - **Aisle Management**: Configure initial aisle assignments for zone layout
    - **Auto-Generated Codes**: Automatic zoneId and zoneCode generation from zoneName

    **Use Cases**:
    - **Warehouse Setup**: Initial zone configuration during warehouse setup
    - **Zone Expansion**: Add new zones to accommodate growth
    - **Specialized Areas**: Create temperature-controlled or purpose-specific zones


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateZoneResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
