from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.update_world_body import UpdateWorldBody
from ...models.update_world_response_200 import UpdateWorldResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    *,
    body: UpdateWorldBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": f"/world/{world_id}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, UpdateWorldResponse200]]:
    if response.status_code == 200:
        response_200 = UpdateWorldResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, UpdateWorldResponse200]]:
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
    body: UpdateWorldBody,
) -> Response[Union[ErrorResponse, UpdateWorldResponse200]]:
    """Partially update a world environment


    ## Update World

    Partially update a world environment's configuration. Only the fields provided in the request body
    will be updated.

    ### Updatable Fields
    - **name**: Change the world's display name
    - **description**: Update the world description
    - **is_default**: Set or unset as default world
    - **layout**: Change the layout template (does not re-seed data)
    - **realHoursPerSimDay**: Adjust simulation speed
    - **samplingStrategy**: Update capability sampling configuration
    - **capabilityIds**: Directly set capability IDs
    - **personas**: Update persona access configuration
    - **chaos**: Update chaos engineering policy
    - **ticketCreationEnabled**: Enable/disable ITSM ticket creation

    ### Use Cases
    - Adjust simulation parameters without recreating the world
    - Enable/disable chaos engineering for testing
    - Update persona access permissions
    - Change default world assignment
    - Fine-tune capability assignments

    ### Notes
    - Updating `samplingStrategy` will re-sample capabilities based on the new strategy
    - Changing `is_default` to true will automatically unset the previous default world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWorldResponse200]]
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
    body: UpdateWorldBody,
) -> Optional[Union[ErrorResponse, UpdateWorldResponse200]]:
    """Partially update a world environment


    ## Update World

    Partially update a world environment's configuration. Only the fields provided in the request body
    will be updated.

    ### Updatable Fields
    - **name**: Change the world's display name
    - **description**: Update the world description
    - **is_default**: Set or unset as default world
    - **layout**: Change the layout template (does not re-seed data)
    - **realHoursPerSimDay**: Adjust simulation speed
    - **samplingStrategy**: Update capability sampling configuration
    - **capabilityIds**: Directly set capability IDs
    - **personas**: Update persona access configuration
    - **chaos**: Update chaos engineering policy
    - **ticketCreationEnabled**: Enable/disable ITSM ticket creation

    ### Use Cases
    - Adjust simulation parameters without recreating the world
    - Enable/disable chaos engineering for testing
    - Update persona access permissions
    - Change default world assignment
    - Fine-tune capability assignments

    ### Notes
    - Updating `samplingStrategy` will re-sample capabilities based on the new strategy
    - Changing `is_default` to true will automatically unset the previous default world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWorldResponse200]
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
    body: UpdateWorldBody,
) -> Response[Union[ErrorResponse, UpdateWorldResponse200]]:
    """Partially update a world environment


    ## Update World

    Partially update a world environment's configuration. Only the fields provided in the request body
    will be updated.

    ### Updatable Fields
    - **name**: Change the world's display name
    - **description**: Update the world description
    - **is_default**: Set or unset as default world
    - **layout**: Change the layout template (does not re-seed data)
    - **realHoursPerSimDay**: Adjust simulation speed
    - **samplingStrategy**: Update capability sampling configuration
    - **capabilityIds**: Directly set capability IDs
    - **personas**: Update persona access configuration
    - **chaos**: Update chaos engineering policy
    - **ticketCreationEnabled**: Enable/disable ITSM ticket creation

    ### Use Cases
    - Adjust simulation parameters without recreating the world
    - Enable/disable chaos engineering for testing
    - Update persona access permissions
    - Change default world assignment
    - Fine-tune capability assignments

    ### Notes
    - Updating `samplingStrategy` will re-sample capabilities based on the new strategy
    - Changing `is_default` to true will automatically unset the previous default world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, UpdateWorldResponse200]]
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
    body: UpdateWorldBody,
) -> Optional[Union[ErrorResponse, UpdateWorldResponse200]]:
    """Partially update a world environment


    ## Update World

    Partially update a world environment's configuration. Only the fields provided in the request body
    will be updated.

    ### Updatable Fields
    - **name**: Change the world's display name
    - **description**: Update the world description
    - **is_default**: Set or unset as default world
    - **layout**: Change the layout template (does not re-seed data)
    - **realHoursPerSimDay**: Adjust simulation speed
    - **samplingStrategy**: Update capability sampling configuration
    - **capabilityIds**: Directly set capability IDs
    - **personas**: Update persona access configuration
    - **chaos**: Update chaos engineering policy
    - **ticketCreationEnabled**: Enable/disable ITSM ticket creation

    ### Use Cases
    - Adjust simulation parameters without recreating the world
    - Enable/disable chaos engineering for testing
    - Update persona access permissions
    - Change default world assignment
    - Fine-tune capability assignments

    ### Notes
    - Updating `samplingStrategy` will re-sample capabilities based on the new strategy
    - Changing `is_default` to true will automatically unset the previous default world


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.
        body (UpdateWorldBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, UpdateWorldResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
            body=body,
        )
    ).parsed
