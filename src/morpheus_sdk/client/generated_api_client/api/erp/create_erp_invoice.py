from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_erp_invoice_body import CreateERPInvoiceBody
from ...models.create_erp_invoice_response_201 import CreateERPInvoiceResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateERPInvoiceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/invoices",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateERPInvoiceResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateERPInvoiceResponse201.from_dict(response.json())

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
) -> Response[Union[CreateERPInvoiceResponse201, ErrorResponse]]:
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
    body: CreateERPInvoiceBody,
) -> Response[Union[CreateERPInvoiceResponse201, ErrorResponse]]:
    """Create new ERP invoice


    Create a new ERP invoice with comprehensive billing information and line item details.

    **Core Features**:
    - **Invoice Generation**: Complete invoice setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic invoiceId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and taxes
    - **Financial Calculations**: Automatic subtotal, tax, allowance, and charge calculations
    - **Multiple Types**: Support for standard, credit, debit, and correction invoices

    **Use Cases**:
    - **Billing Operations**: Generate invoices for customer transactions
    - **Financial Management**: Track invoice values and payment obligations
    - **Tax Compliance**: Generate invoices with proper tax calculations
    - **Credit Management**: Issue credit and debit memos for adjustments


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPInvoiceResponse201, ErrorResponse]]
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
    body: CreateERPInvoiceBody,
) -> Optional[Union[CreateERPInvoiceResponse201, ErrorResponse]]:
    """Create new ERP invoice


    Create a new ERP invoice with comprehensive billing information and line item details.

    **Core Features**:
    - **Invoice Generation**: Complete invoice setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic invoiceId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and taxes
    - **Financial Calculations**: Automatic subtotal, tax, allowance, and charge calculations
    - **Multiple Types**: Support for standard, credit, debit, and correction invoices

    **Use Cases**:
    - **Billing Operations**: Generate invoices for customer transactions
    - **Financial Management**: Track invoice values and payment obligations
    - **Tax Compliance**: Generate invoices with proper tax calculations
    - **Credit Management**: Issue credit and debit memos for adjustments


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPInvoiceResponse201, ErrorResponse]
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
    body: CreateERPInvoiceBody,
) -> Response[Union[CreateERPInvoiceResponse201, ErrorResponse]]:
    """Create new ERP invoice


    Create a new ERP invoice with comprehensive billing information and line item details.

    **Core Features**:
    - **Invoice Generation**: Complete invoice setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic invoiceId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and taxes
    - **Financial Calculations**: Automatic subtotal, tax, allowance, and charge calculations
    - **Multiple Types**: Support for standard, credit, debit, and correction invoices

    **Use Cases**:
    - **Billing Operations**: Generate invoices for customer transactions
    - **Financial Management**: Track invoice values and payment obligations
    - **Tax Compliance**: Generate invoices with proper tax calculations
    - **Credit Management**: Issue credit and debit memos for adjustments


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPInvoiceResponse201, ErrorResponse]]
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
    body: CreateERPInvoiceBody,
) -> Optional[Union[CreateERPInvoiceResponse201, ErrorResponse]]:
    """Create new ERP invoice


    Create a new ERP invoice with comprehensive billing information and line item details.

    **Core Features**:
    - **Invoice Generation**: Complete invoice setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic invoiceId generation via generateIdByService
    - **Multi-Line Support**: Support for multiple line items with detailed pricing and taxes
    - **Financial Calculations**: Automatic subtotal, tax, allowance, and charge calculations
    - **Multiple Types**: Support for standard, credit, debit, and correction invoices

    **Use Cases**:
    - **Billing Operations**: Generate invoices for customer transactions
    - **Financial Management**: Track invoice values and payment obligations
    - **Tax Compliance**: Generate invoices with proper tax calculations
    - **Credit Management**: Issue credit and debit memos for adjustments


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPInvoiceResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
