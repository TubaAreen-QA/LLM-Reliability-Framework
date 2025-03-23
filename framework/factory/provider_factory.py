from __future__ import annotations

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.exceptions.provider_error import (
    ProviderError,
)

from providers.base_provider import (
    BaseProvider,
)

from providers.fake_provider import (
    FakeProvider,
)


class ProviderFactory:

    _providers: dict[
        str,
        type[BaseProvider],
    ] = {}

    @classmethod
    def register(
        cls,
        provider: type[
            BaseProvider
        ],
    ) -> None:

        instance = provider()

        cls._providers[
            instance.name
        ] = provider

    @classmethod
    def create(
        cls,
        config: ProviderConfig,
    ) -> BaseProvider:

        provider = cls._providers.get(
            config.name
        )

        if provider is None:

            raise ProviderError(
                f"Provider '{config.name}' is not registered."
            )

        return provider(config)


ProviderFactory.register(
    FakeProvider
)