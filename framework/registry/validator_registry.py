from validators.Substring_Validator import SubstringValidator


from framework.factory.validator_factory import (
    ValidatorFactory
)


class ValidatorRegistry:

    def __init__(self, validator_names):

        self.validator_names = validator_names

    def get_validators(self):

        validators = []

        for validator in self.validator_names:

            validators.append(

                ValidatorFactory.create(
                    validator
                )

            )

        return validators