from behave import *




@then("Check the button is enabled after 5 seconds")
def step_impl(context):
    context.dynamic_prop.check_button_enabled()


@then("Testing Button Changes Color")
def step_impl(context):
    context.dynamic_prop.check_color_change()


@then("Testing visibility of the button")
def step_impl(context):
    context.dynamic_prop.check_button_visibility()


@then("testing text validation from dynamic ID")
def step_impl(context):
    context.dynamic_prop.verify_text_from_dynamic_ID()