from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_random_erp_company_response_200 import GetRandomERPCompanyResponse200
from ...models.get_random_erp_company_type import GetRandomERPCompanyType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    world_id: str,
    *,
    type_: Union[Unset, GetRandomERPCompanyType] = GetRandomERPCompanyType.NPC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type_: Union[Unset, str] = UNSET
    if not isinstance(type_, Unset):
        json_type_ = type_.value

    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/{world_id}/erp/companies/random",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetRandomERPCompanyResponse200]]:
    if response.status_code == 200:
        response_200 = GetRandomERPCompanyResponse200.from_dict(response.json())

        return response_200

    if response.status_code == 404:
        response_404 = ErrorResponse.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ErrorResponse, GetRandomERPCompanyResponse200]]:
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
    type_: Union[Unset, GetRandomERPCompanyType] = GetRandomERPCompanyType.NPC,
) -> Response[Union[ErrorResponse, GetRandomERPCompanyResponse200]]:
    """Get random ERP company


    Retrieve a random company from the world environment, with optional type filtering.

    **Core Features**:
    - **Random Selection**: Algorithmically random company selection
    - **Type Filtering**: Choose between MPC and NPC (Non-Player Company) types
    - **Test Data Support**: Ideal for testing and demonstration purposes
    - **World Scoping**: Random selection within specific world environment

    **Use Cases**:
    - **Testing & Development**: Generate random test data for development
    - **Demo Scenarios**: Create realistic demo scenarios with random companies
    - **Load Testing**: Use random company data for performance testing
    - **Data Sampling**: Statistical sampling of company data for analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetRandomERPCompanyType]):  Default: GetRandomERPCompanyType.NPC.
            Example: npc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetRandomERPCompanyResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, GetRandomERPCompanyType] = GetRandomERPCompanyType.NPC,
) -> Optional[Union[ErrorResponse, GetRandomERPCompanyResponse200]]:
    """Get random ERP company


    Retrieve a random company from the world environment, with optional type filtering.

    **Core Features**:
    - **Random Selection**: Algorithmically random company selection
    - **Type Filtering**: Choose between MPC and NPC (Non-Player Company) types
    - **Test Data Support**: Ideal for testing and demonstration purposes
    - **World Scoping**: Random selection within specific world environment

    **Use Cases**:
    - **Testing & Development**: Generate random test data for development
    - **Demo Scenarios**: Create realistic demo scenarios with random companies
    - **Load Testing**: Use random company data for performance testing
    - **Data Sampling**: Statistical sampling of company data for analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetRandomERPCompanyType]):  Default: GetRandomERPCompanyType.NPC.
            Example: npc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetRandomERPCompanyResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, GetRandomERPCompanyType] = GetRandomERPCompanyType.NPC,
) -> Response[Union[ErrorResponse, GetRandomERPCompanyResponse200]]:
    """Get random ERP company


    Retrieve a random company from the world environment, with optional type filtering.

    **Core Features**:
    - **Random Selection**: Algorithmically random company selection
    - **Type Filtering**: Choose between MPC and NPC (Non-Player Company) types
    - **Test Data Support**: Ideal for testing and demonstration purposes
    - **World Scoping**: Random selection within specific world environment

    **Use Cases**:
    - **Testing & Development**: Generate random test data for development
    - **Demo Scenarios**: Create realistic demo scenarios with random companies
    - **Load Testing**: Use random company data for performance testing
    - **Data Sampling**: Statistical sampling of company data for analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetRandomERPCompanyType]):  Default: GetRandomERPCompanyType.NPC.
            Example: npc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetRandomERPCompanyResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    type_: Union[Unset, GetRandomERPCompanyType] = GetRandomERPCompanyType.NPC,
) -> Optional[Union[ErrorResponse, GetRandomERPCompanyResponse200]]:
    """Get random ERP company


    Retrieve a random company from the world environment, with optional type filtering.

    **Core Features**:
    - **Random Selection**: Algorithmically random company selection
    - **Type Filtering**: Choose between MPC and NPC (Non-Player Company) types
    - **Test Data Support**: Ideal for testing and demonstration purposes
    - **World Scoping**: Random selection within specific world environment

    **Use Cases**:
    - **Testing & Development**: Generate random test data for development
    - **Demo Scenarios**: Create realistic demo scenarios with random companies
    - **Load Testing**: Use random company data for performance testing
    - **Data Sampling**: Statistical sampling of company data for analysis


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        type_ (Union[Unset, GetRandomERPCompanyType]):  Default: GetRandomERPCompanyType.NPC.
            Example: npc.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetRandomERPCompanyResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            type_=type_,
        )
    ).parsed
