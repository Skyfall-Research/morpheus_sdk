from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_shipments_by_tracking_number_response_200 import GetWMSShipmentsByTrackingNumberResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    tracking_number: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/shipments/tracking/{tracking_number}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSShipmentsByTrackingNumberResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    tracking_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]:
    """Get shipment by tracking number


    **Shipment Tracking Lookup**

    Retrieve shipment information using carrier tracking number.

    **Use Cases:**
    - Customer service inquiries
    - Carrier integration callbacks
    - Delivery confirmation tracking
    - Exception handling

    **Field Mapping:**
    - Uses `trackingNumber` field for lookup
    - Returns single shipment object (tracking numbers are typically unique)


    Args:
        world_id (str):
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        tracking_number=tracking_number,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    tracking_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]:
    """Get shipment by tracking number


    **Shipment Tracking Lookup**

    Retrieve shipment information using carrier tracking number.

    **Use Cases:**
    - Customer service inquiries
    - Carrier integration callbacks
    - Delivery confirmation tracking
    - Exception handling

    **Field Mapping:**
    - Uses `trackingNumber` field for lookup
    - Returns single shipment object (tracking numbers are typically unique)


    Args:
        world_id (str):
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        tracking_number=tracking_number,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    tracking_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]:
    """Get shipment by tracking number


    **Shipment Tracking Lookup**

    Retrieve shipment information using carrier tracking number.

    **Use Cases:**
    - Customer service inquiries
    - Carrier integration callbacks
    - Delivery confirmation tracking
    - Exception handling

    **Field Mapping:**
    - Uses `trackingNumber` field for lookup
    - Returns single shipment object (tracking numbers are typically unique)


    Args:
        world_id (str):
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        tracking_number=tracking_number,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    tracking_number: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]]:
    """Get shipment by tracking number


    **Shipment Tracking Lookup**

    Retrieve shipment information using carrier tracking number.

    **Use Cases:**
    - Customer service inquiries
    - Carrier integration callbacks
    - Delivery confirmation tracking
    - Exception handling

    **Field Mapping:**
    - Uses `trackingNumber` field for lookup
    - Returns single shipment object (tracking numbers are typically unique)


    Args:
        world_id (str):
        tracking_number (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSShipmentsByTrackingNumberResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            tracking_number=tracking_number,
            client=client,
        )
    ).parsed
