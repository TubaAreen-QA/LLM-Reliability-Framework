from __future__ import annotations

from dataclasses import dataclass, field

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)


@dataclass(slots=True, frozen=True)
class ModelComparison:
    """
    Represents the comparison of multiple
    benchmark executions.
    """

    summaries: list[BenchmarkSummary]

    winner: str

    ranking: list[str]

    metadata: dict = field(
        default_factory=dict,
    )