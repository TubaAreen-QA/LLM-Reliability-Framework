from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path

from framework.contracts.evaluation_result import (
    EvaluationResult,
)


class BaseReporter(ABC):

    @property
    @abstractmethod
    def name(self) -> str:
        ...

    @abstractmethod
    def generate(
        self,
        result: EvaluationResult,
        output_directory: Path,
    ) -> Path:
        ...