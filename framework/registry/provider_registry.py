from __future__ import annotations

from providers.base_provider import BaseProvider


class ProviderRegistry:

    def __init__(self) -> None:

        self._providers: dict[
            str,
            type[BaseProvider]
        ] = {}

    def register(
        self,
        provider: type[BaseProvider]
    ) -> None:

        instance = provider()

        self._providers[
            instance.name
        ] = provider

    def exists(
        self,
        name: str
    ) -> bool:

        return name in self._providers

    def get(
        self,
        name: str
    ) -> type[BaseProvider]:

        return self._providers[name]

    def names(self) -> list[str]:

        return sorted(
            self._providers.keys()
        )