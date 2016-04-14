Feature: Create a Shopping List
  As a shopper
  I want to create a Shopping List

  Scenario: I create a list
    Given I have a shopping list called "My List"
    Then it should have 0 items
    And it should have a state of "todo"