import pytest
from playwright.sync_api import Playwright


def test_status_endpoint(before_each_test):
    """Test GET request to /status endpoint"""
    request = before_each_test
    
    # Make GET request to /status endpoint
    response = request.get("/status")
    
    # Assert status code is 200
    assert response.status == 200, f"Expected status 200, got {response.status}"
    
    # Get JSON response
    response_json = response.json()
    
    # Assert JSON response
    assert response_json == {"status": "UP"}, f"Expected {{'status': 'UP'}}, got {response_json}"
    
    print(f"✅ Status endpoint test passed!")
    print(f"Response: {response_json}")
