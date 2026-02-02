from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_world_capabilities_response_200 import GetWorldCapabilitiesResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/world/{world_id}/capabilities",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]:
    if response.status_code == 200:
        response_200 = GetWorldCapabilitiesResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]:
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
) -> Response[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]:
    """Get capabilities assigned to a world


    ## Get World Capabilities

    Retrieve the list of capabilities assigned to a specific world, including sampling strategy
    information and full capability details.

    ### Response Data
    - **worldId**: The world's unique identifier
    - **worldName**: Human-readable world name
    - **samplingStrategy**: The strategy used to select capabilities
    - **count**: Total number of assigned capabilities
    - **capabilityIds**: Array of capability ID strings
    - **capabilities**: Full capability objects with metadata

    ### Capability Information
    Each capability includes:
    - **id**: Unique capability identifier
    - **name**: Human-readable name
    - **description**: What the capability does
    - **domain**: Business domain (e.g., order-management, inventory)
    - **odId**: Associated Operational Descriptor ID
    - **tags**: Metadata including personas, services, complexity

    ### Use Cases
    - Display available capabilities for a world
    - Verify capability sampling results
    - Debug persona-capability mappings
    - Audit world configurations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]:
    """Get capabilities assigned to a world


    ## Get World Capabilities

    Retrieve the list of capabilities assigned to a specific world, including sampling strategy
    information and full capability details.

    ### Response Data
    - **worldId**: The world's unique identifier
    - **worldName**: Human-readable world name
    - **samplingStrategy**: The strategy used to select capabilities
    - **count**: Total number of assigned capabilities
    - **capabilityIds**: Array of capability ID strings
    - **capabilities**: Full capability objects with metadata

    ### Capability Information
    Each capability includes:
    - **id**: Unique capability identifier
    - **name**: Human-readable name
    - **description**: What the capability does
    - **domain**: Business domain (e.g., order-management, inventory)
    - **odId**: Associated Operational Descriptor ID
    - **tags**: Metadata including personas, services, complexity

    ### Use Cases
    - Display available capabilities for a world
    - Verify capability sampling results
    - Debug persona-capability mappings
    - Audit world configurations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWorldCapabilitiesResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]:
    """Get capabilities assigned to a world


    ## Get World Capabilities

    Retrieve the list of capabilities assigned to a specific world, including sampling strategy
    information and full capability details.

    ### Response Data
    - **worldId**: The world's unique identifier
    - **worldName**: Human-readable world name
    - **samplingStrategy**: The strategy used to select capabilities
    - **count**: Total number of assigned capabilities
    - **capabilityIds**: Array of capability ID strings
    - **capabilities**: Full capability objects with metadata

    ### Capability Information
    Each capability includes:
    - **id**: Unique capability identifier
    - **name**: Human-readable name
    - **description**: What the capability does
    - **domain**: Business domain (e.g., order-management, inventory)
    - **odId**: Associated Operational Descriptor ID
    - **tags**: Metadata including personas, services, complexity

    ### Use Cases
    - Display available capabilities for a world
    - Verify capability sampling results
    - Debug persona-capability mappings
    - Audit world configurations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ErrorResponse, GetWorldCapabilitiesResponse200]]:
    """Get capabilities assigned to a world


    ## Get World Capabilities

    Retrieve the list of capabilities assigned to a specific world, including sampling strategy
    information and full capability details.

    ### Response Data
    - **worldId**: The world's unique identifier
    - **worldName**: Human-readable world name
    - **samplingStrategy**: The strategy used to select capabilities
    - **count**: Total number of assigned capabilities
    - **capabilityIds**: Array of capability ID strings
    - **capabilities**: Full capability objects with metadata

    ### Capability Information
    Each capability includes:
    - **id**: Unique capability identifier
    - **name**: Human-readable name
    - **description**: What the capability does
    - **domain**: Business domain (e.g., order-management, inventory)
    - **odId**: Associated Operational Descriptor ID
    - **tags**: Metadata including personas, services, complexity

    ### Use Cases
    - Display available capabilities for a world
    - Verify capability sampling results
    - Debug persona-capability mappings
    - Audit world configurations


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, GetWorldCapabilitiesResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
