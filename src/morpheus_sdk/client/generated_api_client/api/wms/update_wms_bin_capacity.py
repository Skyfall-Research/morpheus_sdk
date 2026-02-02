from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_wms_bin_capacity_response_200 import UpdateWMSBinCapacityResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    bin_id: str,
    *,
    body: Any,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/wms/bins/{bin_id}/capacity",
    }

    _kwargs["json"]: Any
    _kwargs["json"] = body

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWMSBinCapacityResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Response[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]:
    """Update bin capacity


    ## Update WMS Bin Capacity

    Update the capacity constraints for a warehouse bin to reflect changes in storage capabilities,
    equipment modifications, or operational requirements.

    ### Features
    - **Capacity Management**: Update weight, volume, and pallet capacity constraints
    - **Operational Flexibility**: Modify capacity based on operational changes
    - **Safety Compliance**: Ensure capacity limits meet safety requirements
    - **Slotting Support**: Support slotting optimization with accurate capacity data
    - **Equipment Integration**: Reflect changes in storage equipment capabilities

    ### Capacity Parameters
    - **maxWeightLbs**: Maximum weight capacity in pounds
    - **maxCubicFeet**: Maximum volume capacity in cubic feet
    - **maxPallets**: Maximum number of pallets that can be stored

    ### Business Rules
    - At least one capacity parameter must be provided
    - Capacity values must be positive numbers
    - Weight and volume can include decimal values for precision
    - Pallet count must be integer value
    - Changes are logged for audit and capacity planning

    ### Use Cases
    - **Equipment Changes**: Update capacity after storage equipment modifications
    - **Safety Updates**: Adjust capacity limits for safety compliance
    - **Slotting Optimization**: Update capacity data for slotting analysis
    - **Operational Changes**: Reflect operational procedure changes affecting capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Optional[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]:
    """Update bin capacity


    ## Update WMS Bin Capacity

    Update the capacity constraints for a warehouse bin to reflect changes in storage capabilities,
    equipment modifications, or operational requirements.

    ### Features
    - **Capacity Management**: Update weight, volume, and pallet capacity constraints
    - **Operational Flexibility**: Modify capacity based on operational changes
    - **Safety Compliance**: Ensure capacity limits meet safety requirements
    - **Slotting Support**: Support slotting optimization with accurate capacity data
    - **Equipment Integration**: Reflect changes in storage equipment capabilities

    ### Capacity Parameters
    - **maxWeightLbs**: Maximum weight capacity in pounds
    - **maxCubicFeet**: Maximum volume capacity in cubic feet
    - **maxPallets**: Maximum number of pallets that can be stored

    ### Business Rules
    - At least one capacity parameter must be provided
    - Capacity values must be positive numbers
    - Weight and volume can include decimal values for precision
    - Pallet count must be integer value
    - Changes are logged for audit and capacity planning

    ### Use Cases
    - **Equipment Changes**: Update capacity after storage equipment modifications
    - **Safety Updates**: Adjust capacity limits for safety compliance
    - **Slotting Optimization**: Update capacity data for slotting analysis
    - **Operational Changes**: Reflect operational procedure changes affecting capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSBinCapacityResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        bin_id=bin_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Response[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]:
    """Update bin capacity


    ## Update WMS Bin Capacity

    Update the capacity constraints for a warehouse bin to reflect changes in storage capabilities,
    equipment modifications, or operational requirements.

    ### Features
    - **Capacity Management**: Update weight, volume, and pallet capacity constraints
    - **Operational Flexibility**: Modify capacity based on operational changes
    - **Safety Compliance**: Ensure capacity limits meet safety requirements
    - **Slotting Support**: Support slotting optimization with accurate capacity data
    - **Equipment Integration**: Reflect changes in storage equipment capabilities

    ### Capacity Parameters
    - **maxWeightLbs**: Maximum weight capacity in pounds
    - **maxCubicFeet**: Maximum volume capacity in cubic feet
    - **maxPallets**: Maximum number of pallets that can be stored

    ### Business Rules
    - At least one capacity parameter must be provided
    - Capacity values must be positive numbers
    - Weight and volume can include decimal values for precision
    - Pallet count must be integer value
    - Changes are logged for audit and capacity planning

    ### Use Cases
    - **Equipment Changes**: Update capacity after storage equipment modifications
    - **Safety Updates**: Adjust capacity limits for safety compliance
    - **Slotting Optimization**: Update capacity data for slotting analysis
    - **Operational Changes**: Reflect operational procedure changes affecting capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Any,
) -> Optional[Union[ErrorResponse, UpdateWMSBinCapacityResponse200]]:
    """Update bin capacity


    ## Update WMS Bin Capacity

    Update the capacity constraints for a warehouse bin to reflect changes in storage capabilities,
    equipment modifications, or operational requirements.

    ### Features
    - **Capacity Management**: Update weight, volume, and pallet capacity constraints
    - **Operational Flexibility**: Modify capacity based on operational changes
    - **Safety Compliance**: Ensure capacity limits meet safety requirements
    - **Slotting Support**: Support slotting optimization with accurate capacity data
    - **Equipment Integration**: Reflect changes in storage equipment capabilities

    ### Capacity Parameters
    - **maxWeightLbs**: Maximum weight capacity in pounds
    - **maxCubicFeet**: Maximum volume capacity in cubic feet
    - **maxPallets**: Maximum number of pallets that can be stored

    ### Business Rules
    - At least one capacity parameter must be provided
    - Capacity values must be positive numbers
    - Weight and volume can include decimal values for precision
    - Pallet count must be integer value
    - Changes are logged for audit and capacity planning

    ### Use Cases
    - **Equipment Changes**: Update capacity after storage equipment modifications
    - **Safety Updates**: Adjust capacity limits for safety compliance
    - **Slotting Optimization**: Update capacity data for slotting analysis
    - **Operational Changes**: Reflect operational procedure changes affecting capacity


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        bin_id (str):  Example: BIN_ATL_A01_001.
        body (Any):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWMSBinCapacityResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            bin_id=bin_id,
            client=client,
            body=body,
        )
    ).parsed
