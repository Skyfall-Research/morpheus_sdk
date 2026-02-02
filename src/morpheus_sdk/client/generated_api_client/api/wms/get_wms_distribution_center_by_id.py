from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_distribution_center_by_id_response_200 import GetWMSDistributionCenterByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    dc_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/distribution-centers/{dc_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSDistributionCenterByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]:
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
) -> Response[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]:
    """Get distribution center by ID


    ## Get WMS Distribution Center by ID

    Retrieve a specific distribution center using its unique identifier for detailed facility
    information and configuration access.

    ### Features
    - **Direct Access**: Retrieve facility using unique distribution center identifier
    - **Complete Information**: Full facility details including configuration and contact information
    - **Single Facility Focus**: Detailed view of specific facility for management operations
    - **Configuration Access**: Access to complete facility configuration and settings

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must be a valid, existing distribution center identifier
    - Returns complete facility record with all configuration details
    - Includes operational status, contact information, and custom fields
    - Null response if distribution center is not found
    - Full facility data for comprehensive management operations

    ### Use Cases
    - **Facility Details**: Access complete facility information for operations
    - **Configuration Review**: Review facility configuration and settings
    - **Contact Information**: Access facility contact details for coordination
    - **Status Verification**: Verify current operational status and configuration
    - **Integration Support**: Provide facility data for integration with other systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]
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
) -> Optional[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]:
    """Get distribution center by ID


    ## Get WMS Distribution Center by ID

    Retrieve a specific distribution center using its unique identifier for detailed facility
    information and configuration access.

    ### Features
    - **Direct Access**: Retrieve facility using unique distribution center identifier
    - **Complete Information**: Full facility details including configuration and contact information
    - **Single Facility Focus**: Detailed view of specific facility for management operations
    - **Configuration Access**: Access to complete facility configuration and settings

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must be a valid, existing distribution center identifier
    - Returns complete facility record with all configuration details
    - Includes operational status, contact information, and custom fields
    - Null response if distribution center is not found
    - Full facility data for comprehensive management operations

    ### Use Cases
    - **Facility Details**: Access complete facility information for operations
    - **Configuration Review**: Review facility configuration and settings
    - **Contact Information**: Access facility contact details for coordination
    - **Status Verification**: Verify current operational status and configuration
    - **Integration Support**: Provide facility data for integration with other systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]
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
) -> Response[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]:
    """Get distribution center by ID


    ## Get WMS Distribution Center by ID

    Retrieve a specific distribution center using its unique identifier for detailed facility
    information and configuration access.

    ### Features
    - **Direct Access**: Retrieve facility using unique distribution center identifier
    - **Complete Information**: Full facility details including configuration and contact information
    - **Single Facility Focus**: Detailed view of specific facility for management operations
    - **Configuration Access**: Access to complete facility configuration and settings

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must be a valid, existing distribution center identifier
    - Returns complete facility record with all configuration details
    - Includes operational status, contact information, and custom fields
    - Null response if distribution center is not found
    - Full facility data for comprehensive management operations

    ### Use Cases
    - **Facility Details**: Access complete facility information for operations
    - **Configuration Review**: Review facility configuration and settings
    - **Contact Information**: Access facility contact details for coordination
    - **Status Verification**: Verify current operational status and configuration
    - **Integration Support**: Provide facility data for integration with other systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]
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
) -> Optional[Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]]:
    """Get distribution center by ID


    ## Get WMS Distribution Center by ID

    Retrieve a specific distribution center using its unique identifier for detailed facility
    information and configuration access.

    ### Features
    - **Direct Access**: Retrieve facility using unique distribution center identifier
    - **Complete Information**: Full facility details including configuration and contact information
    - **Single Facility Focus**: Detailed view of specific facility for management operations
    - **Configuration Access**: Access to complete facility configuration and settings

    ### Path Parameters
    - **dcId**: Required - Unique identifier for the distribution center

    ### Business Logic
    - dcId must be a valid, existing distribution center identifier
    - Returns complete facility record with all configuration details
    - Includes operational status, contact information, and custom fields
    - Null response if distribution center is not found
    - Full facility data for comprehensive management operations

    ### Use Cases
    - **Facility Details**: Access complete facility information for operations
    - **Configuration Review**: Review facility configuration and settings
    - **Contact Information**: Access facility contact details for coordination
    - **Status Verification**: Verify current operational status and configuration
    - **Integration Support**: Provide facility data for integration with other systems


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        dc_id (str):  Example: wms_distribution-center_674565c1234567890abcdef.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSDistributionCenterByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            dc_id=dc_id,
            client=client,
        )
    ).parsed
