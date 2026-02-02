from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_tms_trailer_delay_body import AddTMSTrailerDelayBody
from ...models.add_tms_trailer_delay_response_200 import AddTMSTrailerDelayResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
    *,
    body: AddTMSTrailerDelayBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/delays",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddTMSTrailerDelayResponse200.from_dict(response.json())

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
) -> Response[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddTMSTrailerDelayBody,
) -> Response[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]:
    """Add delay information to trailer


    ## Add TMS Trailer Delay

    Record and track delay information for trailers to monitor operational disruptions, support
    proactive communication, and enable data-driven delay prevention strategies.

    ### Features
    - **Comprehensive Delay Tracking**: Record various types of operational delays with detailed
    categorization
    - **Impact Assessment**: Capture estimated delay duration for planning adjustments
    - **Root Cause Analysis**: Categorize delay reasons for trend analysis and prevention
    - **Proactive Communication**: Support customer and stakeholder notification workflows
    - **Historical Analytics**: Enable delay pattern analysis and operational improvements
    - **Multiple Delay Support**: Track multiple delays for single trailer if needed

    ### Delay Type Categories
    - **TRAFFIC**: Traffic congestion, road construction, or transportation infrastructure issues
    - **WEATHER**: Weather-related delays including storms, snow, ice, or extreme conditions
    - **CARRIER**: Carrier operational issues such as equipment failure or driver availability
    - **DOCK_AVAILABILITY**: Facility dock scheduling conflicts or capacity constraints
    - **MECHANICAL**: Vehicle or equipment mechanical issues requiring repair
    - **REGULATORY**: Inspection delays, permit issues, or regulatory compliance holds
    - **OTHER**: Other operational disruptions not covered by standard categories

    ### Delay Information Requirements
    - **delayType**: Required - Standardized categorization for analytics and reporting
    - **reason**: Required - Detailed explanation for communication and analysis
    - **reportedAt**: Required - Timestamp when delay was first identified and reported
    - **estimatedDelay**: Optional - Expected delay duration in minutes for planning

    ### Business Rules
    - **Multiple Delays**: Multiple delay records can be added to same trailer for complex situations
    - **Independent Tracking**: Each delay is timestamped and tracked independently
    - **Cumulative Impact**: Multiple delays contribute to overall arrival time adjustments
    - **Status Integration**: Delays may trigger automatic status updates (DELAYED)
    - **Historical Preservation**: All delay records maintained for analytics and audit
    - **Communication Triggers**: Delay addition can trigger automated notification workflows

    ### Use Cases
    - **Operational Visibility**: Real-time tracking of trailer delays and impacts
    - **Customer Communication**: Proactive notification of delivery delays
    - **Performance Analytics**: Analyze delay patterns and identify improvement opportunities
    - **Resource Planning**: Adjust dock schedules and resource allocation based on delays
    - **Carrier Performance**: Track carrier reliability and delay frequency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AddTMSTrailerDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        trailer_id=trailer_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddTMSTrailerDelayBody,
) -> Optional[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]:
    """Add delay information to trailer


    ## Add TMS Trailer Delay

    Record and track delay information for trailers to monitor operational disruptions, support
    proactive communication, and enable data-driven delay prevention strategies.

    ### Features
    - **Comprehensive Delay Tracking**: Record various types of operational delays with detailed
    categorization
    - **Impact Assessment**: Capture estimated delay duration for planning adjustments
    - **Root Cause Analysis**: Categorize delay reasons for trend analysis and prevention
    - **Proactive Communication**: Support customer and stakeholder notification workflows
    - **Historical Analytics**: Enable delay pattern analysis and operational improvements
    - **Multiple Delay Support**: Track multiple delays for single trailer if needed

    ### Delay Type Categories
    - **TRAFFIC**: Traffic congestion, road construction, or transportation infrastructure issues
    - **WEATHER**: Weather-related delays including storms, snow, ice, or extreme conditions
    - **CARRIER**: Carrier operational issues such as equipment failure or driver availability
    - **DOCK_AVAILABILITY**: Facility dock scheduling conflicts or capacity constraints
    - **MECHANICAL**: Vehicle or equipment mechanical issues requiring repair
    - **REGULATORY**: Inspection delays, permit issues, or regulatory compliance holds
    - **OTHER**: Other operational disruptions not covered by standard categories

    ### Delay Information Requirements
    - **delayType**: Required - Standardized categorization for analytics and reporting
    - **reason**: Required - Detailed explanation for communication and analysis
    - **reportedAt**: Required - Timestamp when delay was first identified and reported
    - **estimatedDelay**: Optional - Expected delay duration in minutes for planning

    ### Business Rules
    - **Multiple Delays**: Multiple delay records can be added to same trailer for complex situations
    - **Independent Tracking**: Each delay is timestamped and tracked independently
    - **Cumulative Impact**: Multiple delays contribute to overall arrival time adjustments
    - **Status Integration**: Delays may trigger automatic status updates (DELAYED)
    - **Historical Preservation**: All delay records maintained for analytics and audit
    - **Communication Triggers**: Delay addition can trigger automated notification workflows

    ### Use Cases
    - **Operational Visibility**: Real-time tracking of trailer delays and impacts
    - **Customer Communication**: Proactive notification of delivery delays
    - **Performance Analytics**: Analyze delay patterns and identify improvement opportunities
    - **Resource Planning**: Adjust dock schedules and resource allocation based on delays
    - **Carrier Performance**: Track carrier reliability and delay frequency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AddTMSTrailerDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddTMSTrailerDelayResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        trailer_id=trailer_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddTMSTrailerDelayBody,
) -> Response[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]:
    """Add delay information to trailer


    ## Add TMS Trailer Delay

    Record and track delay information for trailers to monitor operational disruptions, support
    proactive communication, and enable data-driven delay prevention strategies.

    ### Features
    - **Comprehensive Delay Tracking**: Record various types of operational delays with detailed
    categorization
    - **Impact Assessment**: Capture estimated delay duration for planning adjustments
    - **Root Cause Analysis**: Categorize delay reasons for trend analysis and prevention
    - **Proactive Communication**: Support customer and stakeholder notification workflows
    - **Historical Analytics**: Enable delay pattern analysis and operational improvements
    - **Multiple Delay Support**: Track multiple delays for single trailer if needed

    ### Delay Type Categories
    - **TRAFFIC**: Traffic congestion, road construction, or transportation infrastructure issues
    - **WEATHER**: Weather-related delays including storms, snow, ice, or extreme conditions
    - **CARRIER**: Carrier operational issues such as equipment failure or driver availability
    - **DOCK_AVAILABILITY**: Facility dock scheduling conflicts or capacity constraints
    - **MECHANICAL**: Vehicle or equipment mechanical issues requiring repair
    - **REGULATORY**: Inspection delays, permit issues, or regulatory compliance holds
    - **OTHER**: Other operational disruptions not covered by standard categories

    ### Delay Information Requirements
    - **delayType**: Required - Standardized categorization for analytics and reporting
    - **reason**: Required - Detailed explanation for communication and analysis
    - **reportedAt**: Required - Timestamp when delay was first identified and reported
    - **estimatedDelay**: Optional - Expected delay duration in minutes for planning

    ### Business Rules
    - **Multiple Delays**: Multiple delay records can be added to same trailer for complex situations
    - **Independent Tracking**: Each delay is timestamped and tracked independently
    - **Cumulative Impact**: Multiple delays contribute to overall arrival time adjustments
    - **Status Integration**: Delays may trigger automatic status updates (DELAYED)
    - **Historical Preservation**: All delay records maintained for analytics and audit
    - **Communication Triggers**: Delay addition can trigger automated notification workflows

    ### Use Cases
    - **Operational Visibility**: Real-time tracking of trailer delays and impacts
    - **Customer Communication**: Proactive notification of delivery delays
    - **Performance Analytics**: Analyze delay patterns and identify improvement opportunities
    - **Resource Planning**: Adjust dock schedules and resource allocation based on delays
    - **Carrier Performance**: Track carrier reliability and delay frequency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AddTMSTrailerDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        trailer_id=trailer_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    trailer_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddTMSTrailerDelayBody,
) -> Optional[Union[AddTMSTrailerDelayResponse200, ErrorResponse]]:
    """Add delay information to trailer


    ## Add TMS Trailer Delay

    Record and track delay information for trailers to monitor operational disruptions, support
    proactive communication, and enable data-driven delay prevention strategies.

    ### Features
    - **Comprehensive Delay Tracking**: Record various types of operational delays with detailed
    categorization
    - **Impact Assessment**: Capture estimated delay duration for planning adjustments
    - **Root Cause Analysis**: Categorize delay reasons for trend analysis and prevention
    - **Proactive Communication**: Support customer and stakeholder notification workflows
    - **Historical Analytics**: Enable delay pattern analysis and operational improvements
    - **Multiple Delay Support**: Track multiple delays for single trailer if needed

    ### Delay Type Categories
    - **TRAFFIC**: Traffic congestion, road construction, or transportation infrastructure issues
    - **WEATHER**: Weather-related delays including storms, snow, ice, or extreme conditions
    - **CARRIER**: Carrier operational issues such as equipment failure or driver availability
    - **DOCK_AVAILABILITY**: Facility dock scheduling conflicts or capacity constraints
    - **MECHANICAL**: Vehicle or equipment mechanical issues requiring repair
    - **REGULATORY**: Inspection delays, permit issues, or regulatory compliance holds
    - **OTHER**: Other operational disruptions not covered by standard categories

    ### Delay Information Requirements
    - **delayType**: Required - Standardized categorization for analytics and reporting
    - **reason**: Required - Detailed explanation for communication and analysis
    - **reportedAt**: Required - Timestamp when delay was first identified and reported
    - **estimatedDelay**: Optional - Expected delay duration in minutes for planning

    ### Business Rules
    - **Multiple Delays**: Multiple delay records can be added to same trailer for complex situations
    - **Independent Tracking**: Each delay is timestamped and tracked independently
    - **Cumulative Impact**: Multiple delays contribute to overall arrival time adjustments
    - **Status Integration**: Delays may trigger automatic status updates (DELAYED)
    - **Historical Preservation**: All delay records maintained for analytics and audit
    - **Communication Triggers**: Delay addition can trigger automated notification workflows

    ### Use Cases
    - **Operational Visibility**: Real-time tracking of trailer delays and impacts
    - **Customer Communication**: Proactive notification of delivery delays
    - **Performance Analytics**: Analyze delay patterns and identify improvement opportunities
    - **Resource Planning**: Adjust dock schedules and resource allocation based on delays
    - **Carrier Performance**: Track carrier reliability and delay frequency


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (AddTMSTrailerDelayBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddTMSTrailerDelayResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
            body=body,
        )
    ).parsed
