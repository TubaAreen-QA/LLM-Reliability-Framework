from __future__ import annotations

from pathlib import Path

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)


class BenchmarkHtmlReporter:
    """
    Generates a simple HTML report for a benchmark summary.
    """

    def generate(
        self,
        summary: BenchmarkSummary,
        output_directory: Path,
    ) -> Path:

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>EvalForge Benchmark Report</title>
</head>
<body>

<h1>Benchmark Summary</h1>

<table border="1" cellpadding="6">

<tr><th>Provider</th><td>{summary.provider}</td></tr>

<tr><th>Model</th><td>{summary.model}</td></tr>

<tr><th>Profile</th><td>{summary.profile}</td></tr>

<tr><th>Samples</th><td>{summary.sample_count}</td></tr>

<tr><th>Passed</th><td>{summary.passed}</td></tr>

<tr><th>Failed</th><td>{summary.failed}</td></tr>

<tr><th>Pass Rate</th><td>{summary.pass_rate}%</td></tr>

<tr><th>Average Score</th><td>{summary.average_score}</td></tr>

<tr><th>Average Latency</th><td>{summary.average_latency_ms} ms</td></tr>

</table>

</body>
</html>
"""

        report = output_directory / "benchmark.html"

        report.write_text(
            html,
            encoding="utf-8",
        )

        return report