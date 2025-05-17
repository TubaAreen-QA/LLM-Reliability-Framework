from __future__ import annotations

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)


class Leaderboard:

    """
    Produces ranked benchmark results.
    """

    def rank(
        self,
        summaries: list[
            BenchmarkSummary
        ],
    ) -> list[BenchmarkSummary]:

        return sorted(

            summaries,

            key=lambda item: (

                item.average_score,

                item.pass_rate,

                -item.average_latency_ms,

            ),

            reverse=True,

        )