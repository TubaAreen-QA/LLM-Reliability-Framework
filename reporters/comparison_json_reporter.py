from __future__ import annotations

import json
from pathlib import Path

from framework.contracts.comparison_summary import (
    ComparisonSummary,
)


class ComparisonJsonReporter:

    def generate(

        self,

        summary: ComparisonSummary,

        output_directory: Path,

    ) -> Path:

        output_directory.mkdir(

            parents=True,

            exist_ok=True,

        )

        report = {

            "winner": summary.winner,

            "score_difference":
                summary.score_difference,

            "reason": summary.reason,

            "rankings": [

                {

                    "provider":
                        model.provider,

                    "model":
                        model.model,

                    "score":
                        model.evaluation.overall_score,

                }

                for model

                in summary.rankings

            ],

        }

        file = (

            output_directory

            / "comparison.json"

        )

        with file.open(

            "w",

            encoding="utf-8",

        ) as fp:

            json.dump(

                report,

                fp,

                indent=4,

                ensure_ascii=False,

            )

        return file