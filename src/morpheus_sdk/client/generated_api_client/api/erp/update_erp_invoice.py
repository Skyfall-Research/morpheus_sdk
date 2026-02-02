from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_invoice_body import UpdateERPInvoiceBody
from ...models.update_erp_invoice_response_200 import UpdateERPInvoiceResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    invoice_id: str,
    *,
    body: UpdateERPInvoiceBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/invoices/{invoice_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPInvoiceResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPInvoiceResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPInvoiceResponse200]]:
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
    body: UpdateERPInvoiceBody,
) -> Response[Union[ErrorResponse, UpdateERPInvoiceResponse200]]:
    """Update ERP invoice


    Update ERP invoice information with partial data for billing and financial management.

    **Core Features**:
    - **Partial Updates**: Update specific invoice fields without replacing entire record
    - **Line Item Management**: Modify invoice line items and pricing
    - **Financial Updates**: Update amounts, allowances, and charges
    - **Status Management**: Control invoice workflow and processing state

    **Use Cases**:
    - **Invoice Corrections**: Modify invoice details per customer or business requirements
    - **Amount Adjustments**: Update line item quantities, pricing, and totals
    - **Status Updates**: Manage invoice processing workflow
    - **Financial Corrections**: Adjust allowances, charges, and tax information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPInvoiceResponse200]]
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
    body: UpdateERPInvoiceBody,
) -> Optional[Union[ErrorResponse, UpdateERPInvoiceResponse200]]:
    """Update ERP invoice


    Update ERP invoice information with partial data for billing and financial management.

    **Core Features**:
    - **Partial Updates**: Update specific invoice fields without replacing entire record
    - **Line Item Management**: Modify invoice line items and pricing
    - **Financial Updates**: Update amounts, allowances, and charges
    - **Status Management**: Control invoice workflow and processing state

    **Use Cases**:
    - **Invoice Corrections**: Modify invoice details per customer or business requirements
    - **Amount Adjustments**: Update line item quantities, pricing, and totals
    - **Status Updates**: Manage invoice processing workflow
    - **Financial Corrections**: Adjust allowances, charges, and tax information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPInvoiceResponse200]
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
    body: UpdateERPInvoiceBody,
) -> Response[Union[ErrorResponse, UpdateERPInvoiceResponse200]]:
    """Update ERP invoice


    Update ERP invoice information with partial data for billing and financial management.

    **Core Features**:
    - **Partial Updates**: Update specific invoice fields without replacing entire record
    - **Line Item Management**: Modify invoice line items and pricing
    - **Financial Updates**: Update amounts, allowances, and charges
    - **Status Management**: Control invoice workflow and processing state

    **Use Cases**:
    - **Invoice Corrections**: Modify invoice details per customer or business requirements
    - **Amount Adjustments**: Update line item quantities, pricing, and totals
    - **Status Updates**: Manage invoice processing workflow
    - **Financial Corrections**: Adjust allowances, charges, and tax information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPInvoiceResponse200]]
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
    body: UpdateERPInvoiceBody,
) -> Optional[Union[ErrorResponse, UpdateERPInvoiceResponse200]]:
    """Update ERP invoice


    Update ERP invoice information with partial data for billing and financial management.

    **Core Features**:
    - **Partial Updates**: Update specific invoice fields without replacing entire record
    - **Line Item Management**: Modify invoice line items and pricing
    - **Financial Updates**: Update amounts, allowances, and charges
    - **Status Management**: Control invoice workflow and processing state

    **Use Cases**:
    - **Invoice Corrections**: Modify invoice details per customer or business requirements
    - **Amount Adjustments**: Update line item quantities, pricing, and totals
    - **Status Updates**: Manage invoice processing workflow
    - **Financial Corrections**: Adjust allowances, charges, and tax information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.
        body (UpdateERPInvoiceBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPInvoiceResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            invoice_id=invoice_id,
            client=client,
            body=body,
        )
    ).parsed
