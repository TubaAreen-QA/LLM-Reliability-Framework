from __future__ import annotations

from dataclasses import dataclass, field

from framework.contracts.evaluation_result import EvaluationResult


@dataclass(slots=True, frozen=True)
class ComparisonResult:
    """
    Comparison between multiple model evaluations.
    """

    evaluations: list[EvaluationResult]

    winner: str

    score_difference: float

    reason: str

    metadata: dict = field(default_factory=dict)