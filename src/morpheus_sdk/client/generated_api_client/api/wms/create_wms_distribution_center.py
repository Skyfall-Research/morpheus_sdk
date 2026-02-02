from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_distribution_center_body import CreateWMSDistributionCenterBody
from ...models.create_wms_distribution_center_response_201 import CreateWMSDistributionCenterResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSDistributionCenterBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/distribution-centers",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSDistributionCenterResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 409:
        response_409 = ErrorResponse.from_dict(response.json())

        return response_409

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]:
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
    body: CreateWMSDistributionCenterBody,
) -> Response[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]:
    """Create new distribution center


    ## Create WMS Distribution Center

    Create a new distribution center within a warehouse for comprehensive facility management and
    operational coordination.

    ### Features
    - **Facility Management**: Complete distribution center configuration and management
    - **Multi-Type Support**: Support for various DC types (Fulfillment, Cross-dock, Cold storage, 3PL)
    - **Location Integration**: Full address and timezone configuration for accurate operations
    - **Operational Hours**: Configurable operating hours for scheduling and planning
    - **Contact Management**: Complete contact information for facility coordination
    - **Custom Configuration**: Flexible custom fields for facility-specific requirements

    ### Distribution Center Types
    - **FULFILLMENT**: Standard fulfillment centers for order processing and shipping
    - **CROSS_DOCK**: Cross-docking facilities for rapid product flow and minimal storage
    - **COLD_STORAGE**: Temperature-controlled facilities for perishable goods
    - **3PL**: Third-party logistics facilities for outsourced operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational and accepting operations
    - **INACTIVE**: Temporarily inactive but available for activation
    - **MAINTENANCE**: Under maintenance, operations suspended

    ### Business Rules
    - dcId is auto-generated with unique identifier if not provided
    - warehouseId and dcName are required for facility creation
    - dcName must be unique within the warehouse
    - Operating hours support full weekly schedule configuration
    - Custom fields support facility-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDistributionCenterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]
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
    body: CreateWMSDistributionCenterBody,
) -> Optional[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]:
    """Create new distribution center


    ## Create WMS Distribution Center

    Create a new distribution center within a warehouse for comprehensive facility management and
    operational coordination.

    ### Features
    - **Facility Management**: Complete distribution center configuration and management
    - **Multi-Type Support**: Support for various DC types (Fulfillment, Cross-dock, Cold storage, 3PL)
    - **Location Integration**: Full address and timezone configuration for accurate operations
    - **Operational Hours**: Configurable operating hours for scheduling and planning
    - **Contact Management**: Complete contact information for facility coordination
    - **Custom Configuration**: Flexible custom fields for facility-specific requirements

    ### Distribution Center Types
    - **FULFILLMENT**: Standard fulfillment centers for order processing and shipping
    - **CROSS_DOCK**: Cross-docking facilities for rapid product flow and minimal storage
    - **COLD_STORAGE**: Temperature-controlled facilities for perishable goods
    - **3PL**: Third-party logistics facilities for outsourced operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational and accepting operations
    - **INACTIVE**: Temporarily inactive but available for activation
    - **MAINTENANCE**: Under maintenance, operations suspended

    ### Business Rules
    - dcId is auto-generated with unique identifier if not provided
    - warehouseId and dcName are required for facility creation
    - dcName must be unique within the warehouse
    - Operating hours support full weekly schedule configuration
    - Custom fields support facility-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDistributionCenterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSDistributionCenterResponse201, ErrorResponse]
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
    body: CreateWMSDistributionCenterBody,
) -> Response[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]:
    """Create new distribution center


    ## Create WMS Distribution Center

    Create a new distribution center within a warehouse for comprehensive facility management and
    operational coordination.

    ### Features
    - **Facility Management**: Complete distribution center configuration and management
    - **Multi-Type Support**: Support for various DC types (Fulfillment, Cross-dock, Cold storage, 3PL)
    - **Location Integration**: Full address and timezone configuration for accurate operations
    - **Operational Hours**: Configurable operating hours for scheduling and planning
    - **Contact Management**: Complete contact information for facility coordination
    - **Custom Configuration**: Flexible custom fields for facility-specific requirements

    ### Distribution Center Types
    - **FULFILLMENT**: Standard fulfillment centers for order processing and shipping
    - **CROSS_DOCK**: Cross-docking facilities for rapid product flow and minimal storage
    - **COLD_STORAGE**: Temperature-controlled facilities for perishable goods
    - **3PL**: Third-party logistics facilities for outsourced operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational and accepting operations
    - **INACTIVE**: Temporarily inactive but available for activation
    - **MAINTENANCE**: Under maintenance, operations suspended

    ### Business Rules
    - dcId is auto-generated with unique identifier if not provided
    - warehouseId and dcName are required for facility creation
    - dcName must be unique within the warehouse
    - Operating hours support full weekly schedule configuration
    - Custom fields support facility-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDistributionCenterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]
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
    body: CreateWMSDistributionCenterBody,
) -> Optional[Union[CreateWMSDistributionCenterResponse201, ErrorResponse]]:
    """Create new distribution center


    ## Create WMS Distribution Center

    Create a new distribution center within a warehouse for comprehensive facility management and
    operational coordination.

    ### Features
    - **Facility Management**: Complete distribution center configuration and management
    - **Multi-Type Support**: Support for various DC types (Fulfillment, Cross-dock, Cold storage, 3PL)
    - **Location Integration**: Full address and timezone configuration for accurate operations
    - **Operational Hours**: Configurable operating hours for scheduling and planning
    - **Contact Management**: Complete contact information for facility coordination
    - **Custom Configuration**: Flexible custom fields for facility-specific requirements

    ### Distribution Center Types
    - **FULFILLMENT**: Standard fulfillment centers for order processing and shipping
    - **CROSS_DOCK**: Cross-docking facilities for rapid product flow and minimal storage
    - **COLD_STORAGE**: Temperature-controlled facilities for perishable goods
    - **3PL**: Third-party logistics facilities for outsourced operations

    ### Operational Status Values
    - **ACTIVE**: Fully operational and accepting operations
    - **INACTIVE**: Temporarily inactive but available for activation
    - **MAINTENANCE**: Under maintenance, operations suspended

    ### Business Rules
    - dcId is auto-generated with unique identifier if not provided
    - warehouseId and dcName are required for facility creation
    - dcName must be unique within the warehouse
    - Operating hours support full weekly schedule configuration
    - Custom fields support facility-specific operational requirements


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSDistributionCenterBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSDistributionCenterResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
