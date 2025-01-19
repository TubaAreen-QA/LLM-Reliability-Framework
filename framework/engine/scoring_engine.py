from framework.models.validation_result import validation_Result

class scoring_engine:
    def calculate(self, validation_results: list[validation_Result]) ->float:
        if not validation_results:
            return 0
        total = sum(result.score for result in validation_results)
        return total /len(validation_results)