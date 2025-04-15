from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class NormalizedResponse:
    """
    Vendor-independent response representation.
    Every provider response is converted into this format
    before constructing ProviderResponse.
    """

    answer: str

    prompt_tokens: int

    completion_tokens: int

    total_tokens: int

    finish_reason: str | None = None

    model: str | None = None

    metadata: dict[str, Any] = field(
        default_factory=dict
    )