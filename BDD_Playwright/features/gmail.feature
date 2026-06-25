Feature: Login into Gmail account
  Scenario: User should be able to login into Gmail account
    Given User is on Gmail login page
    When User enters valid username and password
    And User clicks on the Sign in button
    Then User should be logged in successfully