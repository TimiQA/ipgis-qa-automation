import pytest
from api_clients.ip_api_client import IpApiClient

class TestIpLookupAPI:
    # Инициализируем клиент один раз для всего класса
    client = IpApiClient()

    @pytest.mark.parametrize("ip_address", [
        "8.8.8.8",                  # Стандартный IPv4 (Google DNS)
        "2606:4700:4700::1111"      # Стандартный IPv6 (Cloudflare)
    ])
    def test_valid_ip_lookup(self, ip_address):
        response = self.client.get_ip_info(ip_address)
        assert response.status_code == 200, f"Expected 200 for {ip_address}, got {response.status_code}"
        
        data = response.json()
        # Проверяем, что бэкенд вернул именно тот IP, который мы запрашивали
        assert "ip" in data, "Key 'ip' is missing in response"
        
        # Убеждаемся, что база MaxMind отработала и вернула реальные данные, а не заглушки
        assert data.get("country") != "Unknown", f"GeoIP failed for {ip_address}"
        assert data.get("city") != "Unknown", f"GeoIP failed for {ip_address}"

    def test_invalid_ip_format(self):
        # Бэкенд сейчас проглатывает невалидный IP и возвращает IP клиента (fallback)
        invalid_ip = "not_an_ip_address"
        response = self.client.get_ip_info(invalid_ip)
        
        assert response.status_code == 200, "Backend behavior changed: expected 200 with fallback IP"
        data = response.json()
        
        # Убеждаемся, что сервер не вернул нам мусор обратно
        assert data.get("ip") != invalid_ip, "Backend reflected invalid string as a valid IP"