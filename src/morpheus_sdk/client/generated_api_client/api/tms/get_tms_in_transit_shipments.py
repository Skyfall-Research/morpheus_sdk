from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_in_transit_shipments_response_200 import GetTMSInTransitShipmentsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/shipments/in-transit",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]:
    if response.status_code == 200:
        response_200 = GetTMSInTransitShipmentsResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 500:
        response_500 = ErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]:
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
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]:
    """Get all in-transit shipments


    ## Get In-Transit TMS Shipments

    Retrieve all shipments currently in transit with real-time location and ETA information.

    ### Features
    - **Real-Time Tracking**: Current location and movement data
    - **ETA Calculations**: Estimated delivery times based on current position
    - **Exception Monitoring**: Identify shipments with delays or exceptions
    - **Performance Metrics**: Transit time and on-time delivery tracking

    ### In-Transit Status Definition
    Shipments with status IN_TRANSIT, including those with recent location updates and active tracking.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
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
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]:
    """Get all in-transit shipments


    ## Get In-Transit TMS Shipments

    Retrieve all shipments currently in transit with real-time location and ETA information.

    ### Features
    - **Real-Time Tracking**: Current location and movement data
    - **ETA Calculations**: Estimated delivery times based on current position
    - **Exception Monitoring**: Identify shipments with delays or exceptions
    - **Performance Metrics**: Transit time and on-time delivery tracking

    ### In-Transit Status Definition
    Shipments with status IN_TRANSIT, including those with recent location updates and active tracking.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]:
    """Get all in-transit shipments


    ## Get In-Transit TMS Shipments

    Retrieve all shipments currently in transit with real-time location and ETA information.

    ### Features
    - **Real-Time Tracking**: Current location and movement data
    - **ETA Calculations**: Estimated delivery times based on current position
    - **Exception Monitoring**: Identify shipments with delays or exceptions
    - **Performance Metrics**: Transit time and on-time delivery tracking

    ### In-Transit Status Definition
    Shipments with status IN_TRANSIT, including those with recent location updates and active tracking.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]]:
    """Get all in-transit shipments


    ## Get In-Transit TMS Shipments

    Retrieve all shipments currently in transit with real-time location and ETA information.

    ### Features
    - **Real-Time Tracking**: Current location and movement data
    - **ETA Calculations**: Estimated delivery times based on current position
    - **Exception Monitoring**: Identify shipments with delays or exceptions
    - **Performance Metrics**: Transit time and on-time delivery tracking

    ### In-Transit Status Definition
    Shipments with status IN_TRANSIT, including those with recent location updates and active tracking.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetTMSInTransitShipmentsResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
