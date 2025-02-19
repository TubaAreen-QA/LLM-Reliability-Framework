from __future__ import annotations

import time

from framework.constants.execution_status import ExecutionStatus
from framework.contracts.provider_request import ProviderRequest
from framework.contracts.provider_response import ProviderResponse
from framework.contracts.validation_result import ValidationResult

from validators.base_validator import BaseValidator


class SubstringValidator(BaseValidator):

    @property
    def name(self) -> str:
        return "substring"

    @property
    def threshold(self) -> float:
        return 100.0

    def validate(
        self,
        request: ProviderRequest,
        response: ProviderResponse,
        expected
    ) -> ValidationResult:

        start = time.perf_counter()

        actual = response.answer

        passed = (
            expected.lower()
            in actual.lower()
        )

        elapsed = (
            time.perf_counter() - start
        ) * 1000

        return ValidationResult(
            validator=self.name,
            passed=passed,
            score=100.0 if passed else 0.0,
            threshold=self.threshold,
            actual=actual,
            expected=expected,
            execution_time_ms=round(
                elapsed,
                3
            ),
            message=(
                ExecutionStatus.PASS.value
                if passed
                else ExecutionStatus.FAIL.value
            )
        )