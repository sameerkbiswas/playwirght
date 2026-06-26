Feature: Login into yahoo account
  Scenario Outline: User should be able to login into yahoo account
    Given User is on Yahoo login page
    When User enters valid username "<username>" and password "<password>"
    And User clicks on the Sign in button in the yahoo
    Then User should be logged in successfully for yahoo page
    Examples:
      | username | password |
      | Name1    | Password1 |
      | Name2    | Password2 |
      | Name3    | Password3 |
      | Name4    | Password4 |
      | Name5    | Password5 |