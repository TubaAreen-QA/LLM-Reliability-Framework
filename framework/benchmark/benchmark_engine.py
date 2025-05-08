from __future__ import annotations

from statistics import mean

from framework.contracts.benchmark_result import (
    BenchmarkResult,
)


class BenchmarkEngine:

    """
    Aggregates benchmark execution results.
    """

    def summarize(
        self,
        results: list[
            BenchmarkResult
        ],
    ):

        overall_scores = [

            result.evaluation.overall_score

            for result

            in results

        ]

        execution_times = [

            result.evaluation.execution_time_ms

            for result

            in results

        ]

        passed = sum(

            result.evaluation.overall_passed

            for result

            in results

        )

        return {

            "samples": len(results),

            "passed": passed,

            "failed": len(results) - passed,

            "average_score": round(

                mean(overall_scores),

                2,

            ),

            "average_latency_ms": round(

                mean(execution_times),

                2,

            ),

            "pass_rate": round(

                (passed / len(results))

                * 100,

                2,

            )

            if results

            else 0,

        }