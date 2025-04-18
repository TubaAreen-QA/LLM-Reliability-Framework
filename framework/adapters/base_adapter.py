from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from framework.contracts.provider_request import (
    ProviderRequest,
)

from framework.contracts.provider_response import (
    ProviderResponse,
)


class BaseAdapter(ABC):

    @abstractmethod
    def adapt(
        self,
        request: ProviderRequest,
        raw_response: dict,
        provider: str,
        model: str,
        latency_ms: float,
    ) -> ProviderResponse:
        ...