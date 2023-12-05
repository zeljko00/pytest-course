Feature: Division operation - parametrized

  Scenario Outline: Division by number
    Given dividend is <a>
    When divide by <b>
    Then result is <r>

  Examples:
    | a  | b  | r  |
    | 15 | 3  | 5  |
    | 21 | 7  | 3  |
    | 50 | 10 | 6  |
