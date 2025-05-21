from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class PromptTemplate:
    """
    Represents a reusable prompt template.
    """

    name: str

    template: str

    variables: dict[str, Any] = field(
        default_factory=dict,
    )