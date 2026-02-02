from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_item_to_wms_receiving_transaction_body import AddItemToWMSReceivingTransactionBody
from ...models.add_item_to_wms_receiving_transaction_response_200 import AddItemToWMSReceivingTransactionResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    transaction_id: str,
    *,
    body: AddItemToWMSReceivingTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/receiving-transactions/{transaction_id}/items",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddItemToWMSReceivingTransactionResponse200.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddItemToWMSReceivingTransactionBody,
) -> Response[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]:
    """Add item to receiving transaction


    ## Add Item to WMS Receiving Transaction

    Add a new item to an existing receiving transaction for multi-item receiving operations.

    ### Features
    - **Multi-Item Support**: Add multiple products to single receiving transaction
    - **Batch Tracking**: Lot numbers and serial number support for traceability
    - **Condition Recording**: Item condition assessment and documentation
    - **Location Assignment**: Specific location assignment for received items
    - **Quantity Validation**: Expected vs received quantity tracking
    - **Real-time Updates**: Immediate transaction update with new item data

    ### Item Data Includes
    - **Product Information**: SKU, product name, and identification
    - **Quantity Tracking**: Expected vs received quantity comparison
    - **Batch/Serial Data**: Lot numbers and serial number arrays
    - **Condition Assessment**: Item condition for quality control
    - **Location Assignment**: Specific bin/zone location targeting
    - **Measurement Units**: Unit of measure specification

    ### Business Logic
    - Items are appended to existing transaction's item array
    - Each item maintains independent quantity and condition tracking
    - Location assignments can be bin-specific or zone-level
    - Serial numbers stored as array for individual item tracking
    - Condition assessment supports quality control workflows

    **CRITICAL NOTE**: Parameter uses 'transactionId' but targets model's 'receivingId' field.

    ### Use Cases
    - **Multi-Product Receiving**: Add different products to single transaction
    - **Partial Receiving**: Add items as they are processed sequentially
    - **Location-Specific Storage**: Assign items to specific storage locations
    - **Batch Management**: Maintain lot number and serial tracking
    - **Quality Segregation**: Separate items by condition assessment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (AddItemToWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddItemToWMSReceivingTransactionBody,
) -> Optional[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]:
    """Add item to receiving transaction


    ## Add Item to WMS Receiving Transaction

    Add a new item to an existing receiving transaction for multi-item receiving operations.

    ### Features
    - **Multi-Item Support**: Add multiple products to single receiving transaction
    - **Batch Tracking**: Lot numbers and serial number support for traceability
    - **Condition Recording**: Item condition assessment and documentation
    - **Location Assignment**: Specific location assignment for received items
    - **Quantity Validation**: Expected vs received quantity tracking
    - **Real-time Updates**: Immediate transaction update with new item data

    ### Item Data Includes
    - **Product Information**: SKU, product name, and identification
    - **Quantity Tracking**: Expected vs received quantity comparison
    - **Batch/Serial Data**: Lot numbers and serial number arrays
    - **Condition Assessment**: Item condition for quality control
    - **Location Assignment**: Specific bin/zone location targeting
    - **Measurement Units**: Unit of measure specification

    ### Business Logic
    - Items are appended to existing transaction's item array
    - Each item maintains independent quantity and condition tracking
    - Location assignments can be bin-specific or zone-level
    - Serial numbers stored as array for individual item tracking
    - Condition assessment supports quality control workflows

    **CRITICAL NOTE**: Parameter uses 'transactionId' but targets model's 'receivingId' field.

    ### Use Cases
    - **Multi-Product Receiving**: Add different products to single transaction
    - **Partial Receiving**: Add items as they are processed sequentially
    - **Location-Specific Storage**: Assign items to specific storage locations
    - **Batch Management**: Maintain lot number and serial tracking
    - **Quality Segregation**: Separate items by condition assessment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (AddItemToWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        transaction_id=transaction_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddItemToWMSReceivingTransactionBody,
) -> Response[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]:
    """Add item to receiving transaction


    ## Add Item to WMS Receiving Transaction

    Add a new item to an existing receiving transaction for multi-item receiving operations.

    ### Features
    - **Multi-Item Support**: Add multiple products to single receiving transaction
    - **Batch Tracking**: Lot numbers and serial number support for traceability
    - **Condition Recording**: Item condition assessment and documentation
    - **Location Assignment**: Specific location assignment for received items
    - **Quantity Validation**: Expected vs received quantity tracking
    - **Real-time Updates**: Immediate transaction update with new item data

    ### Item Data Includes
    - **Product Information**: SKU, product name, and identification
    - **Quantity Tracking**: Expected vs received quantity comparison
    - **Batch/Serial Data**: Lot numbers and serial number arrays
    - **Condition Assessment**: Item condition for quality control
    - **Location Assignment**: Specific bin/zone location targeting
    - **Measurement Units**: Unit of measure specification

    ### Business Logic
    - Items are appended to existing transaction's item array
    - Each item maintains independent quantity and condition tracking
    - Location assignments can be bin-specific or zone-level
    - Serial numbers stored as array for individual item tracking
    - Condition assessment supports quality control workflows

    **CRITICAL NOTE**: Parameter uses 'transactionId' but targets model's 'receivingId' field.

    ### Use Cases
    - **Multi-Product Receiving**: Add different products to single transaction
    - **Partial Receiving**: Add items as they are processed sequentially
    - **Location-Specific Storage**: Assign items to specific storage locations
    - **Batch Management**: Maintain lot number and serial tracking
    - **Quality Segregation**: Separate items by condition assessment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (AddItemToWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        transaction_id=transaction_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    transaction_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddItemToWMSReceivingTransactionBody,
) -> Optional[Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]]:
    """Add item to receiving transaction


    ## Add Item to WMS Receiving Transaction

    Add a new item to an existing receiving transaction for multi-item receiving operations.

    ### Features
    - **Multi-Item Support**: Add multiple products to single receiving transaction
    - **Batch Tracking**: Lot numbers and serial number support for traceability
    - **Condition Recording**: Item condition assessment and documentation
    - **Location Assignment**: Specific location assignment for received items
    - **Quantity Validation**: Expected vs received quantity tracking
    - **Real-time Updates**: Immediate transaction update with new item data

    ### Item Data Includes
    - **Product Information**: SKU, product name, and identification
    - **Quantity Tracking**: Expected vs received quantity comparison
    - **Batch/Serial Data**: Lot numbers and serial number arrays
    - **Condition Assessment**: Item condition for quality control
    - **Location Assignment**: Specific bin/zone location targeting
    - **Measurement Units**: Unit of measure specification

    ### Business Logic
    - Items are appended to existing transaction's item array
    - Each item maintains independent quantity and condition tracking
    - Location assignments can be bin-specific or zone-level
    - Serial numbers stored as array for individual item tracking
    - Condition assessment supports quality control workflows

    **CRITICAL NOTE**: Parameter uses 'transactionId' but targets model's 'receivingId' field.

    ### Use Cases
    - **Multi-Product Receiving**: Add different products to single transaction
    - **Partial Receiving**: Add items as they are processed sequentially
    - **Location-Specific Storage**: Assign items to specific storage locations
    - **Batch Management**: Maintain lot number and serial tracking
    - **Quality Segregation**: Separate items by condition assessment


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (AddItemToWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddItemToWMSReceivingTransactionResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
