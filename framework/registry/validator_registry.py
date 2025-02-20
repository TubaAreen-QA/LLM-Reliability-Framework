from __future__ import annotations

from validators.base_validator import BaseValidator


class ValidatorRegistry:

    def __init__(self) -> None:

        self._validators: dict[
            str,
            type[BaseValidator]
        ] = {}

    def register(
        self,
        validator: type[BaseValidator]
    ) -> None:

        instance = validator()

        self._validators[
            instance.name
        ] = validator

    def exists(
        self,
        validator_name: str
    ) -> bool:

        return (
            validator_name
            in self._validators
        )

    def get(
        self,
        validator_name: str
    ) -> type[BaseValidator]:

        return self._validators[
            validator_name
        ]

    def names(self) -> list[str]:

        return sorted(
            self._validators.keys()
        )