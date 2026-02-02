from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_receiving_transaction_body import CreateWMSReceivingTransactionBody
from ...models.create_wms_receiving_transaction_response_201 import CreateWMSReceivingTransactionResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSReceivingTransactionBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/receiving-transactions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSReceivingTransactionResponse201.from_dict(response.json())

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
) -> Response[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]:
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
    body: CreateWMSReceivingTransactionBody,
) -> Response[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]:
    r"""Create receiving transaction


    ## Create WMS Receiving Transaction

    Create a new receiving transaction to record the receipt of inventory items from inbound orders.

    ### Features
    - **Receiving Documentation**: Create structured records of goods received
    - **Quality Control Integration**: Record quality inspection and condition assessment
    - **Batch/Serial Tracking**: Support for lot numbers and serial number recording
    - **Damage Recording**: Document damaged items with detailed notes
    - **Status Management**: Track receiving status through workflow stages
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId and inboundOrderId are required for transaction creation
    - Transaction automatically receives a unique receivingId (auto-generated)
    - receivingStatus defaults to \"RECEIVED\" upon creation
    - Quality status defaults to \"PENDING\" until inspection
    - Each transaction represents receipt of specific products/quantities
    - Supports putaway location assignment for warehouse management

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior (transactionId
    parameter usage).

    ### Use Cases
    - **Inbound Receipt Processing**: Record receipt of purchase order items
    - **Quality Control Documentation**: Track inspection results and quality status
    - **Batch Compliance**: Maintain lot number and expiration date records
    - **Damage Claims**: Document damaged goods for vendor claims processing
    - **Inventory Updates**: Trigger inventory adjustments based on received quantities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]
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
    body: CreateWMSReceivingTransactionBody,
) -> Optional[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]:
    r"""Create receiving transaction


    ## Create WMS Receiving Transaction

    Create a new receiving transaction to record the receipt of inventory items from inbound orders.

    ### Features
    - **Receiving Documentation**: Create structured records of goods received
    - **Quality Control Integration**: Record quality inspection and condition assessment
    - **Batch/Serial Tracking**: Support for lot numbers and serial number recording
    - **Damage Recording**: Document damaged items with detailed notes
    - **Status Management**: Track receiving status through workflow stages
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId and inboundOrderId are required for transaction creation
    - Transaction automatically receives a unique receivingId (auto-generated)
    - receivingStatus defaults to \"RECEIVED\" upon creation
    - Quality status defaults to \"PENDING\" until inspection
    - Each transaction represents receipt of specific products/quantities
    - Supports putaway location assignment for warehouse management

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior (transactionId
    parameter usage).

    ### Use Cases
    - **Inbound Receipt Processing**: Record receipt of purchase order items
    - **Quality Control Documentation**: Track inspection results and quality status
    - **Batch Compliance**: Maintain lot number and expiration date records
    - **Damage Claims**: Document damaged goods for vendor claims processing
    - **Inventory Updates**: Trigger inventory adjustments based on received quantities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]
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
    body: CreateWMSReceivingTransactionBody,
) -> Response[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]:
    r"""Create receiving transaction


    ## Create WMS Receiving Transaction

    Create a new receiving transaction to record the receipt of inventory items from inbound orders.

    ### Features
    - **Receiving Documentation**: Create structured records of goods received
    - **Quality Control Integration**: Record quality inspection and condition assessment
    - **Batch/Serial Tracking**: Support for lot numbers and serial number recording
    - **Damage Recording**: Document damaged items with detailed notes
    - **Status Management**: Track receiving status through workflow stages
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId and inboundOrderId are required for transaction creation
    - Transaction automatically receives a unique receivingId (auto-generated)
    - receivingStatus defaults to \"RECEIVED\" upon creation
    - Quality status defaults to \"PENDING\" until inspection
    - Each transaction represents receipt of specific products/quantities
    - Supports putaway location assignment for warehouse management

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior (transactionId
    parameter usage).

    ### Use Cases
    - **Inbound Receipt Processing**: Record receipt of purchase order items
    - **Quality Control Documentation**: Track inspection results and quality status
    - **Batch Compliance**: Maintain lot number and expiration date records
    - **Damage Claims**: Document damaged goods for vendor claims processing
    - **Inventory Updates**: Trigger inventory adjustments based on received quantities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]
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
    body: CreateWMSReceivingTransactionBody,
) -> Optional[Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]]:
    r"""Create receiving transaction


    ## Create WMS Receiving Transaction

    Create a new receiving transaction to record the receipt of inventory items from inbound orders.

    ### Features
    - **Receiving Documentation**: Create structured records of goods received
    - **Quality Control Integration**: Record quality inspection and condition assessment
    - **Batch/Serial Tracking**: Support for lot numbers and serial number recording
    - **Damage Recording**: Document damaged items with detailed notes
    - **Status Management**: Track receiving status through workflow stages
    - **Auto-ID Generation**: Automatic transaction ID assignment for unique tracking

    ### Business Logic
    - warehouseId and inboundOrderId are required for transaction creation
    - Transaction automatically receives a unique receivingId (auto-generated)
    - receivingStatus defaults to \"RECEIVED\" upon creation
    - Quality status defaults to \"PENDING\" until inspection
    - Each transaction represents receipt of specific products/quantities
    - Supports putaway location assignment for warehouse management

    **CRITICAL NOTE**: The model defines the primary identifier as 'receivingId' but the implementation
    uses 'transactionId' in queries. This documentation reflects the actual API behavior (transactionId
    parameter usage).

    ### Use Cases
    - **Inbound Receipt Processing**: Record receipt of purchase order items
    - **Quality Control Documentation**: Track inspection results and quality status
    - **Batch Compliance**: Maintain lot number and expiration date records
    - **Damage Claims**: Document damaged goods for vendor claims processing
    - **Inventory Updates**: Trigger inventory adjustments based on received quantities


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSReceivingTransactionBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSReceivingTransactionResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
