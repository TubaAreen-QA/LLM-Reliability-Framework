from __future__ import annotations

from abc import ABC
from abc import abstractmethod
from typing import Any


class BaseHttpClient(ABC):

    @abstractmethod
    def post(
        self,
        url: str,
        headers: dict[str, str],
        payload: dict[str, Any],
        timeout: int,
    ) -> dict[str, Any]:
        ...