from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.process_tms_edi_214_update_body import ProcessTMSEdi214UpdateBody
from ...models.process_tms_edi_214_update_response_200 import ProcessTMSEdi214UpdateResponse200
from ...models.process_tms_edi_214_update_response_400 import ProcessTMSEdi214UpdateResponse400
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: ProcessTMSEdi214UpdateBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/edi214",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]:
    if response.status_code == 200:
        response_200 = ProcessTMSEdi214UpdateResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = ProcessTMSEdi214UpdateResponse400.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]:
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
    body: ProcessTMSEdi214UpdateBody,
) -> Response[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]:
    """Process EDI 214 status update


    ## Process EDI 214 Transportation Status Update

    Process an incoming EDI 214 Transportation Status message to update shipment status and location.

    ### Features
    - **EDI 214 Processing**: Parse and process standard EDI 214 messages
    - **Status Mapping**: Map EDI status codes to internal shipment statuses
    - **Location Updates**: Extract and update location information from EDI
    - **ETA Updates**: Update estimated delivery dates based on EDI data
    - **Raw Data Preservation**: Store complete raw EDI message for audit

    ### EDI 214 Message Types
    - **Departure**: Shipment departed from location
    - **Arrival**: Shipment arrived at location
    - **In-Transit**: Shipment status update during transit
    - **Delivery**: Final delivery confirmation
    - **Exception**: Delays or problems during transit

    ### Data Processing
    - Validates EDI message structure
    - Maps EDI status codes to shipment statuses
    - Updates location and ETA information
    - Creates corresponding status events
    - Preserves raw EDI for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (ProcessTMSEdi214UpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]
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
    body: ProcessTMSEdi214UpdateBody,
) -> Optional[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]:
    """Process EDI 214 status update


    ## Process EDI 214 Transportation Status Update

    Process an incoming EDI 214 Transportation Status message to update shipment status and location.

    ### Features
    - **EDI 214 Processing**: Parse and process standard EDI 214 messages
    - **Status Mapping**: Map EDI status codes to internal shipment statuses
    - **Location Updates**: Extract and update location information from EDI
    - **ETA Updates**: Update estimated delivery dates based on EDI data
    - **Raw Data Preservation**: Store complete raw EDI message for audit

    ### EDI 214 Message Types
    - **Departure**: Shipment departed from location
    - **Arrival**: Shipment arrived at location
    - **In-Transit**: Shipment status update during transit
    - **Delivery**: Final delivery confirmation
    - **Exception**: Delays or problems during transit

    ### Data Processing
    - Validates EDI message structure
    - Maps EDI status codes to shipment statuses
    - Updates location and ETA information
    - Creates corresponding status events
    - Preserves raw EDI for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (ProcessTMSEdi214UpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]
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
    body: ProcessTMSEdi214UpdateBody,
) -> Response[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]:
    """Process EDI 214 status update


    ## Process EDI 214 Transportation Status Update

    Process an incoming EDI 214 Transportation Status message to update shipment status and location.

    ### Features
    - **EDI 214 Processing**: Parse and process standard EDI 214 messages
    - **Status Mapping**: Map EDI status codes to internal shipment statuses
    - **Location Updates**: Extract and update location information from EDI
    - **ETA Updates**: Update estimated delivery dates based on EDI data
    - **Raw Data Preservation**: Store complete raw EDI message for audit

    ### EDI 214 Message Types
    - **Departure**: Shipment departed from location
    - **Arrival**: Shipment arrived at location
    - **In-Transit**: Shipment status update during transit
    - **Delivery**: Final delivery confirmation
    - **Exception**: Delays or problems during transit

    ### Data Processing
    - Validates EDI message structure
    - Maps EDI status codes to shipment statuses
    - Updates location and ETA information
    - Creates corresponding status events
    - Preserves raw EDI for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (ProcessTMSEdi214UpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]
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
    body: ProcessTMSEdi214UpdateBody,
) -> Optional[Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]]:
    """Process EDI 214 status update


    ## Process EDI 214 Transportation Status Update

    Process an incoming EDI 214 Transportation Status message to update shipment status and location.

    ### Features
    - **EDI 214 Processing**: Parse and process standard EDI 214 messages
    - **Status Mapping**: Map EDI status codes to internal shipment statuses
    - **Location Updates**: Extract and update location information from EDI
    - **ETA Updates**: Update estimated delivery dates based on EDI data
    - **Raw Data Preservation**: Store complete raw EDI message for audit

    ### EDI 214 Message Types
    - **Departure**: Shipment departed from location
    - **Arrival**: Shipment arrived at location
    - **In-Transit**: Shipment status update during transit
    - **Delivery**: Final delivery confirmation
    - **Exception**: Delays or problems during transit

    ### Data Processing
    - Validates EDI message structure
    - Maps EDI status codes to shipment statuses
    - Updates location and ETA information
    - Creates corresponding status events
    - Preserves raw EDI for compliance


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (ProcessTMSEdi214UpdateBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ProcessTMSEdi214UpdateResponse200, ProcessTMSEdi214UpdateResponse400]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
