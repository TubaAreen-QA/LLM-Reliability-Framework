from __future__ import annotations

from framework.pipeline.evaluation_pipeline import (
    EvaluationPipeline,
)

from framework.pipeline.prompt_render_step import (
    PromptRenderStep,
)

from framework.pipeline.provider_execution_step import (
    ProviderExecutionStep,
)

from framework.pipeline.validation_step import (
    ValidationStep,
)

from framework.pipeline.scoring_step import (
    ScoringStep,
)

from framework.pipeline.reporting_step import (
    ReportingStep,
)


class PipelineFactory:
    """
    Creates evaluation pipelines from
    configuration.
    """

    _STEP_MAP = {

        "prompt_render": PromptRenderStep,

        "provider_execution": ProviderExecutionStep,

        "validation": ValidationStep,

        "scoring": ScoringStep,

        "reporting": ReportingStep,

    }

    @classmethod
    def create(
        cls,
        configuration: list[str],
    ) -> EvaluationPipeline:

        pipeline = EvaluationPipeline()

        for step_name in configuration:

            if step_name not in cls._STEP_MAP:

                raise ValueError(

                    f"Unknown pipeline step "

                    f"'{step_name}'."

                )

            pipeline.add_step(

                cls._STEP_MAP[
                    step_name
                ]()

            )

        return pipeline