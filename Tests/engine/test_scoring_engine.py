from framework.engine.scoring_engine import (
    ScoringEngine
)

from framework.models.validation_result import (
    ValidationResult
)


engine = ScoringEngine()


def test_average_score():

    results = [

        ValidationResult(
            validator="substring",
            status="PASS",
            score=100,
            actual="Paris",
            expected="Paris",
            message=""
        ),

        ValidationResult(
            validator="confidence",
            status="PASS",
            score=80,
            actual=0.80,
            expected=0.75,
            message=""
        )

    ]

    score = engine.calculate(results)

    assert score == 90