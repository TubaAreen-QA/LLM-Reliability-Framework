from abc import ABC, abstractmethod

from framework.models.provider_request import provider_request
from framework.models.provider_response import provider_Response


class BaseProvider(ABC):

    @abstractmethod
    def ask(
        self,
        request: provider_request
    ) -> provider_Response:
        pass