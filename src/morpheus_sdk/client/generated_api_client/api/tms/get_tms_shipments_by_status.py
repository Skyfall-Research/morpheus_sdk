import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_shipments_by_status_response_200 import GetTMSShipmentsByStatusResponse200
from ...models.get_tms_shipments_by_status_shipment_type import GetTMSShipmentsByStatusShipmentType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    shipment_type: Union[Unset, GetTMSShipmentsByStatusShipmentType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["status"] = status

    params["carrierId"] = carrier_id

    json_from_: Union[Unset, str] = UNSET
    if not isinstance(from_, Unset):
        json_from_ = from_.isoformat()
    params["from"] = json_from_

    json_to: Union[Unset, str] = UNSET
    if not isinstance(to, Unset):
        json_to = to.isoformat()
    params["to"] = json_to

    json_shipment_type: Union[Unset, str] = UNSET
    if not isinstance(shipment_type, Unset):
        json_shipment_type = shipment_type.value

    params["shipmentType"] = json_shipment_type

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/shipments",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSShipmentsByStatusResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]:
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
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    shipment_type: Union[Unset, GetTMSShipmentsByStatusShipmentType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]:
    """Get shipments by status with filtering


    ## Get TMS Shipments by Status

    Retrieve shipments filtered by status with advanced filtering and pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by multiple statuses using comma-separated values
    - **Advanced Filters**: Filter by carrier, date range, shipment type
    - **Cursor Pagination**: Efficient pagination for large result sets
    - **Performance Optimized**: Indexed queries for fast response times

    ### Status Values
    - PLANNED: Shipment created but not yet tendered
    - TENDERED: Shipment tendered to carrier
    - ACCEPTED: Carrier accepted the shipment
    - PICKED_UP: Cargo picked up from origin
    - IN_TRANSIT: Shipment in transit
    - OUT_FOR_DELIVERY: Out for final delivery
    - DELIVERED: Successfully delivered
    - CANCELLED: Shipment cancelled
    - DELAYED: Shipment experiencing delays
    - EXCEPTION: Exception occurred during transit


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: IN_TRANSIT,OUT_FOR_DELIVERY.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        shipment_type (Union[Unset, GetTMSShipmentsByStatusShipmentType]):  Example: OUTBOUND.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        carrier_id=carrier_id,
        from_=from_,
        to=to,
        shipment_type=shipment_type,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    shipment_type: Union[Unset, GetTMSShipmentsByStatusShipmentType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]:
    """Get shipments by status with filtering


    ## Get TMS Shipments by Status

    Retrieve shipments filtered by status with advanced filtering and pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by multiple statuses using comma-separated values
    - **Advanced Filters**: Filter by carrier, date range, shipment type
    - **Cursor Pagination**: Efficient pagination for large result sets
    - **Performance Optimized**: Indexed queries for fast response times

    ### Status Values
    - PLANNED: Shipment created but not yet tendered
    - TENDERED: Shipment tendered to carrier
    - ACCEPTED: Carrier accepted the shipment
    - PICKED_UP: Cargo picked up from origin
    - IN_TRANSIT: Shipment in transit
    - OUT_FOR_DELIVERY: Out for final delivery
    - DELIVERED: Successfully delivered
    - CANCELLED: Shipment cancelled
    - DELAYED: Shipment experiencing delays
    - EXCEPTION: Exception occurred during transit


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: IN_TRANSIT,OUT_FOR_DELIVERY.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        shipment_type (Union[Unset, GetTMSShipmentsByStatusShipmentType]):  Example: OUTBOUND.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        status=status,
        carrier_id=carrier_id,
        from_=from_,
        to=to,
        shipment_type=shipment_type,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    shipment_type: Union[Unset, GetTMSShipmentsByStatusShipmentType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]:
    """Get shipments by status with filtering


    ## Get TMS Shipments by Status

    Retrieve shipments filtered by status with advanced filtering and pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by multiple statuses using comma-separated values
    - **Advanced Filters**: Filter by carrier, date range, shipment type
    - **Cursor Pagination**: Efficient pagination for large result sets
    - **Performance Optimized**: Indexed queries for fast response times

    ### Status Values
    - PLANNED: Shipment created but not yet tendered
    - TENDERED: Shipment tendered to carrier
    - ACCEPTED: Carrier accepted the shipment
    - PICKED_UP: Cargo picked up from origin
    - IN_TRANSIT: Shipment in transit
    - OUT_FOR_DELIVERY: Out for final delivery
    - DELIVERED: Successfully delivered
    - CANCELLED: Shipment cancelled
    - DELAYED: Shipment experiencing delays
    - EXCEPTION: Exception occurred during transit


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: IN_TRANSIT,OUT_FOR_DELIVERY.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        shipment_type (Union[Unset, GetTMSShipmentsByStatusShipmentType]):  Example: OUTBOUND.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        status=status,
        carrier_id=carrier_id,
        from_=from_,
        to=to,
        shipment_type=shipment_type,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    status: str,
    carrier_id: Union[Unset, str] = UNSET,
    from_: Union[Unset, datetime.datetime] = UNSET,
    to: Union[Unset, datetime.datetime] = UNSET,
    shipment_type: Union[Unset, GetTMSShipmentsByStatusShipmentType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]]:
    """Get shipments by status with filtering


    ## Get TMS Shipments by Status

    Retrieve shipments filtered by status with advanced filtering and pagination capabilities.

    ### Features
    - **Multi-Status Filtering**: Filter by multiple statuses using comma-separated values
    - **Advanced Filters**: Filter by carrier, date range, shipment type
    - **Cursor Pagination**: Efficient pagination for large result sets
    - **Performance Optimized**: Indexed queries for fast response times

    ### Status Values
    - PLANNED: Shipment created but not yet tendered
    - TENDERED: Shipment tendered to carrier
    - ACCEPTED: Carrier accepted the shipment
    - PICKED_UP: Cargo picked up from origin
    - IN_TRANSIT: Shipment in transit
    - OUT_FOR_DELIVERY: Out for final delivery
    - DELIVERED: Successfully delivered
    - CANCELLED: Shipment cancelled
    - DELAYED: Shipment experiencing delays
    - EXCEPTION: Exception occurred during transit


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        status (str):  Example: IN_TRANSIT,OUT_FOR_DELIVERY.
        carrier_id (Union[Unset, str]):  Example: CARRIER_FEDEX_001.
        from_ (Union[Unset, datetime.datetime]):  Example: 2024-11-01T00:00:00.000Z.
        to (Union[Unset, datetime.datetime]):  Example: 2024-11-30T23:59:59.999Z.
        shipment_type (Union[Unset, GetTMSShipmentsByStatusShipmentType]):  Example: OUTBOUND.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSShipmentsByStatusResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            status=status,
            carrier_id=carrier_id,
            from_=from_,
            to=to,
            shipment_type=shipment_type,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
