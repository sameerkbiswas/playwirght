from playwright.sync_api import APIRequestContext

import json
import pytest

file_path = "global_data.json"

@pytest.mark.order(4)
@pytest.mark.parametrize("productId", [1225, 1709, 1710])
def test_add_an_item_to_cart(before_each_test: APIRequestContext, productId):
    with open(file_path, "r") as file:
        data = json.load(file)

    cart_id = data["cart_id"]
    payload = {
        "productId": productId,
        "quantity": 1
    }
    response = before_each_test.post(f"/carts/{cart_id}/items", data=payload)
    print(f"Status code : {response.status}")
    print(json.dumps(response.json(), indent=4))

    assert response.status == 201
    # assert "Created" in response.text_content("body")

    data["item_id"].append(productId)
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)