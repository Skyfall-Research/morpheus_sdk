from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_order_body import UpdateERPOrderBody
from ...models.update_erp_order_response_200 import UpdateERPOrderResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
    *,
    body: UpdateERPOrderBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/orders/{order_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPOrderResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPOrderResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPOrderResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPOrderBody,
) -> Response[Union[ErrorResponse, UpdateERPOrderResponse200]]:
    """Update ERP order


    Update ERP order information with partial data for order management and lifecycle processing.

    **Core Features**:
    - **Partial Updates**: Update specific order fields without replacing entire record
    - **Line Item Management**: Modify order line items and quantities
    - **Financial Updates**: Update pricing, discounts, and total calculations
    - **Status Management**: Control order workflow and processing state

    **Use Cases**:
    - **Order Changes**: Modify order details per customer requests
    - **Quantity Adjustments**: Update line item quantities and pricing
    - **Status Updates**: Manage order processing workflow
    - **Financial Corrections**: Adjust pricing and discount information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPOrderResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPOrderBody,
) -> Optional[Union[ErrorResponse, UpdateERPOrderResponse200]]:
    """Update ERP order


    Update ERP order information with partial data for order management and lifecycle processing.

    **Core Features**:
    - **Partial Updates**: Update specific order fields without replacing entire record
    - **Line Item Management**: Modify order line items and quantities
    - **Financial Updates**: Update pricing, discounts, and total calculations
    - **Status Management**: Control order workflow and processing state

    **Use Cases**:
    - **Order Changes**: Modify order details per customer requests
    - **Quantity Adjustments**: Update line item quantities and pricing
    - **Status Updates**: Manage order processing workflow
    - **Financial Corrections**: Adjust pricing and discount information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPOrderResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        order_id=order_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPOrderBody,
) -> Response[Union[ErrorResponse, UpdateERPOrderResponse200]]:
    """Update ERP order


    Update ERP order information with partial data for order management and lifecycle processing.

    **Core Features**:
    - **Partial Updates**: Update specific order fields without replacing entire record
    - **Line Item Management**: Modify order line items and quantities
    - **Financial Updates**: Update pricing, discounts, and total calculations
    - **Status Management**: Control order workflow and processing state

    **Use Cases**:
    - **Order Changes**: Modify order details per customer requests
    - **Quantity Adjustments**: Update line item quantities and pricing
    - **Status Updates**: Manage order processing workflow
    - **Financial Corrections**: Adjust pricing and discount information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPOrderResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        order_id=order_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    order_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPOrderBody,
) -> Optional[Union[ErrorResponse, UpdateERPOrderResponse200]]:
    """Update ERP order


    Update ERP order information with partial data for order management and lifecycle processing.

    **Core Features**:
    - **Partial Updates**: Update specific order fields without replacing entire record
    - **Line Item Management**: Modify order line items and quantities
    - **Financial Updates**: Update pricing, discounts, and total calculations
    - **Status Management**: Control order workflow and processing state

    **Use Cases**:
    - **Order Changes**: Modify order details per customer requests
    - **Quantity Adjustments**: Update line item quantities and pricing
    - **Status Updates**: Manage order processing workflow
    - **Financial Corrections**: Adjust pricing and discount information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPOrderResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
