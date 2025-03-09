from __future__ import annotations

from pathlib import Path

import yaml

from framework.scoring.weighted_profile import (
    ValidatorWeight,
    WeightedProfile,
)


class ProfileLoader:

    def __init__(
        self,
        file: str | Path,
    ) -> None:

        self._file = Path(file)

    def load(
        self,
        profile_name: str,
    ) -> WeightedProfile:

        with self._file.open(
            encoding="utf-8"
        ) as fp:

            data = yaml.safe_load(fp)

        profile = data["profiles"][profile_name]

        validators = {}

        for validator, config in profile.items():

            validators[validator] = ValidatorWeight(

                validator=validator,

                weight=config["weight"],

                threshold=config.get(
                    "threshold"
                ),
            )

        return WeightedProfile(

            name=profile_name,

            validators=validators,
        )