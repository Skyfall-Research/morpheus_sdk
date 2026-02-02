from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_tms_shipment_response_201 import CreateTMSShipmentResponse201
from ...models.error_response import ErrorResponse
from ...models.tms_shipment_input import TMSShipmentInput
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: TMSShipmentInput,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/shipments",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateTMSShipmentResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateTMSShipmentResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateTMSShipmentResponse201, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TMSShipmentInput,
) -> Response[Union[CreateTMSShipmentResponse201, ErrorResponse]]:
    """Create a new TMS shipment


    ## Create TMS Shipment

    Create a new shipment in the Transportation Management System with comprehensive tracking and
    logistics information.

    ### Features
    - **Complete Shipment Definition**: Origin, destination, carrier, cargo, and routing information
    - **Status Management**: Automatic status initialization to PLANNED
    - **Auto ID Generation**: Automatic shipmentId generation if not provided
    - **Audit Trail**: Full audit logging of shipment creation

    ### Shipment Status Flow
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → DELIVERED

    ### Required Fields
    - shipmentNumber: Unique business identifier
    - origin: Complete origin location information
    - destination: Complete destination location information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSShipmentInput): Input data for creating a new TMS shipment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTMSShipmentResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TMSShipmentInput,
) -> Optional[Union[CreateTMSShipmentResponse201, ErrorResponse]]:
    """Create a new TMS shipment


    ## Create TMS Shipment

    Create a new shipment in the Transportation Management System with comprehensive tracking and
    logistics information.

    ### Features
    - **Complete Shipment Definition**: Origin, destination, carrier, cargo, and routing information
    - **Status Management**: Automatic status initialization to PLANNED
    - **Auto ID Generation**: Automatic shipmentId generation if not provided
    - **Audit Trail**: Full audit logging of shipment creation

    ### Shipment Status Flow
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → DELIVERED

    ### Required Fields
    - shipmentNumber: Unique business identifier
    - origin: Complete origin location information
    - destination: Complete destination location information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSShipmentInput): Input data for creating a new TMS shipment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTMSShipmentResponse201, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TMSShipmentInput,
) -> Response[Union[CreateTMSShipmentResponse201, ErrorResponse]]:
    """Create a new TMS shipment


    ## Create TMS Shipment

    Create a new shipment in the Transportation Management System with comprehensive tracking and
    logistics information.

    ### Features
    - **Complete Shipment Definition**: Origin, destination, carrier, cargo, and routing information
    - **Status Management**: Automatic status initialization to PLANNED
    - **Auto ID Generation**: Automatic shipmentId generation if not provided
    - **Audit Trail**: Full audit logging of shipment creation

    ### Shipment Status Flow
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → DELIVERED

    ### Required Fields
    - shipmentNumber: Unique business identifier
    - origin: Complete origin location information
    - destination: Complete destination location information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSShipmentInput): Input data for creating a new TMS shipment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateTMSShipmentResponse201, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TMSShipmentInput,
) -> Optional[Union[CreateTMSShipmentResponse201, ErrorResponse]]:
    """Create a new TMS shipment


    ## Create TMS Shipment

    Create a new shipment in the Transportation Management System with comprehensive tracking and
    logistics information.

    ### Features
    - **Complete Shipment Definition**: Origin, destination, carrier, cargo, and routing information
    - **Status Management**: Automatic status initialization to PLANNED
    - **Auto ID Generation**: Automatic shipmentId generation if not provided
    - **Audit Trail**: Full audit logging of shipment creation

    ### Shipment Status Flow
    PLANNED → TENDERED → ACCEPTED → PICKED_UP → IN_TRANSIT → DELIVERED

    ### Required Fields
    - shipmentNumber: Unique business identifier
    - origin: Complete origin location information
    - destination: Complete destination location information


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (TMSShipmentInput): Input data for creating a new TMS shipment

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateTMSShipmentResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
