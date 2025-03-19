from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ProviderConfig:
    """
    Immutable provider configuration loaded from YAML.
    """

    name: str

    model: str

    api_key: str | None

    base_url: str | None

    timeout: int

    temperature: float

    max_tokens: int

    retries: int

    enabled: bool = True

    metadata: dict[str, Any] = field(
        default_factory=dict
    )