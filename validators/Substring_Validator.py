from validators.base_validator import BaseValidator

from framework.models.validation_result import ValidationResult

class SubstringValidator(BaseValidator):

    def validate(self, actual, expected):

        if expected.lower() in actual.lower():

            return ValidationResult(
                validator="substring",
                status="PASS",
                score=100,
                actual=actual,
                expected=expected,
                message="Substring matched."
            )

        return ValidationResult(
            validator="substring",
            status="FAIL",
            score=0,
            actual=actual,
            expected=expected,
            message="Substring not found."
        )