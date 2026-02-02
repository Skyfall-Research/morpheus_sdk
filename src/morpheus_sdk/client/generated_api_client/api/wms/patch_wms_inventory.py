from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.patch_wms_inventory_body import PatchWMSInventoryBody
from ...types import Response


def _get_kwargs(
    world_id: str,
    inventory_id: str,
    *,
    body: PatchWMSInventoryBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/{world_id}/wms/inventory/{inventory_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    inventory_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInventoryBody,
) -> Response[ErrorResponse]:
    """Partially update inventory item


    ## Patch WMS Inventory Item

    Partially update an inventory record with only the specified fields. This is useful for updating
    specific properties like status, lot number, or location without affecting other fields.

    ### Allowed Fields
    - **inventoryStatus**: Update the inventory status (AVAILABLE, ALLOCATED, QUARANTINE, HOLD, DAMAGED,
    EXPIRED)
    - **lotNumber**: Update or assign a lot number for batch tracking
    - **expirationDate**: Update the expiration date for perishable items
    - **binId**: Update the storage location (move inventory to a different bin)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports quick status changes for inventory management

    ### Use Cases
    - Put inventory on hold for quality issues
    - Update lot numbers after verification
    - Move inventory to different bins
    - Update expiration dates
    - Mark inventory as damaged or expired


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (PatchWMSInventoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inventory_id=inventory_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    inventory_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInventoryBody,
) -> Optional[ErrorResponse]:
    """Partially update inventory item


    ## Patch WMS Inventory Item

    Partially update an inventory record with only the specified fields. This is useful for updating
    specific properties like status, lot number, or location without affecting other fields.

    ### Allowed Fields
    - **inventoryStatus**: Update the inventory status (AVAILABLE, ALLOCATED, QUARANTINE, HOLD, DAMAGED,
    EXPIRED)
    - **lotNumber**: Update or assign a lot number for batch tracking
    - **expirationDate**: Update the expiration date for perishable items
    - **binId**: Update the storage location (move inventory to a different bin)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports quick status changes for inventory management

    ### Use Cases
    - Put inventory on hold for quality issues
    - Update lot numbers after verification
    - Move inventory to different bins
    - Update expiration dates
    - Mark inventory as damaged or expired


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (PatchWMSInventoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        world_id=world_id,
        inventory_id=inventory_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    inventory_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInventoryBody,
) -> Response[ErrorResponse]:
    """Partially update inventory item


    ## Patch WMS Inventory Item

    Partially update an inventory record with only the specified fields. This is useful for updating
    specific properties like status, lot number, or location without affecting other fields.

    ### Allowed Fields
    - **inventoryStatus**: Update the inventory status (AVAILABLE, ALLOCATED, QUARANTINE, HOLD, DAMAGED,
    EXPIRED)
    - **lotNumber**: Update or assign a lot number for batch tracking
    - **expirationDate**: Update the expiration date for perishable items
    - **binId**: Update the storage location (move inventory to a different bin)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports quick status changes for inventory management

    ### Use Cases
    - Put inventory on hold for quality issues
    - Update lot numbers after verification
    - Move inventory to different bins
    - Update expiration dates
    - Mark inventory as damaged or expired


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (PatchWMSInventoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inventory_id=inventory_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    inventory_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: PatchWMSInventoryBody,
) -> Optional[ErrorResponse]:
    """Partially update inventory item


    ## Patch WMS Inventory Item

    Partially update an inventory record with only the specified fields. This is useful for updating
    specific properties like status, lot number, or location without affecting other fields.

    ### Allowed Fields
    - **inventoryStatus**: Update the inventory status (AVAILABLE, ALLOCATED, QUARANTINE, HOLD, DAMAGED,
    EXPIRED)
    - **lotNumber**: Update or assign a lot number for batch tracking
    - **expirationDate**: Update the expiration date for perishable items
    - **binId**: Update the storage location (move inventory to a different bin)

    ### Features
    - Partial updates - only specified fields are modified
    - Automatically updates the updatedAt timestamp
    - Supports quick status changes for inventory management

    ### Use Cases
    - Put inventory on hold for quality issues
    - Update lot numbers after verification
    - Move inventory to different bins
    - Update expiration dates
    - Mark inventory as damaged or expired


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (PatchWMSInventoryBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            inventory_id=inventory_id,
            client=client,
            body=body,
        )
    ).parsed
