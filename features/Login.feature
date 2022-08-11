# Created by Hp at 8/11/2022
Feature: This is to test iria app login functionality
  Background:
    Given Launch the browser
    When Open the iris URL

  Scenario: Test Login Funcionality
    Then We Login to the iris website
    Then Verify we are on the View Page
    Then Close the browser