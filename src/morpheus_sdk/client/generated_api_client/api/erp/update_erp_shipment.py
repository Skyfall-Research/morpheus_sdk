from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_shipment_body import UpdateERPShipmentBody
from ...models.update_erp_shipment_response_200 import UpdateERPShipmentResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: UpdateERPShipmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/shipments/{shipment_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPShipmentResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPShipmentResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPShipmentResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPShipmentBody,
) -> Response[Union[ErrorResponse, UpdateERPShipmentResponse200]]:
    """Update ERP shipment


    Update ERP shipment information with partial data for logistics and tracking management.

    **Core Features**:
    - **Partial Updates**: Update specific shipment fields without replacing entire record
    - **Logistics Management**: Modify carrier information, dates, and routing details
    - **Status Updates**: Update shipment status and tracking information
    - **Line Item Updates**: Modify shipment line items and quantities

    **Use Cases**:
    - **Shipment Changes**: Modify shipment details per logistics requirements
    - **Carrier Updates**: Update carrier information and tracking numbers
    - **Route Changes**: Modify addresses and delivery information
    - **Status Management**: Update shipment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPShipmentResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPShipmentBody,
) -> Optional[Union[ErrorResponse, UpdateERPShipmentResponse200]]:
    """Update ERP shipment


    Update ERP shipment information with partial data for logistics and tracking management.

    **Core Features**:
    - **Partial Updates**: Update specific shipment fields without replacing entire record
    - **Logistics Management**: Modify carrier information, dates, and routing details
    - **Status Updates**: Update shipment status and tracking information
    - **Line Item Updates**: Modify shipment line items and quantities

    **Use Cases**:
    - **Shipment Changes**: Modify shipment details per logistics requirements
    - **Carrier Updates**: Update carrier information and tracking numbers
    - **Route Changes**: Modify addresses and delivery information
    - **Status Management**: Update shipment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPShipmentResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        shipment_id=shipment_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPShipmentBody,
) -> Response[Union[ErrorResponse, UpdateERPShipmentResponse200]]:
    """Update ERP shipment


    Update ERP shipment information with partial data for logistics and tracking management.

    **Core Features**:
    - **Partial Updates**: Update specific shipment fields without replacing entire record
    - **Logistics Management**: Modify carrier information, dates, and routing details
    - **Status Updates**: Update shipment status and tracking information
    - **Line Item Updates**: Modify shipment line items and quantities

    **Use Cases**:
    - **Shipment Changes**: Modify shipment details per logistics requirements
    - **Carrier Updates**: Update carrier information and tracking numbers
    - **Route Changes**: Modify addresses and delivery information
    - **Status Management**: Update shipment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPShipmentResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        shipment_id=shipment_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    shipment_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: UpdateERPShipmentBody,
) -> Optional[Union[ErrorResponse, UpdateERPShipmentResponse200]]:
    """Update ERP shipment


    Update ERP shipment information with partial data for logistics and tracking management.

    **Core Features**:
    - **Partial Updates**: Update specific shipment fields without replacing entire record
    - **Logistics Management**: Modify carrier information, dates, and routing details
    - **Status Updates**: Update shipment status and tracking information
    - **Line Item Updates**: Modify shipment line items and quantities

    **Use Cases**:
    - **Shipment Changes**: Modify shipment details per logistics requirements
    - **Carrier Updates**: Update carrier information and tracking numbers
    - **Route Changes**: Modify addresses and delivery information
    - **Status Management**: Update shipment processing state

    **Important**: For status-only updates, use the dedicated status endpoint for better performance.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPShipmentResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
