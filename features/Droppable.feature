
Feature: Droppable Page Test Cases
  Background:
    Given Launch the browser
    When Open Drag and Drop Page

  Scenario: Testing Simple Drag and Drop Function
    Then Click on Simple Tab
    Then Drag and Drop boxes

  Scenario: Testing Acceptable drag and drop
    Then Click on Accept Tab
    Then Test Acceptable Drag and Drop

  Scenario: Testing Not Acceptable drag and drop
    Then Click on Accept Tab
    Then Test Non Acceptable Drag and Drop

  Scenario: Testing Prevent Progogation Outer drop
    Then Click on Prevent Propogation tab
    Then Test Out Droppable Not Greedy
    Then Test Inner Droppable Not Greedy
    Then Test Outter Droppable Greedy
    Then Test Inner Droppable Greedy

  Scenario: Testing Revert Droppables
    Then Click on Revert Draggable Tab
    Then Test out Will Revert