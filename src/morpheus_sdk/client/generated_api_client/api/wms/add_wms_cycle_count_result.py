from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_wms_cycle_count_result_body import AddWMSCycleCountResultBody
from ...models.add_wms_cycle_count_result_response_200 import AddWMSCycleCountResultResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
    cycle_count_id: str,
    *,
    body: AddWMSCycleCountResultBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/{world_id}/wms/cycle-counts/{cycle_count_id}/results",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = AddWMSCycleCountResultResponse200.from_dict(response.json())

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
) -> Response[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]:
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
    body: AddWMSCycleCountResultBody,
) -> Response[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]:
    """Add count result to cycle count


    ## Add Count Result to WMS Cycle Count

    Record individual count results for cycle count execution with precise variance calculation and
    audit tracking.

    ### Features
    - **Precise Count Recording**: Record exact counted quantities for each item/location
    - **Automatic Variance Calculation**: Calculate variance between expected and actual quantities
    - **User Attribution**: Track who performed each count for accountability
    - **Timestamp Recording**: Capture exact timing of count execution
    - **Notes Support**: Add contextual notes for count discrepancies or observations
    - **Lot Tracking**: Support lot number tracking for detailed inventory control

    ### Count Result Data
    - **Location Information**: Bin and product identification for precise tracking
    - **Quantity Reconciliation**: Expected vs. actual quantity comparison
    - **Variance Analysis**: Automatic calculation of quantity and percentage variances
    - **User Accountability**: Record counting user and timestamp for audit trail
    - **Additional Context**: Optional notes for explaining variances or observations

    ### Business Rules
    - binId and productId are required for location and item identification
    - expectedQuantity and actualQuantity enable variance calculation
    - countedBy and countedAt provide user attribution and timing
    - variance is calculated automatically (actualQuantity - expectedQuantity)
    - All count results are preserved for audit and analysis purposes

    ### Use Cases
    - **Count Execution**: Record results during cycle count execution
    - **Variance Tracking**: Track and analyze inventory variances
    - **Audit Documentation**: Provide detailed audit trail for count results
    - **Accuracy Analysis**: Support inventory accuracy reporting and improvement


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AddWMSCycleCountResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        body=body,
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
    body: AddWMSCycleCountResultBody,
) -> Optional[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]:
    """Add count result to cycle count


    ## Add Count Result to WMS Cycle Count

    Record individual count results for cycle count execution with precise variance calculation and
    audit tracking.

    ### Features
    - **Precise Count Recording**: Record exact counted quantities for each item/location
    - **Automatic Variance Calculation**: Calculate variance between expected and actual quantities
    - **User Attribution**: Track who performed each count for accountability
    - **Timestamp Recording**: Capture exact timing of count execution
    - **Notes Support**: Add contextual notes for count discrepancies or observations
    - **Lot Tracking**: Support lot number tracking for detailed inventory control

    ### Count Result Data
    - **Location Information**: Bin and product identification for precise tracking
    - **Quantity Reconciliation**: Expected vs. actual quantity comparison
    - **Variance Analysis**: Automatic calculation of quantity and percentage variances
    - **User Accountability**: Record counting user and timestamp for audit trail
    - **Additional Context**: Optional notes for explaining variances or observations

    ### Business Rules
    - binId and productId are required for location and item identification
    - expectedQuantity and actualQuantity enable variance calculation
    - countedBy and countedAt provide user attribution and timing
    - variance is calculated automatically (actualQuantity - expectedQuantity)
    - All count results are preserved for audit and analysis purposes

    ### Use Cases
    - **Count Execution**: Record results during cycle count execution
    - **Variance Tracking**: Track and analyze inventory variances
    - **Audit Documentation**: Provide detailed audit trail for count results
    - **Accuracy Analysis**: Support inventory accuracy reporting and improvement


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AddWMSCycleCountResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddWMSCycleCountResultResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddWMSCycleCountResultBody,
) -> Response[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]:
    """Add count result to cycle count


    ## Add Count Result to WMS Cycle Count

    Record individual count results for cycle count execution with precise variance calculation and
    audit tracking.

    ### Features
    - **Precise Count Recording**: Record exact counted quantities for each item/location
    - **Automatic Variance Calculation**: Calculate variance between expected and actual quantities
    - **User Attribution**: Track who performed each count for accountability
    - **Timestamp Recording**: Capture exact timing of count execution
    - **Notes Support**: Add contextual notes for count discrepancies or observations
    - **Lot Tracking**: Support lot number tracking for detailed inventory control

    ### Count Result Data
    - **Location Information**: Bin and product identification for precise tracking
    - **Quantity Reconciliation**: Expected vs. actual quantity comparison
    - **Variance Analysis**: Automatic calculation of quantity and percentage variances
    - **User Accountability**: Record counting user and timestamp for audit trail
    - **Additional Context**: Optional notes for explaining variances or observations

    ### Business Rules
    - binId and productId are required for location and item identification
    - expectedQuantity and actualQuantity enable variance calculation
    - countedBy and countedAt provide user attribution and timing
    - variance is calculated automatically (actualQuantity - expectedQuantity)
    - All count results are preserved for audit and analysis purposes

    ### Use Cases
    - **Count Execution**: Record results during cycle count execution
    - **Variance Tracking**: Track and analyze inventory variances
    - **Audit Documentation**: Provide detailed audit trail for count results
    - **Accuracy Analysis**: Support inventory accuracy reporting and improvement


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AddWMSCycleCountResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        cycle_count_id=cycle_count_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    cycle_count_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: AddWMSCycleCountResultBody,
) -> Optional[Union[AddWMSCycleCountResultResponse200, ErrorResponse]]:
    """Add count result to cycle count


    ## Add Count Result to WMS Cycle Count

    Record individual count results for cycle count execution with precise variance calculation and
    audit tracking.

    ### Features
    - **Precise Count Recording**: Record exact counted quantities for each item/location
    - **Automatic Variance Calculation**: Calculate variance between expected and actual quantities
    - **User Attribution**: Track who performed each count for accountability
    - **Timestamp Recording**: Capture exact timing of count execution
    - **Notes Support**: Add contextual notes for count discrepancies or observations
    - **Lot Tracking**: Support lot number tracking for detailed inventory control

    ### Count Result Data
    - **Location Information**: Bin and product identification for precise tracking
    - **Quantity Reconciliation**: Expected vs. actual quantity comparison
    - **Variance Analysis**: Automatic calculation of quantity and percentage variances
    - **User Accountability**: Record counting user and timestamp for audit trail
    - **Additional Context**: Optional notes for explaining variances or observations

    ### Business Rules
    - binId and productId are required for location and item identification
    - expectedQuantity and actualQuantity enable variance calculation
    - countedBy and countedAt provide user attribution and timing
    - variance is calculated automatically (actualQuantity - expectedQuantity)
    - All count results are preserved for audit and analysis purposes

    ### Use Cases
    - **Count Execution**: Record results during cycle count execution
    - **Variance Tracking**: Track and analyze inventory variances
    - **Audit Documentation**: Provide detailed audit trail for count results
    - **Accuracy Analysis**: Support inventory accuracy reporting and improvement


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        cycle_count_id (str):  Example: CC_ATL_2024_001.
        body (AddWMSCycleCountResultBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AddWMSCycleCountResultResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            cycle_count_id=cycle_count_id,
            client=client,
            body=body,
        )
    ).parsed
