from __future__ import annotations

import json
from pathlib import Path

from framework.contracts.benchmark_summary import (
    BenchmarkSummary,
)


class BenchmarkJsonReporter:

    def generate(
        self,
        summary: BenchmarkSummary,
        output_directory: Path,
    ) -> Path:

        output_directory.mkdir(

            parents=True,

            exist_ok=True,

        )

        report = {

            "provider": summary.provider,

            "model": summary.model,

            "profile": summary.profile,

            "sample_count": summary.sample_count,

            "passed": summary.passed,

            "failed": summary.failed,

            "pass_rate": summary.pass_rate,

            "average_score": summary.average_score,

            "average_latency_ms": summary.average_latency_ms,

            "metadata": summary.metadata,

        }

        output = (

            output_directory

            / "benchmark_summary.json"

        )

        with output.open(

            "w",

            encoding="utf-8",

        ) as fp:

            json.dump(

                report,

                fp,

                indent=4,

                ensure_ascii=False,

            )

        return output