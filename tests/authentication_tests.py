import unittest
from unittest.mock import patch
from mongomock import MongoClient
from src import create_app
import src.database


class PyMongoMock(MongoClient):
    def init_app(self, app):
        return super().__init__()


class TestAuthentication(unittest.TestCase):
    def test_login_successful(self):
        request = {
            "username": "arnon",
            "password": "123"
        }

        with patch.object(src.database.mongo, "mongo", PyMongoMock()):
            app = create_app("some_db_name").test_client()
            src.database.mongo.insert_one_user({"user_id": 5, "username": "arnon", "password": "123"})
            response = app.post("/login", json=request)
            self.assertEqual(response.status_code, 200)

            # Validate the content
            response_json = response.get_json()
            expected_json = {
                "success": True
            }
            self.assertEqual(response_json, expected_json)

    def test_login_unsuccessful_wrong_password(self):
        request = {
            "username": "arnon",
            "password": "wrong password"
        }

        with patch.object(src.database.mongo, "mongo", PyMongoMock()):
            app = create_app("some_db_name").test_client()
            src.database.mongo.insert_one_user({"user_id": 5, "username": "arnon", "password": "123"})
            response = app.post("/login", json=request)
            self.assertEqual(response.status_code, 200)

            # Validate the content
            response_json = response.get_json()
            expected_json = {
                "success": False
            }
            self.assertEqual(response_json, expected_json)

    def test_login_unsuccessful_username_not_exist(self):
        request = {
            "username": "not existing username",
            "password": "123"
        }

        with patch.object(src.database.mongo, "mongo", PyMongoMock()):
            app = create_app("some_db_name").test_client()
            src.database.mongo.insert_one_user({"user_id": 5, "username": "arnon", "password": "123"})
            response = app.post("/login", json=request)
            self.assertEqual(response.status_code, 400)
