from __future__ import annotations

from framework.contracts.prompt_template import (
    PromptTemplate,
)


class PromptRenderer:
    """
    Renders prompt templates using Python's
    built-in string formatting.
    """

    def render(
        self,
        template: PromptTemplate,
    ) -> str:

        return template.template.format(
            **template.variables
        )