from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_order_status_body import UpdateERPOrderStatusBody
from ...models.update_erp_order_status_response_200 import UpdateERPOrderStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    order_id: str,
    *,
    body: UpdateERPOrderStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/orders/{order_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPOrderStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]:
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
    body: UpdateERPOrderStatusBody,
) -> Response[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]:
    """Update ERP order status


    Update ERP order status for order lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage order progression through business states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Order Processing**: Move orders through fulfillment workflow
    - **Status Updates**: Update order status from external systems
    - **Workflow Management**: Control order processing state
    - **Integration Support**: Status updates from ERP and warehouse systems

    **Status Values**:
    - **RECEIVED**: Initial order received
    - **ACKED**: Order acknowledged
    - **IN_PROGRESS**: Order being processed
    - **PARTIALLY_SHIPPED**: Partial fulfillment
    - **COMPLETED**: Order fully completed
    - **CANCELLED**: Order cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]
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
    body: UpdateERPOrderStatusBody,
) -> Optional[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]:
    """Update ERP order status


    Update ERP order status for order lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage order progression through business states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Order Processing**: Move orders through fulfillment workflow
    - **Status Updates**: Update order status from external systems
    - **Workflow Management**: Control order processing state
    - **Integration Support**: Status updates from ERP and warehouse systems

    **Status Values**:
    - **RECEIVED**: Initial order received
    - **ACKED**: Order acknowledged
    - **IN_PROGRESS**: Order being processed
    - **PARTIALLY_SHIPPED**: Partial fulfillment
    - **COMPLETED**: Order fully completed
    - **CANCELLED**: Order cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPOrderStatusResponse200]
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
    body: UpdateERPOrderStatusBody,
) -> Response[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]:
    """Update ERP order status


    Update ERP order status for order lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage order progression through business states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Order Processing**: Move orders through fulfillment workflow
    - **Status Updates**: Update order status from external systems
    - **Workflow Management**: Control order processing state
    - **Integration Support**: Status updates from ERP and warehouse systems

    **Status Values**:
    - **RECEIVED**: Initial order received
    - **ACKED**: Order acknowledged
    - **IN_PROGRESS**: Order being processed
    - **PARTIALLY_SHIPPED**: Partial fulfillment
    - **COMPLETED**: Order fully completed
    - **CANCELLED**: Order cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]
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
    body: UpdateERPOrderStatusBody,
) -> Optional[Union[ErrorResponse, UpdateERPOrderStatusResponse200]]:
    """Update ERP order status


    Update ERP order status for order lifecycle and workflow management.

    **Core Features**:
    - **Status Workflow**: Manage order progression through business states
    - **Dedicated Endpoint**: Specialized endpoint for status-only updates
    - **Business Logic**: Enforce business rules for status transitions
    - **Audit Tracking**: Complete audit trail of status changes

    **Use Cases**:
    - **Order Processing**: Move orders through fulfillment workflow
    - **Status Updates**: Update order status from external systems
    - **Workflow Management**: Control order processing state
    - **Integration Support**: Status updates from ERP and warehouse systems

    **Status Values**:
    - **RECEIVED**: Initial order received
    - **ACKED**: Order acknowledged
    - **IN_PROGRESS**: Order being processed
    - **PARTIALLY_SHIPPED**: Partial fulfillment
    - **COMPLETED**: Order fully completed
    - **CANCELLED**: Order cancelled


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        order_id (str):  Example: ORDER_507f1f77bcf86cd799439012.
        body (UpdateERPOrderStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPOrderStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            order_id=order_id,
            client=client,
            body=body,
        )
    ).parsed
