import json
import pytest

from playwright.sync_api import APIRequestContext

@pytest.mark.order(2)
def test_get_a_product(before_each_test: APIRequestContext):
    response = before_each_test.get("/products/1225")
    # print("Status code: ", response.status)
    print(f"Status code : {response.status}")

    assert response.status == 200
    # assert "OK" in response.text_content("body")

    # print("Response body: ", response.text())
    # print("Response JSON: ", response.json())
    print(json.dumps(response.json(), indent=4))