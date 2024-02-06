import unittest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app import models

class TestUserRouter(unittest.TestCase):
    def setUp(self):
        engine = create_engine("sqlite:///:memory:")
        models.Base.metadata.create_all(bind=engine)
        TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        self.dependency_overrides = {
            get_db: lambda: TestingSessionLocal()
        }
        self.client = TestClient(app)

    def tearDown(self):
        pass

    def test_register_user(self):
        user_data = {"email": "test@example.com", "password": "testpassword"}
        response = self.client.post("/register", json=user_data)
        self.assertEqual(response.status_code, 200)
        created_user = response.json()
        self.assertEqual(created_user["email"], "test@example.com")

    
    def test_update_user_avatar(self):
        user_data = {"email": "test@example.com", "password": "testpassword"}
        create_user_response = self.client.post("/register", json=user_data)
        created_user = create_user_response.json()

        access_token_response = self.client.post("/token", data={"username": "test@example.com", "password": "testpassword"})
        access_token = access_token_response.json()["access_token"]

        with TestClient(app, headers={"Authorization": f"Bearer {access_token}"}) as authorized_client:
            avatar_file = ("test_avatar.png", open("path/to/test_avatar.png", "rb"))
            response = authorized_client.put("/users/me/avatar", files={"avatar": avatar_file})
            
            self.assertEqual(response.status_code, 200)
            updated_user = response.json()
            self.assertIn("avatar_url", updated_user)

if __name__ == "__main__":
    unittest.main()