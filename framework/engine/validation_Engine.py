from validators.Substring_Validator import SubstringValidator
from framework.registry.validator_registry import (
    ValidatorRegistry
)
from framework.models.provider_response import (
    provider_Response
)


validator = SubstringValidator()


def response(answer):

    return provider_Response(
        provider="fake",
        model="fake",
        prompt="",
        answer=answer,
        response_time_ms=0,
        token_usage={}
    )


def test_substring_pass():

    result = validator.validate(
        response("Paris"),
        "Paris"
    )

    assert result.status == "PASS"

    assert result.score == 100


def test_substring_fail():

    result = validator.validate(
        response("London"),
        "Paris"
    )

    assert result.status == "FAIL"

    assert result.score == 0