from __future__ import annotations

from dataclasses import dataclass

from framework.contracts.evaluation_result import (
    EvaluationResult,
)


@dataclass(slots=True, frozen=True)
class ModelResult:
    """
    Represents a single model execution.
    """

    provider: str

    model: str

    evaluation: EvaluationResult