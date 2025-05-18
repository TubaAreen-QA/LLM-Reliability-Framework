from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class EvaluationTask:
    """
    Represents a single evaluation job.
    """

    provider: str

    model: str

    profile: str

    prompt: str

    expected: Any

    metadata: dict[str, Any]