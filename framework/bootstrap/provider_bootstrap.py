from __future__ import annotations

from framework.factory.provider_factory import (
    ProviderFactory,
)

from providers.fake_provider import (
    FakeProvider,
)

from providers.openai_provider import (
    OpenAIProvider,
)

from providers.claude_provider import (
    ClaudeProvider,
)

from providers.gemini_provider import (
    GeminiProvider,
)


class ProviderBootstrap:
    """
    Registers all built-in providers.

    Called once during application startup.
    """

    _initialized = False

    @classmethod
    def initialize(cls) -> None:

        if cls._initialized:
            return

        ProviderFactory.register(
            FakeProvider
        )

        ProviderFactory.register(
            OpenAIProvider
        )

        ProviderFactory.register(
            ClaudeProvider
        )

        ProviderFactory.register(
            GeminiProvider
        )

        cls._initialized = True