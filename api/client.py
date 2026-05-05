import requests
from utils.config_reader import ConfigReader


class APIClient:
    def __init__(self):
        self.base_url = ConfigReader.get("BASE_URL")
        self.session = requests.Session()

    def get(self, endpoint):              
        return self.session.get(f"{self.base_url}{endpoint}")

    def post(self, endpoint, payload):    
        return self.session.post(f"{self.base_url}{endpoint}", json=payload)

    def put(self, endpoint, payload):     
        return self.session.put(f"{self.base_url}{endpoint}", json=payload)

    def delete(self, endpoint):           
        return self.session.delete(f"{self.base_url}{endpoint}")