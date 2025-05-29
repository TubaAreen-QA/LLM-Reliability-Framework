from __future__ import annotations

from framework.contracts.execution_context import (
    ExecutionContext,
)

from framework.factory.provider_factory import (
    ProviderFactory,
)

from framework.pipeline.pipeline_step import (
    PipelineStep,
)


class ProviderExecutionStep(PipelineStep):

    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:

        provider = ProviderFactory.create(
            context.metadata[
                "provider_config"
            ]
        )

        context.response = provider.ask(
            context.request
        )

        return context