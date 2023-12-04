Feature: Division operation

  Scenario: Money withdrawal
    Given dividend is 10
    When divide by 2
    Then result is 5
    But if divisor is 0
    Then result is Nan
