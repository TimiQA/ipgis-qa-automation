from api_clients.base_client import BaseClient

class IpApiClient(BaseClient):
    def get_ip_info(self, ip_address: str):
        return self.get("/api/ip", params={"ip": ip_address})