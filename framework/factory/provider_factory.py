from __future__ import annotations

from framework.exceptions.provider_error import (
    ProviderError
)

from framework.registry.provider_registry import (
    ProviderRegistry
)

from providers.fake_provider import FakeProvider


class ProviderFactory:

    _registry = ProviderRegistry()

    _initialized = False

    @classmethod
    def initialize(cls) -> None:

        if cls._initialized:
            return

        cls._registry.register(
            FakeProvider
        )

        cls._initialized = True

    @classmethod
    def create(
        cls,
        provider_name: str
    ):

        cls.initialize()

        if not cls._registry.exists(
            provider_name
        ):

            raise ProviderError(
                f"Unknown provider: {provider_name}"
            )

        provider = cls._registry.get(
            provider_name
        )

        return provider()

    @classmethod
    def available(
        cls
    ) -> list[str]:

        cls.initialize()

        return cls._registry.names()