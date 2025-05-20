from app import app

def test_home():
    # Membuat test client dari aplikasi Flask
    client = app.test_client()
    response = client.get('/')
    
    assert response.status_code == 200
    assert response.data == b'Hello from Flask!'
