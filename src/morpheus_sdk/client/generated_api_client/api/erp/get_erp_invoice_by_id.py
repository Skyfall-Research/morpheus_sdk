from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_invoice_by_id_response_200 import GetERPInvoiceByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    invoice_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/invoices/{invoice_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPInvoiceByIdResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]:
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
) -> Response[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]:
    """Get ERP invoice by ID


    Retrieve specific ERP invoice by invoice identifier for detailed billing information access.

    **Core Features**:
    - **Direct Access**: Get invoice by unique invoiceId identifier
    - **Complete Profile**: Returns full invoice data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed invoiceId field
    - **Financial Intelligence**: Access comprehensive invoice data for accounting operations

    **Use Cases**:
    - **Invoice Details**: Get complete invoice information for billing operations
    - **Customer Service**: Resolve billing inquiries using invoice ID references
    - **Accounting Operations**: Access invoice details for financial processing
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        invoice_id=invoice_id,
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
) -> Optional[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]:
    """Get ERP invoice by ID


    Retrieve specific ERP invoice by invoice identifier for detailed billing information access.

    **Core Features**:
    - **Direct Access**: Get invoice by unique invoiceId identifier
    - **Complete Profile**: Returns full invoice data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed invoiceId field
    - **Financial Intelligence**: Access comprehensive invoice data for accounting operations

    **Use Cases**:
    - **Invoice Details**: Get complete invoice information for billing operations
    - **Customer Service**: Resolve billing inquiries using invoice ID references
    - **Accounting Operations**: Access invoice details for financial processing
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPInvoiceByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        invoice_id=invoice_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]:
    """Get ERP invoice by ID


    Retrieve specific ERP invoice by invoice identifier for detailed billing information access.

    **Core Features**:
    - **Direct Access**: Get invoice by unique invoiceId identifier
    - **Complete Profile**: Returns full invoice data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed invoiceId field
    - **Financial Intelligence**: Access comprehensive invoice data for accounting operations

    **Use Cases**:
    - **Invoice Details**: Get complete invoice information for billing operations
    - **Customer Service**: Resolve billing inquiries using invoice ID references
    - **Accounting Operations**: Access invoice details for financial processing
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        invoice_id=invoice_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    invoice_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetERPInvoiceByIdResponse200]]:
    """Get ERP invoice by ID


    Retrieve specific ERP invoice by invoice identifier for detailed billing information access.

    **Core Features**:
    - **Direct Access**: Get invoice by unique invoiceId identifier
    - **Complete Profile**: Returns full invoice data including line items and financial details
    - **Fast Lookup**: Optimized query using indexed invoiceId field
    - **Financial Intelligence**: Access comprehensive invoice data for accounting operations

    **Use Cases**:
    - **Invoice Details**: Get complete invoice information for billing operations
    - **Customer Service**: Resolve billing inquiries using invoice ID references
    - **Accounting Operations**: Access invoice details for financial processing
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPInvoiceByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
