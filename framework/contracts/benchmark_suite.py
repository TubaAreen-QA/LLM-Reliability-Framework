from __future__ import annotations

from dataclasses import dataclass, field

from framework.benchmark.base_dataset import (
    BaseDataset,
)


@dataclass(slots=True)
class BenchmarkSuite:
    """
    A collection of datasets, providers,
    and scoring profiles that are executed
    together.
    """

    name: str

    datasets: list[BaseDataset]

    providers: list[str]

    profiles: list[str]

    metadata: dict = field(
        default_factory=dict,
    )