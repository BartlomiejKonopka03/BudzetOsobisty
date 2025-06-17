import unittest
import os
import csv
from auth import register_user, login_user, USERS_FILE

class TestAuth(unittest.TestCase):
    def setUp(self):
        os.makedirs("data", exist_ok=True)
        with open(USERS_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["username", "password_hash"])

    def tearDown(self):
        if os.path.exists(USERS_FILE):
            os.remove(USERS_FILE)

    def test_register_new_user(self):
        result = register_user("jan", "haslo123")
        self.assertEqual(result, "jan")

    def test_register_duplicate_user(self):
        register_user("jan", "haslo123")
        result = register_user("jan", "haslo123")
        self.assertIsNone(result)

    def test_login_valid_user(self):
        register_user("jan", "haslo123")
        result = login_user("jan", "haslo123")
        self.assertEqual(result, "jan")

    def test_login_invalid_user(self):
        register_user("jan", "haslo123")
        result = login_user("nieistnieje", "haslo123")
        self.assertIsNone(result)

    def test_login_invalid_password(self):
        register_user("jan", "haslo123")
        result = login_user("jan", "zlehaslo")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
