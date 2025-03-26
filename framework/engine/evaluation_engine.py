from __future__ import annotations

import time

from framework.config.provider_loader import (
    ProviderLoader,
)

from framework.contracts.evaluation_result import (
    EvaluationResult,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.engine.scoring_engine import (
    ScoringEngine,
)

from framework.engine.validation_Engine import (
    ValidationEngine,
)

from framework.factory.provider_factory import (
    ProviderFactory,
)

from framework.services.provider_service import (
    ProviderService,
)


class EvaluationEngine:

    def __init__(
        self,
        provider_name: str,
        validator_names: list[str],
        provider_file: str,
        profile_name: str,
        profile_file: str,
    ) -> None:

        config = ProviderLoader(
            provider_file
        ).load(
            provider_name
        )

        self._provider = (
            ProviderFactory.create(
                config
            )
        )

        self._provider_service = (
            ProviderService()
        )

        self._validation_engine = (
            ValidationEngine(
                validator_names
            )
        )

        self._scoring_engine = (
            ScoringEngine(
                profile_name,
                profile_file,
            )
        )

    def evaluate(
        self,
        request: ProviderRequest,
        expected,
    ) -> EvaluationResult:

        start = time.perf_counter()

        response = (
            self._provider_service.execute(
                self._provider,
                request,
            )
        )

        validation_results = (
            self._validation_engine.execute(
                request=request,
                response=response,
                expected=expected,
            )
        )

        weighted_score = (
            self._scoring_engine.calculate(
                validation_results
            )
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        return EvaluationResult(
            provider_response=response,
            validation_results=validation_results,
            overall_score=weighted_score.score,
            overall_passed=weighted_score.passed,
            execution_time_ms=round(
                elapsed,
                3,
            ),
            metadata={
                "profile": weighted_score.profile,
                "weighted_score": weighted_score,
            },
        )