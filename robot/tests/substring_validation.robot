*** Settings ***

Resource

../resources/Evaluation.resource


*** Test Cases ***

Substring Validation

    ${result}=

    Evaluate Prompt

    What is the capital of France?

    Paris

    Overall Score Should Be

    ${result}

    100

    Overall Status Should Be

    ${result}

    ${TRUE}

    Validator Score Should Be

    ${result}

    substring

    100