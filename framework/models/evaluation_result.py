# provider
# model
# overall_score
# confidence_score
# hallucination_score
# quality_score
# results

from dataclasses import dataclass 
from framework.models.validation_result import validation_Result
from framework.models.provider_response import provider_Response
from framework.models.evaluation_result import (
    EvaluationResult
)
from framework.engine.scoring_engine import (
    ScoringEngine
)


class EvaluationEngine:

    def __init__(
        self,
        provider,
        validator_names
    ):

        self.provider = provider

        self.validation_engine = validation_Result(
            validator_names
        )

        self.scoring_engine = ScoringEngine()

    def evaluate(
        self,
        request,
        expected
    ):

        response = self.provider.ask(
            request
        )

        validations = (
            self.validation_engine.validate(
                response,
                expected
            )
        )

        score = (
            self.scoring_engine.calculate(
                validations
            )
        )

        return EvaluationResult(
            provider_response=response,
            validation_results=validations,
            overall_score=score
        )


