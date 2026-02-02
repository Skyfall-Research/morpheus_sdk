from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_wms_cycle_count_by_id_response_200 import GetWMSCycleCountByIdResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    cycle_count_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/cycle-counts/{cycle_count_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]:
    if response.status_code == 200:
        response_200 = GetWMSCycleCountByIdResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]:
    """Get cycle count by ID


    ## Get WMS Cycle Count by ID

    Retrieve detailed information for a specific cycle count including complete count results,
    assignments, and variance analysis.

    ### Features
    - **Complete Count Profile**: Full cycle count details including scope, schedule, and assignments
    - **Count Results**: Detailed count results with expected vs. actual quantities
    - **Variance Analysis**: Comprehensive variance reporting and analysis
    - **Assignment Details**: User assignments with status and progress tracking
    - **Audit Information**: Complete audit trail with timestamps and user actions
    - **Progress Tracking**: Current status and completion percentage

    ### Response Data Includes
    - **Identification**: Cycle count ID, type, and status information
    - **Scheduling**: Scheduled, start, and completion timestamps
    - **Scope**: Target zones, bins, products, and classifications
    - **Assignments**: User assignments with bin allocations and status
    - **Count Results**: Item-by-item count results with variance analysis
    - **Summary**: Overall count accuracy and variance statistics
    - **Audit Trail**: Creation, updates, and approval information

    ### Use Cases
    - **Count Execution**: Access count details during execution process
    - **Result Review**: Review count results and variance analysis
    - **Approval Workflow**: Support count approval and rejection workflows
    - **Progress Monitoring**: Track count progress and completion status
    - **Audit Review**: Historical analysis and audit trail examination


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]:
    """Get cycle count by ID


    ## Get WMS Cycle Count by ID

    Retrieve detailed information for a specific cycle count including complete count results,
    assignments, and variance analysis.

    ### Features
    - **Complete Count Profile**: Full cycle count details including scope, schedule, and assignments
    - **Count Results**: Detailed count results with expected vs. actual quantities
    - **Variance Analysis**: Comprehensive variance reporting and analysis
    - **Assignment Details**: User assignments with status and progress tracking
    - **Audit Information**: Complete audit trail with timestamps and user actions
    - **Progress Tracking**: Current status and completion percentage

    ### Response Data Includes
    - **Identification**: Cycle count ID, type, and status information
    - **Scheduling**: Scheduled, start, and completion timestamps
    - **Scope**: Target zones, bins, products, and classifications
    - **Assignments**: User assignments with bin allocations and status
    - **Count Results**: Item-by-item count results with variance analysis
    - **Summary**: Overall count accuracy and variance statistics
    - **Audit Trail**: Creation, updates, and approval information

    ### Use Cases
    - **Count Execution**: Access count details during execution process
    - **Result Review**: Review count results and variance analysis
    - **Approval Workflow**: Support count approval and rejection workflows
    - **Progress Monitoring**: Track count progress and completion status
    - **Audit Review**: Historical analysis and audit trail examination


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountByIdResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]:
    """Get cycle count by ID


    ## Get WMS Cycle Count by ID

    Retrieve detailed information for a specific cycle count including complete count results,
    assignments, and variance analysis.

    ### Features
    - **Complete Count Profile**: Full cycle count details including scope, schedule, and assignments
    - **Count Results**: Detailed count results with expected vs. actual quantities
    - **Variance Analysis**: Comprehensive variance reporting and analysis
    - **Assignment Details**: User assignments with status and progress tracking
    - **Audit Information**: Complete audit trail with timestamps and user actions
    - **Progress Tracking**: Current status and completion percentage

    ### Response Data Includes
    - **Identification**: Cycle count ID, type, and status information
    - **Scheduling**: Scheduled, start, and completion timestamps
    - **Scope**: Target zones, bins, products, and classifications
    - **Assignments**: User assignments with bin allocations and status
    - **Count Results**: Item-by-item count results with variance analysis
    - **Summary**: Overall count accuracy and variance statistics
    - **Audit Trail**: Creation, updates, and approval information

    ### Use Cases
    - **Count Execution**: Access count details during execution process
    - **Result Review**: Review count results and variance analysis
    - **Approval Workflow**: Support count approval and rejection workflows
    - **Progress Monitoring**: Track count progress and completion status
    - **Audit Review**: Historical analysis and audit trail examination


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWMSCycleCountByIdResponse200]]:
    """Get cycle count by ID


    ## Get WMS Cycle Count by ID

    Retrieve detailed information for a specific cycle count including complete count results,
    assignments, and variance analysis.

    ### Features
    - **Complete Count Profile**: Full cycle count details including scope, schedule, and assignments
    - **Count Results**: Detailed count results with expected vs. actual quantities
    - **Variance Analysis**: Comprehensive variance reporting and analysis
    - **Assignment Details**: User assignments with status and progress tracking
    - **Audit Information**: Complete audit trail with timestamps and user actions
    - **Progress Tracking**: Current status and completion percentage

    ### Response Data Includes
    - **Identification**: Cycle count ID, type, and status information
    - **Scheduling**: Scheduled, start, and completion timestamps
    - **Scope**: Target zones, bins, products, and classifications
    - **Assignments**: User assignments with bin allocations and status
    - **Count Results**: Item-by-item count results with variance analysis
    - **Summary**: Overall count accuracy and variance statistics
    - **Audit Trail**: Creation, updates, and approval information

    ### Use Cases
    - **Count Execution**: Access count details during execution process
    - **Result Review**: Review count results and variance analysis
    - **Approval Workflow**: Support count approval and rejection workflows
    - **Progress Monitoring**: Track count progress and completion status
    - **Audit Review**: Historical analysis and audit trail examination


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWMSCycleCountByIdResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            cycle_count_id=cycle_count_id,
            client=client,
        )
    ).parsed
