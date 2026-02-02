from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_wms_cycle_count_body import CreateWMSCycleCountBody
from ...models.create_wms_cycle_count_response_201 import CreateWMSCycleCountResponse201
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: CreateWMSCycleCountBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/cycle-counts",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CreateWMSCycleCountResponse201, ErrorResponse]]:
    if response.status_code == 201:
        response_201 = CreateWMSCycleCountResponse201.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = ErrorResponse.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[CreateWMSCycleCountResponse201, ErrorResponse]]:
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
    body: CreateWMSCycleCountBody,
) -> Response[Union[CreateWMSCycleCountResponse201, ErrorResponse]]:
    """Create new cycle count


    ## Create WMS Cycle Count

    Create a new cycle count for inventory accuracy verification with comprehensive scheduling, scope
    definition, and assignment capabilities.

    ### Features
    - **Flexible Counting Types**: Support for daily, weekly, monthly, ABC, full, spot, and blind counts
    - **Precision Scheduling**: Define exact scheduling dates and execution windows
    - **Scope Configuration**: Target specific zones, bins, products, or ABC classifications
    - **User Assignment**: Assign specific users to count tasks with bin allocations
    - **Status Tracking**: Comprehensive status management throughout count lifecycle
    - **Result Aggregation**: Structured count results with variance analysis

    ### Count Type Categories
    - **DAILY**: Daily cycle count operations
    - **WEEKLY**: Weekly scheduled cycle counts
    - **MONTHLY**: Monthly comprehensive counts
    - **ABC**: ABC classification-based counts
    - **FULL**: Full warehouse inventory counts
    - **SPOT**: Spot checks for specific items or locations
    - **BLIND**: Blind counts without system quantity display

    ### Count Status Flow
    - **SCHEDULED**: Count scheduled and ready for execution
    - **IN_PROGRESS**: Count execution in progress
    - **COMPLETED**: Count execution completed
    - **APPROVED**: Count results approved
    - **REJECTED**: Count results rejected for recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Rules
    - cycleCountId is auto-generated with unique identifier if not provided
    - warehouseId is required for warehouse scoping
    - countType determines counting methodology and workflow
    - Scheduled date must be present or future date
    - Scope configuration defines count boundaries and targets
    - User assignments can be configured during creation or later


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSCycleCountResponse201, ErrorResponse]]
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
    body: CreateWMSCycleCountBody,
) -> Optional[Union[CreateWMSCycleCountResponse201, ErrorResponse]]:
    """Create new cycle count


    ## Create WMS Cycle Count

    Create a new cycle count for inventory accuracy verification with comprehensive scheduling, scope
    definition, and assignment capabilities.

    ### Features
    - **Flexible Counting Types**: Support for daily, weekly, monthly, ABC, full, spot, and blind counts
    - **Precision Scheduling**: Define exact scheduling dates and execution windows
    - **Scope Configuration**: Target specific zones, bins, products, or ABC classifications
    - **User Assignment**: Assign specific users to count tasks with bin allocations
    - **Status Tracking**: Comprehensive status management throughout count lifecycle
    - **Result Aggregation**: Structured count results with variance analysis

    ### Count Type Categories
    - **DAILY**: Daily cycle count operations
    - **WEEKLY**: Weekly scheduled cycle counts
    - **MONTHLY**: Monthly comprehensive counts
    - **ABC**: ABC classification-based counts
    - **FULL**: Full warehouse inventory counts
    - **SPOT**: Spot checks for specific items or locations
    - **BLIND**: Blind counts without system quantity display

    ### Count Status Flow
    - **SCHEDULED**: Count scheduled and ready for execution
    - **IN_PROGRESS**: Count execution in progress
    - **COMPLETED**: Count execution completed
    - **APPROVED**: Count results approved
    - **REJECTED**: Count results rejected for recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Rules
    - cycleCountId is auto-generated with unique identifier if not provided
    - warehouseId is required for warehouse scoping
    - countType determines counting methodology and workflow
    - Scheduled date must be present or future date
    - Scope configuration defines count boundaries and targets
    - User assignments can be configured during creation or later


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSCycleCountResponse201, ErrorResponse]
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
    body: CreateWMSCycleCountBody,
) -> Response[Union[CreateWMSCycleCountResponse201, ErrorResponse]]:
    """Create new cycle count


    ## Create WMS Cycle Count

    Create a new cycle count for inventory accuracy verification with comprehensive scheduling, scope
    definition, and assignment capabilities.

    ### Features
    - **Flexible Counting Types**: Support for daily, weekly, monthly, ABC, full, spot, and blind counts
    - **Precision Scheduling**: Define exact scheduling dates and execution windows
    - **Scope Configuration**: Target specific zones, bins, products, or ABC classifications
    - **User Assignment**: Assign specific users to count tasks with bin allocations
    - **Status Tracking**: Comprehensive status management throughout count lifecycle
    - **Result Aggregation**: Structured count results with variance analysis

    ### Count Type Categories
    - **DAILY**: Daily cycle count operations
    - **WEEKLY**: Weekly scheduled cycle counts
    - **MONTHLY**: Monthly comprehensive counts
    - **ABC**: ABC classification-based counts
    - **FULL**: Full warehouse inventory counts
    - **SPOT**: Spot checks for specific items or locations
    - **BLIND**: Blind counts without system quantity display

    ### Count Status Flow
    - **SCHEDULED**: Count scheduled and ready for execution
    - **IN_PROGRESS**: Count execution in progress
    - **COMPLETED**: Count execution completed
    - **APPROVED**: Count results approved
    - **REJECTED**: Count results rejected for recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Rules
    - cycleCountId is auto-generated with unique identifier if not provided
    - warehouseId is required for warehouse scoping
    - countType determines counting methodology and workflow
    - Scheduled date must be present or future date
    - Scope configuration defines count boundaries and targets
    - User assignments can be configured during creation or later


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CreateWMSCycleCountResponse201, ErrorResponse]]
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
    body: CreateWMSCycleCountBody,
) -> Optional[Union[CreateWMSCycleCountResponse201, ErrorResponse]]:
    """Create new cycle count


    ## Create WMS Cycle Count

    Create a new cycle count for inventory accuracy verification with comprehensive scheduling, scope
    definition, and assignment capabilities.

    ### Features
    - **Flexible Counting Types**: Support for daily, weekly, monthly, ABC, full, spot, and blind counts
    - **Precision Scheduling**: Define exact scheduling dates and execution windows
    - **Scope Configuration**: Target specific zones, bins, products, or ABC classifications
    - **User Assignment**: Assign specific users to count tasks with bin allocations
    - **Status Tracking**: Comprehensive status management throughout count lifecycle
    - **Result Aggregation**: Structured count results with variance analysis

    ### Count Type Categories
    - **DAILY**: Daily cycle count operations
    - **WEEKLY**: Weekly scheduled cycle counts
    - **MONTHLY**: Monthly comprehensive counts
    - **ABC**: ABC classification-based counts
    - **FULL**: Full warehouse inventory counts
    - **SPOT**: Spot checks for specific items or locations
    - **BLIND**: Blind counts without system quantity display

    ### Count Status Flow
    - **SCHEDULED**: Count scheduled and ready for execution
    - **IN_PROGRESS**: Count execution in progress
    - **COMPLETED**: Count execution completed
    - **APPROVED**: Count results approved
    - **REJECTED**: Count results rejected for recount
    - **CANCELLED**: Count cancelled before completion

    ### Business Rules
    - cycleCountId is auto-generated with unique identifier if not provided
    - warehouseId is required for warehouse scoping
    - countType determines counting methodology and workflow
    - Scheduled date must be present or future date
    - Scope configuration defines count boundaries and targets
    - User assignments can be configured during creation or later


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (CreateWMSCycleCountBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CreateWMSCycleCountResponse201, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
