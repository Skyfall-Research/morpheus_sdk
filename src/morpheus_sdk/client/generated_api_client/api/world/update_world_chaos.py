from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chaos_policy import ChaosPolicy
from ...models.error_response import ErrorResponse
from ...models.update_world_chaos_response_200 import UpdateWorldChaosResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: ChaosPolicy,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/world/{world_id}/chaos",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWorldChaosResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWorldChaosResponse200.from_dict(response.json())

        return response_200

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


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, UpdateWorldChaosResponse200]]:
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
    body: ChaosPolicy,
) -> Response[Union[ErrorResponse, UpdateWorldChaosResponse200]]:
    """Update chaos configuration for a world


    ## Update World Chaos Configuration

    Replace the chaos engineering configuration for a specific world environment.

    ### Request Body
    Provide a complete chaos policy configuration:
    - **enabled**: Set to true to activate chaos injection
    - **probability**: Chance (0.0-1.0) that chaos occurs per workflow step
    - **scenarios**: Array of chaos scenarios to enable
    - **seed**: Optional seed for reproducible chaos sequences

    ### Chaos Scenarios
    Available scenario types:
    - **data_corruption**: Corrupt field values
    - **missing_data**: Remove fields from responses
    - **stale_data**: Return outdated data
    - **format_change**: Alter data structure
    - **permission_denied**: Simulate access errors
    - **rate_limit**: Inject rate limiting delays
    - **partial_data**: Return incomplete results
    - **duplicate_data**: Return duplicate records
    - **invalid_state**: Return records in invalid states
    - **dependency_failure**: Simulate downstream service failures
    - **timing_issue**: Inject timing-related problems

    ### Use Cases
    - Enable chaos testing for a development environment
    - Configure specific failure scenarios for testing
    - Set reproducible chaos with a seed for debugging
    - Gradually increase chaos probability during testing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (ChaosPolicy): Chaos engineering policy for injecting failures and anomalies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWorldChaosResponse200]]
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
    body: ChaosPolicy,
) -> Optional[Union[ErrorResponse, UpdateWorldChaosResponse200]]:
    """Update chaos configuration for a world


    ## Update World Chaos Configuration

    Replace the chaos engineering configuration for a specific world environment.

    ### Request Body
    Provide a complete chaos policy configuration:
    - **enabled**: Set to true to activate chaos injection
    - **probability**: Chance (0.0-1.0) that chaos occurs per workflow step
    - **scenarios**: Array of chaos scenarios to enable
    - **seed**: Optional seed for reproducible chaos sequences

    ### Chaos Scenarios
    Available scenario types:
    - **data_corruption**: Corrupt field values
    - **missing_data**: Remove fields from responses
    - **stale_data**: Return outdated data
    - **format_change**: Alter data structure
    - **permission_denied**: Simulate access errors
    - **rate_limit**: Inject rate limiting delays
    - **partial_data**: Return incomplete results
    - **duplicate_data**: Return duplicate records
    - **invalid_state**: Return records in invalid states
    - **dependency_failure**: Simulate downstream service failures
    - **timing_issue**: Inject timing-related problems

    ### Use Cases
    - Enable chaos testing for a development environment
    - Configure specific failure scenarios for testing
    - Set reproducible chaos with a seed for debugging
    - Gradually increase chaos probability during testing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (ChaosPolicy): Chaos engineering policy for injecting failures and anomalies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWorldChaosResponse200]
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
    body: ChaosPolicy,
) -> Response[Union[ErrorResponse, UpdateWorldChaosResponse200]]:
    """Update chaos configuration for a world


    ## Update World Chaos Configuration

    Replace the chaos engineering configuration for a specific world environment.

    ### Request Body
    Provide a complete chaos policy configuration:
    - **enabled**: Set to true to activate chaos injection
    - **probability**: Chance (0.0-1.0) that chaos occurs per workflow step
    - **scenarios**: Array of chaos scenarios to enable
    - **seed**: Optional seed for reproducible chaos sequences

    ### Chaos Scenarios
    Available scenario types:
    - **data_corruption**: Corrupt field values
    - **missing_data**: Remove fields from responses
    - **stale_data**: Return outdated data
    - **format_change**: Alter data structure
    - **permission_denied**: Simulate access errors
    - **rate_limit**: Inject rate limiting delays
    - **partial_data**: Return incomplete results
    - **duplicate_data**: Return duplicate records
    - **invalid_state**: Return records in invalid states
    - **dependency_failure**: Simulate downstream service failures
    - **timing_issue**: Inject timing-related problems

    ### Use Cases
    - Enable chaos testing for a development environment
    - Configure specific failure scenarios for testing
    - Set reproducible chaos with a seed for debugging
    - Gradually increase chaos probability during testing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (ChaosPolicy): Chaos engineering policy for injecting failures and anomalies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWorldChaosResponse200]]
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
    body: ChaosPolicy,
) -> Optional[Union[ErrorResponse, UpdateWorldChaosResponse200]]:
    """Update chaos configuration for a world


    ## Update World Chaos Configuration

    Replace the chaos engineering configuration for a specific world environment.

    ### Request Body
    Provide a complete chaos policy configuration:
    - **enabled**: Set to true to activate chaos injection
    - **probability**: Chance (0.0-1.0) that chaos occurs per workflow step
    - **scenarios**: Array of chaos scenarios to enable
    - **seed**: Optional seed for reproducible chaos sequences

    ### Chaos Scenarios
    Available scenario types:
    - **data_corruption**: Corrupt field values
    - **missing_data**: Remove fields from responses
    - **stale_data**: Return outdated data
    - **format_change**: Alter data structure
    - **permission_denied**: Simulate access errors
    - **rate_limit**: Inject rate limiting delays
    - **partial_data**: Return incomplete results
    - **duplicate_data**: Return duplicate records
    - **invalid_state**: Return records in invalid states
    - **dependency_failure**: Simulate downstream service failures
    - **timing_issue**: Inject timing-related problems

    ### Use Cases
    - Enable chaos testing for a development environment
    - Configure specific failure scenarios for testing
    - Set reproducible chaos with a seed for debugging
    - Gradually increase chaos probability during testing


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (ChaosPolicy): Chaos engineering policy for injecting failures and anomalies

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWorldChaosResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
