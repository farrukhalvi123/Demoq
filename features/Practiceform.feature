# Created by Hp at 6/20/2022
Feature: Testing Practice Form

  Background:
    Given Launch the browser
    When Open the practice form

  Scenario: click submit and check field behavior
    Then Click on Submit Button
    Then Verify field validation

  Scenario Outline: Testing Required fields with correct and Incorrect data
    Then Fill out Mandatory fields "<firstname>" "<lastname>" "<Mobileph>" "<email>".
    Examples:
    |firstname |lastname | Mobileph | email|
    |Farrukh   | Alvi    |1234567897|fja@gmail.com|
    |abc123@#! | xyz123@#$|abc12343 |abcxyz       |

  Scenario: Fill out all Fields
    Then Fill out Mandatory fields



