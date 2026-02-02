from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.reset_world_response_200 import ResetWorldResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/world/{world_id}/reset",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ErrorResponse, ResetWorldResponse200]]:
    if response.status_code == 200:
        response_200 = ResetWorldResponse200.from_dict(response.json())

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
) -> Response[Union[ErrorResponse, ResetWorldResponse200]]:
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
) -> Response[Union[ErrorResponse, ResetWorldResponse200]]:
    """Reset a world environment


    ## Reset World Environment

    Reset a world environment to its initial state, clearing all data while preserving the world
    definition and configuration.

    ### What happens during reset:
    1.  **Data Cleanup**: All existing data associated with the world is permanently deleted:
        -   Companies, products, and customers
        -   Orders, invoices, and shipments
        -   EDI transactions and logs
        -   WMS inventory and tasks
        -   ITSM tickets
    2.  **Re-Seeding**: The world is automatically re-populated with fresh seed data:
        -   Main company (MPC) regeneration
        -   Partner/Customer generation based on world layout
        -   Product catalog regeneration
        -   Operational Descriptor (OD) re-initialization

    ### Use Cases
    -   **Simulation Restart**: Restarting a simulation scenario from scratch
    -   **Test Automation**: Cleaning up state between test runs
    -   **Development Loop**: Rapidly iterating on world configurations
    -   **Demo Resets**: Resetting a demo environment for a new audience

    ### ⚠️ Warning
    This action deletes all transactional data. Ensure you have backed up any critical information
    before proceeding.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResetWorldResponse200]]
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
) -> Optional[Union[ErrorResponse, ResetWorldResponse200]]:
    """Reset a world environment


    ## Reset World Environment

    Reset a world environment to its initial state, clearing all data while preserving the world
    definition and configuration.

    ### What happens during reset:
    1.  **Data Cleanup**: All existing data associated with the world is permanently deleted:
        -   Companies, products, and customers
        -   Orders, invoices, and shipments
        -   EDI transactions and logs
        -   WMS inventory and tasks
        -   ITSM tickets
    2.  **Re-Seeding**: The world is automatically re-populated with fresh seed data:
        -   Main company (MPC) regeneration
        -   Partner/Customer generation based on world layout
        -   Product catalog regeneration
        -   Operational Descriptor (OD) re-initialization

    ### Use Cases
    -   **Simulation Restart**: Restarting a simulation scenario from scratch
    -   **Test Automation**: Cleaning up state between test runs
    -   **Development Loop**: Rapidly iterating on world configurations
    -   **Demo Resets**: Resetting a demo environment for a new audience

    ### ⚠️ Warning
    This action deletes all transactional data. Ensure you have backed up any critical information
    before proceeding.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResetWorldResponse200]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ErrorResponse, ResetWorldResponse200]]:
    """Reset a world environment


    ## Reset World Environment

    Reset a world environment to its initial state, clearing all data while preserving the world
    definition and configuration.

    ### What happens during reset:
    1.  **Data Cleanup**: All existing data associated with the world is permanently deleted:
        -   Companies, products, and customers
        -   Orders, invoices, and shipments
        -   EDI transactions and logs
        -   WMS inventory and tasks
        -   ITSM tickets
    2.  **Re-Seeding**: The world is automatically re-populated with fresh seed data:
        -   Main company (MPC) regeneration
        -   Partner/Customer generation based on world layout
        -   Product catalog regeneration
        -   Operational Descriptor (OD) re-initialization

    ### Use Cases
    -   **Simulation Restart**: Restarting a simulation scenario from scratch
    -   **Test Automation**: Cleaning up state between test runs
    -   **Development Loop**: Rapidly iterating on world configurations
    -   **Demo Resets**: Resetting a demo environment for a new audience

    ### ⚠️ Warning
    This action deletes all transactional data. Ensure you have backed up any critical information
    before proceeding.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ErrorResponse, ResetWorldResponse200]]
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
) -> Optional[Union[ErrorResponse, ResetWorldResponse200]]:
    """Reset a world environment


    ## Reset World Environment

    Reset a world environment to its initial state, clearing all data while preserving the world
    definition and configuration.

    ### What happens during reset:
    1.  **Data Cleanup**: All existing data associated with the world is permanently deleted:
        -   Companies, products, and customers
        -   Orders, invoices, and shipments
        -   EDI transactions and logs
        -   WMS inventory and tasks
        -   ITSM tickets
    2.  **Re-Seeding**: The world is automatically re-populated with fresh seed data:
        -   Main company (MPC) regeneration
        -   Partner/Customer generation based on world layout
        -   Product catalog regeneration
        -   Operational Descriptor (OD) re-initialization

    ### Use Cases
    -   **Simulation Restart**: Restarting a simulation scenario from scratch
    -   **Test Automation**: Cleaning up state between test runs
    -   **Development Loop**: Rapidly iterating on world configurations
    -   **Demo Resets**: Resetting a demo environment for a new audience

    ### ⚠️ Warning
    This action deletes all transactional data. Ensure you have backed up any critical information
    before proceeding.


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ErrorResponse, ResetWorldResponse200]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
