from playwright.sync_api import APIRequestContext

import json
import pytest

file_path = "global_data.json"

@pytest.mark.order(5)
def test_delete_an_item_from_cart(before_each_test: APIRequestContext):
    with open(file_path, "r") as file:
        data = json.load(file)

    cart_id = data["cart_id"]
    item_id = data["item_id"][0]  # Get the first item ID from the list

    response = before_each_test.delete(f"/carts/{cart_id}/items/{item_id}")
    print(f"Status code : {response.status}")
    print(json.dumps(response.json(), indent=4))

    assert response.status == 200
    # assert "OK" in response.text_content("body")

    # Remove the deleted item ID from the list
    data["item_id"].remove(item_id)
    
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
        