from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class ValidatorWeight:

    validator: str

    weight: float

    threshold: float | None = None


@dataclass(slots=True, frozen=True)
class WeightedProfile:

    name: str

    validators: dict[str, ValidatorWeight]