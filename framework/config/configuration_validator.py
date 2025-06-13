from __future__ import annotations

from pathlib import Path


class ConfigurationValidator:

    REQUIRED_FILES = [

        "config/providers.yaml",

        "config/profiles.yaml",

        "config/pipeline.yaml",

    ]

    @classmethod
    def validate(cls):

        missing = [

            file

            for file

            in cls.REQUIRED_FILES

            if not Path(file).exists()

        ]

        if missing:

            raise FileNotFoundError(

                "Missing configuration files:\n"

                + "\n".join(missing)

            )