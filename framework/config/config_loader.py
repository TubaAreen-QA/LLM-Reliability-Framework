from __future__ import annotations

from pathlib import Path

import yaml

from framework.exceptions.configuration_error import (
    ConfigurationError,
)


class ConfigLoader:

    def __init__(
        self,
        config_path: str | Path
    ) -> None:

        self._config_path = Path(config_path)

    def load(self) -> dict:

        if not self._config_path.exists():

            raise ConfigurationError(
                f"Configuration file not found: "
                f"{self._config_path}"
            )

        with self._config_path.open(
            encoding="utf-8"
        ) as fp:

            config = yaml.safe_load(fp)

        if config is None:

            raise ConfigurationError(
                "Configuration file is empty."
            )

        return config