from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from framework.contracts.execution_context import (
    ExecutionContext,
)


class PipelineStep(ABC):

    @abstractmethod
    def execute(
        self,
        context: ExecutionContext,
    ) -> ExecutionContext:
        ...