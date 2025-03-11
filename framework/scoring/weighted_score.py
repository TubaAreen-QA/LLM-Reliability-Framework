from __future__ import annotations

from framework.contracts.validation_result import (
    ValidationResult,
)

from framework.contracts.weighted_score_result import (
    WeightedScoreResult,
)

from framework.scoring.weighted_profile import (
    WeightedProfile,
)


class WeightedScore:

    def calculate(
        self,
        profile: WeightedProfile,
        results: list[
            ValidationResult
        ],
    ) -> WeightedScoreResult:

        lookup = {

            result.validator: result

            for result

            in results

        }

        achieved_weight = 0.0

        total_weight = 0.0

        breakdown = {}

        for (
            validator_name,
            config,
        ) in profile.validators.items():

            total_weight += config.weight

            result = lookup.get(
                validator_name
            )

            if result is None:

                breakdown[
                    validator_name
                ] = {

                    "weight": config.weight,

                    "earned": 0,

                    "status": "MISSING",

                }

                continue

            earned = (

                config.weight

                * result.score

                / 100

            )

            achieved_weight += earned

            breakdown[
                validator_name
            ] = {

                "weight": config.weight,

                "earned": round(
                    earned,
                    2,
                ),

                "validator_score":
                    result.score,

                "passed":
                    result.passed,

            }

        final_score = round(

            achieved_weight,

            2,

        )

        percentage = round(

            (

                achieved_weight

                / total_weight

            )

            * 100,

            2,

        )

        return WeightedScoreResult(

            profile=profile.name,

            total_weight=total_weight,

            achieved_weight=achieved_weight,

            score=percentage,

            passed=percentage >= 70,

            breakdown=breakdown,

        )