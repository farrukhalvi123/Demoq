from behave import *

use_step_matcher("re")


@then("test Iframes and getting text")
def step_impl(context):
    context.frames_handle.handle_iframe1()
    assert "This is a sample page" in context.driver.page_source
    print("first text found")
    context.driver.switch_to.default_content()
    context.frames_handle.handle_iframe2()
    assert "This is a sample page" in context.driver.page_source
    print("second text found")