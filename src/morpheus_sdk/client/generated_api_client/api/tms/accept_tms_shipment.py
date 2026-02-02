from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.accept_tms_shipment_body import AcceptTMSShipmentBody
from ...models.accept_tms_shipment_response_200 import AcceptTMSShipmentResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: AcceptTMSShipmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/accept",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AcceptTMSShipmentResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AcceptTMSShipmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[AcceptTMSShipmentResponse200, ErrorResponse]]:
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
    body: AcceptTMSShipmentBody,
) -> Response[Union[AcceptTMSShipmentResponse200, ErrorResponse]]:
    """Accept shipment by carrier


    ## Accept Shipment by Carrier

    Carrier accepts a tendered shipment, transitioning from TENDERED to ACCEPTED status.

    ### Features
    - **Carrier Acceptance**: Confirms carrier commitment to transport
    - **Tracking Information**: Optional PRO number and tracking details
    - **Pickup Scheduling**: Optional estimated pickup date
    - **Status Transition**: TENDERED → ACCEPTED with audit trail

    ### Business Process
    1. Shipment must be in TENDERED status
    2. Carrier provides acceptance with optional details
    3. Status changes to ACCEPTED
    4. Pickup can now be scheduled
    5. Status change event is automatically created

    ### Optional Carrier Data
    - proNumber: Carrier's Progressive Number
    - trackingNumber: Carrier's tracking reference
    - estimatedPickupDate: When carrier plans to pickup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AcceptTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcceptTMSShipmentResponse200, ErrorResponse]]
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
    body: AcceptTMSShipmentBody,
) -> Optional[Union[AcceptTMSShipmentResponse200, ErrorResponse]]:
    """Accept shipment by carrier


    ## Accept Shipment by Carrier

    Carrier accepts a tendered shipment, transitioning from TENDERED to ACCEPTED status.

    ### Features
    - **Carrier Acceptance**: Confirms carrier commitment to transport
    - **Tracking Information**: Optional PRO number and tracking details
    - **Pickup Scheduling**: Optional estimated pickup date
    - **Status Transition**: TENDERED → ACCEPTED with audit trail

    ### Business Process
    1. Shipment must be in TENDERED status
    2. Carrier provides acceptance with optional details
    3. Status changes to ACCEPTED
    4. Pickup can now be scheduled
    5. Status change event is automatically created

    ### Optional Carrier Data
    - proNumber: Carrier's Progressive Number
    - trackingNumber: Carrier's tracking reference
    - estimatedPickupDate: When carrier plans to pickup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AcceptTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcceptTMSShipmentResponse200, ErrorResponse]
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
    body: AcceptTMSShipmentBody,
) -> Response[Union[AcceptTMSShipmentResponse200, ErrorResponse]]:
    """Accept shipment by carrier


    ## Accept Shipment by Carrier

    Carrier accepts a tendered shipment, transitioning from TENDERED to ACCEPTED status.

    ### Features
    - **Carrier Acceptance**: Confirms carrier commitment to transport
    - **Tracking Information**: Optional PRO number and tracking details
    - **Pickup Scheduling**: Optional estimated pickup date
    - **Status Transition**: TENDERED → ACCEPTED with audit trail

    ### Business Process
    1. Shipment must be in TENDERED status
    2. Carrier provides acceptance with optional details
    3. Status changes to ACCEPTED
    4. Pickup can now be scheduled
    5. Status change event is automatically created

    ### Optional Carrier Data
    - proNumber: Carrier's Progressive Number
    - trackingNumber: Carrier's tracking reference
    - estimatedPickupDate: When carrier plans to pickup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AcceptTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AcceptTMSShipmentResponse200, ErrorResponse]]
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
    body: AcceptTMSShipmentBody,
) -> Optional[Union[AcceptTMSShipmentResponse200, ErrorResponse]]:
    """Accept shipment by carrier


    ## Accept Shipment by Carrier

    Carrier accepts a tendered shipment, transitioning from TENDERED to ACCEPTED status.

    ### Features
    - **Carrier Acceptance**: Confirms carrier commitment to transport
    - **Tracking Information**: Optional PRO number and tracking details
    - **Pickup Scheduling**: Optional estimated pickup date
    - **Status Transition**: TENDERED → ACCEPTED with audit trail

    ### Business Process
    1. Shipment must be in TENDERED status
    2. Carrier provides acceptance with optional details
    3. Status changes to ACCEPTED
    4. Pickup can now be scheduled
    5. Status change event is automatically created

    ### Optional Carrier Data
    - proNumber: Carrier's Progressive Number
    - trackingNumber: Carrier's tracking reference
    - estimatedPickupDate: When carrier plans to pickup


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AcceptTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AcceptTMSShipmentResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
