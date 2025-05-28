from __future__ import annotations

from framework.contracts.execution_context import (
    ExecutionContext,
)

from framework.pipeline.pipeline_step import (
    PipelineStep,
)


class EvaluationPipeline:

    def __init__(self):

        self._steps: list[
            PipelineStep
        ] = []

    def add_step(
        self,
        step: PipelineStep,
    ):

        self._steps.append(
            step
        )

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        for step in self._steps:

            context = step.execute(
                context
            )

        return context