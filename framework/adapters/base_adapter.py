from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from framework.contracts.normalized_response import (
    NormalizedResponse,
)


class BaseAdapter(ABC):

    @abstractmethod
    def normalize(
        self,
        raw_response: dict,
    ) -> NormalizedResponse:
        ... 