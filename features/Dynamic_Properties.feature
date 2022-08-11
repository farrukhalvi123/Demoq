# Created by Hp at 6/21/2022
Feature: Testing Dynamic Properties
  Background:
    Given Launch the browser
    When Open Dynamic Properties Page

  Scenario: Testing Button Enabled delay
    Then Check the button is enabled after 5 seconds

  Scenario: Testing if the button changes color on click
    Then Testing Button Changes Color

  Scenario: Test the visibility of the button after delay
    Then Testing visibility of the button

  Scenario: Get text from a dynamic ID
    Then testing text validation from dynamic ID

