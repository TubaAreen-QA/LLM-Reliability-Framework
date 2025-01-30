from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ProviderResponse:
    """
    Immutable response returned by a provider.
    """

    provider: str

    model: str

    prompt: str

    answer: str

    response_time_ms: float

    token_usage: dict[str, int]

    raw_response: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)