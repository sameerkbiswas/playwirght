Feature: Login into Gmail account
  Scenario: User should be able to login into Gmail account
    Given User is on Gmail login page
    When User enters valid gmail username and password
    And User clicks on the Sign in button
    Then User should be logged in successfully

  @run
  Scenario: User should be able to login into Gmail account
    Given User is on Gmail login page
    When User enters valid gmail username1 and password1
    And User clicks on the Sign in button
    Then User should be logged in successfully
  @smoke
  Scenario: User should be able to login into Gmail account
    Given User is on Gmail login page
    When User enters valid gmail username2 and password2
    And User clicks on the Sign in button
    Then User should be logged in successfully
  @run @smoke
  Scenario: User should be able to login into Gmail account
    Given User is on Gmail login page
    When User enters valid gmail username3 and password3
    And User clicks on the Sign in button
    Then User should be logged in successfully