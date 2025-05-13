from __future__ import annotations

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)

from framework.contracts.model_comparison import (
    ModelComparison,
)


class ComparisonEngine:
    """
    Compares benchmark summaries across
    multiple providers/models.
    """

    def compare(
        self,
        summaries: list[BenchmarkSummary],
    ) -> ModelComparison:

        if not summaries:
            raise ValueError(
                "No benchmark summaries supplied."
            )

        ordered = sorted(
            summaries,
            key=lambda summary: (
                summary.average_score,
                summary.pass_rate,
                -summary.average_latency_ms,
            ),
            reverse=True,
        )

        ranking = [
            f"{item.provider}:{item.model}"
            for item in ordered
        ]

        winner = ranking[0]

        return ModelComparison(
            summaries=ordered,
            winner=winner,
            ranking=ranking,
        )