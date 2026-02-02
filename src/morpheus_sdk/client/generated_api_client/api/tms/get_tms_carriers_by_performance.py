from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_tms_carriers_by_performance_carrier_type import GetTMSCarriersByPerformanceCarrierType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    min_on_time_rate: Union[Unset, float] = UNSET,
    max_damage_rate: Union[Unset, float] = UNSET,
    max_transit_time: Union[Unset, float] = UNSET,
    carrier_type: Union[Unset, GetTMSCarriersByPerformanceCarrierType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["minOnTimeRate"] = min_on_time_rate

    params["maxDamageRate"] = max_damage_rate

    params["maxTransitTime"] = max_transit_time

    json_carrier_type: Union[Unset, str] = UNSET
    if not isinstance(carrier_type, Unset):
        json_carrier_type = carrier_type.value

    params["carrierType"] = json_carrier_type

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/carriers/performance",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
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
    min_on_time_rate: Union[Unset, float] = UNSET,
    max_damage_rate: Union[Unset, float] = UNSET,
    max_transit_time: Union[Unset, float] = UNSET,
    carrier_type: Union[Unset, GetTMSCarriersByPerformanceCarrierType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[ErrorResponse]:
    """Get carriers by performance criteria


    ## Get Carriers by Performance

    Find carriers that meet specific performance criteria and service level requirements.

    ### Features
    - **Performance Filtering**: Filter by on-time rate, damage rate, and transit time
    - **Quality Assurance**: Find top-performing carriers for critical shipments
    - **Benchmarking**: Compare carrier performance against standards
    - **Service Level Optimization**: Match carriers to shipment requirements
    - **Performance Sorting**: Results sorted by performance metrics

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage of shipments delivered on time
    - **Damage Claim Rate**: Percentage of shipments with damage claims
    - **Average Transit Time**: Average hours in transit
    - **Total Shipments**: Historical volume completed

    ### Use Cases
    - Premium service lane setup
    - Carrier performance benchmarking
    - Service level agreement compliance
    - Quality-focused carrier selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        min_on_time_rate (Union[Unset, float]):  Example: 0.95.
        max_damage_rate (Union[Unset, float]):  Example: 0.01.
        max_transit_time (Union[Unset, float]):  Example: 72.
        carrier_type (Union[Unset, GetTMSCarriersByPerformanceCarrierType]):  Example: FTL.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        min_on_time_rate=min_on_time_rate,
        max_damage_rate=max_damage_rate,
        max_transit_time=max_transit_time,
        carrier_type=carrier_type,
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
    min_on_time_rate: Union[Unset, float] = UNSET,
    max_damage_rate: Union[Unset, float] = UNSET,
    max_transit_time: Union[Unset, float] = UNSET,
    carrier_type: Union[Unset, GetTMSCarriersByPerformanceCarrierType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[ErrorResponse]:
    """Get carriers by performance criteria


    ## Get Carriers by Performance

    Find carriers that meet specific performance criteria and service level requirements.

    ### Features
    - **Performance Filtering**: Filter by on-time rate, damage rate, and transit time
    - **Quality Assurance**: Find top-performing carriers for critical shipments
    - **Benchmarking**: Compare carrier performance against standards
    - **Service Level Optimization**: Match carriers to shipment requirements
    - **Performance Sorting**: Results sorted by performance metrics

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage of shipments delivered on time
    - **Damage Claim Rate**: Percentage of shipments with damage claims
    - **Average Transit Time**: Average hours in transit
    - **Total Shipments**: Historical volume completed

    ### Use Cases
    - Premium service lane setup
    - Carrier performance benchmarking
    - Service level agreement compliance
    - Quality-focused carrier selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        min_on_time_rate (Union[Unset, float]):  Example: 0.95.
        max_damage_rate (Union[Unset, float]):  Example: 0.01.
        max_transit_time (Union[Unset, float]):  Example: 72.
        carrier_type (Union[Unset, GetTMSCarriersByPerformanceCarrierType]):  Example: FTL.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        min_on_time_rate=min_on_time_rate,
        max_damage_rate=max_damage_rate,
        max_transit_time=max_transit_time,
        carrier_type=carrier_type,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    min_on_time_rate: Union[Unset, float] = UNSET,
    max_damage_rate: Union[Unset, float] = UNSET,
    max_transit_time: Union[Unset, float] = UNSET,
    carrier_type: Union[Unset, GetTMSCarriersByPerformanceCarrierType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Response[ErrorResponse]:
    """Get carriers by performance criteria


    ## Get Carriers by Performance

    Find carriers that meet specific performance criteria and service level requirements.

    ### Features
    - **Performance Filtering**: Filter by on-time rate, damage rate, and transit time
    - **Quality Assurance**: Find top-performing carriers for critical shipments
    - **Benchmarking**: Compare carrier performance against standards
    - **Service Level Optimization**: Match carriers to shipment requirements
    - **Performance Sorting**: Results sorted by performance metrics

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage of shipments delivered on time
    - **Damage Claim Rate**: Percentage of shipments with damage claims
    - **Average Transit Time**: Average hours in transit
    - **Total Shipments**: Historical volume completed

    ### Use Cases
    - Premium service lane setup
    - Carrier performance benchmarking
    - Service level agreement compliance
    - Quality-focused carrier selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        min_on_time_rate (Union[Unset, float]):  Example: 0.95.
        max_damage_rate (Union[Unset, float]):  Example: 0.01.
        max_transit_time (Union[Unset, float]):  Example: 72.
        carrier_type (Union[Unset, GetTMSCarriersByPerformanceCarrierType]):  Example: FTL.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        min_on_time_rate=min_on_time_rate,
        max_damage_rate=max_damage_rate,
        max_transit_time=max_transit_time,
        carrier_type=carrier_type,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    min_on_time_rate: Union[Unset, float] = UNSET,
    max_damage_rate: Union[Unset, float] = UNSET,
    max_transit_time: Union[Unset, float] = UNSET,
    carrier_type: Union[Unset, GetTMSCarriersByPerformanceCarrierType] = UNSET,
    limit: Union[Unset, int] = UNSET,
    cursor: Union[Unset, str] = UNSET,
) -> Optional[ErrorResponse]:
    """Get carriers by performance criteria


    ## Get Carriers by Performance

    Find carriers that meet specific performance criteria and service level requirements.

    ### Features
    - **Performance Filtering**: Filter by on-time rate, damage rate, and transit time
    - **Quality Assurance**: Find top-performing carriers for critical shipments
    - **Benchmarking**: Compare carrier performance against standards
    - **Service Level Optimization**: Match carriers to shipment requirements
    - **Performance Sorting**: Results sorted by performance metrics

    ### Performance Metrics
    - **On-Time Delivery Rate**: Percentage of shipments delivered on time
    - **Damage Claim Rate**: Percentage of shipments with damage claims
    - **Average Transit Time**: Average hours in transit
    - **Total Shipments**: Historical volume completed

    ### Use Cases
    - Premium service lane setup
    - Carrier performance benchmarking
    - Service level agreement compliance
    - Quality-focused carrier selection


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        min_on_time_rate (Union[Unset, float]):  Example: 0.95.
        max_damage_rate (Union[Unset, float]):  Example: 0.01.
        max_transit_time (Union[Unset, float]):  Example: 72.
        carrier_type (Union[Unset, GetTMSCarriersByPerformanceCarrierType]):  Example: FTL.
        limit (Union[Unset, int]):  Example: 50.
        cursor (Union[Unset, str]):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            min_on_time_rate=min_on_time_rate,
            max_damage_rate=max_damage_rate,
            max_transit_time=max_transit_time,
            carrier_type=carrier_type,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
