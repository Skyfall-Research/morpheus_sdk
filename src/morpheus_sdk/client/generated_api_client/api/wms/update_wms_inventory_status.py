from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_inventory_status_body import UpdateWMSInventoryStatusBody
from ...types import Response


def _get_kwargs(
    world_id: str,
    inventory_id: str,
    *,
    body: UpdateWMSInventoryStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/inventory/{inventory_id}/status",
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
    body: UpdateWMSInventoryStatusBody,
) -> Response[ErrorResponse]:
    """Update inventory status


    ## Update WMS Inventory Status

    Update the status of a specific inventory item for inventory control and management operations.

    ### Features
    - **Status Management**: Change inventory item status for operational control
    - **Validation**: Ensures valid status values are provided
    - **Audit Trail**: Automatically updates timestamp on status change

    ### Valid Status Values
    - **AVAILABLE**: Ready for allocation and fulfillment
    - **HOLD**: Temporarily held for review or special handling
    - **QUARANTINE**: Isolated for quality inspection
    - **ALLOCATED**: Reserved for specific orders
    - **EXPIRED**: Past expiration date, not available for sale

    ### Use Cases
    - **Quality Control**: Place items on hold or quarantine for inspection
    - **Inventory Adjustment**: Update status based on physical inspection
    - **Expiration Management**: Mark expired inventory appropriately


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (UpdateWMSInventoryStatusBody):

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
    body: UpdateWMSInventoryStatusBody,
) -> Optional[ErrorResponse]:
    """Update inventory status


    ## Update WMS Inventory Status

    Update the status of a specific inventory item for inventory control and management operations.

    ### Features
    - **Status Management**: Change inventory item status for operational control
    - **Validation**: Ensures valid status values are provided
    - **Audit Trail**: Automatically updates timestamp on status change

    ### Valid Status Values
    - **AVAILABLE**: Ready for allocation and fulfillment
    - **HOLD**: Temporarily held for review or special handling
    - **QUARANTINE**: Isolated for quality inspection
    - **ALLOCATED**: Reserved for specific orders
    - **EXPIRED**: Past expiration date, not available for sale

    ### Use Cases
    - **Quality Control**: Place items on hold or quarantine for inspection
    - **Inventory Adjustment**: Update status based on physical inspection
    - **Expiration Management**: Mark expired inventory appropriately


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (UpdateWMSInventoryStatusBody):

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
    body: UpdateWMSInventoryStatusBody,
) -> Response[ErrorResponse]:
    """Update inventory status


    ## Update WMS Inventory Status

    Update the status of a specific inventory item for inventory control and management operations.

    ### Features
    - **Status Management**: Change inventory item status for operational control
    - **Validation**: Ensures valid status values are provided
    - **Audit Trail**: Automatically updates timestamp on status change

    ### Valid Status Values
    - **AVAILABLE**: Ready for allocation and fulfillment
    - **HOLD**: Temporarily held for review or special handling
    - **QUARANTINE**: Isolated for quality inspection
    - **ALLOCATED**: Reserved for specific orders
    - **EXPIRED**: Past expiration date, not available for sale

    ### Use Cases
    - **Quality Control**: Place items on hold or quarantine for inspection
    - **Inventory Adjustment**: Update status based on physical inspection
    - **Expiration Management**: Mark expired inventory appropriately


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (UpdateWMSInventoryStatusBody):

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
    body: UpdateWMSInventoryStatusBody,
) -> Optional[ErrorResponse]:
    """Update inventory status


    ## Update WMS Inventory Status

    Update the status of a specific inventory item for inventory control and management operations.

    ### Features
    - **Status Management**: Change inventory item status for operational control
    - **Validation**: Ensures valid status values are provided
    - **Audit Trail**: Automatically updates timestamp on status change

    ### Valid Status Values
    - **AVAILABLE**: Ready for allocation and fulfillment
    - **HOLD**: Temporarily held for review or special handling
    - **QUARANTINE**: Isolated for quality inspection
    - **ALLOCATED**: Reserved for specific orders
    - **EXPIRED**: Past expiration date, not available for sale

    ### Use Cases
    - **Quality Control**: Place items on hold or quarantine for inspection
    - **Inventory Adjustment**: Update status based on physical inspection
    - **Expiration Management**: Mark expired inventory appropriately


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inventory_id (str):  Example: wms_inventory_674565c1234567890abcdef.
        body (UpdateWMSInventoryStatusBody):

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
