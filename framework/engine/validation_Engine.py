from validators.substring_validator import SubstringValidator


class ValidationEngine:

    def __init__(self):

        self.substring = SubstringValidator()

    def validate(self, response, expected):

        results = []

        results.append(

            self.substring.validate(

                response.answer,

                expected

            )

        )

        return results