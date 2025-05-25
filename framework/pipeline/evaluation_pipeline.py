from __future__ import annotations

from framework.pipeline.pipeline_step import (
    PipelineStep,
)


class EvaluationPipeline:
    """
    Executes pipeline steps sequentially.
    """

    def __init__(self):

        self._steps: list[
            PipelineStep
        ] = []

    def add_step(
        self,
        step: PipelineStep,
    ) -> None:

        self._steps.append(step)

    def execute(
        self,
        context: dict,
    ) -> dict:

        current = context

        for step in self._steps:

            current = step.execute(
                current
            )

        return current