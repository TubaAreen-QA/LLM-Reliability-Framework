from __future__ import annotations

from dataclasses import dataclass, field

from framework.contracts.evaluation_result import EvaluationResult


@dataclass(slots=True, frozen=True)
class BenchmarkResult:
    """
    Aggregated benchmark execution result.
    """

    provider: str

    model: str

    total_prompts: int

    passed: int

    failed: int

    average_score: float

    average_latency_ms: float

    evaluations: list[EvaluationResult]

    metadata: dict = field(default_factory=dict)