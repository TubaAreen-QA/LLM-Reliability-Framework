from abc import ABC, abstractmethod

from framework.models.provider_response import provider_Response
from framework.models.validation_result import validation_Result

class BaseValidator(ABC):

    name = "base"

    @abstractmethod
    def validate(
        self,
        response: provider_Response,
        expected
    ) -> validation_Result:
        pass