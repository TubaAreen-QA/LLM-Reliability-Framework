from __future__ import annotations

import json
from pathlib import Path

from framework.benchmark.base_dataset import (
    BaseDataset,
)


class JsonDataset(BaseDataset):

    def __init__(
        self,
        dataset_file: str,
    ):

        self.file = Path(dataset_file)

        with open(
            self.file,
            encoding="utf-8",
        ) as fp:

            self.data = json.load(fp)

    def __iter__(
        self,
    ):

        yield from self.data

    def size(
        self,
    ) -> int:

        return len(
            self.data
        )