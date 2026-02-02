from __future__ import annotations
from typing import  Awaitable, Callable
from pydantic import BaseModel
from httpx import Response


class ModelHttpClientInputs(BaseModel):
    base_url: str = "http://localhost:8282"
    headers: dict[str, str] = {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    timeout: float = 150.0


SyncRequestFn = Callable[...,  Response]
AsyncRequestFn = Callable[..., Awaitable[Response]]


class ModelHttpClientOutputs(BaseModel):
    get: SyncRequestFn
    post: SyncRequestFn
    put: SyncRequestFn
    delete: SyncRequestFn
    close: Callable[[], None]

    model_config = {"arbitrary_types_allowed": True}


class ModelHttpAsyncClientOutputs(BaseModel):
    get: AsyncRequestFn
    post: AsyncRequestFn
    put: AsyncRequestFn
    delete: AsyncRequestFn
    aclose: Callable[[], Awaitable[None]]

    model_config = {"arbitrary_types_allowed": True}
