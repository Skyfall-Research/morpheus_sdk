from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_erp_payment_body import CreateERPPaymentBody
from ...models.create_erp_payment_response_201 import CreateERPPaymentResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateERPPaymentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/payments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateERPPaymentResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateERPPaymentResponse201.from_dict(response.json())

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
) -> Response[Union[CreateERPPaymentResponse201, ErrorResponse]]:
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
    body: CreateERPPaymentBody,
) -> Response[Union[CreateERPPaymentResponse201, ErrorResponse]]:
    """Create new ERP payment


    Create a new ERP payment with comprehensive financial and allocation information.

    **Core Features**:
    - **Payment Processing**: Complete payment setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic paymentId generation via generateIdByService
    - **Multi-Method Support**: Support for ACH, Wire, Check, Credit Card, and other payment methods
    - **Allocation Management**: Advanced payment allocation to invoices with discount tracking
    - **Bank Integration**: Comprehensive bank details and remittance information

    **Use Cases**:
    - **Accounts Receivable**: Process customer payments for outstanding invoices
    - **Financial Management**: Track payment values and allocation details
    - **Cash Application**: Apply payments to specific invoices with discount tracking
    - **Bank Reconciliation**: Manage bank details and payment method information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPPaymentResponse201, ErrorResponse]]
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
    body: CreateERPPaymentBody,
) -> Optional[Union[CreateERPPaymentResponse201, ErrorResponse]]:
    """Create new ERP payment


    Create a new ERP payment with comprehensive financial and allocation information.

    **Core Features**:
    - **Payment Processing**: Complete payment setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic paymentId generation via generateIdByService
    - **Multi-Method Support**: Support for ACH, Wire, Check, Credit Card, and other payment methods
    - **Allocation Management**: Advanced payment allocation to invoices with discount tracking
    - **Bank Integration**: Comprehensive bank details and remittance information

    **Use Cases**:
    - **Accounts Receivable**: Process customer payments for outstanding invoices
    - **Financial Management**: Track payment values and allocation details
    - **Cash Application**: Apply payments to specific invoices with discount tracking
    - **Bank Reconciliation**: Manage bank details and payment method information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPPaymentResponse201, ErrorResponse]
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
    body: CreateERPPaymentBody,
) -> Response[Union[CreateERPPaymentResponse201, ErrorResponse]]:
    """Create new ERP payment


    Create a new ERP payment with comprehensive financial and allocation information.

    **Core Features**:
    - **Payment Processing**: Complete payment setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic paymentId generation via generateIdByService
    - **Multi-Method Support**: Support for ACH, Wire, Check, Credit Card, and other payment methods
    - **Allocation Management**: Advanced payment allocation to invoices with discount tracking
    - **Bank Integration**: Comprehensive bank details and remittance information

    **Use Cases**:
    - **Accounts Receivable**: Process customer payments for outstanding invoices
    - **Financial Management**: Track payment values and allocation details
    - **Cash Application**: Apply payments to specific invoices with discount tracking
    - **Bank Reconciliation**: Manage bank details and payment method information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateERPPaymentResponse201, ErrorResponse]]
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
    body: CreateERPPaymentBody,
) -> Optional[Union[CreateERPPaymentResponse201, ErrorResponse]]:
    """Create new ERP payment


    Create a new ERP payment with comprehensive financial and allocation information.

    **Core Features**:
    - **Payment Processing**: Complete payment setup with customer/partner relationships
    - **Auto-Generated IDs**: Automatic paymentId generation via generateIdByService
    - **Multi-Method Support**: Support for ACH, Wire, Check, Credit Card, and other payment methods
    - **Allocation Management**: Advanced payment allocation to invoices with discount tracking
    - **Bank Integration**: Comprehensive bank details and remittance information

    **Use Cases**:
    - **Accounts Receivable**: Process customer payments for outstanding invoices
    - **Financial Management**: Track payment values and allocation details
    - **Cash Application**: Apply payments to specific invoices with discount tracking
    - **Bank Reconciliation**: Manage bank details and payment method information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateERPPaymentResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
