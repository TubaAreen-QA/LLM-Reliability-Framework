from framework.contracts.validation_result import (
    ValidationResult,
)

from framework.scoring.profile_loader import (
    ProfileLoader,
)

from framework.scoring.weighted_score import (
    WeightedScore,
)


def test_weighted_score():

    profile = ProfileLoader(

        "config/scoring_profiles.yaml"

    ).load(

        "factual"

    )

    results = [

        ValidationResult(

            validator="correctness",

            passed=True,

            score=100,

            threshold=90,

            actual=100,

            expected=90,

            execution_time_ms=10,

        ),

        ValidationResult(

            validator="confidence",

            passed=True,

            score=100,

            threshold=0.8,

            actual=0.95,

            expected=0.8,

            execution_time_ms=10,

        ),

        ValidationResult(

            validator="latency",

            passed=False,

            score=50,

            threshold=2000,

            actual=3000,

            expected=2000,

            execution_time_ms=10,

        ),

        ValidationResult(

            validator="hallucination",

            passed=True,

            score=100,

            threshold=0,

            actual=0,

            expected=0,

            execution_time_ms=10,

        ),

        ValidationResult(

            validator="toxicity",

            passed=True,

            score=100,

            threshold=0,

            actual=0,

            expected=0,

            execution_time_ms=10,

        ),

    ]

    score = WeightedScore().calculate(

        profile,

        results,

    )

    assert score.score == 97.5

    assert score.passed