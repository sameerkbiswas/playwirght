import json
import os

from playwright.sync_api import Playwright

def test_create_cart(playwright: Playwright):

    api_key = os.getenv("GITHUB_API_KEY", "your_api_key_here")

    request = playwright.request.new_context()
    response = request.get(
        "https://api.github.com/user/repos",
        headers={"Authorization": f"Bearer {api_key}"}
    )
    print(json.dumps(response.json(), indent=4))

    assert response.status == 200
    print(json.dumps(response.json(), indent=4))

    request.dispose()