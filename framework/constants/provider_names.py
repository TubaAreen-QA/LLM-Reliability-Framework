from enum import StrEnum


class ProviderName(StrEnum):

    FAKE = "fake"

    OPENAI = "openai"

    CLAUDE = "claude"

    GEMINI = "gemini"

    OLLAMA = "ollama"

    AZURE_OPENAI = "azure-openai"

    BEDROCK = "bedrock"