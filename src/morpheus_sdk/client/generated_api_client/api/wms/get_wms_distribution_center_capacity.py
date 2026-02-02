from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_distribution_center_capacity_response_200 import GetWMSDistributionCenterCapacityResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    dc_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/distribution-centers/{dc_id}/capacity",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDistributionCenterCapacityResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]:
    """Get distribution center capacity and utilization


    ## Get WMS Distribution Center Capacity

    Retrieve comprehensive capacity and utilization metrics for a distribution center including space
    utilization, zone metrics, and operational efficiency indicators.

    ### Features
    - **Space Utilization**: Complete space utilization metrics and analysis
    - **Zone Metrics**: Total zones and operational zone configuration
    - **Bin Utilization**: Bin occupancy and utilization percentage tracking
    - **Operational Hours**: Complete operating hours schedule for capacity planning
    - **Capacity Planning**: Support for capacity planning and optimization analysis
    - **Real-Time Data**: Current utilization metrics for operational decision-making

    ### Capacity Metrics
    - **Total Square Footage**: Complete facility square footage for space planning
    - **Total Zones**: Number of operational zones within the facility
    - **Total Bins**: Complete bin count for storage capacity assessment
    - **Occupied Bins**: Currently occupied bins for real-time utilization
    - **Utilization Percentage**: Calculated utilization percentage for capacity monitoring

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must reference an existing distribution center
    - Utilization metrics calculated from real-time zone and bin data
    - Operating hours included for capacity planning coordination
    - Comprehensive metrics for operational efficiency analysis
    - Future implementation will include real-time zone and bin queries

    ### Use Cases
    - **Capacity Planning**: Assess current capacity and plan for future growth
    - **Utilization Monitoring**: Monitor real-time facility utilization
    - **Operational Efficiency**: Analyze operational efficiency and optimization opportunities
    - **Space Management**: Optimize space allocation and utilization
    - **Resource Planning**: Plan resource allocation based on capacity metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]:
    """Get distribution center capacity and utilization


    ## Get WMS Distribution Center Capacity

    Retrieve comprehensive capacity and utilization metrics for a distribution center including space
    utilization, zone metrics, and operational efficiency indicators.

    ### Features
    - **Space Utilization**: Complete space utilization metrics and analysis
    - **Zone Metrics**: Total zones and operational zone configuration
    - **Bin Utilization**: Bin occupancy and utilization percentage tracking
    - **Operational Hours**: Complete operating hours schedule for capacity planning
    - **Capacity Planning**: Support for capacity planning and optimization analysis
    - **Real-Time Data**: Current utilization metrics for operational decision-making

    ### Capacity Metrics
    - **Total Square Footage**: Complete facility square footage for space planning
    - **Total Zones**: Number of operational zones within the facility
    - **Total Bins**: Complete bin count for storage capacity assessment
    - **Occupied Bins**: Currently occupied bins for real-time utilization
    - **Utilization Percentage**: Calculated utilization percentage for capacity monitoring

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must reference an existing distribution center
    - Utilization metrics calculated from real-time zone and bin data
    - Operating hours included for capacity planning coordination
    - Comprehensive metrics for operational efficiency analysis
    - Future implementation will include real-time zone and bin queries

    ### Use Cases
    - **Capacity Planning**: Assess current capacity and plan for future growth
    - **Utilization Monitoring**: Monitor real-time facility utilization
    - **Operational Efficiency**: Analyze operational efficiency and optimization opportunities
    - **Space Management**: Optimize space allocation and utilization
    - **Resource Planning**: Plan resource allocation based on capacity metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        dc_id=dc_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]:
    """Get distribution center capacity and utilization


    ## Get WMS Distribution Center Capacity

    Retrieve comprehensive capacity and utilization metrics for a distribution center including space
    utilization, zone metrics, and operational efficiency indicators.

    ### Features
    - **Space Utilization**: Complete space utilization metrics and analysis
    - **Zone Metrics**: Total zones and operational zone configuration
    - **Bin Utilization**: Bin occupancy and utilization percentage tracking
    - **Operational Hours**: Complete operating hours schedule for capacity planning
    - **Capacity Planning**: Support for capacity planning and optimization analysis
    - **Real-Time Data**: Current utilization metrics for operational decision-making

    ### Capacity Metrics
    - **Total Square Footage**: Complete facility square footage for space planning
    - **Total Zones**: Number of operational zones within the facility
    - **Total Bins**: Complete bin count for storage capacity assessment
    - **Occupied Bins**: Currently occupied bins for real-time utilization
    - **Utilization Percentage**: Calculated utilization percentage for capacity monitoring

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must reference an existing distribution center
    - Utilization metrics calculated from real-time zone and bin data
    - Operating hours included for capacity planning coordination
    - Comprehensive metrics for operational efficiency analysis
    - Future implementation will include real-time zone and bin queries

    ### Use Cases
    - **Capacity Planning**: Assess current capacity and plan for future growth
    - **Utilization Monitoring**: Monitor real-time facility utilization
    - **Operational Efficiency**: Analyze operational efficiency and optimization opportunities
    - **Space Management**: Optimize space allocation and utilization
    - **Resource Planning**: Plan resource allocation based on capacity metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        dc_id=dc_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    dc_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]]:
    """Get distribution center capacity and utilization


    ## Get WMS Distribution Center Capacity

    Retrieve comprehensive capacity and utilization metrics for a distribution center including space
    utilization, zone metrics, and operational efficiency indicators.

    ### Features
    - **Space Utilization**: Complete space utilization metrics and analysis
    - **Zone Metrics**: Total zones and operational zone configuration
    - **Bin Utilization**: Bin occupancy and utilization percentage tracking
    - **Operational Hours**: Complete operating hours schedule for capacity planning
    - **Capacity Planning**: Support for capacity planning and optimization analysis
    - **Real-Time Data**: Current utilization metrics for operational decision-making

    ### Capacity Metrics
    - **Total Square Footage**: Complete facility square footage for space planning
    - **Total Zones**: Number of operational zones within the facility
    - **Total Bins**: Complete bin count for storage capacity assessment
    - **Occupied Bins**: Currently occupied bins for real-time utilization
    - **Utilization Percentage**: Calculated utilization percentage for capacity monitoring

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must reference an existing distribution center
    - Utilization metrics calculated from real-time zone and bin data
    - Operating hours included for capacity planning coordination
    - Comprehensive metrics for operational efficiency analysis
    - Future implementation will include real-time zone and bin queries

    ### Use Cases
    - **Capacity Planning**: Assess current capacity and plan for future growth
    - **Utilization Monitoring**: Monitor real-time facility utilization
    - **Operational Efficiency**: Analyze operational efficiency and optimization opportunities
    - **Space Management**: Optimize space allocation and utilization
    - **Resource Planning**: Plan resource allocation based on capacity metrics


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDistributionCenterCapacityResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            dc_id=dc_id,
            client=client,
        )
    ).parsed
