from abc import ABC, abstractmethod

from framework.models.provider_request import provider_request
from framework.models.provider_response import provider_Response

from __future__ import annotations


class BaseProvider(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def ask(
        self,
        request: provider_request
    ) -> provider_Response:
        ...

    @abstractmethod
    def health_check(self) -> bool:
        ...

    @abstractmethod
    def supported_models(self) -> list[str]:
        ...