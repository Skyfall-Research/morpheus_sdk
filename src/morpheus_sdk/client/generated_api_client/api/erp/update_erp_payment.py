from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_payment_body import UpdateERPPaymentBody
from ...models.update_erp_payment_response_200 import UpdateERPPaymentResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    payment_id: str,
    *,
    body: UpdateERPPaymentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/payments/{payment_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPPaymentResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPPaymentResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPPaymentResponse200]]:
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
    body: UpdateERPPaymentBody,
) -> Response[Union[ErrorResponse, UpdateERPPaymentResponse200]]:
    """Update ERP payment


    Update ERP payment information with partial data for financial and allocation management.

    **Core Features**:
    - **Partial Updates**: Update specific payment fields without replacing entire record
    - **Financial Management**: Modify payment amounts, methods, and bank details
    - **Allocation Updates**: Update payment allocations and invoice applications
    - **Status Management**: Control payment processing workflow

    **Use Cases**:
    - **Payment Corrections**: Modify payment details per accounting requirements
    - **Allocation Adjustments**: Update invoice allocations and discount information
    - **Bank Updates**: Modify bank details and payment method information
    - **Status Management**: Update payment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPPaymentResponse200]]
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
    body: UpdateERPPaymentBody,
) -> Optional[Union[ErrorResponse, UpdateERPPaymentResponse200]]:
    """Update ERP payment


    Update ERP payment information with partial data for financial and allocation management.

    **Core Features**:
    - **Partial Updates**: Update specific payment fields without replacing entire record
    - **Financial Management**: Modify payment amounts, methods, and bank details
    - **Allocation Updates**: Update payment allocations and invoice applications
    - **Status Management**: Control payment processing workflow

    **Use Cases**:
    - **Payment Corrections**: Modify payment details per accounting requirements
    - **Allocation Adjustments**: Update invoice allocations and discount information
    - **Bank Updates**: Modify bank details and payment method information
    - **Status Management**: Update payment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPPaymentResponse200]
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
    body: UpdateERPPaymentBody,
) -> Response[Union[ErrorResponse, UpdateERPPaymentResponse200]]:
    """Update ERP payment


    Update ERP payment information with partial data for financial and allocation management.

    **Core Features**:
    - **Partial Updates**: Update specific payment fields without replacing entire record
    - **Financial Management**: Modify payment amounts, methods, and bank details
    - **Allocation Updates**: Update payment allocations and invoice applications
    - **Status Management**: Control payment processing workflow

    **Use Cases**:
    - **Payment Corrections**: Modify payment details per accounting requirements
    - **Allocation Adjustments**: Update invoice allocations and discount information
    - **Bank Updates**: Modify bank details and payment method information
    - **Status Management**: Update payment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPPaymentResponse200]]
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
    body: UpdateERPPaymentBody,
) -> Optional[Union[ErrorResponse, UpdateERPPaymentResponse200]]:
    """Update ERP payment


    Update ERP payment information with partial data for financial and allocation management.

    **Core Features**:
    - **Partial Updates**: Update specific payment fields without replacing entire record
    - **Financial Management**: Modify payment amounts, methods, and bank details
    - **Allocation Updates**: Update payment allocations and invoice applications
    - **Status Management**: Control payment processing workflow

    **Use Cases**:
    - **Payment Corrections**: Modify payment details per accounting requirements
    - **Allocation Adjustments**: Update invoice allocations and discount information
    - **Bank Updates**: Modify bank details and payment method information
    - **Status Management**: Update payment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.
        body (UpdateERPPaymentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPPaymentResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            payment_id=payment_id,
            client=client,
            body=body,
        )
    ).parsed
