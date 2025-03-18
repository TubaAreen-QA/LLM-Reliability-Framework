from framework.contracts.model_result import (
    ModelResult,
)

from framework.engine.comparison_engine import (
    ComparisonEngine,
)


class FakeEvaluation:

    def __init__(
        self,
        score: float,
    ):

        self.overall_score = score


def test_compare_models():

    openai = ModelResult(

        provider="OpenAI",

        model="gpt-4.1",

        evaluation=FakeEvaluation(
            97
        ),

    )

    claude = ModelResult(

        provider="Claude",

        model="Claude Sonnet",

        evaluation=FakeEvaluation(
            94
        ),

    )

    result = ComparisonEngine().compare(

        [

            openai,

            claude,

        ]

    )

    assert result.winner == "OpenAI"

    assert result.score_difference == 3