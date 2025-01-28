from providers.fake_provider import FakeProvider

from framework.engine.evaluation_engine import (
    EvaluationEngine
)

from framework.models.provider_request import (
    ProviderRequest
)


provider = FakeProvider()

engine = EvaluationEngine(
    provider=provider,
    validator_names=[
        "substring"
    ]
)


def test_complete_pipeline():

    request = ProviderRequest(
        provider="fake",
        model="fake-gpt",
        prompt="What is the capital of France?"
    )

    result = engine.evaluate(
        request=request,
        expected="Paris"
    )

    assert (
        result.provider_response.answer
        == "Paris"
    )

    assert (
        result.validation_results[0].status
        == "PASS"
    )

    assert result.overall_score == 100