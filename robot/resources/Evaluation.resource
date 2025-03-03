*** Settings ***

Library    robot.libraries.evaluation_library.EvaluationLibrary


*** Keywords ***

Evaluate Prompt

    [Arguments]

    ...    ${prompt}

    ...    ${expected}

    ${result}=

    Evaluate Prompt

    ${prompt}

    ${expected}

    RETURN

    ${result}


Overall Score Should Be

    [Arguments]

    ...    ${result}

    ...    ${score}

    Should Be Equal As Numbers

    ${result.overall_score}

    ${score}


Overall Status Should Be

    [Arguments]

    ...    ${result}

    ...    ${status}

    ${actual}=

    Evaluate

    ${result.overall_passed}

    Should Be Equal

    ${actual}

    ${status}


Validator Score Should Be

    [Arguments]

    ...    ${result}

    ...    ${validator}

    ...    ${score}

    FOR

    ${item}

    IN

    @{result.validation_results}

        IF

        '${item.validator}' == '${validator}'

            Should Be Equal As Numbers

            ${item.score}

            ${score}

        END

    END