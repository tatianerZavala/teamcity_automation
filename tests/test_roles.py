import unittest
from src.api_client import APIClient
from src.role_manager import RoleManager


class RoleTest(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient(base_url='http://localhost:8111', username='admin', password='admin')
        self.role_manager = RoleManager(self.api_client)

    def test_assign_role(self):
        role_data = {
            "roleId": "PROJECT_ADMIN",
            "scope": "g"
        }
        response = self.role_manager.assign_role(role_data)
        self.assertEqual(response.status_code, 200)

    def test_assign_role_invalid(self):
        role_data = {
            "roleId": "",
            "scope": "g"
        }
        response = self.role_manager.assign_role(role_data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
