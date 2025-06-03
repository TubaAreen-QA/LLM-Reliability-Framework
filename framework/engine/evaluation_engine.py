from __future__ import annotations

from framework.bootstrap.provider_bootstrap import (
    ProviderBootstrap,
)

from framework.config.pipeline_loader import (
    PipelineLoader,
)

from framework.config.provider_loader import (
    ProviderLoader,
)

from framework.contracts.evaluation_result import (
    EvaluationResult,
)

from framework.contracts.execution_context import (
    ExecutionContext,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.engine.scoring_engine import (
    ScoringEngine,
)

from framework.engine.validation_engine import (
    ValidationEngine,
)

from framework.factory.provider_factory import (
    ProviderFactory,
)

from framework.pipeline.pipeline_factory import (
    PipelineFactory,
)

from framework.services.provider_service import (
    ProviderService,
)


class EvaluationEngine:
    """
    Coordinates the complete evaluation workflow.

    The execution flow is delegated to the configurable
    evaluation pipeline.
    """

    def __init__(
        self,
        provider_name: str,
        validator_names: list[str],
        provider_file: str,
        profile_name: str,
        profile_file: str,
    ) -> None:

        ProviderBootstrap.initialize()

        pipeline_steps = PipelineLoader(
            "config/pipeline.yaml"
        ).load()

        self.pipeline = PipelineFactory.create(
            pipeline_steps
        )

        config = ProviderLoader(
            provider_file
        ).load(
            provider_name
        )

        self._provider = ProviderFactory.create(
            config
        )

        self._provider_service = ProviderService()

        self._validation_engine = ValidationEngine(
            validator_names
        )

        self._scoring_engine = ScoringEngine(
            profile_name,
            profile_file,
        )

    def evaluate(
        self,
        request: ProviderRequest,
        expected,
    ) -> EvaluationResult:

        context = ExecutionContext(

            request=request,

            provider=self._provider.name,

            model=self._provider.config.model,

            profile=self._scoring_engine.profile_name,

        )

        context.metadata["provider"] = self._provider

        context.metadata[
            "provider_service"
        ] = self._provider_service

        context.metadata[
            "validation_engine"
        ] = self._validation_engine

        context.metadata[
            "scoring_engine"
        ] = self._scoring_engine

        context.metadata[
            "expected"
        ] = expected

        context = self.pipeline.execute(
            context
        )

        return context.evaluation