class ProjectManager:
    def __init__(self, api_client):
        self.api_client = api_client

    def create_project(self, project_data):
        response = self.api_client.post('app/rest/projects', project_data)
        return response
