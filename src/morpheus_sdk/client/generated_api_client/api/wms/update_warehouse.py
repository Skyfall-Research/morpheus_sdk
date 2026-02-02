from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_warehouse_body import UpdateWarehouseBody
from ...models.update_warehouse_response_200 import UpdateWarehouseResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    warehouse_id: str,
    *,
    body: UpdateWarehouseBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/warehouses/{warehouse_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWarehouseResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWarehouseResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWarehouseResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWarehouseBody,
) -> Response[Union[ErrorResponse, UpdateWarehouseResponse200]]:
    """Update warehouse configuration


    Update warehouse configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific warehouse fields without replacing entire record
    - **Configuration Changes**: Modify address, timezone, type, and operational settings
    - **Validation**: Ensures data consistency during updates
    - **Flexible Modification**: Support for incremental configuration changes

    **Use Cases**:
    - **Address Updates**: Update warehouse physical location information
    - **Timezone Changes**: Adjust timezone settings for operational requirements
    - **Type Modifications**: Convert warehouse purposes based on operational needs
    - **Configuration Maintenance**: Keep warehouse data current and accurate


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.
        body (UpdateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWarehouseResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWarehouseBody,
) -> Optional[Union[ErrorResponse, UpdateWarehouseResponse200]]:
    """Update warehouse configuration


    Update warehouse configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific warehouse fields without replacing entire record
    - **Configuration Changes**: Modify address, timezone, type, and operational settings
    - **Validation**: Ensures data consistency during updates
    - **Flexible Modification**: Support for incremental configuration changes

    **Use Cases**:
    - **Address Updates**: Update warehouse physical location information
    - **Timezone Changes**: Adjust timezone settings for operational requirements
    - **Type Modifications**: Convert warehouse purposes based on operational needs
    - **Configuration Maintenance**: Keep warehouse data current and accurate


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.
        body (UpdateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWarehouseResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        warehouse_id=warehouse_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWarehouseBody,
) -> Response[Union[ErrorResponse, UpdateWarehouseResponse200]]:
    """Update warehouse configuration


    Update warehouse configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific warehouse fields without replacing entire record
    - **Configuration Changes**: Modify address, timezone, type, and operational settings
    - **Validation**: Ensures data consistency during updates
    - **Flexible Modification**: Support for incremental configuration changes

    **Use Cases**:
    - **Address Updates**: Update warehouse physical location information
    - **Timezone Changes**: Adjust timezone settings for operational requirements
    - **Type Modifications**: Convert warehouse purposes based on operational needs
    - **Configuration Maintenance**: Keep warehouse data current and accurate


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.
        body (UpdateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWarehouseResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        warehouse_id=warehouse_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    warehouse_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWarehouseBody,
) -> Optional[Union[ErrorResponse, UpdateWarehouseResponse200]]:
    """Update warehouse configuration


    Update warehouse configuration with partial data for operational adjustments.

    **Core Features**:
    - **Partial Updates**: Update specific warehouse fields without replacing entire record
    - **Configuration Changes**: Modify address, timezone, type, and operational settings
    - **Validation**: Ensures data consistency during updates
    - **Flexible Modification**: Support for incremental configuration changes

    **Use Cases**:
    - **Address Updates**: Update warehouse physical location information
    - **Timezone Changes**: Adjust timezone settings for operational requirements
    - **Type Modifications**: Convert warehouse purposes based on operational needs
    - **Configuration Maintenance**: Keep warehouse data current and accurate


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        warehouse_id (str):  Example: WH_507f1f77bcf86cd799439012.
        body (UpdateWarehouseBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWarehouseResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            warehouse_id=warehouse_id,
            client=client,
            body=body,
        )
    ).parsed
