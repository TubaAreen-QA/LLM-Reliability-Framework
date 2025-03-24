from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)


class BaseProvider(ABC):

    def __init__(
        self,
        config: ProviderConfig,
    ) -> None:

        self.config = config

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def ask(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:
        ...

    @abstractmethod
    def health_check(self) -> bool:
        ...

    @abstractmethod
    def supported_models(
        self,
    ) -> list[str]:
        ...