Feature: Add Item to Shopping List
  As a shopper
  I want to add items to my Shopping List

  Scenario: Add item to list
    Given I have a shopping list called "Test List"
    When I add a new item "Apples"
    Then I should see "Apples" in the shopping list
    And "Apples" should have a quantity of 1
    And "Apples" should have a state of "needed"