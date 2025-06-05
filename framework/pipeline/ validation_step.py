from __future__ import annotations

from framework.contracts.execution_context import (
    ExecutionContext,
)

from framework.pipeline.pipeline_step import (
    PipelineStep,
)


class ValidationStep(PipelineStep):
    """
    Executes all configured validators and stores
    the validation results inside the execution context.
    """

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        validation_engine = context.metadata[
            "validation_engine"
        ]

        expected = context.metadata[
            "expected"
        ]

        context.validation_results = (
            validation_engine.execute(
                request=context.request,
                response=context.response,
                expected=expected,
            )
        )

        return context