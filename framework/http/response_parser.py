from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from framework.contracts.provider_response import (
    ProviderResponse,
)


class ResponseParser(ABC):

    @abstractmethod
    def parse(
        self,
        response: dict,
    ) -> ProviderResponse:
        ...