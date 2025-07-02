from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True, frozen=True)
class ProviderConfig:
    """
    Provider configuration loaded from YAML.
    """

    name: str

    model: str

    api_key_env: str | None = None

    base_url: str | None = None

    timeout: int = 60

    options: dict[str, Any] = field(
        default_factory=dict,
    )