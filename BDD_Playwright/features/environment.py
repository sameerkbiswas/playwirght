import logging
import os

def before_all(context):
    os.makedirs("logs", exist_ok=True)
    logging.basicConfig(
        filename="logs/test.log",
        filemode="a",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )
    logging.info("===========Test Execution Started============")