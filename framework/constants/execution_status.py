from enum import StrEnum


class ExecutionStatus(StrEnum):

    PASS = "PASS"

    FAIL = "FAIL"

    ERROR = "ERROR"

    SKIPPED = "SKIPPED"

    WARNING = "WARNING"