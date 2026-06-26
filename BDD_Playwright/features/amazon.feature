Feature: Add an item to cart from amazon website
  Scenario Outline: Add an item to cart from amazon website
    Given User is on Amazon department page
    When User select department as "<department>"
    And User selects the first item from the search results
    And User clicks on the "Add to Cart" button
    Then The item should be added to the cart successfully
    Examples:
      | department |
      | Movie & TV |
      | Books       |
      | Video Games |