import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_login_page(client):
    """Test halaman login bisa diakses (status code 200)"""
    response = client.get('/login')
    assert response.status_code == 200
    assert b'Login Page' in response.data

def test_login_success(client):
    """Test login berhasil dengan username dan password benar"""
    response = client.post('/login', data={
        'username': 'admin',
        'password': 'password'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Welcome, admin!' in response.data

def test_login_fail(client):
    """Test login gagal dengan username/password salah"""
    response = client.post('/login', data={
        'username': 'wrong',
        'password': 'user'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b'Invalid Credentials' in response.data
