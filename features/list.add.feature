Feature: Add Item to Shopping List
  As a shopper
  I want to add items to my Shopping List

  Background:
    Given I have a shopping list called "Test List"

  Scenario: Add item
    Given I add "Apple"
    Then I should see "Apple" in the shopping list
    And "Apple" should have a quantity of 1
    And "Apple" should have a state of "needed"

  Scenario: Add item with quantity
    Given I add "Eggs" with a quantity of 2
    Then I should see "Eggs" in the shopping list
    And "Eggs" should have a quantity of 2
    And "Eggs" should have a state of "needed"
