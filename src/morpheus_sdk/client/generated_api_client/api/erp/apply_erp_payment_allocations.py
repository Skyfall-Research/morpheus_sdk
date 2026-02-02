from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.apply_erp_payment_allocations_body import ApplyERPPaymentAllocationsBody
from ...models.apply_erp_payment_allocations_response_200 import ApplyERPPaymentAllocationsResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    payment_id: str,
    *,
    body: ApplyERPPaymentAllocationsBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/payments/{payment_id}/allocations",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = ApplyERPPaymentAllocationsResponse200.from_dict(response.json())

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
) -> Response[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]:
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
    body: ApplyERPPaymentAllocationsBody,
) -> Response[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]:
    """Apply ERP payment allocations


    Apply payment allocations to invoices for comprehensive cash application and accounts receivable
    management.

    **Core Features**:
    - **Cash Application**: Apply payments to specific invoices with precise allocation tracking
    - **Discount Management**: Track early payment discounts and adjustments
    - **Multiple Allocations**: Support for splitting payments across multiple invoices
    - **Business Validation**: Ensure allocation amounts do not exceed payment totals
    - **Automatic Status Updates**: Updates payment status to APPLIED when allocations are applied

    **Use Cases**:
    - **Accounts Receivable**: Apply customer payments to outstanding invoices
    - **Cash Management**: Allocate payments across multiple invoices for customers
    - **Discount Processing**: Apply early payment discounts and calculate net amounts
    - **Financial Reconciliation**: Match payments with invoices for accurate accounting

    **Important**: Total allocation amounts cannot exceed the payment total amount.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (ApplyERPPaymentAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]
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
    body: ApplyERPPaymentAllocationsBody,
) -> Optional[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]:
    """Apply ERP payment allocations


    Apply payment allocations to invoices for comprehensive cash application and accounts receivable
    management.

    **Core Features**:
    - **Cash Application**: Apply payments to specific invoices with precise allocation tracking
    - **Discount Management**: Track early payment discounts and adjustments
    - **Multiple Allocations**: Support for splitting payments across multiple invoices
    - **Business Validation**: Ensure allocation amounts do not exceed payment totals
    - **Automatic Status Updates**: Updates payment status to APPLIED when allocations are applied

    **Use Cases**:
    - **Accounts Receivable**: Apply customer payments to outstanding invoices
    - **Cash Management**: Allocate payments across multiple invoices for customers
    - **Discount Processing**: Apply early payment discounts and calculate net amounts
    - **Financial Reconciliation**: Match payments with invoices for accurate accounting

    **Important**: Total allocation amounts cannot exceed the payment total amount.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (ApplyERPPaymentAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]
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
    body: ApplyERPPaymentAllocationsBody,
) -> Response[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]:
    """Apply ERP payment allocations


    Apply payment allocations to invoices for comprehensive cash application and accounts receivable
    management.

    **Core Features**:
    - **Cash Application**: Apply payments to specific invoices with precise allocation tracking
    - **Discount Management**: Track early payment discounts and adjustments
    - **Multiple Allocations**: Support for splitting payments across multiple invoices
    - **Business Validation**: Ensure allocation amounts do not exceed payment totals
    - **Automatic Status Updates**: Updates payment status to APPLIED when allocations are applied

    **Use Cases**:
    - **Accounts Receivable**: Apply customer payments to outstanding invoices
    - **Cash Management**: Allocate payments across multiple invoices for customers
    - **Discount Processing**: Apply early payment discounts and calculate net amounts
    - **Financial Reconciliation**: Match payments with invoices for accurate accounting

    **Important**: Total allocation amounts cannot exceed the payment total amount.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (ApplyERPPaymentAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]
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
    body: ApplyERPPaymentAllocationsBody,
) -> Optional[Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]]:
    """Apply ERP payment allocations


    Apply payment allocations to invoices for comprehensive cash application and accounts receivable
    management.

    **Core Features**:
    - **Cash Application**: Apply payments to specific invoices with precise allocation tracking
    - **Discount Management**: Track early payment discounts and adjustments
    - **Multiple Allocations**: Support for splitting payments across multiple invoices
    - **Business Validation**: Ensure allocation amounts do not exceed payment totals
    - **Automatic Status Updates**: Updates payment status to APPLIED when allocations are applied

    **Use Cases**:
    - **Accounts Receivable**: Apply customer payments to outstanding invoices
    - **Cash Management**: Allocate payments across multiple invoices for customers
    - **Discount Processing**: Apply early payment discounts and calculate net amounts
    - **Financial Reconciliation**: Match payments with invoices for accurate accounting

    **Important**: Total allocation amounts cannot exceed the payment total amount.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (ApplyERPPaymentAllocationsBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ApplyERPPaymentAllocationsResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            payment_id=payment_id,
            client=client,
            body=body,
        )
    ).parsed
