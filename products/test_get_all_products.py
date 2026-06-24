import json
import pytest

from playwright.sync_api import Playwright

base_url = "https://simple-grocery-store-api.click"

@pytest.mark.order(1)
def test_get_all_products(playwright: Playwright):
    request = playwright.request.new_context(base_url=base_url)
    response = request.get("/products")
    print("Status code: ", response.status)

    assert response.status == 200
    # assert "OK" in response.text_content("body")

    # print("Response body: ", response.text())
    # print("Response JSON: ", response.json())
    print(json.dumps(response.json(), indent=4))

    request.dispose()