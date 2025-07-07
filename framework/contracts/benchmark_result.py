from __future__ import annotations

from dataclasses import dataclass

from framework.contracts.evaluation_result import (
    EvaluationResult,
)


@dataclass(slots=True, frozen=True)
class BenchmarkResult:
    """
    Result of evaluating one benchmark sample.
    """

    sample_id: str

    evaluation: EvaluationResult