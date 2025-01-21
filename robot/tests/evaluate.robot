*** Settings ***

Library    ../../libraries/evaluation_library.py

*** Test Cases ***

Evaluate Capital

    ${result}=    Run Evaluation
    ...    What is the capital of France?
    ...    Paris

    Log    ${result.overall_score}

    Should Be Equal As Numbers
    ...    ${result.overall_score}
    ...    100