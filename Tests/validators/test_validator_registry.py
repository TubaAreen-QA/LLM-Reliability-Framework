from framework.registry.validator_registry import (
    ValidatorRegistry
)


def test_registry_returns_validator():

    registry = ValidatorRegistry(
        ["substring"]
    )

    validators = registry.get_validators()

    assert len(validators) == 1

    assert validators[0].name == "substring"