from __future__ import annotations

from framework.benchmark.base_dataset import (
    BaseDataset,
)

from framework.contracts.benchmark_sample import (
    BenchmarkSample,
)

from framework.engine.evaluation_engine import (
    EvaluationEngine,
)


class BenchmarkRunner:

    """
    Executes an EvaluationEngine against
    an entire benchmark dataset.
    """

    def __init__(
        self,
        engine: EvaluationEngine,
    ):

        self.engine = engine

    def run(
        self,
        dataset: BaseDataset,
    ):

        results = []

        for sample in dataset:

            result = self.engine.evaluate(

                request=sample.prompt,

                expected=sample.expected,

            )

            results.append(result)

        return results