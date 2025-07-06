from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class BenchmarkSample:
    """
    Single benchmark example.
    """

    id: str

    prompt: str

    expected: Any

    validators: list[str]

    profile: str

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )