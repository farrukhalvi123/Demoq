from behave import *
from selenium.webdriver.chrome import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
use_step_matcher("re")


@given("I open Chrome")
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())


@when("I am on Google")
def step_impl(context):
    print("i am on google")


@then("verify field")
def step_impl(context):
    print("click on search field")