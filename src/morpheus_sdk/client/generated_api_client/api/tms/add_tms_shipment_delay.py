from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_tms_shipment_delay_body import AddTMSShipmentDelayBody
from ...models.add_tms_shipment_delay_response_200 import AddTMSShipmentDelayResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: AddTMSShipmentDelayBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/shipments/{shipment_id}/delays",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddTMSShipmentDelayResponse200.from_dict(response.json())

        return response_200

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
) -> Response[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]:
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
    body: AddTMSShipmentDelayBody,
) -> Response[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]:
    """Add shipment delay


    ## Add Shipment Delay

    Record a delay for a shipment with detailed information about the cause and impact.

    ### Features
    - **Delay Tracking**: Comprehensive delay recording and impact analysis
    - **Delay Types**: Categorized delay types for better analytics
    - **Time Tracking**: Start time, end time, and estimated delay duration
    - **Impact Analysis**: Understand delay impact on delivery schedules
    - **Customer Communication**: Data for proactive customer notifications

    ### Delay Types
    - **WEATHER**: Weather-related delays
    - **TRAFFIC**: Traffic congestion or road closures
    - **MECHANICAL**: Vehicle or equipment issues
    - **CARRIER**: Carrier operational issues
    - **CUSTOMS**: Customs or border delays (international)
    - **OTHER**: Other unforeseen circumstances

    ### Delay Management
    - Delays can be ongoing (no end time) or completed
    - Estimated delay helps with ETA recalculation
    - Detailed reasons support customer communication
    - Delay patterns help improve route planning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AddTMSShipmentDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]
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
    body: AddTMSShipmentDelayBody,
) -> Optional[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]:
    """Add shipment delay


    ## Add Shipment Delay

    Record a delay for a shipment with detailed information about the cause and impact.

    ### Features
    - **Delay Tracking**: Comprehensive delay recording and impact analysis
    - **Delay Types**: Categorized delay types for better analytics
    - **Time Tracking**: Start time, end time, and estimated delay duration
    - **Impact Analysis**: Understand delay impact on delivery schedules
    - **Customer Communication**: Data for proactive customer notifications

    ### Delay Types
    - **WEATHER**: Weather-related delays
    - **TRAFFIC**: Traffic congestion or road closures
    - **MECHANICAL**: Vehicle or equipment issues
    - **CARRIER**: Carrier operational issues
    - **CUSTOMS**: Customs or border delays (international)
    - **OTHER**: Other unforeseen circumstances

    ### Delay Management
    - Delays can be ongoing (no end time) or completed
    - Estimated delay helps with ETA recalculation
    - Detailed reasons support customer communication
    - Delay patterns help improve route planning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AddTMSShipmentDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddTMSShipmentDelayResponse200, ErrorResponse]
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
    body: AddTMSShipmentDelayBody,
) -> Response[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]:
    """Add shipment delay


    ## Add Shipment Delay

    Record a delay for a shipment with detailed information about the cause and impact.

    ### Features
    - **Delay Tracking**: Comprehensive delay recording and impact analysis
    - **Delay Types**: Categorized delay types for better analytics
    - **Time Tracking**: Start time, end time, and estimated delay duration
    - **Impact Analysis**: Understand delay impact on delivery schedules
    - **Customer Communication**: Data for proactive customer notifications

    ### Delay Types
    - **WEATHER**: Weather-related delays
    - **TRAFFIC**: Traffic congestion or road closures
    - **MECHANICAL**: Vehicle or equipment issues
    - **CARRIER**: Carrier operational issues
    - **CUSTOMS**: Customs or border delays (international)
    - **OTHER**: Other unforeseen circumstances

    ### Delay Management
    - Delays can be ongoing (no end time) or completed
    - Estimated delay helps with ETA recalculation
    - Detailed reasons support customer communication
    - Delay patterns help improve route planning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AddTMSShipmentDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]
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
    body: AddTMSShipmentDelayBody,
) -> Optional[Union[AddTMSShipmentDelayResponse200, ErrorResponse]]:
    """Add shipment delay


    ## Add Shipment Delay

    Record a delay for a shipment with detailed information about the cause and impact.

    ### Features
    - **Delay Tracking**: Comprehensive delay recording and impact analysis
    - **Delay Types**: Categorized delay types for better analytics
    - **Time Tracking**: Start time, end time, and estimated delay duration
    - **Impact Analysis**: Understand delay impact on delivery schedules
    - **Customer Communication**: Data for proactive customer notifications

    ### Delay Types
    - **WEATHER**: Weather-related delays
    - **TRAFFIC**: Traffic congestion or road closures
    - **MECHANICAL**: Vehicle or equipment issues
    - **CARRIER**: Carrier operational issues
    - **CUSTOMS**: Customs or border delays (international)
    - **OTHER**: Other unforeseen circumstances

    ### Delay Management
    - Delays can be ongoing (no end time) or completed
    - Estimated delay helps with ETA recalculation
    - Detailed reasons support customer communication
    - Delay patterns help improve route planning


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP-2024-001234.
        body (AddTMSShipmentDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddTMSShipmentDelayResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
