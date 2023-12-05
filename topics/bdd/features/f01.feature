@featureclass1
Feature: Bank Transaction

  Background: Setup actions
    Given start of background actions
    And end of background actions
  @scenarioclass1
  Scenario: Money withdrawal
    Given account balance is 100$
    When account owner withdraws 70$
    Then account balance is 30$

  Scenario: Set manipulation
    Given set has 3 elements
    When remove random element
    Then set has 2 elements now
