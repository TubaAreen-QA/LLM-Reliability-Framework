from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class WeightedScoreResult:
    """
    Final weighted score calculation.
    """

    profile: str

    total_weight: float

    achieved_weight: float

    score: float

    passed: bool

    breakdown: dict[str, Any] = field(
        default_factory=dict
    )