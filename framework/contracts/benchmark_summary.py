from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True, frozen=True)
class BenchmarkSummary:
    """
    Aggregate summary produced after executing
    a benchmark dataset.
    """

    provider: str

    model: str

    profile: str

    sample_count: int

    passed: int

    failed: int

    pass_rate: float

    average_score: float

    average_latency_ms: float

    metadata: dict[str, Any]