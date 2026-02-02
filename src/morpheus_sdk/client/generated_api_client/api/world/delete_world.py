from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_world_response_200 import DeleteWorldResponse200
from ...models.error_response import ErrorResponse
from ...types import Response


def _get_kwargs(
    world_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/world/{world_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteWorldResponse200, ErrorResponse]]:
    if response.status_code == 200:
        response_200 = DeleteWorldResponse200.from_dict(response.json())

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
) -> Response[Union[DeleteWorldResponse200, ErrorResponse]]:
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
) -> Response[Union[DeleteWorldResponse200, ErrorResponse]]:
    """Delete a world environment


    ## Delete World

    Permanently delete a world environment and all associated data.

    ### ⚠️ Warning
    This action is **irreversible** and will delete:
    - The world environment and all its metadata
    - All companies, products, and business data within the world
    - All EDI transactions, logs, and audit records
    - All ITSM tickets and work notes
    - All WMS and TMS data
    - All configuration and settings

    ### When to Delete Worlds
    - **Test environments** that are no longer needed
    - **Development worlds** after project completion
    - **Duplicate worlds** created by mistake
    - **Deprecated environments** during cleanup
    - **Data migration scenarios** after successful migration

    ### Before Deletion
    Consider these actions before deleting:
    - **Export important data** for archival
    - **Notify stakeholders** who may be using the world
    - **Verify no active integrations** depend on this world
    - **Check for dependent worlds** that reference this one
    - **Review audit logs** for compliance requirements

    ### Alternative Actions
    Instead of deletion, consider:
    - **Archiving**: Mark the world as inactive
    - **Backup**: Export data before deletion
    - **Migration**: Move data to another world
    - **Suspension**: Temporarily disable access

    ### Best Practices
    - Use deletion sparingly in production environments
    - Always backup critical data before deletion
    - Document the reason for deletion
    - Verify the correct worldId before confirming deletion
    - Implement approval workflows for production world deletions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteWorldResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteWorldResponse200, ErrorResponse]]:
    """Delete a world environment


    ## Delete World

    Permanently delete a world environment and all associated data.

    ### ⚠️ Warning
    This action is **irreversible** and will delete:
    - The world environment and all its metadata
    - All companies, products, and business data within the world
    - All EDI transactions, logs, and audit records
    - All ITSM tickets and work notes
    - All WMS and TMS data
    - All configuration and settings

    ### When to Delete Worlds
    - **Test environments** that are no longer needed
    - **Development worlds** after project completion
    - **Duplicate worlds** created by mistake
    - **Deprecated environments** during cleanup
    - **Data migration scenarios** after successful migration

    ### Before Deletion
    Consider these actions before deleting:
    - **Export important data** for archival
    - **Notify stakeholders** who may be using the world
    - **Verify no active integrations** depend on this world
    - **Check for dependent worlds** that reference this one
    - **Review audit logs** for compliance requirements

    ### Alternative Actions
    Instead of deletion, consider:
    - **Archiving**: Mark the world as inactive
    - **Backup**: Export data before deletion
    - **Migration**: Move data to another world
    - **Suspension**: Temporarily disable access

    ### Best Practices
    - Use deletion sparingly in production environments
    - Always backup critical data before deletion
    - Document the reason for deletion
    - Verify the correct worldId before confirming deletion
    - Implement approval workflows for production world deletions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteWorldResponse200, ErrorResponse]
    """

    return sync_detailed(
        world_id=world_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[DeleteWorldResponse200, ErrorResponse]]:
    """Delete a world environment


    ## Delete World

    Permanently delete a world environment and all associated data.

    ### ⚠️ Warning
    This action is **irreversible** and will delete:
    - The world environment and all its metadata
    - All companies, products, and business data within the world
    - All EDI transactions, logs, and audit records
    - All ITSM tickets and work notes
    - All WMS and TMS data
    - All configuration and settings

    ### When to Delete Worlds
    - **Test environments** that are no longer needed
    - **Development worlds** after project completion
    - **Duplicate worlds** created by mistake
    - **Deprecated environments** during cleanup
    - **Data migration scenarios** after successful migration

    ### Before Deletion
    Consider these actions before deleting:
    - **Export important data** for archival
    - **Notify stakeholders** who may be using the world
    - **Verify no active integrations** depend on this world
    - **Check for dependent worlds** that reference this one
    - **Review audit logs** for compliance requirements

    ### Alternative Actions
    Instead of deletion, consider:
    - **Archiving**: Mark the world as inactive
    - **Backup**: Export data before deletion
    - **Migration**: Move data to another world
    - **Suspension**: Temporarily disable access

    ### Best Practices
    - Use deletion sparingly in production environments
    - Always backup critical data before deletion
    - Document the reason for deletion
    - Verify the correct worldId before confirming deletion
    - Implement approval workflows for production world deletions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteWorldResponse200, ErrorResponse]]
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
) -> Optional[Union[DeleteWorldResponse200, ErrorResponse]]:
    """Delete a world environment


    ## Delete World

    Permanently delete a world environment and all associated data.

    ### ⚠️ Warning
    This action is **irreversible** and will delete:
    - The world environment and all its metadata
    - All companies, products, and business data within the world
    - All EDI transactions, logs, and audit records
    - All ITSM tickets and work notes
    - All WMS and TMS data
    - All configuration and settings

    ### When to Delete Worlds
    - **Test environments** that are no longer needed
    - **Development worlds** after project completion
    - **Duplicate worlds** created by mistake
    - **Deprecated environments** during cleanup
    - **Data migration scenarios** after successful migration

    ### Before Deletion
    Consider these actions before deleting:
    - **Export important data** for archival
    - **Notify stakeholders** who may be using the world
    - **Verify no active integrations** depend on this world
    - **Check for dependent worlds** that reference this one
    - **Review audit logs** for compliance requirements

    ### Alternative Actions
    Instead of deletion, consider:
    - **Archiving**: Mark the world as inactive
    - **Backup**: Export data before deletion
    - **Migration**: Move data to another world
    - **Suspension**: Temporarily disable access

    ### Best Practices
    - Use deletion sparingly in production environments
    - Always backup critical data before deletion
    - Document the reason for deletion
    - Verify the correct worldId before confirming deletion
    - Implement approval workflows for production world deletions


    Args:
        world_id (str):  Example: 507f1f77bcf86cd799439011.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteWorldResponse200, ErrorResponse]
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            client=client,
        )
    ).parsed
