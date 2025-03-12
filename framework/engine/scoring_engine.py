from __future__ import annotations

from framework.contracts.validation_result import (
    ValidationResult,
)

from framework.contracts.weighted_score_result import (
    WeightedScoreResult,
)

from framework.scoring.profile_loader import (
    ProfileLoader,
)

from framework.scoring.weighted_score import (
    WeightedScore,
)


class ScoringEngine:

    def __init__(
        self,
        profile_name: str,
        profile_file: str,
    ) -> None:

        self._profile = (

            ProfileLoader(

                profile_file,

            ).load(

                profile_name,

            )

        )

        self._strategy = (

            WeightedScore()

        )

    def calculate(
        self,
        validation_results: list[
            ValidationResult
        ],
    ) -> WeightedScoreResult:

        return self._strategy.calculate(

            self._profile,

            validation_results,

        )