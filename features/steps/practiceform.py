import time

from behave import *

@then("Click on Submit Button")
def step_impl(context):
    context.practice.click_submit()


@then("Verify field validation")
def step_impl(context):
    context.practice.identify_color()


@then("Fill Out Practice form")
def step_impl(context):
    context.practice.enter_firstname("fja")
    context.practice.enter_firstname("abc123@#$")
    context.practice.enter_lastname("xyz321)(*")
    context.practice.enter_email("farrukh@gmail.com")
    context.practice.select_gender()
    context.practice.enter_mobile("1234567891")
    context.practice.select_date()
    context.practice.enter_subject("English")
    context.practice.click_submit()
    context.practice.identify_phone_color()
    time.sleep(5)


@then("Fill out Mandatory fields")
def step_impl(context):
    context.practice.select_date()
    context.practice.enter_subject("English")
    context.practice.enter_mobile("1234567891")
    context.practice.select_hobbies()
    context.practice.enter_picture()
    context.practice.enter_currentaddress("abc 14 !@#!@ test address")
    context.practice.click_state()
    context.practice.click_city()
    # self.test_partial_form_filled()


@then('Fill out Mandatory fields "{firstname}" "{lastname}" "{Mobileph}" "{email}".')
def step_impl(context, firstname, lastname, Mobileph, email):
    context.practice.enter_firstname(firstname)
    context.practice.enter_lastname(lastname)
    context.practice.select_gender()
    context.practice.enter_mobile(Mobileph)
    context.practice.enter_email(email)
    context.practice.click_submit()
    context.practice.identify_color()
