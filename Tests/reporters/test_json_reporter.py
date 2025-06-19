from pathlib import Path

from reporters.json_reporter import (
    JsonReporter,
)

from framework.contracts.evaluation_result import (
    EvaluationResult,
)


def test_json_report_created(tmp_path: Path):

    reporter = JsonReporter()

    result = EvaluationResult(

        provider_response=None,

        validation_results=[],

        overall_score=100,

        overall_passed=True,

        execution_time_ms=10,

        metadata={},

    )

    report = reporter.generate(

        result,

        tmp_path,

    )

    assert report.exists()