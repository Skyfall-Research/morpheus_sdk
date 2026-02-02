from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_zone_body import UpdateZoneBody
from ...models.update_zone_response_200 import UpdateZoneResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    zone_id: str,
    *,
    body: UpdateZoneBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/zones/{zone_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateZoneResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateZoneResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateZoneResponse200]]:
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
    body: UpdateZoneBody,
) -> Response[Union[ErrorResponse, UpdateZoneResponse200]]:
    """Update zone configuration


    Update zone configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific zone fields without replacing entire record
    - **Configuration Changes**: Modify capacity, temperature settings, and type
    - **Validation**: Ensures data consistency during updates

    **Use Cases**:
    - **Capacity Adjustments**: Update storage capacity based on operational changes
    - **Type Changes**: Convert zone purposes based on operational needs
    - **Temperature Updates**: Modify climate control settings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (UpdateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateZoneResponse200]]
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
    body: UpdateZoneBody,
) -> Optional[Union[ErrorResponse, UpdateZoneResponse200]]:
    """Update zone configuration


    Update zone configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific zone fields without replacing entire record
    - **Configuration Changes**: Modify capacity, temperature settings, and type
    - **Validation**: Ensures data consistency during updates

    **Use Cases**:
    - **Capacity Adjustments**: Update storage capacity based on operational changes
    - **Type Changes**: Convert zone purposes based on operational needs
    - **Temperature Updates**: Modify climate control settings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (UpdateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateZoneResponse200]
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
    body: UpdateZoneBody,
) -> Response[Union[ErrorResponse, UpdateZoneResponse200]]:
    """Update zone configuration


    Update zone configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific zone fields without replacing entire record
    - **Configuration Changes**: Modify capacity, temperature settings, and type
    - **Validation**: Ensures data consistency during updates

    **Use Cases**:
    - **Capacity Adjustments**: Update storage capacity based on operational changes
    - **Type Changes**: Convert zone purposes based on operational needs
    - **Temperature Updates**: Modify climate control settings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (UpdateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateZoneResponse200]]
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
    body: UpdateZoneBody,
) -> Optional[Union[ErrorResponse, UpdateZoneResponse200]]:
    """Update zone configuration


    Update zone configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific zone fields without replacing entire record
    - **Configuration Changes**: Modify capacity, temperature settings, and type
    - **Validation**: Ensures data consistency during updates

    **Use Cases**:
    - **Capacity Adjustments**: Update storage capacity based on operational changes
    - **Type Changes**: Convert zone purposes based on operational needs
    - **Temperature Updates**: Modify climate control settings


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        zone_id (str):  Example: ZNE_507f1f77bcf86cd799439012.
        body (UpdateZoneBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateZoneResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            zone_id=zone_id,
            client=client,
            body=body,
        )
    ).parsed
