from behave import *




@then("Click on Simple Tab")
def step_impl(context):
    context.draganddrop.click_simple()



@then("Drag and Drop boxes")
def step_impl(context):
    context.draganddrop.dragacceptable()

@then("Click on Accept Tab")
def step_impl(context):
   context.draganddrop.click_accept()


@then("Test Acceptable Drag and Drop")
def step_impl(context):
    context.draganddrop.drag_and_drop()


@then("Test Non Acceptable Drag and Drop")
def step_impl(context):
    context.draganddrop.notacceptable()


@then("Click on Prevent Propogation tab")
def step_impl(context):
    context.draganddrop.click_prev_prop()
    context.draganddrop.Not_Greedy_Prevent_Propogation_Outter();


@then("Test Out Droppable Not Greedy")
def step_impl(context):
    context.draganddrop.Greedy_prevent_propogation_Outter()


@then("Test Inner Droppable Not Greedy")
def step_impl(context):
    context.draganddrop.Not_Greedy_Prevent_Propogation_Inner()


@then("Test Outter Droppable Greedy")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then Test Outter Droppable Greedy')


@then("Test Inner Droppable Greedy")
def step_impl(context):
    context.draganddrop.Greedy_prevent_propogation_Inner()

@then("Click on Revert Draggable Tab")
def step_impl(context):
    context.draganddrop.check_willrevert()


@then("Test out Will Revert")
def step_impl(context):
   context.draganddrop.click_revert_drag()