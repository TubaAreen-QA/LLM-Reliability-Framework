def test_substring_validator_pass():

    actual = "The capital of France is Paris."

    expected = "Paris"

    result = validator.validate(actual, expected)

    assert result.status == "PASS"


def test_substring_validator_fail():

    actual = "London"

    expected = "Paris"

    result = validator.validate(actual, expected)

    assert result.status == "FAIL"