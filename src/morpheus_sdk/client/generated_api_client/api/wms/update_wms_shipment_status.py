from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_shipment_status_body import UpdateWMSShipmentStatusBody
from ...models.update_wms_shipment_status_response_200 import UpdateWMSShipmentStatusResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: UpdateWMSShipmentStatusBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/shipments/{shipment_id}/status",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSShipmentStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]:
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
    body: UpdateWMSShipmentStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]:
    """Update shipment status with automatic timestamp tracking


    **Shipment Status Management**

    Update shipment status with automatic workflow timestamp tracking.

    **Automatic Timestamp Updates:**
    - MANIFESTED → `dates.manifestDate`
    - SHIPPED → `dates.actualShipTime` (can include tracking number)
    - IN_TRANSIT → Ensures `dates.actualShipTime` is set
    - DELIVERED → `dates.actualDeliveryDate`

    **Tracking Integration:**
    Shipped status updates can optionally include tracking number assignment.


    Args:
        world_id (str):
        shipment_id (str):
        body (UpdateWMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]
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
    body: UpdateWMSShipmentStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]:
    """Update shipment status with automatic timestamp tracking


    **Shipment Status Management**

    Update shipment status with automatic workflow timestamp tracking.

    **Automatic Timestamp Updates:**
    - MANIFESTED → `dates.manifestDate`
    - SHIPPED → `dates.actualShipTime` (can include tracking number)
    - IN_TRANSIT → Ensures `dates.actualShipTime` is set
    - DELIVERED → `dates.actualDeliveryDate`

    **Tracking Integration:**
    Shipped status updates can optionally include tracking number assignment.


    Args:
        world_id (str):
        shipment_id (str):
        body (UpdateWMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]
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
    body: UpdateWMSShipmentStatusBody,
) -> Response[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]:
    """Update shipment status with automatic timestamp tracking


    **Shipment Status Management**

    Update shipment status with automatic workflow timestamp tracking.

    **Automatic Timestamp Updates:**
    - MANIFESTED → `dates.manifestDate`
    - SHIPPED → `dates.actualShipTime` (can include tracking number)
    - IN_TRANSIT → Ensures `dates.actualShipTime` is set
    - DELIVERED → `dates.actualDeliveryDate`

    **Tracking Integration:**
    Shipped status updates can optionally include tracking number assignment.


    Args:
        world_id (str):
        shipment_id (str):
        body (UpdateWMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]
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
    body: UpdateWMSShipmentStatusBody,
) -> Optional[Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]]:
    """Update shipment status with automatic timestamp tracking


    **Shipment Status Management**

    Update shipment status with automatic workflow timestamp tracking.

    **Automatic Timestamp Updates:**
    - MANIFESTED → `dates.manifestDate`
    - SHIPPED → `dates.actualShipTime` (can include tracking number)
    - IN_TRANSIT → Ensures `dates.actualShipTime` is set
    - DELIVERED → `dates.actualDeliveryDate`

    **Tracking Integration:**
    Shipped status updates can optionally include tracking number assignment.


    Args:
        world_id (str):
        shipment_id (str):
        body (UpdateWMSShipmentStatusBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSShipmentStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
