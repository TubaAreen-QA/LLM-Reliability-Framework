from framework.models.provider_request import provider_request
from providers.fake_provider import FakeProvider
from framework.engine.evaluation_engine import EvaluationEngine

class Evaluation_Library:
    def __init__(self):
        self.provider = FakeProvider()

        self.engine = EvaluationEngine(
            self.provider
        )

    def run_evaluation(
        self,
        prompt,
        expected
    ):

        request = provider_request(
            provider="fake",
            model="fake-gpt",
            prompt=prompt
        )

        result = self.engine.evaluate(
            request,
            expected
        )

        return result