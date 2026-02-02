from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_inbound_order_receiving_progress_body import UpdateWMSInboundOrderReceivingProgressBody
from ...models.update_wms_inbound_order_receiving_progress_response_200 import (
    UpdateWMSInboundOrderReceivingProgressResponse200,
)
from ...types import Response


def _get_kwargs(
    world_id: str,
    inbound_order_id: str,
    *,
    body: UpdateWMSInboundOrderReceivingProgressBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/inbound-orders/{inbound_order_id}/receiving-progress",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSInboundOrderReceivingProgressResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSInboundOrderReceivingProgressBody,
) -> Response[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]:
    """Update receiving progress


    ## Update WMS Inbound Order Receiving Progress

    Update the receiving progress for specific line items within an inbound order, tracking quantities
    received and batch information.

    ### Features
    - **Line-Item Tracking**: Update receiving progress for individual product lines
    - **Quantity Management**: Track received quantities against expected quantities
    - **Batch Tracking**: Record lot numbers and expiration dates for compliance
    - **Progress Calculation**: Automatic calculation of receiving completion percentages
    - **Real-Time Updates**: Immediate visibility into receiving operations progress

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - lineNumber must exist within the order's line items
    - receivedQuantity is added to existing received quantity (cumulative)
    - Line status automatically updated based on receiving progress:
      - RECEIVING: When receivedQuantity > 0 but < expectedQuantity
      - RECEIVED: When receivedQuantity >= expectedQuantity
    - Lot number and expiration date updates support batch tracking requirements

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **lineNumber**: Required - Line number within the order for specific product
    - **receivedQuantity**: Required - Quantity received in this receiving session
    - **lotNumber**: Optional - Lot number for batch tracking and traceability
    - **expirationDate**: Optional - Product expiration date for perishable items

    ### Business Rules
    - Received quantities are cumulative across multiple receiving sessions
    - Line status updates automatically based on receiving completion
    - Lot numbers and expiration dates support regulatory compliance
    - Progress tracking enables real-time receiving dashboard updates

    ### Use Cases
    - **Receiving Operations**: Track progress as products are received and processed
    - **Quality Control**: Record batch information during receiving inspection
    - **Inventory Management**: Update inventory levels with received quantities
    - **Compliance Tracking**: Maintain lot numbers and expiration dates for regulations
    - **Performance Monitoring**: Monitor receiving efficiency and completion rates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderReceivingProgressBody):  Example: {'lineNumber': 1,
            'receivedQuantity': 150, 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSInboundOrderReceivingProgressBody,
) -> Optional[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]:
    """Update receiving progress


    ## Update WMS Inbound Order Receiving Progress

    Update the receiving progress for specific line items within an inbound order, tracking quantities
    received and batch information.

    ### Features
    - **Line-Item Tracking**: Update receiving progress for individual product lines
    - **Quantity Management**: Track received quantities against expected quantities
    - **Batch Tracking**: Record lot numbers and expiration dates for compliance
    - **Progress Calculation**: Automatic calculation of receiving completion percentages
    - **Real-Time Updates**: Immediate visibility into receiving operations progress

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - lineNumber must exist within the order's line items
    - receivedQuantity is added to existing received quantity (cumulative)
    - Line status automatically updated based on receiving progress:
      - RECEIVING: When receivedQuantity > 0 but < expectedQuantity
      - RECEIVED: When receivedQuantity >= expectedQuantity
    - Lot number and expiration date updates support batch tracking requirements

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **lineNumber**: Required - Line number within the order for specific product
    - **receivedQuantity**: Required - Quantity received in this receiving session
    - **lotNumber**: Optional - Lot number for batch tracking and traceability
    - **expirationDate**: Optional - Product expiration date for perishable items

    ### Business Rules
    - Received quantities are cumulative across multiple receiving sessions
    - Line status updates automatically based on receiving completion
    - Lot numbers and expiration dates support regulatory compliance
    - Progress tracking enables real-time receiving dashboard updates

    ### Use Cases
    - **Receiving Operations**: Track progress as products are received and processed
    - **Quality Control**: Record batch information during receiving inspection
    - **Inventory Management**: Update inventory levels with received quantities
    - **Compliance Tracking**: Maintain lot numbers and expiration dates for regulations
    - **Performance Monitoring**: Monitor receiving efficiency and completion rates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderReceivingProgressBody):  Example: {'lineNumber': 1,
            'receivedQuantity': 150, 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSInboundOrderReceivingProgressBody,
) -> Response[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]:
    """Update receiving progress


    ## Update WMS Inbound Order Receiving Progress

    Update the receiving progress for specific line items within an inbound order, tracking quantities
    received and batch information.

    ### Features
    - **Line-Item Tracking**: Update receiving progress for individual product lines
    - **Quantity Management**: Track received quantities against expected quantities
    - **Batch Tracking**: Record lot numbers and expiration dates for compliance
    - **Progress Calculation**: Automatic calculation of receiving completion percentages
    - **Real-Time Updates**: Immediate visibility into receiving operations progress

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - lineNumber must exist within the order's line items
    - receivedQuantity is added to existing received quantity (cumulative)
    - Line status automatically updated based on receiving progress:
      - RECEIVING: When receivedQuantity > 0 but < expectedQuantity
      - RECEIVED: When receivedQuantity >= expectedQuantity
    - Lot number and expiration date updates support batch tracking requirements

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **lineNumber**: Required - Line number within the order for specific product
    - **receivedQuantity**: Required - Quantity received in this receiving session
    - **lotNumber**: Optional - Lot number for batch tracking and traceability
    - **expirationDate**: Optional - Product expiration date for perishable items

    ### Business Rules
    - Received quantities are cumulative across multiple receiving sessions
    - Line status updates automatically based on receiving completion
    - Lot numbers and expiration dates support regulatory compliance
    - Progress tracking enables real-time receiving dashboard updates

    ### Use Cases
    - **Receiving Operations**: Track progress as products are received and processed
    - **Quality Control**: Record batch information during receiving inspection
    - **Inventory Management**: Update inventory levels with received quantities
    - **Compliance Tracking**: Maintain lot numbers and expiration dates for regulations
    - **Performance Monitoring**: Monitor receiving efficiency and completion rates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderReceivingProgressBody):  Example: {'lineNumber': 1,
            'receivedQuantity': 150, 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        inbound_order_id=inbound_order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    inbound_order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateWMSInboundOrderReceivingProgressBody,
) -> Optional[Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]]:
    """Update receiving progress


    ## Update WMS Inbound Order Receiving Progress

    Update the receiving progress for specific line items within an inbound order, tracking quantities
    received and batch information.

    ### Features
    - **Line-Item Tracking**: Update receiving progress for individual product lines
    - **Quantity Management**: Track received quantities against expected quantities
    - **Batch Tracking**: Record lot numbers and expiration dates for compliance
    - **Progress Calculation**: Automatic calculation of receiving completion percentages
    - **Real-Time Updates**: Immediate visibility into receiving operations progress

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - lineNumber must exist within the order's line items
    - receivedQuantity is added to existing received quantity (cumulative)
    - Line status automatically updated based on receiving progress:
      - RECEIVING: When receivedQuantity > 0 but < expectedQuantity
      - RECEIVED: When receivedQuantity >= expectedQuantity
    - Lot number and expiration date updates support batch tracking requirements

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **lineNumber**: Required - Line number within the order for specific product
    - **receivedQuantity**: Required - Quantity received in this receiving session
    - **lotNumber**: Optional - Lot number for batch tracking and traceability
    - **expirationDate**: Optional - Product expiration date for perishable items

    ### Business Rules
    - Received quantities are cumulative across multiple receiving sessions
    - Line status updates automatically based on receiving completion
    - Lot numbers and expiration dates support regulatory compliance
    - Progress tracking enables real-time receiving dashboard updates

    ### Use Cases
    - **Receiving Operations**: Track progress as products are received and processed
    - **Quality Control**: Record batch information during receiving inspection
    - **Inventory Management**: Update inventory levels with received quantities
    - **Compliance Tracking**: Maintain lot numbers and expiration dates for regulations
    - **Performance Monitoring**: Monitor receiving efficiency and completion rates


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderReceivingProgressBody):  Example: {'lineNumber': 1,
            'receivedQuantity': 150, 'lotNumber': 'LOT-2024-W47', 'expirationDate':
            '2025-11-27T00:00:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSInboundOrderReceivingProgressResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            inbound_order_id=inbound_order_id,
            client=client,
            body=body,
        )
    ).parsed
