from __future__ import annotations

from framework.contracts.comparison_summary import (
    ComparisonSummary,
)

from framework.contracts.model_result import (
    ModelResult,
)


class ComparisonEngine:

    def compare(
        self,
        evaluations: list[ModelResult],
    ) -> ComparisonSummary:

        rankings = sorted(

            evaluations,

            key=lambda result:
            result.evaluation.overall_score,

            reverse=True,

        )

        winner = rankings[0]

        runner_up = rankings[1]

        difference = round(

            winner.evaluation.overall_score

            -

            runner_up.evaluation.overall_score,

            2,

        )

        return ComparisonSummary(

            winner=winner.provider,

            score_difference=difference,

            reason="Higher evaluation score",

            rankings=rankings,

        )