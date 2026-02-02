from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_inventory_transaction_body import CreateWMSInventoryTransactionBody
from ...models.create_wms_inventory_transaction_response_201 import CreateWMSInventoryTransactionResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSInventoryTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/inventory-transactions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSInventoryTransactionResponse201.from_dict(response.json())

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
) -> Response[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]:
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
    body: CreateWMSInventoryTransactionBody,
) -> Response[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]:
    """Create inventory transaction


    ## Create WMS Inventory Transaction

    Create a new inventory transaction to record movement, adjustment, or other inventory operations
    within the warehouse.

    ### Features
    - **Transaction Recording**: Document all inventory movements and changes
    - **Multi-Transaction Types**: Support for RECEIVE, PUTAWAY, PICK, MOVE, ADJUST, CYCLE_COUNT,
    RETURN, DAMAGE, SHIP
    - **Bin-to-Bin Tracking**: Record inventory movements between storage locations
    - **Reference Integration**: Link transactions to orders, tasks, and cycle counts
    - **Lot/License Plate Tracking**: Support for batch and container tracking
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId, transactionType, productId, and quantity are required
    - transactionId is auto-generated with wms_inventory-transaction prefix
    - transactionDate defaults to current timestamp if not provided
    - Supports bin-to-bin movement tracking with fromBinId/toBinId
    - referenceType must be one of: PO, ORDER, TASK, CYCLE_COUNT

    ### Use Cases
    - **Receiving Operations**: Record inventory receipt from inbound orders
    - **Putaway Activities**: Track movement from receiving to storage locations
    - **Picking Operations**: Document inventory removal for outbound orders
    - **Inventory Adjustments**: Record quantity adjustments and corrections
    - **Cycle Count Updates**: Apply cycle count variances to inventory
    - **Returns Processing**: Handle returned merchandise transactions
    - **Damage Recording**: Document damaged inventory write-offs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInventoryTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]
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
    body: CreateWMSInventoryTransactionBody,
) -> Optional[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]:
    """Create inventory transaction


    ## Create WMS Inventory Transaction

    Create a new inventory transaction to record movement, adjustment, or other inventory operations
    within the warehouse.

    ### Features
    - **Transaction Recording**: Document all inventory movements and changes
    - **Multi-Transaction Types**: Support for RECEIVE, PUTAWAY, PICK, MOVE, ADJUST, CYCLE_COUNT,
    RETURN, DAMAGE, SHIP
    - **Bin-to-Bin Tracking**: Record inventory movements between storage locations
    - **Reference Integration**: Link transactions to orders, tasks, and cycle counts
    - **Lot/License Plate Tracking**: Support for batch and container tracking
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId, transactionType, productId, and quantity are required
    - transactionId is auto-generated with wms_inventory-transaction prefix
    - transactionDate defaults to current timestamp if not provided
    - Supports bin-to-bin movement tracking with fromBinId/toBinId
    - referenceType must be one of: PO, ORDER, TASK, CYCLE_COUNT

    ### Use Cases
    - **Receiving Operations**: Record inventory receipt from inbound orders
    - **Putaway Activities**: Track movement from receiving to storage locations
    - **Picking Operations**: Document inventory removal for outbound orders
    - **Inventory Adjustments**: Record quantity adjustments and corrections
    - **Cycle Count Updates**: Apply cycle count variances to inventory
    - **Returns Processing**: Handle returned merchandise transactions
    - **Damage Recording**: Document damaged inventory write-offs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInventoryTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]
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
    body: CreateWMSInventoryTransactionBody,
) -> Response[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]:
    """Create inventory transaction


    ## Create WMS Inventory Transaction

    Create a new inventory transaction to record movement, adjustment, or other inventory operations
    within the warehouse.

    ### Features
    - **Transaction Recording**: Document all inventory movements and changes
    - **Multi-Transaction Types**: Support for RECEIVE, PUTAWAY, PICK, MOVE, ADJUST, CYCLE_COUNT,
    RETURN, DAMAGE, SHIP
    - **Bin-to-Bin Tracking**: Record inventory movements between storage locations
    - **Reference Integration**: Link transactions to orders, tasks, and cycle counts
    - **Lot/License Plate Tracking**: Support for batch and container tracking
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId, transactionType, productId, and quantity are required
    - transactionId is auto-generated with wms_inventory-transaction prefix
    - transactionDate defaults to current timestamp if not provided
    - Supports bin-to-bin movement tracking with fromBinId/toBinId
    - referenceType must be one of: PO, ORDER, TASK, CYCLE_COUNT

    ### Use Cases
    - **Receiving Operations**: Record inventory receipt from inbound orders
    - **Putaway Activities**: Track movement from receiving to storage locations
    - **Picking Operations**: Document inventory removal for outbound orders
    - **Inventory Adjustments**: Record quantity adjustments and corrections
    - **Cycle Count Updates**: Apply cycle count variances to inventory
    - **Returns Processing**: Handle returned merchandise transactions
    - **Damage Recording**: Document damaged inventory write-offs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInventoryTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]
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
    body: CreateWMSInventoryTransactionBody,
) -> Optional[Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]]:
    """Create inventory transaction


    ## Create WMS Inventory Transaction

    Create a new inventory transaction to record movement, adjustment, or other inventory operations
    within the warehouse.

    ### Features
    - **Transaction Recording**: Document all inventory movements and changes
    - **Multi-Transaction Types**: Support for RECEIVE, PUTAWAY, PICK, MOVE, ADJUST, CYCLE_COUNT,
    RETURN, DAMAGE, SHIP
    - **Bin-to-Bin Tracking**: Record inventory movements between storage locations
    - **Reference Integration**: Link transactions to orders, tasks, and cycle counts
    - **Lot/License Plate Tracking**: Support for batch and container tracking
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId, transactionType, productId, and quantity are required
    - transactionId is auto-generated with wms_inventory-transaction prefix
    - transactionDate defaults to current timestamp if not provided
    - Supports bin-to-bin movement tracking with fromBinId/toBinId
    - referenceType must be one of: PO, ORDER, TASK, CYCLE_COUNT

    ### Use Cases
    - **Receiving Operations**: Record inventory receipt from inbound orders
    - **Putaway Activities**: Track movement from receiving to storage locations
    - **Picking Operations**: Document inventory removal for outbound orders
    - **Inventory Adjustments**: Record quantity adjustments and corrections
    - **Cycle Count Updates**: Apply cycle count variances to inventory
    - **Returns Processing**: Handle returned merchandise transactions
    - **Damage Recording**: Document damaged inventory write-offs


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSInventoryTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSInventoryTransactionResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
