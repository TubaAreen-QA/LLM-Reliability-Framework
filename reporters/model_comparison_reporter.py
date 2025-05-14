from __future__ import annotations

import json
from pathlib import Path

from framework.contracts.model_comparison import (
    ModelComparison,
)


class ModelComparisonReporter:

    def generate(
        self,
        comparison: ModelComparison,
        output_directory: Path,
    ) -> Path:

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        report = {

            "winner": comparison.winner,

            "ranking": comparison.ranking,

            "models": [

                {

                    "provider": summary.provider,

                    "model": summary.model,

                    "profile": summary.profile,

                    "average_score": summary.average_score,

                    "pass_rate": summary.pass_rate,

                    "average_latency_ms": summary.average_latency_ms,

                }

                for summary

                in comparison.summaries

            ],

        }

        output = (
            output_directory
            / "comparison.json"
        )

        with output.open(
            "w",
            encoding="utf-8",
        ) as fp:

            json.dump(
                report,
                fp,
                indent=4,
            )

        return output