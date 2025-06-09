from __future__ import annotations

from pathlib import Path

import yaml

from framework.benchmark.json_dataset import (
    JsonDataset,
)

from framework.contracts.benchmark_suite import (
    BenchmarkSuite,
)


class SuiteLoader:
    """
    Loads benchmark suite definitions from YAML.
    """

    def load(
        self,
        filename: str,
    ) -> BenchmarkSuite:

        path = Path(filename)

        with path.open(
            encoding="utf-8",
        ) as fp:

            config = yaml.safe_load(fp)

        datasets = [

            JsonDataset(dataset)

            for dataset

            in config["datasets"]

        ]

        return BenchmarkSuite(

            name=config["name"],

            datasets=datasets,

            providers=config["providers"],

            profiles=config["profiles"],

            metadata=config.get(
                "metadata",
                {},
            ),

        )