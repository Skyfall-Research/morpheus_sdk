from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_erp_payment_response_200 import DeleteERPPaymentResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    payment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/{world_id}/erp/payments/{payment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteERPPaymentResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteERPPaymentResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteERPPaymentResponse200, ErrorResponse]]:
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
) -> Response[Union[DeleteERPPaymentResponse200, ErrorResponse]]:
    """Delete ERP payment


    Delete ERP payment record from the system for financial cleanup and accounting management.

    **Core Features**:
    - **Complete Removal**: Permanently delete payment record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Payment Cleanup**: Remove erroneous or duplicate payments
    - **Data Management**: Clean up test or invalid payment data
    - **System Maintenance**: Remove obsolete payment records
    - **Compliance**: Payment deletion per data retention policies

    **Important**: Ensure payment is not allocated to invoices before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteERPPaymentResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        payment_id=payment_id,
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
) -> Optional[Union[DeleteERPPaymentResponse200, ErrorResponse]]:
    """Delete ERP payment


    Delete ERP payment record from the system for financial cleanup and accounting management.

    **Core Features**:
    - **Complete Removal**: Permanently delete payment record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Payment Cleanup**: Remove erroneous or duplicate payments
    - **Data Management**: Clean up test or invalid payment data
    - **System Maintenance**: Remove obsolete payment records
    - **Compliance**: Payment deletion per data retention policies

    **Important**: Ensure payment is not allocated to invoices before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteERPPaymentResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        payment_id=payment_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeleteERPPaymentResponse200, ErrorResponse]]:
    """Delete ERP payment


    Delete ERP payment record from the system for financial cleanup and accounting management.

    **Core Features**:
    - **Complete Removal**: Permanently delete payment record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Payment Cleanup**: Remove erroneous or duplicate payments
    - **Data Management**: Clean up test or invalid payment data
    - **System Maintenance**: Remove obsolete payment records
    - **Compliance**: Payment deletion per data retention policies

    **Important**: Ensure payment is not allocated to invoices before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteERPPaymentResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        payment_id=payment_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    payment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[DeleteERPPaymentResponse200, ErrorResponse]]:
    """Delete ERP payment


    Delete ERP payment record from the system for financial cleanup and accounting management.

    **Core Features**:
    - **Complete Removal**: Permanently delete payment record from database
    - **World Scoping**: Ensures deletion only within specified world environment
    - **Business Safety**: Validate deletion constraints before removal
    - **Audit Trail**: Deletion tracked through audit plugin

    **Use Cases**:
    - **Payment Cleanup**: Remove erroneous or duplicate payments
    - **Data Management**: Clean up test or invalid payment data
    - **System Maintenance**: Remove obsolete payment records
    - **Compliance**: Payment deletion per data retention policies

    **Important**: Ensure payment is not allocated to invoices before deletion.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteERPPaymentResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            payment_id=payment_id,
            client=client,
        )
    ).parsed
