from providers.fake_provider import FakeProvider

from framework.engine.evaluation_engine import EvaluationEngine

from framework.models.provider_request import ProviderRequest


def test_evaluation_pipeline():

    provider = FakeProvider()

    engine = EvaluationEngine(provider)

    request = ProviderRequest(

        provider="fake",

        model="fake-gpt",

        prompt="What is the capital of France?"

    )

    result = engine.evaluate(

        request,

        expected="Paris"

    )

    assert result.overall_score == 100

    assert result.provider_response.answer == "Paris"

    assert len(result.validation_results) == 1

    assert result.validation_results[0].status == "PASS"