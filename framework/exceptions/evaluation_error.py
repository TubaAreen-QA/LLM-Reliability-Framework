class EvaluationError(Exception):
    """
    Base exception for all framework evaluation errors.
    """

    def __init__(
        self,
        message: str
    ) -> None:

        super().__init__(message)