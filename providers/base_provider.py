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

    PROVIDER_NAME = ""

    def __init__(
        self,
        config: ProviderConfig,
    ):

        self.config = config

    @property
    def name(
        self,
    ) -> str:

        return self.PROVIDER_NAME

    @abstractmethod
    def ask(
        self,
        request: ProviderRequest,
    ) -> ProviderResponse:
        ...

    @abstractmethod
    def health_check(
        self,
    ) -> bool:
        ...

    @abstractmethod
    def supported_models(
        self,
    ) -> list[str]:
        ...