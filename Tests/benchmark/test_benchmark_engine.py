from framework.benchmark.benchmark_engine import (
    BenchmarkEngine,
)

from framework.contracts.benchmark_result import (
    BenchmarkResult,
)

from framework.contracts.evaluation_result import (
    EvaluationResult,
)


def create_result(score, passed, latency):

    evaluation = EvaluationResult(

        provider_response=None,

        validation_results=[],

        overall_score=score,

        overall_passed=passed,

        execution_time_ms=latency,

        metadata={},

    )

    return BenchmarkResult(

        sample_id="sample",

        evaluation=evaluation,

    )


def test_benchmark_summary():

    engine = BenchmarkEngine()

    results = [

        create_result(90, True, 120),

        create_result(80, True, 100),

        create_result(60, False, 150),

    ]

    summary = engine.summarize(

        provider="fake",

        model="fake-model",

        profile="default",

        results=results,

    )

    assert summary.sample_count == 3

    assert summary.passed == 2

    assert summary.failed == 1

    assert summary.average_score == 76.67