from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ValidationResult:
    """
    Result produced by a validator.
    """

    validator: str

    status: str

    score: float

    expected: str

    actual: str

    message: str