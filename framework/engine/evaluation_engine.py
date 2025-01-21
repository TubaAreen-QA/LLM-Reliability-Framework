from framework.engine.validation_Engine import ValidationEngine
from framework.engine.scoring_engine import ScoringEngine

from framework.models.evaluation_result import EvaluationResult


class EvaluationEngine:

    def __init__(self, provider):

        self.provider = provider

        self.validation_engine = ValidationEngine()

        self.scoring_engine = ScoringEngine()

    def evaluate(self, request, expected):

        response = self.provider.ask(request)

        validations = self.validation_engine.validate(

            response,

            expected

        )

        score = self.scoring_engine.calculate(

            validations

        )

        return EvaluationResult(

            provider_response=response,

            validation_results=validations,

            overall_score=score

        )