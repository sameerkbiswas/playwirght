import json
import pytest

from playwright.sync_api import APIRequestContext

file_path = "global_data.json"

@pytest.mark.order(3)
def test_create_cart(before_each_test: APIRequestContext):
    with open(file_path, "r") as file:
        data = json.load(file)

    response = before_each_test.post("/carts")
    print(f"Status code : {response.status}")
    print(json.dumps(response.json(), indent=4))

    assert response.status == 201
    # assert "Created" in response.text_content("body")

    data["cart_id"] = response.json()["cartId"]
    data["item_id"] = []
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)