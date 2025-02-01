from __future__ import annotations

from dataclasses import dataclass, field

from framework.contracts.provider_response import ProviderResponse
from framework.contracts.validation_result import ValidationResult


@dataclass(slots=True, frozen=True)
class EvaluationResult:
    """
    Final evaluation produced by the framework.
    """

    provider_response: ProviderResponse

    validation_results: list[ValidationResult]

    overall_score: float

    overall_passed: bool

    execution_time_ms: float

    metadata: dict = field(default_factory=dict)