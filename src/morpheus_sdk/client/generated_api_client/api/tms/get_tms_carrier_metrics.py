from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    carrier_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/tms/carriers/{carrier_id}/metrics",
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[ErrorResponse]:
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


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[ErrorResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ErrorResponse]:
    """Get carrier performance and compliance metrics


    ## Get TMS Carrier Metrics

    Retrieve comprehensive performance and compliance metrics for a specific carrier.

    ### Features
    - **Current Performance**: Real-time performance indicators
    - **Recent Trends**: Historical performance trend data
    - **Compliance Status**: DOT, MC, insurance, and safety information
    - **Operational Intelligence**: Data for carrier selection and evaluation

    ### Performance Metrics Included
    - **On-Time Delivery Rate**: Current percentage (0.0-1.0)
    - **Damage Claim Rate**: Current damage rate (0.0-1.0)
    - **Average Transit Time**: Current average in hours
    - **Total Shipments**: Lifetime completed shipment count
    - **Last Update**: When metrics were last refreshed

    ### Compliance Metrics Included
    - **DOT Number**: Department of Transportation registration
    - **MC Number**: Motor Carrier authority number
    - **SCAC Code**: Standard Carrier Alpha Code
    - **SmartWay Certification**: Environmental compliance status
    - **Insurance Expiry**: Current insurance coverage expiration
    - **Safety Rating**: Current DOT safety assessment

    ### Business Use Cases
    - Carrier selection and ranking algorithms
    - Performance benchmarking and analysis
    - Compliance monitoring and alerts
    - Contract negotiation data
    - Risk assessment and mitigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_id=carrier_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ErrorResponse]:
    """Get carrier performance and compliance metrics


    ## Get TMS Carrier Metrics

    Retrieve comprehensive performance and compliance metrics for a specific carrier.

    ### Features
    - **Current Performance**: Real-time performance indicators
    - **Recent Trends**: Historical performance trend data
    - **Compliance Status**: DOT, MC, insurance, and safety information
    - **Operational Intelligence**: Data for carrier selection and evaluation

    ### Performance Metrics Included
    - **On-Time Delivery Rate**: Current percentage (0.0-1.0)
    - **Damage Claim Rate**: Current damage rate (0.0-1.0)
    - **Average Transit Time**: Current average in hours
    - **Total Shipments**: Lifetime completed shipment count
    - **Last Update**: When metrics were last refreshed

    ### Compliance Metrics Included
    - **DOT Number**: Department of Transportation registration
    - **MC Number**: Motor Carrier authority number
    - **SCAC Code**: Standard Carrier Alpha Code
    - **SmartWay Certification**: Environmental compliance status
    - **Insurance Expiry**: Current insurance coverage expiration
    - **Safety Rating**: Current DOT safety assessment

    ### Business Use Cases
    - Carrier selection and ranking algorithms
    - Performance benchmarking and analysis
    - Compliance monitoring and alerts
    - Contract negotiation data
    - Risk assessment and mitigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return sync_detailed(
        world_id=world_id,
        carrier_id=carrier_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[ErrorResponse]:
    """Get carrier performance and compliance metrics


    ## Get TMS Carrier Metrics

    Retrieve comprehensive performance and compliance metrics for a specific carrier.

    ### Features
    - **Current Performance**: Real-time performance indicators
    - **Recent Trends**: Historical performance trend data
    - **Compliance Status**: DOT, MC, insurance, and safety information
    - **Operational Intelligence**: Data for carrier selection and evaluation

    ### Performance Metrics Included
    - **On-Time Delivery Rate**: Current percentage (0.0-1.0)
    - **Damage Claim Rate**: Current damage rate (0.0-1.0)
    - **Average Transit Time**: Current average in hours
    - **Total Shipments**: Lifetime completed shipment count
    - **Last Update**: When metrics were last refreshed

    ### Compliance Metrics Included
    - **DOT Number**: Department of Transportation registration
    - **MC Number**: Motor Carrier authority number
    - **SCAC Code**: Standard Carrier Alpha Code
    - **SmartWay Certification**: Environmental compliance status
    - **Insurance Expiry**: Current insurance coverage expiration
    - **Safety Rating**: Current DOT safety assessment

    ### Business Use Cases
    - Carrier selection and ranking algorithms
    - Performance benchmarking and analysis
    - Compliance monitoring and alerts
    - Contract negotiation data
    - Risk assessment and mitigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        carrier_id=carrier_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    carrier_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[ErrorResponse]:
    """Get carrier performance and compliance metrics


    ## Get TMS Carrier Metrics

    Retrieve comprehensive performance and compliance metrics for a specific carrier.

    ### Features
    - **Current Performance**: Real-time performance indicators
    - **Recent Trends**: Historical performance trend data
    - **Compliance Status**: DOT, MC, insurance, and safety information
    - **Operational Intelligence**: Data for carrier selection and evaluation

    ### Performance Metrics Included
    - **On-Time Delivery Rate**: Current percentage (0.0-1.0)
    - **Damage Claim Rate**: Current damage rate (0.0-1.0)
    - **Average Transit Time**: Current average in hours
    - **Total Shipments**: Lifetime completed shipment count
    - **Last Update**: When metrics were last refreshed

    ### Compliance Metrics Included
    - **DOT Number**: Department of Transportation registration
    - **MC Number**: Motor Carrier authority number
    - **SCAC Code**: Standard Carrier Alpha Code
    - **SmartWay Certification**: Environmental compliance status
    - **Insurance Expiry**: Current insurance coverage expiration
    - **Safety Rating**: Current DOT safety assessment

    ### Business Use Cases
    - Carrier selection and ranking algorithms
    - Performance benchmarking and analysis
    - Compliance monitoring and alerts
    - Contract negotiation data
    - Risk assessment and mitigation


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        carrier_id (str):  Example: CARRIER_FEDEX_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            carrier_id=carrier_id,
            client=client,
        )
    ).parsed
