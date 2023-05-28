from typing import Any, TypedDict


class Response(TypedDict):
    error: list[str]
    result: dict[str, Any]
