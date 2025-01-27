from validators.base_validator import BaseValidator
from framework.models.provider_response import provider_Response
from framework.models.validation_result import validation_Result

class SubstringValidator(BaseValidator):
        name = "substring"

        def validate(
        self,
        response: provider_Response,
        expected
    ) -> validation_Result:

        actual = response.answer

        passed = expected.lower() in actual.lower()

        return validation_Result(
            validator=self.name,
            status="PASS" if passed else "FAIL",
            score=100 if passed else 0,
            actual=actual,
            expected=expected,
            message=(
                "Substring matched."
                if passed
                else "Substring not found."
            )
        )