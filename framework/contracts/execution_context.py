from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)

from framework.contracts.evaluation_result import (
    EvaluationResult,
)

from framework.contracts.validation_result import ValidationResult
from framework.contracts.weighted_score import WeightedScore


@dataclass(slots=True)
class ExecutionContext:
    """
    Shared context passed through the
    evaluation pipeline.
    """

    request: ProviderRequest

    response: ProviderResponse | None = None

    evaluation: EvaluationResult | None = None

    benchmark_name: str = ""

    provider: str = ""

    model: str = ""

    profile: str = ""

    correlation_id: str = ""

    metadata: dict[str, Any] = field(
        default_factory=dict,
        
    )

    
    validation_results: list[ValidationResult] = field(
    default_factory=list,
    )

    weighted_score: WeightedScore | None = None