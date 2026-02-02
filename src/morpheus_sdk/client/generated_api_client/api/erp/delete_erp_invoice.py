from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_erp_invoice_response_200 import DeleteERPInvoiceResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    invoice_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/{world_id}/erp/invoices/{invoice_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteERPInvoiceResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteERPInvoiceResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteERPInvoiceResponse200, ErrorResponse]]:
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
) -> Response[Union[DeleteERPInvoiceResponse200, ErrorResponse]]:
    """Delete ERP invoice


    Delete ERP invoice record from the system for billing cleanup and financial management.

    **Core Features**:
    - **Complete Removal**: Permanently delete invoice record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Invoice Cleanup**: Remove cancelled or duplicate invoices
    - **Data Management**: Clean up test or erroneous invoice data
    - **System Maintenance**: Remove invalid invoice records
    - **Compliance**: Invoice deletion per data retention policies

    **Important**: Ensure invoice is in appropriate status for deletion and no payments are applied.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteERPInvoiceResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteERPInvoiceResponse200, ErrorResponse]]:
    """Delete ERP invoice


    Delete ERP invoice record from the system for billing cleanup and financial management.

    **Core Features**:
    - **Complete Removal**: Permanently delete invoice record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Invoice Cleanup**: Remove cancelled or duplicate invoices
    - **Data Management**: Clean up test or erroneous invoice data
    - **System Maintenance**: Remove invalid invoice records
    - **Compliance**: Invoice deletion per data retention policies

    **Important**: Ensure invoice is in appropriate status for deletion and no payments are applied.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteERPInvoiceResponse200, ErrorResponse]
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
) -> Response[Union[DeleteERPInvoiceResponse200, ErrorResponse]]:
    """Delete ERP invoice


    Delete ERP invoice record from the system for billing cleanup and financial management.

    **Core Features**:
    - **Complete Removal**: Permanently delete invoice record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Invoice Cleanup**: Remove cancelled or duplicate invoices
    - **Data Management**: Clean up test or erroneous invoice data
    - **System Maintenance**: Remove invalid invoice records
    - **Compliance**: Invoice deletion per data retention policies

    **Important**: Ensure invoice is in appropriate status for deletion and no payments are applied.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteERPInvoiceResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteERPInvoiceResponse200, ErrorResponse]]:
    """Delete ERP invoice


    Delete ERP invoice record from the system for billing cleanup and financial management.

    **Core Features**:
    - **Complete Removal**: Permanently delete invoice record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Invoice Cleanup**: Remove cancelled or duplicate invoices
    - **Data Management**: Clean up test or erroneous invoice data
    - **System Maintenance**: Remove invalid invoice records
    - **Compliance**: Invoice deletion per data retention policies

    **Important**: Ensure invoice is in appropriate status for deletion and no payments are applied.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        invoice_id (str):  Example: INV_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteERPInvoiceResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            invoice_id=invoice_id,
            client=client,
        )
    ).parsed
