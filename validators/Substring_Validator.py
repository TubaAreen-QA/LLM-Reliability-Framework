from framework.models.validation_result import ValidationResult


class SubstringValidator:

    def validate(self, actual: str, expected: str) -> ValidationResult:

        if expected.lower() in actual.lower():

            return ValidationResult(
                validator="substring",
                status="PASS",
                score=100,
                actual=actual,
                expected=expected,
                message="Expected text found in response."
            )

        return ValidationResult(
            validator="substring",
            status="FAIL",
            score=0,
            actual=actual,
            expected=expected,
            message="Expected text not found in response."
        )