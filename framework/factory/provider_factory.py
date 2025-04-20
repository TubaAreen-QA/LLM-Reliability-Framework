from __future__ import annotations

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.registry.provider_registry import (
    ProviderRegistry,
)


class ProviderFactory:
    """
    Facade responsible for creating provider instances.

    Provider registration is delegated to ProviderRegistry.
    """

    _registry = ProviderRegistry()

    @classmethod
    def register(
        cls,
        provider,
    ) -> None:

        cls._registry.register(
            provider
        )

    @classmethod
    def unregister(
        cls,
        provider_name: str,
    ) -> None:

        cls._registry.unregister(
            provider_name
        )

    @classmethod
    def create(
        cls,
        config: ProviderConfig,
    ):

        return cls._registry.create(
            config
        )

    @classmethod
    def available(
        cls,
    ) -> list[str]:

        return cls._registry.list()