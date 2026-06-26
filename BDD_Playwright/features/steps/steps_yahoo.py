import logging
from behave import given, when, then

@given(u'User is on Yahoo login page')
def step_impl(context):
    logging.info("User is on Yahoo login page")

@when(u'User enters valid username "{username}" and password "{password}"')
def step_impl(context,username, password):
           logging.info(f'User enters valid username "{username}" and password "{password}"')

@when(u'User clicks on the Sign in button in the yahoo')
def step_impl(context):
    logging.info("User clicks on the Sign in button in the yahoo")

@then(u'User should be logged in successfully for yahoo page')
def step_impl(context):
    logging.info("User should be logged in successfully for yahoo page")