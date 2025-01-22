from abc import ABC, abstractmethod

class BaseValidator(ABC):

    @abstractmethod
    def validate(self, response, expected):
        """
        Validate a provider response.
        Must return ValidationResult.
        """
        pass