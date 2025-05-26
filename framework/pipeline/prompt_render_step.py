from __future__ import annotations

from framework.pipeline.pipeline_step import (
    PipelineStep,
)

from framework.prompts.prompt_renderer import (
    PromptRenderer,
)


class PromptRenderStep(PipelineStep):

    def __init__(self):

        self.renderer = PromptRenderer()

    def execute(
        self,
        context: dict,
    ) -> dict:

        template = context.get(
            "template"
        )

        if template is None:
            return context

        context["prompt"] = (

            self.renderer.render(
                template
            )

        )

        return context