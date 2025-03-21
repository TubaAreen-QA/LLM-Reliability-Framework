from __future__ import annotations

from pathlib import Path

import os
import yaml

from framework.contracts.provider_config import (
    ProviderConfig,
)

from framework.exceptions.configuration_error import (
    ConfigurationError,
)


class ProviderLoader:

    def __init__(
        self,
        config_file: str | Path,
    ) -> None:

        self._file = Path(config_file)

    def load(
        self,
        provider_name: str,
    ) -> ProviderConfig:

        if not self._file.exists():

            raise ConfigurationError(
                f"{self._file} not found."
            )

        with self._file.open(
            encoding="utf-8"
        ) as fp:

            data = yaml.safe_load(fp)

        providers = data["providers"]

        if provider_name not in providers:

            raise ConfigurationError(
                f"Provider '{provider_name}' not configured."
            )

        config = providers[provider_name]

        api_key = config.get("api_key")

        if (
            isinstance(api_key, str)
            and api_key.startswith("${")
            and api_key.endswith("}")
        ):

            env_name = api_key[2:-1]

            api_key = os.getenv(env_name)

        return ProviderConfig(

            name=provider_name,

            model=config["model"],

            api_key=api_key,

            base_url=config.get("base_url"),

            timeout=config["timeout"],

            temperature=config["temperature"],

            max_tokens=config["max_tokens"],

            retries=config["retries"],

            enabled=config.get(
                "enabled",
                True,
            ),

            metadata={},
        )