from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_wms_replenishments_by_bin_response_200 import GetWMSReplenishmentsByBinResponse200
from ...models.get_wms_replenishments_by_bin_status_item import GetWMSReplenishmentsByBinStatusItem
from ...models.get_wms_replenishments_by_bin_type import GetWMSReplenishmentsByBinType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    bin_id: str,
    *,
    type_: GetWMSReplenishmentsByBinType,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_ = type_.value
    params["type"] = json_type_

    params["warehouseId"] = warehouse_id

    json_status: Union[Unset, list[str]] = UNSET
    if not isinstance(status, Unset):
        json_status = []
        for status_item_data in status:
            status_item = status_item_data.value
            json_status.append(status_item)

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/wms/replenishments/bin/{bin_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[GetWMSReplenishmentsByBinResponse200]:
    if response.status_code == 200:
        response_200 = GetWMSReplenishmentsByBinResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[GetWMSReplenishmentsByBinResponse200]:
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
    type_: GetWMSReplenishmentsByBinType,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]] = UNSET,
) -> Response[GetWMSReplenishmentsByBinResponse200]:
    """Get replenishments by bin


    ## Get Replenishments by Bin

    Retrieve replenishments involving a specific bin as either source or destination.

    **Bin Relationship Types:**
    - **source**: Bin is the fromBin (stock is taken from this bin)
    - **destination**: Bin is the toBin (stock is moved to this bin)

    **Use Cases:**
    - Bin utilization and activity analysis
    - Source/destination movement tracking
    - Bin-specific workflow management
    - Capacity planning and optimization

    **Field Mapping:**
    - Uses nested field queries: `fromBin.binId` or `toBin.binId`
    - Filters based on `type` parameter (source/destination)


    Args:
        world_id (str):
        bin_id (str):
        type_ (GetWMSReplenishmentsByBinType):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSReplenishmentsByBinResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        type_=type_,
        warehouse_id=warehouse_id,
        status=status,
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
    type_: GetWMSReplenishmentsByBinType,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]] = UNSET,
) -> Optional[GetWMSReplenishmentsByBinResponse200]:
    """Get replenishments by bin


    ## Get Replenishments by Bin

    Retrieve replenishments involving a specific bin as either source or destination.

    **Bin Relationship Types:**
    - **source**: Bin is the fromBin (stock is taken from this bin)
    - **destination**: Bin is the toBin (stock is moved to this bin)

    **Use Cases:**
    - Bin utilization and activity analysis
    - Source/destination movement tracking
    - Bin-specific workflow management
    - Capacity planning and optimization

    **Field Mapping:**
    - Uses nested field queries: `fromBin.binId` or `toBin.binId`
    - Filters based on `type` parameter (source/destination)


    Args:
        world_id (str):
        bin_id (str):
        type_ (GetWMSReplenishmentsByBinType):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSReplenishmentsByBinResponse200
    """

    return sync_detailed(
        world_id=world_id,
        bin_id=bin_id,
        client=client,
        type_=type_,
        warehouse_id=warehouse_id,
        status=status,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: GetWMSReplenishmentsByBinType,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]] = UNSET,
) -> Response[GetWMSReplenishmentsByBinResponse200]:
    """Get replenishments by bin


    ## Get Replenishments by Bin

    Retrieve replenishments involving a specific bin as either source or destination.

    **Bin Relationship Types:**
    - **source**: Bin is the fromBin (stock is taken from this bin)
    - **destination**: Bin is the toBin (stock is moved to this bin)

    **Use Cases:**
    - Bin utilization and activity analysis
    - Source/destination movement tracking
    - Bin-specific workflow management
    - Capacity planning and optimization

    **Field Mapping:**
    - Uses nested field queries: `fromBin.binId` or `toBin.binId`
    - Filters based on `type` parameter (source/destination)


    Args:
        world_id (str):
        bin_id (str):
        type_ (GetWMSReplenishmentsByBinType):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetWMSReplenishmentsByBinResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        bin_id=bin_id,
        type_=type_,
        warehouse_id=warehouse_id,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    bin_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: GetWMSReplenishmentsByBinType,
    warehouse_id: Union[Unset, str] = UNSET,
    status: Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]] = UNSET,
) -> Optional[GetWMSReplenishmentsByBinResponse200]:
    """Get replenishments by bin


    ## Get Replenishments by Bin

    Retrieve replenishments involving a specific bin as either source or destination.

    **Bin Relationship Types:**
    - **source**: Bin is the fromBin (stock is taken from this bin)
    - **destination**: Bin is the toBin (stock is moved to this bin)

    **Use Cases:**
    - Bin utilization and activity analysis
    - Source/destination movement tracking
    - Bin-specific workflow management
    - Capacity planning and optimization

    **Field Mapping:**
    - Uses nested field queries: `fromBin.binId` or `toBin.binId`
    - Filters based on `type` parameter (source/destination)


    Args:
        world_id (str):
        bin_id (str):
        type_ (GetWMSReplenishmentsByBinType):
        warehouse_id (Union[Unset, str]):
        status (Union[Unset, list[GetWMSReplenishmentsByBinStatusItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetWMSReplenishmentsByBinResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            bin_id=bin_id,
            client=client,
            type_=type_,
            warehouse_id=warehouse_id,
            status=status,
        )
    ).parsed
