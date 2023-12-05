Feature: Division operation

  Scenario: Division by number
    Given dividend is 10
    When divide by 2
    Then result is 5
    But if divide by 0
    Then result is NaN
