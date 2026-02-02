from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_wms_tracking_event_body import AddWMSTrackingEventBody
from ...models.add_wms_tracking_event_response_200 import AddWMSTrackingEventResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: AddWMSTrackingEventBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/shipments/{shipment_id}/tracking-events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AddWMSTrackingEventResponse200]:
    if response.status_code == 200:
        response_200 = AddWMSTrackingEventResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AddWMSTrackingEventResponse200]:
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
    body: AddWMSTrackingEventBody,
) -> Response[AddWMSTrackingEventResponse200]:
    """Add tracking event to shipment


    **Shipment Tracking Event Management**

    Add tracking events to shipment history for status monitoring and customer visibility.

    **Event Types:**
    - Carrier status updates
    - Exception events
    - Delivery confirmations
    - Custom milestone events

    **Integration:**
    - Supports carrier event codes for EDI integration
    - Location-based tracking
    - Timestamp precision for accurate tracking


    Args:
        world_id (str):
        shipment_id (str):
        body (AddWMSTrackingEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddWMSTrackingEventResponse200]
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
    body: AddWMSTrackingEventBody,
) -> Optional[AddWMSTrackingEventResponse200]:
    """Add tracking event to shipment


    **Shipment Tracking Event Management**

    Add tracking events to shipment history for status monitoring and customer visibility.

    **Event Types:**
    - Carrier status updates
    - Exception events
    - Delivery confirmations
    - Custom milestone events

    **Integration:**
    - Supports carrier event codes for EDI integration
    - Location-based tracking
    - Timestamp precision for accurate tracking


    Args:
        world_id (str):
        shipment_id (str):
        body (AddWMSTrackingEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddWMSTrackingEventResponse200
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
    body: AddWMSTrackingEventBody,
) -> Response[AddWMSTrackingEventResponse200]:
    """Add tracking event to shipment


    **Shipment Tracking Event Management**

    Add tracking events to shipment history for status monitoring and customer visibility.

    **Event Types:**
    - Carrier status updates
    - Exception events
    - Delivery confirmations
    - Custom milestone events

    **Integration:**
    - Supports carrier event codes for EDI integration
    - Location-based tracking
    - Timestamp precision for accurate tracking


    Args:
        world_id (str):
        shipment_id (str):
        body (AddWMSTrackingEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddWMSTrackingEventResponse200]
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
    body: AddWMSTrackingEventBody,
) -> Optional[AddWMSTrackingEventResponse200]:
    """Add tracking event to shipment


    **Shipment Tracking Event Management**

    Add tracking events to shipment history for status monitoring and customer visibility.

    **Event Types:**
    - Carrier status updates
    - Exception events
    - Delivery confirmations
    - Custom milestone events

    **Integration:**
    - Supports carrier event codes for EDI integration
    - Location-based tracking
    - Timestamp precision for accurate tracking


    Args:
        world_id (str):
        shipment_id (str):
        body (AddWMSTrackingEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddWMSTrackingEventResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
