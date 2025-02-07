from framework.exceptions.evaluation_error import (
    EvaluationError
)


class ConfigurationError(EvaluationError):
    """
    Raised when framework configuration is invalid.
    """

    def __init__(
        self,
        message: str
    ) -> None:

        super().__init__(message)