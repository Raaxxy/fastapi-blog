from fastapi.testclient import TestClient
from app import app
from faker import Faker

fake = Faker()
client = TestClient(app)


def test_signup():
    signup_data = {
        "username" : fake.user_name(),
        "email" : fake.email(),
        "password" : "password1"
    }
    
    response = client.post('/user/singup/' , json=signup_data)
    assert response.status_code == 200
    assert response.json() == {
        "message": "User has been created successfully"
    }