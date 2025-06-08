from __future__ import annotations

import json
from pathlib import Path

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)


class SummaryRepository:

    def __init__(
        self,
        directory: str = "reports",
    ):

        self.directory = Path(directory)

        self.directory.mkdir(

            parents=True,

            exist_ok=True,

        )

    def save(

        self,

        name: str,

        summary: BenchmarkSummary,

    ) -> Path:

        path = self.directory / f"{name}.json"

        with path.open(

            "w",

            encoding="utf-8",

        ) as fp:

            json.dump(

                summary.__dict__,

                fp,

                indent=4,

                default=str,

            )

        return path

    def load(

        self,

        name: str,

    ) -> BenchmarkSummary:

        path = self.directory / f"{name}.json"

        with path.open(

            encoding="utf-8",

        ) as fp:

            data = json.load(fp)

        return BenchmarkSummary(

            **data,

        )