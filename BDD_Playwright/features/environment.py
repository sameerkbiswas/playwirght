import logging
import os

def before_all(context):
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/test.log",
        filemode="w",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("===========Test Execution Started============")

def after_all(context):
    logging.info("===========Gmail Server stopped============")
def before_scenario(context, scenario):
    logging.info(f"-------------Starting Scenario: {scenario.name}--------------------")
def after_scenario(context, scenario):
    logging.info(f"-------------Ending Scenario: {scenario.name}--------------------")
def before_feature(context, feature):
    logging.info(f"**********Starting Feature: {feature.name}**********")
def after_feature(context, feature):
    logging.info(f"**********Ending Feature: {feature.name}**********")
def before_step(context, step):
    logging.info(f"^^^^^^^^^^^^^^^^^^^Executing Step: {step.name}")
def after_step(context, step):
    logging.info(f"^^^^^^^^^^^^^^^^^^^Completed Step: {step.name}")