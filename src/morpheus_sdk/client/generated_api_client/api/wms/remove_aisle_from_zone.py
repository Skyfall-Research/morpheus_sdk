from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remove_aisle_from_zone_response_200 import RemoveAisleFromZoneResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    zone_id: str,
    aisle_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/{world_id}/wms/zones/{zone_id}/aisles/{aisle_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[RemoveAisleFromZoneResponse200]:
    if response.status_code == 200:
        response_200 = RemoveAisleFromZoneResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[RemoveAisleFromZoneResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    zone_id: str,
    aisle_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RemoveAisleFromZoneResponse200]:
    """Remove aisle from zone


    Remove specific aisle from zone configuration for layout management.

    **Core Features**:
    - **Aisle Removal**: Remove specific aisles from zone layout
    - **Configuration Cleanup**: Maintain accurate zone organization
    - **Array Operations**: Uses MongoDB $pull for aisle array management

    **Use Cases**:
    - **Layout Optimization**: Remove unused or inefficient aisles
    - **Zone Restructuring**: Modify zone organization for operational efficiency
    - **Configuration Maintenance**: Keep zone layout data current


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        aisle_id (str):  Example: AISLE_A1_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveAisleFromZoneResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        aisle_id=aisle_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    zone_id: str,
    aisle_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RemoveAisleFromZoneResponse200]:
    """Remove aisle from zone


    Remove specific aisle from zone configuration for layout management.

    **Core Features**:
    - **Aisle Removal**: Remove specific aisles from zone layout
    - **Configuration Cleanup**: Maintain accurate zone organization
    - **Array Operations**: Uses MongoDB $pull for aisle array management

    **Use Cases**:
    - **Layout Optimization**: Remove unused or inefficient aisles
    - **Zone Restructuring**: Modify zone organization for operational efficiency
    - **Configuration Maintenance**: Keep zone layout data current


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        aisle_id (str):  Example: AISLE_A1_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveAisleFromZoneResponse200
    """

    return sync_detailed(
        world_id=world_id,
        zone_id=zone_id,
        aisle_id=aisle_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    zone_id: str,
    aisle_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[RemoveAisleFromZoneResponse200]:
    """Remove aisle from zone


    Remove specific aisle from zone configuration for layout management.

    **Core Features**:
    - **Aisle Removal**: Remove specific aisles from zone layout
    - **Configuration Cleanup**: Maintain accurate zone organization
    - **Array Operations**: Uses MongoDB $pull for aisle array management

    **Use Cases**:
    - **Layout Optimization**: Remove unused or inefficient aisles
    - **Zone Restructuring**: Modify zone organization for operational efficiency
    - **Configuration Maintenance**: Keep zone layout data current


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        aisle_id (str):  Example: AISLE_A1_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RemoveAisleFromZoneResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        zone_id=zone_id,
        aisle_id=aisle_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    zone_id: str,
    aisle_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[RemoveAisleFromZoneResponse200]:
    """Remove aisle from zone


    Remove specific aisle from zone configuration for layout management.

    **Core Features**:
    - **Aisle Removal**: Remove specific aisles from zone layout
    - **Configuration Cleanup**: Maintain accurate zone organization
    - **Array Operations**: Uses MongoDB $pull for aisle array management

    **Use Cases**:
    - **Layout Optimization**: Remove unused or inefficient aisles
    - **Zone Restructuring**: Modify zone organization for operational efficiency
    - **Configuration Maintenance**: Keep zone layout data current


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        aisle_id (str):  Example: AISLE_A1_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        RemoveAisleFromZoneResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            zone_id=zone_id,
            aisle_id=aisle_id,
            client=client,
        )
    ).parsed
