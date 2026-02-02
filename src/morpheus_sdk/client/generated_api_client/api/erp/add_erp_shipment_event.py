from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_erp_shipment_event_body import AddERPShipmentEventBody
from ...models.add_erp_shipment_event_response_200 import AddERPShipmentEventResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: AddERPShipmentEventBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/erp/shipments/{shipment_id}/events",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddERPShipmentEventResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddERPShipmentEventResponse200.from_dict(response.json())

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
) -> Response[Union[AddERPShipmentEventResponse200, ErrorResponse]]:
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
    body: AddERPShipmentEventBody,
) -> Response[Union[AddERPShipmentEventResponse200, ErrorResponse]]:
    """Add ERP shipment event


    Add tracking event to ERP shipment for comprehensive logistics monitoring and audit trail.

    **Core Features**:
    - **Event Tracking**: Add timestamped events for shipment monitoring
    - **Location Updates**: Track shipment movement through various locations
    - **Status Events**: Record status changes with detailed information
    - **Audit Trail**: Maintain complete event history for shipments

    **Use Cases**:
    - **Carrier Integration**: Add events from carrier tracking systems
    - **Logistics Monitoring**: Record shipment progress through distribution network
    - **Exception Management**: Log delivery exceptions and resolution actions
    - **Customer Service**: Provide detailed shipment tracking information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddERPShipmentEventResponse200, ErrorResponse]]
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
    body: AddERPShipmentEventBody,
) -> Optional[Union[AddERPShipmentEventResponse200, ErrorResponse]]:
    """Add ERP shipment event


    Add tracking event to ERP shipment for comprehensive logistics monitoring and audit trail.

    **Core Features**:
    - **Event Tracking**: Add timestamped events for shipment monitoring
    - **Location Updates**: Track shipment movement through various locations
    - **Status Events**: Record status changes with detailed information
    - **Audit Trail**: Maintain complete event history for shipments

    **Use Cases**:
    - **Carrier Integration**: Add events from carrier tracking systems
    - **Logistics Monitoring**: Record shipment progress through distribution network
    - **Exception Management**: Log delivery exceptions and resolution actions
    - **Customer Service**: Provide detailed shipment tracking information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddERPShipmentEventResponse200, ErrorResponse]
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
    body: AddERPShipmentEventBody,
) -> Response[Union[AddERPShipmentEventResponse200, ErrorResponse]]:
    """Add ERP shipment event


    Add tracking event to ERP shipment for comprehensive logistics monitoring and audit trail.

    **Core Features**:
    - **Event Tracking**: Add timestamped events for shipment monitoring
    - **Location Updates**: Track shipment movement through various locations
    - **Status Events**: Record status changes with detailed information
    - **Audit Trail**: Maintain complete event history for shipments

    **Use Cases**:
    - **Carrier Integration**: Add events from carrier tracking systems
    - **Logistics Monitoring**: Record shipment progress through distribution network
    - **Exception Management**: Log delivery exceptions and resolution actions
    - **Customer Service**: Provide detailed shipment tracking information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddERPShipmentEventResponse200, ErrorResponse]]
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
    body: AddERPShipmentEventBody,
) -> Optional[Union[AddERPShipmentEventResponse200, ErrorResponse]]:
    """Add ERP shipment event


    Add tracking event to ERP shipment for comprehensive logistics monitoring and audit trail.

    **Core Features**:
    - **Event Tracking**: Add timestamped events for shipment monitoring
    - **Location Updates**: Track shipment movement through various locations
    - **Status Events**: Record status changes with detailed information
    - **Audit Trail**: Maintain complete event history for shipments

    **Use Cases**:
    - **Carrier Integration**: Add events from carrier tracking systems
    - **Logistics Monitoring**: Record shipment progress through distribution network
    - **Exception Management**: Log delivery exceptions and resolution actions
    - **Customer Service**: Provide detailed shipment tracking information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (AddERPShipmentEventBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddERPShipmentEventResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
