from __future__ import annotations

import time

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.contracts.validation_result import (
    ValidationResult,
)

from validators.base_validator import (
    BaseValidator,
)


class ConfidenceValidator(BaseValidator):

    @property
    def name(self) -> str:

        return "confidence"

    @property
    def threshold(self) -> float:

        return 0.80

    def validate(

        self,

        request: ProviderRequest,

        response: ProviderResponse,

        expected,

    ) -> ValidationResult:

        start = time.perf_counter()

        confidence = response.metadata.get(

            "confidence",

            0.0,

        )

        passed = confidence >= self.threshold

        elapsed = (

            time.perf_counter()

            - start

        ) * 1000

        return ValidationResult(

            validator=self.name,

            passed=passed,

            score=100.0 if passed else 0.0,

            threshold=self.threshold,

            actual=confidence,

            expected=self.threshold,

            execution_time_ms=round(

                elapsed,

                3,

            ),

            message=(

                "Confidence validation"

            ),

        )