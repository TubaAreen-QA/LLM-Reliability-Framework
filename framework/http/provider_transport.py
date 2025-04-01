from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class ProviderTransport(ABC):

    @abstractmethod
    def execute(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        ...