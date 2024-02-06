import unittest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app, get_db
from app import models

class TestContactRouter(unittest.TestCase):
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

    def test_create_contact(self):
        contact_data = {"first_name": "John", "last_name": "Doe", "email": "john@example.com", "phone_number": "1234567890"}
        response = self.client.post("/contacts/", json=contact_data)
        self.assertEqual(response.status_code, 200)
        created_contact = response.json()
        self.assertEqual(created_contact["first_name"], "John")

    def test_get_contacts(self):
        response = self.client.get("/contacts/")
        self.assertEqual(response.status_code, 200)
        contacts = response.json()
        self.assertIsInstance(contacts, list)

    def test_get_contact(self):
        contact_data = {"first_name": "Jane", "last_name": "Doe", "email": "jane@example.com", "phone_number": "9876543210"}
        create_response = self.client.post("/contacts/", json=contact_data)
        created_contact = create_response.json()

        response = self.client.get(f"/contacts/{created_contact['id']}")
        self.assertEqual(response.status_code, 200)
        retrieved_contact = response.json()
        self.assertEqual(retrieved_contact["first_name"], "Jane")


if __name__ == "__main__":
    unittest.main()