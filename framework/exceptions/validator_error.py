from framework.exceptions.evaluation_error import (
    EvaluationError
)


class ValidatorError(EvaluationError):
    """
    Raised when validator execution fails.
    """

    def __init__(
        self,
        message: str
    ) -> None:

        super().__init__(message)