from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_inbound_order_status_body import UpdateWMSInboundOrderStatusBody
from ...models.update_wms_inbound_order_status_response_200 import UpdateWMSInboundOrderStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    inbound_order_id: str,
    *,
    body: UpdateWMSInboundOrderStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/inbound-orders/{inbound_order_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSInboundOrderStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]:
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
    body: UpdateWMSInboundOrderStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]:
    """Update inbound order status


    ## Update WMS Inbound Order Status

    Update the operational status of an inbound order with automatic timestamp tracking for
    comprehensive receiving lifecycle management.

    ### Features
    - **Status Lifecycle Management**: EXPECTED → IN_TRANSIT → RECEIVING → RECEIVED → CLOSED transitions
    - **Automatic Timestamps**: Status-specific date field updates based on status changes
    - **Business Rule Enforcement**: Validates logical status progression
    - **Audit Trail**: Complete history of status modifications with timestamps
    - **ERP Integration**: Status updates can trigger downstream ERP notifications

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Status must be one of the valid enumerated values
    - Automatic timestamp updates based on status:
      - IN_TRANSIT: Updates dates.actualArrival if provided
      - RECEIVING: Updates dates.receivingStarted to current timestamp
      - RECEIVED: Updates dates.receivingCompleted to current timestamp
    - Status changes are tracked with automatic timestamps for audit compliance

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **status**: Required - New operational status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **statusDate**: Optional - Specific date/time for status change (defaults to current time)

    ### Business Rules
    - RECEIVING status indicates active receiving operations in progress
    - RECEIVED status marks completion of all receiving activities
    - CLOSED status finalizes order and prevents further modifications
    - CANCELLED status handles order cancellations with audit trail

    ### Use Cases
    - **Receiving Workflow**: Update status as orders progress through receiving
    - **ERP Synchronization**: Sync status changes with upstream ERP systems
    - **Performance Tracking**: Monitor receiving timelines and efficiency
    - **Exception Handling**: Mark orders as cancelled or handle receiving issues
    - **Compliance Reporting**: Maintain detailed audit trail of status changes


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderStatusBody):  Example: {'status': 'RECEIVING', 'statusDate':
            '2024-11-27T14:30:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]
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
    body: UpdateWMSInboundOrderStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]:
    """Update inbound order status


    ## Update WMS Inbound Order Status

    Update the operational status of an inbound order with automatic timestamp tracking for
    comprehensive receiving lifecycle management.

    ### Features
    - **Status Lifecycle Management**: EXPECTED → IN_TRANSIT → RECEIVING → RECEIVED → CLOSED transitions
    - **Automatic Timestamps**: Status-specific date field updates based on status changes
    - **Business Rule Enforcement**: Validates logical status progression
    - **Audit Trail**: Complete history of status modifications with timestamps
    - **ERP Integration**: Status updates can trigger downstream ERP notifications

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Status must be one of the valid enumerated values
    - Automatic timestamp updates based on status:
      - IN_TRANSIT: Updates dates.actualArrival if provided
      - RECEIVING: Updates dates.receivingStarted to current timestamp
      - RECEIVED: Updates dates.receivingCompleted to current timestamp
    - Status changes are tracked with automatic timestamps for audit compliance

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **status**: Required - New operational status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **statusDate**: Optional - Specific date/time for status change (defaults to current time)

    ### Business Rules
    - RECEIVING status indicates active receiving operations in progress
    - RECEIVED status marks completion of all receiving activities
    - CLOSED status finalizes order and prevents further modifications
    - CANCELLED status handles order cancellations with audit trail

    ### Use Cases
    - **Receiving Workflow**: Update status as orders progress through receiving
    - **ERP Synchronization**: Sync status changes with upstream ERP systems
    - **Performance Tracking**: Monitor receiving timelines and efficiency
    - **Exception Handling**: Mark orders as cancelled or handle receiving issues
    - **Compliance Reporting**: Maintain detailed audit trail of status changes


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderStatusBody):  Example: {'status': 'RECEIVING', 'statusDate':
            '2024-11-27T14:30:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]
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
    body: UpdateWMSInboundOrderStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]:
    """Update inbound order status


    ## Update WMS Inbound Order Status

    Update the operational status of an inbound order with automatic timestamp tracking for
    comprehensive receiving lifecycle management.

    ### Features
    - **Status Lifecycle Management**: EXPECTED → IN_TRANSIT → RECEIVING → RECEIVED → CLOSED transitions
    - **Automatic Timestamps**: Status-specific date field updates based on status changes
    - **Business Rule Enforcement**: Validates logical status progression
    - **Audit Trail**: Complete history of status modifications with timestamps
    - **ERP Integration**: Status updates can trigger downstream ERP notifications

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Status must be one of the valid enumerated values
    - Automatic timestamp updates based on status:
      - IN_TRANSIT: Updates dates.actualArrival if provided
      - RECEIVING: Updates dates.receivingStarted to current timestamp
      - RECEIVED: Updates dates.receivingCompleted to current timestamp
    - Status changes are tracked with automatic timestamps for audit compliance

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **status**: Required - New operational status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **statusDate**: Optional - Specific date/time for status change (defaults to current time)

    ### Business Rules
    - RECEIVING status indicates active receiving operations in progress
    - RECEIVED status marks completion of all receiving activities
    - CLOSED status finalizes order and prevents further modifications
    - CANCELLED status handles order cancellations with audit trail

    ### Use Cases
    - **Receiving Workflow**: Update status as orders progress through receiving
    - **ERP Synchronization**: Sync status changes with upstream ERP systems
    - **Performance Tracking**: Monitor receiving timelines and efficiency
    - **Exception Handling**: Mark orders as cancelled or handle receiving issues
    - **Compliance Reporting**: Maintain detailed audit trail of status changes


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderStatusBody):  Example: {'status': 'RECEIVING', 'statusDate':
            '2024-11-27T14:30:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]
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
    body: UpdateWMSInboundOrderStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]]:
    """Update inbound order status


    ## Update WMS Inbound Order Status

    Update the operational status of an inbound order with automatic timestamp tracking for
    comprehensive receiving lifecycle management.

    ### Features
    - **Status Lifecycle Management**: EXPECTED → IN_TRANSIT → RECEIVING → RECEIVED → CLOSED transitions
    - **Automatic Timestamps**: Status-specific date field updates based on status changes
    - **Business Rule Enforcement**: Validates logical status progression
    - **Audit Trail**: Complete history of status modifications with timestamps
    - **ERP Integration**: Status updates can trigger downstream ERP notifications

    ### Business Logic
    - orderId must reference an existing inbound order within the world
    - Status must be one of the valid enumerated values
    - Automatic timestamp updates based on status:
      - IN_TRANSIT: Updates dates.actualArrival if provided
      - RECEIVING: Updates dates.receivingStarted to current timestamp
      - RECEIVED: Updates dates.receivingCompleted to current timestamp
    - Status changes are tracked with automatic timestamps for audit compliance

    ### Path Parameters
    - **orderId**: Required - Unique identifier for the inbound order

    ### Request Body Fields
    - **status**: Required - New operational status (EXPECTED, IN_TRANSIT, RECEIVING, RECEIVED, CLOSED,
    CANCELLED)
    - **statusDate**: Optional - Specific date/time for status change (defaults to current time)

    ### Business Rules
    - RECEIVING status indicates active receiving operations in progress
    - RECEIVED status marks completion of all receiving activities
    - CLOSED status finalizes order and prevents further modifications
    - CANCELLED status handles order cancellations with audit trail

    ### Use Cases
    - **Receiving Workflow**: Update status as orders progress through receiving
    - **ERP Synchronization**: Sync status changes with upstream ERP systems
    - **Performance Tracking**: Monitor receiving timelines and efficiency
    - **Exception Handling**: Mark orders as cancelled or handle receiving issues
    - **Compliance Reporting**: Maintain detailed audit trail of status changes


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        inbound_order_id (str):  Example: wms_inbound-order_674565c1234567890abcdef.
        body (UpdateWMSInboundOrderStatusBody):  Example: {'status': 'RECEIVING', 'statusDate':
            '2024-11-27T14:30:00Z'}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSInboundOrderStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            inbound_order_id=inbound_order_id,
            client=client,
            body=body,
        )
    ).parsed
