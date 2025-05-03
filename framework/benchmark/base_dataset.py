from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from framework.contracts.provider_request import (
    ProviderRequest,
)


class BaseDataset(ABC):
    """
    Base abstraction for benchmark datasets.

    A dataset supplies evaluation samples
    independent of its storage format.
    """

    @abstractmethod
    def __iter__(
        self,
    ):
        ...

    @abstractmethod
    def size(
        self,
    ) -> int:
        ...