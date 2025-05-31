from __future__ import annotations

import yaml


class PipelineLoader:

    def __init__(
        self,
        filename: str,
    ):

        self.filename = filename

    def load(
        self,
    ) -> list[str]:

        with open(

            self.filename,

            encoding="utf-8",

        ) as fp:

            configuration = yaml.safe_load(fp)

        return configuration[
            "pipeline"
        ]