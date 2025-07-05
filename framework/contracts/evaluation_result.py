from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.contracts.validation_result import (
    ValidationResult,
)


@dataclass(slots=True, frozen=True)
class EvaluationResult:
    """
    Final output produced by EvaluationEngine.
    """

    provider_response: ProviderResponse

    validation_results: list[ValidationResult]

    overall_score: float

    overall_passed: bool

    execution_time_ms: float

    metadata: dict[str, Any] = field(
        default_factory=dict,
    )