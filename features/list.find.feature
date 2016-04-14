Feature: Find Items on Shopping List
  As a shopper
  I want to be able to find items and update my shopping list

  Background:
    Given I have a shopping list called "Test List"
    And I have added the followings items:
      | name   | quantity |
      | Apple  | 1        |
      | Peas   | 2        |

  Scenario: I find an item
    Given I find "Apple"
    Then I should see "Apple" in the shopping list
    And "Apple" should have a quantity of 0
    And "Apple" should have a state of "acquired"

  Scenario: I find some of an item
    Given I find 1 of "Peas"
    Then I should see "Peas" in the shopping list
    And "Peas" should have a quantity of 1
    And "Peas" should have a state of "partial"
