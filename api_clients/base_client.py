import requests

class BaseClient:
    def __init__(self, base_url: str = "https://ipgis.cc"):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint: str, params: dict = None):
        url = f"{self.base_url}{endpoint}"
        return self.session.get(url, params=params)