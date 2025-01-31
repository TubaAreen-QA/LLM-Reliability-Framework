from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ValidationResult:
    """
    Result returned by an individual validator.
    """

    validator: str

    passed: bool

    score: float

    threshold: float

    actual: Any

    expected: Any

    execution_time_ms: float

    message: str = ""

    metadata: dict[str, Any] = field(default_factory=dict)