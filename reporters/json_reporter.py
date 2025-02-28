from __future__ import annotations

import json
from pathlib import Path

from framework.contracts.evaluation_result import (
    EvaluationResult,
)

from reporters.base_reporter import BaseReporter


class JsonReporter(BaseReporter):

    @property
    def name(self) -> str:
        return "json"

    def generate(
        self,
        result: EvaluationResult,
        output_directory: Path,
    ) -> Path:

        output_directory.mkdir(
            parents=True,
            exist_ok=True,
        )

        report = {

            "provider": result.provider_response.provider,

            "model": result.provider_response.model,

            "prompt": result.provider_response.prompt,

            "answer": result.provider_response.answer,

            "overall_score": result.overall_score,

            "overall_passed": result.overall_passed,

            "execution_time_ms": result.execution_time_ms,

            "validators": [

                {

                    "validator": validation.validator,

                    "passed": validation.passed,

                    "score": validation.score,

                    "threshold": validation.threshold,

                    "actual": validation.actual,

                    "expected": validation.expected,

                    "execution_time_ms":
                        validation.execution_time_ms,

                    "message":
                        validation.message,

                }

                for validation

                in result.validation_results

            ],

        }

        output = (

            output_directory

            / "evaluation.json"

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