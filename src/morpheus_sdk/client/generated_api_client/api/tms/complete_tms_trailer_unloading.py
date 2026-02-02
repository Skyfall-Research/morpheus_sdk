from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.complete_tms_trailer_unloading_body import CompleteTMSTrailerUnloadingBody
from ...models.complete_tms_trailer_unloading_response_200 import CompleteTMSTrailerUnloadingResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    trailer_id: str,
    *,
    body: CompleteTMSTrailerUnloadingBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/tms/trailers/{trailer_id}/complete-unloading",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = CompleteTMSTrailerUnloadingResponse200.from_dict(response.json())

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
) -> Response[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]:
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
    body: CompleteTMSTrailerUnloadingBody,
) -> Response[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]:
    """Complete trailer unloading process


    ## Complete TMS Trailer Unloading

    Finalize unloading operations with comprehensive verification, count reconciliation, and timing
    documentation to enable departure workflow.

    ### Features
    - **Process Finalization**: Complete and close unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from UNLOADING to UNLOADED
    - **Count Reconciliation**: Record and verify actual pallet counts against expected quantities
    - **Precision Time Recording**: Capture exact completion timestamp for performance analytics
    - **Quality Verification**: Ensure all cargo has been properly unloaded and verified
    - **Departure Enablement**: Automatically enable trailer departure workflow

    ### Completion Process Workflow
    1. **Final Verification**: Confirm all cargo has been unloaded from trailer
    2. **Count Reconciliation**: Count actual pallets received and verify against manifest
    3. **Quality Check**: Inspect cargo condition and document any discrepancies
    4. **Documentation**: Complete unloading documentation and paperwork
    5. **Time Recording**: Capture precise completion timestamp
    6. **Status Update**: Update trailer status to UNLOADED automatically
    7. **Departure Preparation**: Enable departure workflow and dock release

    ### Required Information
    - **completionTime**: Precise timestamp when unloading operations were completed (required)

    ### Optional Information
    - **actualPallets**: Actual number of pallets received for reconciliation (recommended)

    ### Business Rules
    - **Status Requirement**: Trailer must be in UNLOADING status to complete
    - **Completion Time**: Precise timestamp is mandatory for performance tracking
    - **Count Reconciliation**: Actual pallet count helps with inventory accuracy
    - **Workflow Progression**: Completion automatically enables departure workflow
    - **Documentation**: Completion triggers generation of unloading documentation
    - **Performance Tracking**: Completion data feeds into operational analytics

    ### Use Cases
    - **Inventory Management**: Reconcile received quantities with expected deliveries
    - **Performance Analytics**: Track unloading completion times and efficiency
    - **Quality Control**: Document cargo condition and any issues
    - **Departure Coordination**: Enable timely trailer departure and dock availability


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CompleteTMSTrailerUnloadingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]
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
    body: CompleteTMSTrailerUnloadingBody,
) -> Optional[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]:
    """Complete trailer unloading process


    ## Complete TMS Trailer Unloading

    Finalize unloading operations with comprehensive verification, count reconciliation, and timing
    documentation to enable departure workflow.

    ### Features
    - **Process Finalization**: Complete and close unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from UNLOADING to UNLOADED
    - **Count Reconciliation**: Record and verify actual pallet counts against expected quantities
    - **Precision Time Recording**: Capture exact completion timestamp for performance analytics
    - **Quality Verification**: Ensure all cargo has been properly unloaded and verified
    - **Departure Enablement**: Automatically enable trailer departure workflow

    ### Completion Process Workflow
    1. **Final Verification**: Confirm all cargo has been unloaded from trailer
    2. **Count Reconciliation**: Count actual pallets received and verify against manifest
    3. **Quality Check**: Inspect cargo condition and document any discrepancies
    4. **Documentation**: Complete unloading documentation and paperwork
    5. **Time Recording**: Capture precise completion timestamp
    6. **Status Update**: Update trailer status to UNLOADED automatically
    7. **Departure Preparation**: Enable departure workflow and dock release

    ### Required Information
    - **completionTime**: Precise timestamp when unloading operations were completed (required)

    ### Optional Information
    - **actualPallets**: Actual number of pallets received for reconciliation (recommended)

    ### Business Rules
    - **Status Requirement**: Trailer must be in UNLOADING status to complete
    - **Completion Time**: Precise timestamp is mandatory for performance tracking
    - **Count Reconciliation**: Actual pallet count helps with inventory accuracy
    - **Workflow Progression**: Completion automatically enables departure workflow
    - **Documentation**: Completion triggers generation of unloading documentation
    - **Performance Tracking**: Completion data feeds into operational analytics

    ### Use Cases
    - **Inventory Management**: Reconcile received quantities with expected deliveries
    - **Performance Analytics**: Track unloading completion times and efficiency
    - **Quality Control**: Document cargo condition and any issues
    - **Departure Coordination**: Enable timely trailer departure and dock availability


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CompleteTMSTrailerUnloadingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]
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
    body: CompleteTMSTrailerUnloadingBody,
) -> Response[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]:
    """Complete trailer unloading process


    ## Complete TMS Trailer Unloading

    Finalize unloading operations with comprehensive verification, count reconciliation, and timing
    documentation to enable departure workflow.

    ### Features
    - **Process Finalization**: Complete and close unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from UNLOADING to UNLOADED
    - **Count Reconciliation**: Record and verify actual pallet counts against expected quantities
    - **Precision Time Recording**: Capture exact completion timestamp for performance analytics
    - **Quality Verification**: Ensure all cargo has been properly unloaded and verified
    - **Departure Enablement**: Automatically enable trailer departure workflow

    ### Completion Process Workflow
    1. **Final Verification**: Confirm all cargo has been unloaded from trailer
    2. **Count Reconciliation**: Count actual pallets received and verify against manifest
    3. **Quality Check**: Inspect cargo condition and document any discrepancies
    4. **Documentation**: Complete unloading documentation and paperwork
    5. **Time Recording**: Capture precise completion timestamp
    6. **Status Update**: Update trailer status to UNLOADED automatically
    7. **Departure Preparation**: Enable departure workflow and dock release

    ### Required Information
    - **completionTime**: Precise timestamp when unloading operations were completed (required)

    ### Optional Information
    - **actualPallets**: Actual number of pallets received for reconciliation (recommended)

    ### Business Rules
    - **Status Requirement**: Trailer must be in UNLOADING status to complete
    - **Completion Time**: Precise timestamp is mandatory for performance tracking
    - **Count Reconciliation**: Actual pallet count helps with inventory accuracy
    - **Workflow Progression**: Completion automatically enables departure workflow
    - **Documentation**: Completion triggers generation of unloading documentation
    - **Performance Tracking**: Completion data feeds into operational analytics

    ### Use Cases
    - **Inventory Management**: Reconcile received quantities with expected deliveries
    - **Performance Analytics**: Track unloading completion times and efficiency
    - **Quality Control**: Document cargo condition and any issues
    - **Departure Coordination**: Enable timely trailer departure and dock availability


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CompleteTMSTrailerUnloadingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]
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
    body: CompleteTMSTrailerUnloadingBody,
) -> Optional[Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]]:
    """Complete trailer unloading process


    ## Complete TMS Trailer Unloading

    Finalize unloading operations with comprehensive verification, count reconciliation, and timing
    documentation to enable departure workflow.

    ### Features
    - **Process Finalization**: Complete and close unloading operations with proper documentation
    - **Automatic Status Update**: Updates trailer status from UNLOADING to UNLOADED
    - **Count Reconciliation**: Record and verify actual pallet counts against expected quantities
    - **Precision Time Recording**: Capture exact completion timestamp for performance analytics
    - **Quality Verification**: Ensure all cargo has been properly unloaded and verified
    - **Departure Enablement**: Automatically enable trailer departure workflow

    ### Completion Process Workflow
    1. **Final Verification**: Confirm all cargo has been unloaded from trailer
    2. **Count Reconciliation**: Count actual pallets received and verify against manifest
    3. **Quality Check**: Inspect cargo condition and document any discrepancies
    4. **Documentation**: Complete unloading documentation and paperwork
    5. **Time Recording**: Capture precise completion timestamp
    6. **Status Update**: Update trailer status to UNLOADED automatically
    7. **Departure Preparation**: Enable departure workflow and dock release

    ### Required Information
    - **completionTime**: Precise timestamp when unloading operations were completed (required)

    ### Optional Information
    - **actualPallets**: Actual number of pallets received for reconciliation (recommended)

    ### Business Rules
    - **Status Requirement**: Trailer must be in UNLOADING status to complete
    - **Completion Time**: Precise timestamp is mandatory for performance tracking
    - **Count Reconciliation**: Actual pallet count helps with inventory accuracy
    - **Workflow Progression**: Completion automatically enables departure workflow
    - **Documentation**: Completion triggers generation of unloading documentation
    - **Performance Tracking**: Completion data feeds into operational analytics

    ### Use Cases
    - **Inventory Management**: Reconcile received quantities with expected deliveries
    - **Performance Analytics**: Track unloading completion times and efficiency
    - **Quality Control**: Document cargo condition and any issues
    - **Departure Coordination**: Enable timely trailer departure and dock availability


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        trailer_id (str):  Example: TRAILER_001.
        body (CompleteTMSTrailerUnloadingBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[CompleteTMSTrailerUnloadingResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            trailer_id=trailer_id,
            client=client,
            body=body,
        )
    ).parsed
