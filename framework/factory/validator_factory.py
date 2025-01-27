from validators.substring_validator import (
    SubstringValidator
)


class ValidatorFactory:

    VALIDATORS = {
        "substring": SubstringValidator
    }

    @classmethod
    def create(cls, validator_name):

        validator = cls.VALIDATORS.get(
            validator_name
        )

        if validator is None:
            raise ValueError(
                f"Unknown validator: {validator_name}"
            )

        return validator()