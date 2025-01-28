from framework.models.validation_result import validation_Result

class ScoringEngine:

    def calculate(
        self,
        validation_results: list[validation_Result]
    ) -> float:

        if not validation_results:
            return 0.0

        total = sum(
            result.score
            for result in validation_results
        )

        return round(
            total / len(validation_results),
            2
        )