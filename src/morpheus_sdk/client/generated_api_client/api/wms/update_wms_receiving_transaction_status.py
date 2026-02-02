from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_receiving_transaction_status_body import UpdateWMSReceivingTransactionStatusBody
from ...models.update_wms_receiving_transaction_status_response_200 import (
    UpdateWMSReceivingTransactionStatusResponse200,
)
from ...types import Response


def _get_kwargs(
    world_id: str,
    transaction_id: str,
    *,
    body: UpdateWMSReceivingTransactionStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/receiving-transactions/{transaction_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSReceivingTransactionStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]:
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
    body: UpdateWMSReceivingTransactionStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]:
    """Update receiving transaction status


    ## Update WMS Receiving Transaction Status

    Update the status of a receiving transaction with optional notes for workflow management and audit
    trail.

    ### Features
    - **Status Workflow Management**: Progress transactions through defined workflow stages
    - **Audit Trail**: Automatic timestamp recording of status changes
    - **Notes Support**: Optional notes for status change documentation
    - **Business Rule Enforcement**: Validates status transitions per business logic
    - **Real-time Updates**: Immediate status reflection across the system

    ### Status Workflow
    - **RECEIVED**: Initial status when goods are received at dock door
    - **QC_HOLD**: Quality control inspection required or failed
    - **PUTAWAY_PENDING**: Ready for putaway to storage locations
    - **COMPLETED**: Fully processed and stored
    - **REJECTED**: Rejected due to quality, damage, or other issues

    ### Business Logic
    - Status transitions follow defined workflow rules
    - Status updates include automatic timestamp recording
    - Optional notes provide context for status changes
    - System validates status transitions for data integrity
    - Status changes trigger downstream workflow notifications

    **CRITICAL NOTE**: Parameter uses 'transactionId' but queries model's 'receivingId' field due to
    implementation mapping.

    ### Use Cases
    - **Workflow Management**: Progress transactions through receiving workflow
    - **Quality Control**: Update status after inspection completion
    - **Exception Handling**: Mark transactions as on hold or rejected
    - **Process Completion**: Mark transactions as completed
    - **Audit Documentation**: Add notes for compliance and tracking


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (UpdateWMSReceivingTransactionStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]
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
    body: UpdateWMSReceivingTransactionStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]:
    """Update receiving transaction status


    ## Update WMS Receiving Transaction Status

    Update the status of a receiving transaction with optional notes for workflow management and audit
    trail.

    ### Features
    - **Status Workflow Management**: Progress transactions through defined workflow stages
    - **Audit Trail**: Automatic timestamp recording of status changes
    - **Notes Support**: Optional notes for status change documentation
    - **Business Rule Enforcement**: Validates status transitions per business logic
    - **Real-time Updates**: Immediate status reflection across the system

    ### Status Workflow
    - **RECEIVED**: Initial status when goods are received at dock door
    - **QC_HOLD**: Quality control inspection required or failed
    - **PUTAWAY_PENDING**: Ready for putaway to storage locations
    - **COMPLETED**: Fully processed and stored
    - **REJECTED**: Rejected due to quality, damage, or other issues

    ### Business Logic
    - Status transitions follow defined workflow rules
    - Status updates include automatic timestamp recording
    - Optional notes provide context for status changes
    - System validates status transitions for data integrity
    - Status changes trigger downstream workflow notifications

    **CRITICAL NOTE**: Parameter uses 'transactionId' but queries model's 'receivingId' field due to
    implementation mapping.

    ### Use Cases
    - **Workflow Management**: Progress transactions through receiving workflow
    - **Quality Control**: Update status after inspection completion
    - **Exception Handling**: Mark transactions as on hold or rejected
    - **Process Completion**: Mark transactions as completed
    - **Audit Documentation**: Add notes for compliance and tracking


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (UpdateWMSReceivingTransactionStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]
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
    body: UpdateWMSReceivingTransactionStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]:
    """Update receiving transaction status


    ## Update WMS Receiving Transaction Status

    Update the status of a receiving transaction with optional notes for workflow management and audit
    trail.

    ### Features
    - **Status Workflow Management**: Progress transactions through defined workflow stages
    - **Audit Trail**: Automatic timestamp recording of status changes
    - **Notes Support**: Optional notes for status change documentation
    - **Business Rule Enforcement**: Validates status transitions per business logic
    - **Real-time Updates**: Immediate status reflection across the system

    ### Status Workflow
    - **RECEIVED**: Initial status when goods are received at dock door
    - **QC_HOLD**: Quality control inspection required or failed
    - **PUTAWAY_PENDING**: Ready for putaway to storage locations
    - **COMPLETED**: Fully processed and stored
    - **REJECTED**: Rejected due to quality, damage, or other issues

    ### Business Logic
    - Status transitions follow defined workflow rules
    - Status updates include automatic timestamp recording
    - Optional notes provide context for status changes
    - System validates status transitions for data integrity
    - Status changes trigger downstream workflow notifications

    **CRITICAL NOTE**: Parameter uses 'transactionId' but queries model's 'receivingId' field due to
    implementation mapping.

    ### Use Cases
    - **Workflow Management**: Progress transactions through receiving workflow
    - **Quality Control**: Update status after inspection completion
    - **Exception Handling**: Mark transactions as on hold or rejected
    - **Process Completion**: Mark transactions as completed
    - **Audit Documentation**: Add notes for compliance and tracking


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (UpdateWMSReceivingTransactionStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]
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
    body: UpdateWMSReceivingTransactionStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]]:
    """Update receiving transaction status


    ## Update WMS Receiving Transaction Status

    Update the status of a receiving transaction with optional notes for workflow management and audit
    trail.

    ### Features
    - **Status Workflow Management**: Progress transactions through defined workflow stages
    - **Audit Trail**: Automatic timestamp recording of status changes
    - **Notes Support**: Optional notes for status change documentation
    - **Business Rule Enforcement**: Validates status transitions per business logic
    - **Real-time Updates**: Immediate status reflection across the system

    ### Status Workflow
    - **RECEIVED**: Initial status when goods are received at dock door
    - **QC_HOLD**: Quality control inspection required or failed
    - **PUTAWAY_PENDING**: Ready for putaway to storage locations
    - **COMPLETED**: Fully processed and stored
    - **REJECTED**: Rejected due to quality, damage, or other issues

    ### Business Logic
    - Status transitions follow defined workflow rules
    - Status updates include automatic timestamp recording
    - Optional notes provide context for status changes
    - System validates status transitions for data integrity
    - Status changes trigger downstream workflow notifications

    **CRITICAL NOTE**: Parameter uses 'transactionId' but queries model's 'receivingId' field due to
    implementation mapping.

    ### Use Cases
    - **Workflow Management**: Progress transactions through receiving workflow
    - **Quality Control**: Update status after inspection completion
    - **Exception Handling**: Mark transactions as on hold or rejected
    - **Process Completion**: Mark transactions as completed
    - **Audit Documentation**: Add notes for compliance and tracking


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        transaction_id (str):  Example: wms_receiving-transaction_674565c1234567890abcdef.
        body (UpdateWMSReceivingTransactionStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSReceivingTransactionStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            transaction_id=transaction_id,
            client=client,
            body=body,
        )
    ).parsed
