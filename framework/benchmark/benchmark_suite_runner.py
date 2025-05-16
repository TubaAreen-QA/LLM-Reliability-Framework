from __future__ import annotations

from framework.benchmark.benchmark_engine import (
    BenchmarkEngine,
)

from framework.benchmark.benchmark_runner import (
    BenchmarkRunner,
)

from framework.contracts.benchmark_suite import (
    BenchmarkSuite,
)

from framework.engine.evaluation_engine import (
    EvaluationEngine,
)


class BenchmarkSuiteRunner:
    """
    Executes every provider against every
    dataset using every scoring profile.
    """

    def __init__(
        self,
        provider_file: str,
    ):

        self.provider_file = provider_file

    def run(
        self,
        suite: BenchmarkSuite,
    ):

        summaries = []

        for provider in suite.providers:

            for profile in suite.profiles:

                engine = EvaluationEngine(

                    provider_name=provider,

                    validator_names=[],

                    provider_file=self.provider_file,

                    profile_name=profile,

                    profile_file="profiles.yaml",

                )

                runner = BenchmarkRunner(
                    engine
                )

                benchmark = BenchmarkEngine()

                for dataset in suite.datasets:

                    results = runner.run(
                        dataset
                    )

                    summary = benchmark.summarize(

                        provider=provider,

                        model=engine._provider.config.model,

                        profile=profile,

                        results=results,

                    )

                    summaries.append(
                        summary
                    )

        return summaries