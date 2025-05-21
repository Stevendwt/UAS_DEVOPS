import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Login Page' in response.data

def test_login_success(client):
    response = client.post('/', data=dict(username='admin', password='admin'))
    assert b'Login successful' in response.data

def test_login_fail(client):
    response = client.post('/', data=dict(username='user', password='wrong'))
    assert b'Login failed' in response.data
