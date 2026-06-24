import json
import pytest

from playwright.sync_api import Playwright

file_path = "global_data.json"

@pytest.fixture(scope="function")
def before_each_test(playwright: Playwright):
    with open(file_path, "r") as file:
        data = json.load(file)

    request = playwright.request.new_context(base_url=data["base_url"])
    yield request
    request.dispose()