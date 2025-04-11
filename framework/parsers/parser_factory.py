from __future__ import annotations

from framework.parsers.base_parser import (
    BaseParser,
)

from framework.parsers.claude_parser import (
    ClaudeParser,
)

from framework.parsers.openai_parser import (
    OpenAIParser,
)


class ParserFactory:

    _parsers: dict[
        str,
        type[BaseParser],
    ] = {

        "openai": OpenAIParser,

        "claude": ClaudeParser,

    }

    @classmethod
    def create(
        cls,
        provider: str,
    ) -> BaseParser:

        parser = cls._parsers.get(
            provider
        )

        if parser is None:

            raise ValueError(
                f"No parser registered for '{provider}'."
            )

        return parser()

    @classmethod
    def register(
        cls,
        provider: str,
        parser: type[BaseParser],
    ) -> None:

        cls._parsers[
            provider
        ] = parser