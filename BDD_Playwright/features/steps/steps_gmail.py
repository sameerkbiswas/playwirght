import logging
from behave import given, when, then

@given(u'User is on Gmail login page')
def step_impl(context):
    logging.info("User is on Gmail login page")

@when(u'User enters valid username and password')
def step_impl(context):
    logging.info("User enters valid username and password")

@when(u'User clicks on the Sign in button')
def step_impl(context):
    logging.info("User clicks on the Sign in button")


@then(u'User should be logged in successfully')
def step_impl(context):
    logging.info("User should be logged in successfully")