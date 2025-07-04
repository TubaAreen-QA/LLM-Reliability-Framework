from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class WeightedScore:
    """
    Final weighted score calculated from
    validation results.
    """

    score: float

    passed: bool

    profile: str