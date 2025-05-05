from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class BenchmarkSample:
    """
    Single benchmark sample.
    """

    prompt: str

    expected: Any

    category: str = ""

    metadata: dict = None