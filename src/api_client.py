import requests
from requests.auth import HTTPBasicAuth


class APIClient:
    def __init__(self, base_url, username, password):
        self.base_url = base_url
        self.auth = HTTPBasicAuth(username, password)

    def post(self, endpoint, data):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=data, auth=self.auth, headers={'Accept': 'application/json'})
        return response

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url, auth=self.auth, headers={'Accept': 'application/json'})
        return response
