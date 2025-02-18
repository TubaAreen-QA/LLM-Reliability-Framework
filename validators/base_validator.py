from abc import ABC, abstractmethod
from __future__ import annotations

from framework.contracts.provider_request import ProviderRequest
from framework.contracts.provider_response import ProviderResponse
from framework.contracts.validation_result import ValidationResult


class BaseValidator(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @property
    def weight(self) -> float:
        return 1.0

    @property
    def threshold(self) -> float:
        return 100.0

    @abstractmethod
    def validate(
        self,
        request: ProviderRequest,
        response: ProviderResponse,
        expected
    ) -> ValidationResult:
        ...