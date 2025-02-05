from framework.exceptions.evaluation_error import (
    EvaluationError
)


class ProviderError(EvaluationError):
    """
    Raised when a provider fails to execute.
    """

    def __init__(
        self,
        message: str
    ) -> None:

        super().__init__(message)