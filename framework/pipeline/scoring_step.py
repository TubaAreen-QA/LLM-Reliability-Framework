from __future__ import annotations

from framework.contracts.execution_context import (
    ExecutionContext,
)

from framework.pipeline.pipeline_step import (
    PipelineStep,
)


class ScoringStep(PipelineStep):
    """
    Calculates weighted score using the configured
    scoring profile.
    """

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        scoring_engine = context.metadata[
            "scoring_engine"
        ]

        context.weighted_score = (
            scoring_engine.calculate(
                context.validation_results
            )
        )

        return context