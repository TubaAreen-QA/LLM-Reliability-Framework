from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ProviderRequest:
    """
    Standard request sent to every provider.
    """

    prompt: str

    system_prompt: str | None = None

    temperature: float = 0.0

    max_tokens: int | None = None

    top_p: float = 1.0

    stop_sequences: list[str] = field(
        default_factory=list,
    )

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )