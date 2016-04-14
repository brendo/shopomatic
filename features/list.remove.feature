Feature: Removes Items from Shopping List
  As a shopper
  I want to be able to removes items from my shopping list

  Background:
    Given I have a shopping list called "Test List"
    And I have added the followings items:
      | name   | quantity |
      | Apple  | 1        |
      | Peas   | 2        |

  Scenario: I remove an item
    Given I remove "Apple"
    Then I should not see "Apple" in the shopping list
    And I should see "Peas" in the shopping list
