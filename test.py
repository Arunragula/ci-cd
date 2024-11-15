import pytest
from app import app

@pytest.fixture
def client():
    # Set the app to testing mode for the fixture
    app.config['TESTING'] = True
    # Create a test client and provide it to the tests
    with app.test_client() as client:
        yield client

def test_homepage_route(client):
    # Send a GET request to the homepage
    response = client.get('/')
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    # Assert that the response data contains "Hello World!"
    assert b"Hello World!" in response.data
