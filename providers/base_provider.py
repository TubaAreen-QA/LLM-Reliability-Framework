from abc import ABC, abstractmethod

from framework.models.provider_request import ProviderRequest
from framework.models.provider_response import ProviderResponse


class BaseProvider(ABC):

    @abstractmethod
    def ask(
        self,
        request: ProviderRequest
    ) -> ProviderResponse:
        pass