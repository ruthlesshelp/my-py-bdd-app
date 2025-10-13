Feature: Class1 Data Processing
    As a system user
    I want to process integer inputs through Class1
    So that I can obtain structured output arrays

    Background:
        Given I have a Class1 object

    Scenario: Handle invalid negative input
        When I call Function1 with value -1
        And I call Function2
        Then a ValueError should be raised
        And the message should contain "Input value is not valid"

    Scenario: Process input zero
        When I call Function1 with value 0
        And I call Function2
        Then the output array should contain:
            | Coefficient | Value |
            | 1           | 0     |
            | 5           | 0     |
            | 10          | 0     |
            | 25          | 0     |
