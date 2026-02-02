from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_world_chaos_response_200 import DeleteWorldChaosResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/world/{world_id}/chaos",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteWorldChaosResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteWorldChaosResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteWorldChaosResponse200, ErrorResponse]]:
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
) -> Response[Union[DeleteWorldChaosResponse200, ErrorResponse]]:
    r"""Delete chaos configuration from a world


    ## Delete World Chaos Configuration

    Remove the chaos engineering configuration from a world, resetting it to the disabled default state.

    ### What Happens
    - Removes the chaos policy from the world document
    - Resets the chaos registry entry to disabled state
    - Future workflow executions will not have chaos injection

    ### Default State After Deletion
    ```json
    {
      \"enabled\": false,
      \"probability\": 0.0,
      \"scenarios\": []
    }
    ```

    ### Use Cases
    - Disable chaos after testing is complete
    - Reset a world to clean state before production use
    - Remove misconfigured chaos settings
    - Prepare a world for stable demonstration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteWorldChaosResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteWorldChaosResponse200, ErrorResponse]]:
    r"""Delete chaos configuration from a world


    ## Delete World Chaos Configuration

    Remove the chaos engineering configuration from a world, resetting it to the disabled default state.

    ### What Happens
    - Removes the chaos policy from the world document
    - Resets the chaos registry entry to disabled state
    - Future workflow executions will not have chaos injection

    ### Default State After Deletion
    ```json
    {
      \"enabled\": false,
      \"probability\": 0.0,
      \"scenarios\": []
    }
    ```

    ### Use Cases
    - Disable chaos after testing is complete
    - Reset a world to clean state before production use
    - Remove misconfigured chaos settings
    - Prepare a world for stable demonstration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteWorldChaosResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeleteWorldChaosResponse200, ErrorResponse]]:
    r"""Delete chaos configuration from a world


    ## Delete World Chaos Configuration

    Remove the chaos engineering configuration from a world, resetting it to the disabled default state.

    ### What Happens
    - Removes the chaos policy from the world document
    - Resets the chaos registry entry to disabled state
    - Future workflow executions will not have chaos injection

    ### Default State After Deletion
    ```json
    {
      \"enabled\": false,
      \"probability\": 0.0,
      \"scenarios\": []
    }
    ```

    ### Use Cases
    - Disable chaos after testing is complete
    - Reset a world to clean state before production use
    - Remove misconfigured chaos settings
    - Prepare a world for stable demonstration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteWorldChaosResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteWorldChaosResponse200, ErrorResponse]]:
    r"""Delete chaos configuration from a world


    ## Delete World Chaos Configuration

    Remove the chaos engineering configuration from a world, resetting it to the disabled default state.

    ### What Happens
    - Removes the chaos policy from the world document
    - Resets the chaos registry entry to disabled state
    - Future workflow executions will not have chaos injection

    ### Default State After Deletion
    ```json
    {
      \"enabled\": false,
      \"probability\": 0.0,
      \"scenarios\": []
    }
    ```

    ### Use Cases
    - Disable chaos after testing is complete
    - Reset a world to clean state before production use
    - Remove misconfigured chaos settings
    - Prepare a world for stable demonstration


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteWorldChaosResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
