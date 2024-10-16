import unittest
from src.api_client import APIClient
from src.project_manager import ProjectManager


class ProjectTest(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient(base_url='http://localhost:8111', username='admin', password='admin')
        self.project_manager = ProjectManager(self.api_client)

    def test_create_project_success(self):
        project_data = {
            "parentProject": {"locator": "_Root"},
            "name": "Test Project",
            "id": "test_project_1",
            "copyAllAssociatedSettings": True
        }
        response = self.project_manager.create_project(project_data)
        self.assertEqual(response.status_code, 200)

    def test_create_project_with_existing_id(self):
        project_data = {
            "parentProject": {"locator": "_Root"},
            "name": "Duplicate Project",
            "id": "test_project_1",
            "copyAllAssociatedSettings": True
        }
        response = self.project_manager.create_project(project_data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()
