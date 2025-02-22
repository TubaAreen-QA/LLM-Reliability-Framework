from __future__ import annotations

from framework.exceptions.validator_error import (
    ValidatorError
)

from framework.registry.validator_registry import (
    ValidatorRegistry
)

from validators.Substring_Validator import (
    SubstringValidator
)


class ValidatorFactory:

    _registry = ValidatorRegistry()

    _initialized = False

    @classmethod
    def initialize(cls) -> None:

        if cls._initialized:
            return

        cls._registry.register(
            SubstringValidator
        )

        cls._initialized = True

    @classmethod
    def create(
        cls,
        validator_name: str
    ):

        cls.initialize()

        if not cls._registry.exists(
            validator_name
        ):

            raise ValidatorError(
                f"Unknown validator: {validator_name}"
            )

        validator = cls._registry.get(
            validator_name
        )

        return validator()

    @classmethod
    def available(
        cls
    ) -> list[str]:

        cls.initialize()

        return cls._registry.names()