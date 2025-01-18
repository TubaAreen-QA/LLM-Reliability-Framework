def validate(response, expected):

    results = []

    result = substring_validator(
        response.answer,
        expected
    )

    results.append(result)

    return results