from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_invoice_status_body import UpdateERPInvoiceStatusBody
from ...models.update_erp_invoice_status_response_200 import UpdateERPInvoiceStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    invoice_id: str,
    *,
    body: UpdateERPInvoiceStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/invoices/{invoice_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPInvoiceStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPInvoiceStatusBody,
) -> Response[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]:
    """Update ERP invoice status


    Update ERP invoice status for billing lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage invoice progression through billing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Billing Processing**: Move invoices through billing workflow
    - **Payment Processing**: Update status when payments are received
    - **Workflow Management**: Control invoice processing state
    - **Integration Support**: Status updates from payment and accounting systems

    **Status Values**:
    - **DRAFT**: Invoice in draft state
    - **SENT**: Invoice sent to customer
    - **VALIDATED**: Invoice validated and approved
    - **REJECTED**: Invoice rejected or disputed
    - **PAID**: Invoice fully paid
    - **PARTIALLY_PAID**: Invoice partially paid


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        invoice_id=invoice_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPInvoiceStatusBody,
) -> Optional[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]:
    """Update ERP invoice status


    Update ERP invoice status for billing lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage invoice progression through billing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Billing Processing**: Move invoices through billing workflow
    - **Payment Processing**: Update status when payments are received
    - **Workflow Management**: Control invoice processing state
    - **Integration Support**: Status updates from payment and accounting systems

    **Status Values**:
    - **DRAFT**: Invoice in draft state
    - **SENT**: Invoice sent to customer
    - **VALIDATED**: Invoice validated and approved
    - **REJECTED**: Invoice rejected or disputed
    - **PAID**: Invoice fully paid
    - **PARTIALLY_PAID**: Invoice partially paid


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        invoice_id=invoice_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPInvoiceStatusBody,
) -> Response[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]:
    """Update ERP invoice status


    Update ERP invoice status for billing lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage invoice progression through billing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Billing Processing**: Move invoices through billing workflow
    - **Payment Processing**: Update status when payments are received
    - **Workflow Management**: Control invoice processing state
    - **Integration Support**: Status updates from payment and accounting systems

    **Status Values**:
    - **DRAFT**: Invoice in draft state
    - **SENT**: Invoice sent to customer
    - **VALIDATED**: Invoice validated and approved
    - **REJECTED**: Invoice rejected or disputed
    - **PAID**: Invoice fully paid
    - **PARTIALLY_PAID**: Invoice partially paid


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        invoice_id=invoice_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPInvoiceStatusBody,
) -> Optional[Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]]:
    """Update ERP invoice status


    Update ERP invoice status for billing lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage invoice progression through billing states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Billing Processing**: Move invoices through billing workflow
    - **Payment Processing**: Update status when payments are received
    - **Workflow Management**: Control invoice processing state
    - **Integration Support**: Status updates from payment and accounting systems

    **Status Values**:
    - **DRAFT**: Invoice in draft state
    - **SENT**: Invoice sent to customer
    - **VALIDATED**: Invoice validated and approved
    - **REJECTED**: Invoice rejected or disputed
    - **PAID**: Invoice fully paid
    - **PARTIALLY_PAID**: Invoice partially paid


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPInvoiceStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
