from __future__ import annotations

from statistics import mean

from framework.contracts.benchmark_result import (
    BenchmarkResult,
)

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)


class BenchmarkEngine:

    """
    Produces aggregate benchmark statistics.
    """

    def summarize(
        self,
        provider: str,
        model: str,
        profile: str,
        results: list[BenchmarkResult],
    ) -> BenchmarkSummary:

        if not results:

            return BenchmarkSummary(

                provider=provider,

                model=model,

                profile=profile,

                sample_count=0,

                passed=0,

                failed=0,

                pass_rate=0,

                average_score=0,

                average_latency_ms=0,

                metadata={},

            )

        scores = [

            r.evaluation.overall_score

            for r

            in results

        ]

        latencies = [

            r.evaluation.execution_time_ms

            for r

            in results

        ]

        passed = sum(

            r.evaluation.overall_passed

            for r

            in results

        )

        failed = len(results) - passed

        return BenchmarkSummary(

            provider=provider,

            model=model,

            profile=profile,

            sample_count=len(results),

            passed=passed,

            failed=failed,

            pass_rate=round(

                passed

                * 100

                / len(results),

                2,

            ),

            average_score=round(

                mean(scores),

                2,

            ),

            average_latency_ms=round(

                mean(latencies),

                2,

            ),

            metadata={},

        )