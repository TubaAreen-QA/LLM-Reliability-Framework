from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ProviderResponse:
    """
    Standard response returned by providers.
    """

    content: str

    model: str

    provider: str

    finish_reason: str

    prompt_tokens: int = 0

    completion_tokens: int = 0

    total_tokens: int = 0

    latency_ms: float = 0.0

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )