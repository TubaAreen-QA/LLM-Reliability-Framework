from enum import StrEnum


class ValidatorName(StrEnum):

    SUBSTRING = "substring"

    CONFIDENCE = "confidence"

    LATENCY = "latency"

    REGEX = "regex"

    SEMANTIC = "semantic"

    JSON_SCHEMA = "json_schema"

    FACTUAL = "factual"

    TRANSLATION = "translation"

    CODE = "code"

    CREATIVE = "creative"

    SUMMARIZATION = "summarization"

    TOXICITY = "toxicity"

    HALLUCINATION = "hallucination"

    LLM_JUDGE = "llm_judge"
    