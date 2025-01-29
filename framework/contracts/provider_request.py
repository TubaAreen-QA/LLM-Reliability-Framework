from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ProviderRequest:
    """
    Immutable request sent to an LLM provider.
    """

    provider: str

    model: str

    prompt: str

    temperature: float = 0.0

    max_tokens: int = 512

    timeout: int = 30

    metadata: dict[str, Any] = field(default_factory=dict)