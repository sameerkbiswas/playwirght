import logging
from behave import given, when, then

@given(u'User is on Rediff Mail registration page')
def step_impl(context):
    logging.info("User is on Rediff Mail registration page")
@when(u'User enters valid details for registration')
def step_impl(context):
    for row in context.table:
        username = row['username']
        email = row['email']
        password = row['password']
        phone = row['phone']
        logging.info(f'User enters valid details for registration: username={username}, email={email}, password={password}, phone={phone}')
    

@when(u'User clicks on the Register button')
def step_impl(context):
    logging.info("User clicks on the Register button")

@then(u'User should be registered successfully')
def step_impl(context):
    logging.info("User should be registered successfully")