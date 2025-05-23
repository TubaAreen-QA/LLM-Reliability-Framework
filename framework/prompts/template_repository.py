from __future__ import annotations

import yaml

from framework.contracts.prompt_template import (
    PromptTemplate,
)


class PromptTemplateRepository:

    def __init__(
        self,
        template_file: str,
    ) -> None:

        with open(
            template_file,
            encoding="utf-8",
        ) as fp:

            self._templates = yaml.safe_load(fp)

    def load(
        self,
        name: str,
        variables: dict,
    ) -> PromptTemplate:

        if name not in self._templates:

            raise ValueError(
                f"Unknown template '{name}'."
            )

        return PromptTemplate(

            name=name,

            template=self._templates[name],

            variables=variables,

        )