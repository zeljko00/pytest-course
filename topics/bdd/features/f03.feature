Feature: Multiple division operation

  Scenario: Division by number
    Given dividend is 10
    When divide by 2
    And divide by 5
    Then result is 1
