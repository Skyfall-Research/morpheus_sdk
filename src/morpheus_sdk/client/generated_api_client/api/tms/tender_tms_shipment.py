from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.tender_tms_shipment_body import TenderTMSShipmentBody
from ...models.tender_tms_shipment_response_200 import TenderTMSShipmentResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: TenderTMSShipmentBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/tender",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, TenderTMSShipmentResponse200]]:
    if response.status_code == 200:
        response_200 = TenderTMSShipmentResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

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
) -> Response[Union[ErrorResponse, TenderTMSShipmentResponse200]]:
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
    body: TenderTMSShipmentBody,
) -> Response[Union[ErrorResponse, TenderTMSShipmentResponse200]]:
    """Tender shipment to carrier


    ## Tender Shipment to Carrier

    Tender a shipment to a specific carrier, transitioning from PLANNED to TENDERED status.

    ### Features
    - **Carrier Assignment**: Assign specific carrier with complete information
    - **Status Transition**: PLANNED → TENDERED with audit trail
    - **Automatic Events**: Creates status change event automatically
    - **Validation**: Ensures shipment is in PLANNED status before tendering

    ### Business Process
    1. Shipment must be in PLANNED status
    2. Carrier information is validated and assigned
    3. Status changes to TENDERED
    4. Status change event is automatically created
    5. Carrier can now accept or decline the shipment

    ### Required Carrier Information
    - carrierId: Unique carrier identifier
    - carrierName: Display name of the carrier
    - carrierCode: Standard carrier code
    - scacCode: Standard Carrier Alpha Code


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TenderTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TenderTMSShipmentResponse200]]
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
    body: TenderTMSShipmentBody,
) -> Optional[Union[ErrorResponse, TenderTMSShipmentResponse200]]:
    """Tender shipment to carrier


    ## Tender Shipment to Carrier

    Tender a shipment to a specific carrier, transitioning from PLANNED to TENDERED status.

    ### Features
    - **Carrier Assignment**: Assign specific carrier with complete information
    - **Status Transition**: PLANNED → TENDERED with audit trail
    - **Automatic Events**: Creates status change event automatically
    - **Validation**: Ensures shipment is in PLANNED status before tendering

    ### Business Process
    1. Shipment must be in PLANNED status
    2. Carrier information is validated and assigned
    3. Status changes to TENDERED
    4. Status change event is automatically created
    5. Carrier can now accept or decline the shipment

    ### Required Carrier Information
    - carrierId: Unique carrier identifier
    - carrierName: Display name of the carrier
    - carrierCode: Standard carrier code
    - scacCode: Standard Carrier Alpha Code


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TenderTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TenderTMSShipmentResponse200]
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
    body: TenderTMSShipmentBody,
) -> Response[Union[ErrorResponse, TenderTMSShipmentResponse200]]:
    """Tender shipment to carrier


    ## Tender Shipment to Carrier

    Tender a shipment to a specific carrier, transitioning from PLANNED to TENDERED status.

    ### Features
    - **Carrier Assignment**: Assign specific carrier with complete information
    - **Status Transition**: PLANNED → TENDERED with audit trail
    - **Automatic Events**: Creates status change event automatically
    - **Validation**: Ensures shipment is in PLANNED status before tendering

    ### Business Process
    1. Shipment must be in PLANNED status
    2. Carrier information is validated and assigned
    3. Status changes to TENDERED
    4. Status change event is automatically created
    5. Carrier can now accept or decline the shipment

    ### Required Carrier Information
    - carrierId: Unique carrier identifier
    - carrierName: Display name of the carrier
    - carrierCode: Standard carrier code
    - scacCode: Standard Carrier Alpha Code


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TenderTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, TenderTMSShipmentResponse200]]
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
    body: TenderTMSShipmentBody,
) -> Optional[Union[ErrorResponse, TenderTMSShipmentResponse200]]:
    """Tender shipment to carrier


    ## Tender Shipment to Carrier

    Tender a shipment to a specific carrier, transitioning from PLANNED to TENDERED status.

    ### Features
    - **Carrier Assignment**: Assign specific carrier with complete information
    - **Status Transition**: PLANNED → TENDERED with audit trail
    - **Automatic Events**: Creates status change event automatically
    - **Validation**: Ensures shipment is in PLANNED status before tendering

    ### Business Process
    1. Shipment must be in PLANNED status
    2. Carrier information is validated and assigned
    3. Status changes to TENDERED
    4. Status change event is automatically created
    5. Carrier can now accept or decline the shipment

    ### Required Carrier Information
    - carrierId: Unique carrier identifier
    - carrierName: Display name of the carrier
    - carrierCode: Standard carrier code
    - scacCode: Standard Carrier Alpha Code


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (TenderTMSShipmentBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, TenderTMSShipmentResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
