from __future__ import annotations

from typing import Type

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.exceptions.provider_error import (
    ProviderError,
)

from providers.base_provider import (
    BaseProvider,
)


class ProviderRegistry:
    """
    Central registry for all provider plugins.

    Providers register themselves during framework startup.

    The Evaluation Engine never imports providers directly.
    """

    def __init__(self) -> None:

        self._providers: dict[
            str,
            Type[BaseProvider],
        ] = {}

    def register(
        self,
        provider: Type[BaseProvider],
    ) -> None:

        provider_name = provider.PROVIDER_NAME

        if provider_name in self._providers:

            raise ProviderError(
                f"Provider '{provider_name}' is already registered."
            )

        self._providers[
            provider_name
        ] = provider

    def unregister(
        self,
        provider_name: str,
    ) -> None:

        self._providers.pop(
            provider_name,
            None,
        )

    def exists(
        self,
        provider_name: str,
    ) -> bool:

        return (
            provider_name
            in self._providers
        )

    def create(
        self,
        config: ProviderConfig,
    ) -> BaseProvider:

        provider = self._providers.get(
            config.name
        )

        if provider is None:

            raise ProviderError(

                f"Provider '{config.name}' "
                f"is not registered."

            )

        return provider(config)

    def list(self) -> list[str]:

        return sorted(
            self._providers.keys()
        )

    def clear(self) -> None:

        self._providers.clear()