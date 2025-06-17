from framework.contracts.validation_result import (
    ValidationResult,
)

from framework.engine.scoring_engine import (
    ScoringEngine,
)


def test_scoring_engine_returns_weighted_score():

    engine = ScoringEngine(

        "default",

        "config/profiles.yaml",

    )

    results = [

        ValidationResult(

            validator="exact_match",

            status="PASS",

            score=100,

            expected="Hello",

            actual="Hello",

            message="",

        )

    ]

    score = engine.calculate(

        results,

    )

    assert score.score == 100

    assert score.passed is True