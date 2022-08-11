import time

from behave import *



@then("We Login to the iris website")
def step_impl(context):
    time.sleep(5)
    context.loginpage.enter_email("ngushashaguy@chevron.com")
    context.loginpage.enter_password("Benue83!!")
    context.loginpage.click_login()
    time.sleep(5)


@then("Verify we are on the View Page")
def step_impl(context):
   assert "View" in context.driver.page_source()