from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_erp_payment_by_id_response_200 import GetERPPaymentByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    payment_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/payments/{payment_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetERPPaymentByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetERPPaymentByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetERPPaymentByIdResponse200]]:
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
) -> Response[Union[ErrorResponse, GetERPPaymentByIdResponse200]]:
    """Get ERP payment by ID


    Retrieve specific ERP payment by payment ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get payment by unique payment identifier
    - **Complete Profile**: Returns full payment data including allocation details and bank information
    - **Fast Lookup**: Optimized query using indexed paymentId field
    - **Financial Intelligence**: Access comprehensive payment data for accounting operations

    **Use Cases**:
    - **Payment Details**: Get complete payment information for financial operations
    - **Customer Service**: Resolve payment inquiries using payment ID references
    - **Accounting Operations**: Access payment details for ledger and reconciliation
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPPaymentByIdResponse200]]
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
) -> Optional[Union[ErrorResponse, GetERPPaymentByIdResponse200]]:
    """Get ERP payment by ID


    Retrieve specific ERP payment by payment ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get payment by unique payment identifier
    - **Complete Profile**: Returns full payment data including allocation details and bank information
    - **Fast Lookup**: Optimized query using indexed paymentId field
    - **Financial Intelligence**: Access comprehensive payment data for accounting operations

    **Use Cases**:
    - **Payment Details**: Get complete payment information for financial operations
    - **Customer Service**: Resolve payment inquiries using payment ID references
    - **Accounting Operations**: Access payment details for ledger and reconciliation
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPPaymentByIdResponse200]
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
) -> Response[Union[ErrorResponse, GetERPPaymentByIdResponse200]]:
    """Get ERP payment by ID


    Retrieve specific ERP payment by payment ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get payment by unique payment identifier
    - **Complete Profile**: Returns full payment data including allocation details and bank information
    - **Fast Lookup**: Optimized query using indexed paymentId field
    - **Financial Intelligence**: Access comprehensive payment data for accounting operations

    **Use Cases**:
    - **Payment Details**: Get complete payment information for financial operations
    - **Customer Service**: Resolve payment inquiries using payment ID references
    - **Accounting Operations**: Access payment details for ledger and reconciliation
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetERPPaymentByIdResponse200]]
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
) -> Optional[Union[ErrorResponse, GetERPPaymentByIdResponse200]]:
    """Get ERP payment by ID


    Retrieve specific ERP payment by payment ID for detailed financial information access.

    **Core Features**:
    - **Direct Access**: Get payment by unique payment identifier
    - **Complete Profile**: Returns full payment data including allocation details and bank information
    - **Fast Lookup**: Optimized query using indexed paymentId field
    - **Financial Intelligence**: Access comprehensive payment data for accounting operations

    **Use Cases**:
    - **Payment Details**: Get complete payment information for financial operations
    - **Customer Service**: Resolve payment inquiries using payment ID references
    - **Accounting Operations**: Access payment details for ledger and reconciliation
    - **Integration Support**: Direct API access for external accounting system integration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        payment_id (str):  Example: PAY_507f1f77bcf86cd799439012.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetERPPaymentByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            payment_id=payment_id,
            client=client,
        )
    ).parsed
