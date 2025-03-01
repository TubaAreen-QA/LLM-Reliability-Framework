from __future__ import annotations

from framework.exceptions.configuration_error import (
    ConfigurationError,
)

from reporters.base_reporter import (
    BaseReporter,
)

from reporters.json_reporter import (
    JsonReporter,
)


class ReporterFactory:

    _reporters: dict[
        str,
        type[BaseReporter],
    ] = {

        "json": JsonReporter,

    }

    @classmethod
    def create(
        cls,
        reporter_name: str,
    ) -> BaseReporter:

        reporter = cls._reporters.get(
            reporter_name
        )

        if reporter is None:

            raise ConfigurationError(

                f"Reporter "

                f"'{reporter_name}' "

                f"is not registered."

            )

        return reporter()

    @classmethod
    def register(
        cls,
        reporter: type[
            BaseReporter
        ],
    ) -> None:

        instance = reporter()

        cls._reporters[
            instance.name
        ] = reporter

    @classmethod
    def available(
        cls,
    ) -> list[str]:

        return sorted(

            cls._reporters.keys()

        )