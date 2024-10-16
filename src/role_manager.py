class RoleManager:
    def __init__(self, api_client):
        self.api_client = api_client

    def assign_role(self, role_data):
        response = self.api_client.post('app/rest/roles', role_data)
        return response
