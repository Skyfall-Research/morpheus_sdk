from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_erp_shipment_tracking_body import UpdateERPShipmentTrackingBody
from ...models.update_erp_shipment_tracking_response_200 import UpdateERPShipmentTrackingResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    shipment_id: str,
    *,
    body: UpdateERPShipmentTrackingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/erp/shipments/{shipment_id}/tracking",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateERPShipmentTrackingResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]:
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
    body: UpdateERPShipmentTrackingBody,
) -> Response[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]:
    """Update ERP shipment tracking details


    Update ERP shipment carrier and tracking information for enhanced logistics visibility.

    **Core Features**:
    - **Tracking Management**: Update carrier and tracking number information
    - **Carrier Integration**: Support for multiple carrier integrations
    - **Real-time Updates**: Update tracking details as information becomes available
    - **Visibility Enhancement**: Improve shipment tracking for all stakeholders

    **Use Cases**:
    - **Carrier Integration**: Update tracking when shipments are picked up by carriers
    - **Label Generation**: Add tracking numbers when shipping labels are generated
    - **Customer Service**: Provide tracking updates for customer inquiries
    - **Logistics Operations**: Maintain accurate tracking information for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentTrackingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]
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
    body: UpdateERPShipmentTrackingBody,
) -> Optional[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]:
    """Update ERP shipment tracking details


    Update ERP shipment carrier and tracking information for enhanced logistics visibility.

    **Core Features**:
    - **Tracking Management**: Update carrier and tracking number information
    - **Carrier Integration**: Support for multiple carrier integrations
    - **Real-time Updates**: Update tracking details as information becomes available
    - **Visibility Enhancement**: Improve shipment tracking for all stakeholders

    **Use Cases**:
    - **Carrier Integration**: Update tracking when shipments are picked up by carriers
    - **Label Generation**: Add tracking numbers when shipping labels are generated
    - **Customer Service**: Provide tracking updates for customer inquiries
    - **Logistics Operations**: Maintain accurate tracking information for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentTrackingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]
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
    body: UpdateERPShipmentTrackingBody,
) -> Response[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]:
    """Update ERP shipment tracking details


    Update ERP shipment carrier and tracking information for enhanced logistics visibility.

    **Core Features**:
    - **Tracking Management**: Update carrier and tracking number information
    - **Carrier Integration**: Support for multiple carrier integrations
    - **Real-time Updates**: Update tracking details as information becomes available
    - **Visibility Enhancement**: Improve shipment tracking for all stakeholders

    **Use Cases**:
    - **Carrier Integration**: Update tracking when shipments are picked up by carriers
    - **Label Generation**: Add tracking numbers when shipping labels are generated
    - **Customer Service**: Provide tracking updates for customer inquiries
    - **Logistics Operations**: Maintain accurate tracking information for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentTrackingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]
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
    body: UpdateERPShipmentTrackingBody,
) -> Optional[Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]]:
    """Update ERP shipment tracking details


    Update ERP shipment carrier and tracking information for enhanced logistics visibility.

    **Core Features**:
    - **Tracking Management**: Update carrier and tracking number information
    - **Carrier Integration**: Support for multiple carrier integrations
    - **Real-time Updates**: Update tracking details as information becomes available
    - **Visibility Enhancement**: Improve shipment tracking for all stakeholders

    **Use Cases**:
    - **Carrier Integration**: Update tracking when shipments are picked up by carriers
    - **Label Generation**: Add tracking numbers when shipping labels are generated
    - **Customer Service**: Provide tracking updates for customer inquiries
    - **Logistics Operations**: Maintain accurate tracking information for operations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        shipment_id (str):  Example: SHIP_507f1f77bcf86cd799439012.
        body (UpdateERPShipmentTrackingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateERPShipmentTrackingResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            shipment_id=shipment_id,
            client=client,
            body=body,
        )
    ).parsed
