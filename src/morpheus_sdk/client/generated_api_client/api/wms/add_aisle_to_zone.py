from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_aisle_to_zone_body import AddAisleToZoneBody
from ...models.add_aisle_to_zone_response_200 import AddAisleToZoneResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    zone_id: str,
    *,
    body: AddAisleToZoneBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/zones/{zone_id}/aisles",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddAisleToZoneResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddAisleToZoneResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AddAisleToZoneResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAisleToZoneBody,
) -> Response[Union[AddAisleToZoneResponse200, ErrorResponse]]:
    """Add aisle to zone


    Add aisle configuration to existing zone for layout management and organization.

    **Core Features**:
    - **Aisle Management**: Add new aisles to zone layout
    - **Configuration Tracking**: Maintain aisle type and identification
    - **Array Operations**: Uses MongoDB $push for aisle array management

    **Use Cases**:
    - **Zone Expansion**: Add aisles as zone grows
    - **Layout Updates**: Modify zone organization structure
    - **Configuration Management**: Maintain accurate zone layout data


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (AddAisleToZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddAisleToZoneResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAisleToZoneBody,
) -> Optional[Union[AddAisleToZoneResponse200, ErrorResponse]]:
    """Add aisle to zone


    Add aisle configuration to existing zone for layout management and organization.

    **Core Features**:
    - **Aisle Management**: Add new aisles to zone layout
    - **Configuration Tracking**: Maintain aisle type and identification
    - **Array Operations**: Uses MongoDB $push for aisle array management

    **Use Cases**:
    - **Zone Expansion**: Add aisles as zone grows
    - **Layout Updates**: Modify zone organization structure
    - **Configuration Management**: Maintain accurate zone layout data


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (AddAisleToZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddAisleToZoneResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        zone_id=zone_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAisleToZoneBody,
) -> Response[Union[AddAisleToZoneResponse200, ErrorResponse]]:
    """Add aisle to zone


    Add aisle configuration to existing zone for layout management and organization.

    **Core Features**:
    - **Aisle Management**: Add new aisles to zone layout
    - **Configuration Tracking**: Maintain aisle type and identification
    - **Array Operations**: Uses MongoDB $push for aisle array management

    **Use Cases**:
    - **Zone Expansion**: Add aisles as zone grows
    - **Layout Updates**: Modify zone organization structure
    - **Configuration Management**: Maintain accurate zone layout data


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (AddAisleToZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddAisleToZoneResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    zone_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddAisleToZoneBody,
) -> Optional[Union[AddAisleToZoneResponse200, ErrorResponse]]:
    """Add aisle to zone


    Add aisle configuration to existing zone for layout management and organization.

    **Core Features**:
    - **Aisle Management**: Add new aisles to zone layout
    - **Configuration Tracking**: Maintain aisle type and identification
    - **Array Operations**: Uses MongoDB $push for aisle array management

    **Use Cases**:
    - **Zone Expansion**: Add aisles as zone grows
    - **Layout Updates**: Modify zone organization structure
    - **Configuration Management**: Maintain accurate zone layout data


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (AddAisleToZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddAisleToZoneResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            zone_id=zone_id,
            client=client,
            body=body,
        )
    ).parsed
