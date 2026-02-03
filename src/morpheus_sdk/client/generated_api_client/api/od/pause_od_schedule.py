from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.pause_od_schedule_response_200 import PauseODScheduleResponse200
from ...types import Response


def _get_kwargs(
    world_id: str,
    od_id: str,
    job_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/{world_id}/od/descriptors/{od_id}/schedules/{job_id}/pause",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PauseODScheduleResponse200]:
    if response.status_code == 200:
        response_200 = PauseODScheduleResponse200.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PauseODScheduleResponse200]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PauseODScheduleResponse200]:
    """Pause a specific OD schedule

     Pauses a specific scheduled execution of an OD. It will not run until resumed.

    Args:
        world_id (str):
        od_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PauseODScheduleResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        job_id=job_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PauseODScheduleResponse200]:
    """Pause a specific OD schedule

     Pauses a specific scheduled execution of an OD. It will not run until resumed.

    Args:
        world_id (str):
        od_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PauseODScheduleResponse200
    """

    return sync_detailed(
        world_id=world_id,
        od_id=od_id,
        job_id=job_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PauseODScheduleResponse200]:
    """Pause a specific OD schedule

     Pauses a specific scheduled execution of an OD. It will not run until resumed.

    Args:
        world_id (str):
        od_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PauseODScheduleResponse200]
    """

    kwargs = _get_kwargs(
        world_id=world_id,
        od_id=od_id,
        job_id=job_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    world_id: str,
    od_id: str,
    job_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PauseODScheduleResponse200]:
    """Pause a specific OD schedule

     Pauses a specific scheduled execution of an OD. It will not run until resumed.

    Args:
        world_id (str):
        od_id (str):
        job_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PauseODScheduleResponse200
    """

    return (
        await asyncio_detailed(
            world_id=world_id,
            od_id=od_id,
            job_id=job_id,
            client=client,
        )
    ).parsed
