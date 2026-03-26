from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class UsageDetail:
    input: int = 0
    output: int = 0
    total: int = 0
    cache_read_input_tokens: int = 0


class Logger:
    def on_request_start(
        self,
        id: str,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass

    def on_request_end(
        self,
        id: str,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass

    def on_middleware(
        self,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass

    def on_llm(
        self,
        name: Optional[str] = None,
        model: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
        usage_details: Optional[UsageDetail] = None,
    ) -> None:
        pass

    def on_tool_start(
        self,
        id: str,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass

    def on_tool_end(
        self,
        id: str,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass

    def on_interrupt_start(
        self,
        id: str,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass

    def on_interrupt_end(
        self,
        id: str,
        name: Optional[str] = None,
        input: Optional[Any] = None,
        output: Optional[Any] = None,
        metadata: Optional[Any] = None,
    ) -> None:
        pass
