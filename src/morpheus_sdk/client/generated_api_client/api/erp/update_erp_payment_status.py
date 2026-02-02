from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_payment_status_body import UpdateERPPaymentStatusBody
from ...models.update_erp_payment_status_response_200 import UpdateERPPaymentStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    payment_id: str,
    *,
    body: UpdateERPPaymentStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/payments/{payment_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPPaymentStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPPaymentStatusBody,
) -> Response[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]:
    """Update ERP payment status


    Update ERP payment status for financial lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage payment progression through financial processing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Payment Processing**: Move payments through accounting workflow
    - **Cash Application**: Update status when payments are applied to invoices
    - **Workflow Management**: Control payment processing state
    - **Integration Support**: Status updates from banking and accounting systems

    **Status Values**:
    - **RECEIVED**: Payment initially received
    - **APPLIED**: Payment applied to invoices
    - **UNMATCHED**: Payment without matching invoices
    - **REVERSAL**: Payment reversed or cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        payment_id=payment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPPaymentStatusBody,
) -> Optional[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]:
    """Update ERP payment status


    Update ERP payment status for financial lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage payment progression through financial processing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Payment Processing**: Move payments through accounting workflow
    - **Cash Application**: Update status when payments are applied to invoices
    - **Workflow Management**: Control payment processing state
    - **Integration Support**: Status updates from banking and accounting systems

    **Status Values**:
    - **RECEIVED**: Payment initially received
    - **APPLIED**: Payment applied to invoices
    - **UNMATCHED**: Payment without matching invoices
    - **REVERSAL**: Payment reversed or cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPPaymentStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        payment_id=payment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPPaymentStatusBody,
) -> Response[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]:
    """Update ERP payment status


    Update ERP payment status for financial lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage payment progression through financial processing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Payment Processing**: Move payments through accounting workflow
    - **Cash Application**: Update status when payments are applied to invoices
    - **Workflow Management**: Control payment processing state
    - **Integration Support**: Status updates from banking and accounting systems

    **Status Values**:
    - **RECEIVED**: Payment initially received
    - **APPLIED**: Payment applied to invoices
    - **UNMATCHED**: Payment without matching invoices
    - **REVERSAL**: Payment reversed or cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        payment_id=payment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPPaymentStatusBody,
) -> Optional[Union[ErrorResponse, UpdateERPPaymentStatusResponse200]]:
    """Update ERP payment status


    Update ERP payment status for financial lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage payment progression through financial processing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Payment Processing**: Move payments through accounting workflow
    - **Cash Application**: Update status when payments are applied to invoices
    - **Workflow Management**: Control payment processing state
    - **Integration Support**: Status updates from banking and accounting systems

    **Status Values**:
    - **RECEIVED**: Payment initially received
    - **APPLIED**: Payment applied to invoices
    - **UNMATCHED**: Payment without matching invoices
    - **REVERSAL**: Payment reversed or cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPPaymentStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            payment_id=payment_id,
            client=client,
            body=body,
        )
    ).parsed
