from __future__ import annotations
from typing import Any, Optional

import httpx

from morpheus_sdk.models.model_http_client import (
    ModelHttpClientInputs,
    ModelHttpClientOutputs,
)


def sync_http_client(base_params: ModelHttpClientInputs) -> ModelHttpClientOutputs:
    client = httpx.Client(
        base_url=base_params.base_url,
        headers=base_params.headers,
        timeout=base_params.timeout,
    )

    def get(
        path: str,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return client.get(path, params=params, headers=headers)

    def post(
        path: str,
        json: Optional[dict[str, Any]] = None,
        data: Optional[Any] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return client.post(path, json=json, content=data, headers=headers)

    def put(
        path: str,
        json: Optional[dict[str, Any]] = None,
        data: Optional[Any] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return client.put(path, json=json, content=data, headers=headers)

    def delete(
        path: str,
        params: Optional[dict[str, Any]] = None,
        headers: Optional[dict[str, str]] = None,
    ) -> httpx.Response:
        return client.delete(path, params=params, headers=headers)

    out = ModelHttpClientOutputs(get=get, post=post, put=put, delete=delete)
    out.close = client.close
    return out
