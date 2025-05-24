from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class PipelineStep(ABC):
    """
    Base class for all pipeline steps.
    """

    @abstractmethod
    def execute(
        self,
        context: dict[str, Any],
    ) -> dict[str, Any]:
        ...