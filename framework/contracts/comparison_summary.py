from __future__ import annotations

from dataclasses import dataclass, field

from framework.contracts.model_result import (
    ModelResult,
)


@dataclass(slots=True, frozen=True)
class ComparisonSummary:
    """
    Overall comparison output.
    """

    winner: str

    score_difference: float

    reason: str

    rankings: list[ModelResult]

    metadata: dict = field(
        default_factory=dict
    )