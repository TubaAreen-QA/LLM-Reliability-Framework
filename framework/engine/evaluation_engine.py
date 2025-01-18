class EvaluationEngine:

    def evaluate(self, request, expected):

        response = provider.ask(request)

        validations = validation_engine.validate(
            response,
            expected
        )

        score = scoring_engine.calculate(
            validations
        )

        return EvaluationResult(
            provider_response=response,
            validation_results=validations,
            overall_score=score
        )