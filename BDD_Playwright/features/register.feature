Feature: Register an account in Rediff Mail

  @register
  Scenario: User should be able to register an account in Rediff Mail
    Given User is on Rediff Mail registration page
    When User enters valid details for registration
    |username|password|email|phone|
    |testuser|testpass|test@example.com|1234567890|
    And User clicks on the Register button
    Then User should be registered successfully