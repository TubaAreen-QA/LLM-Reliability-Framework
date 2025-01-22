from validators.Substring_Validator import SubstringValidator


class ValidatorRegistry:

    def __init__(self):

        self.validators = [
            SubstringValidator()
        ]

    def get_validators(self):

        return self.validators