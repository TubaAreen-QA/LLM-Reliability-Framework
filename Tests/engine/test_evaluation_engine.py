from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.engine.evaluation_engine import (
    EvaluationEngine,
)


def test_evaluation_engine_returns_result():

    engine = EvaluationEngine(

        provider_name="fake",

        validator_names=["exact_match"],

        provider_file="config/providers.yaml",

        profile_name="default",

        profile_file="config/profiles.yaml",

    )

    request = ProviderRequest(

        prompt="Hello",

    )

    result = engine.evaluate(

        request=request,

        expected="Hello",

    )

    assert result is not None

    assert result.provider_response is not None

    assert result.validation_results is not None