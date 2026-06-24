from playwright.sync_api import Playwright

base_url = "https://simple-grocery-store-api.click"

def test_status(playwright: Playwright):
    request = playwright.request.new_context()
    response = request.get(f"{base_url}/status")
    print("Status code: ", response.status)

    assert response.status == 200
    # assert "OK" in response.text_content("body")

    request.dispose()