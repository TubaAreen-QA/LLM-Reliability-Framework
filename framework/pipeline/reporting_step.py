from __future__ import annotations

import time

from framework.contracts.evaluation_result import (
    EvaluationResult,
)

from framework.contracts.execution_context import (
    ExecutionContext,
)

from framework.pipeline.pipeline_step import (
    PipelineStep,
)


class ReportingStep(PipelineStep):
    """
    Produces the final EvaluationResult from the
    execution context.
    """

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        started = context.metadata.get(
            "started_at"
        )

        elapsed = 0.0

        if started is not None:

            elapsed = (

                time.perf_counter()

                - started

            ) * 1000

        context.evaluation = EvaluationResult(

            provider_response=context.response,

            validation_results=context.validation_results,

            overall_score=context.weighted_score.score,

            overall_passed=context.weighted_score.passed,

            execution_time_ms=round(
                elapsed,
                3,
            ),

            metadata={

                "profile":

                    context.weighted_score.profile,

                "weighted_score":

                    context.weighted_score,

            },

        )

        return context