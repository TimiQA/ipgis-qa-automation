from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page, texts: dict):
        self.page = page
        self.url = "https://ipgis.cc"
        
        # Динамические локаторы на основе переданного словаря
        self.ip_address_label = page.locator(f"text={texts['yourIpAddress']}")
        self.sensor_status = page.locator(f"text={texts['sensorStatus']}")

    def open(self):
        self.page.goto(self.url)

    def get_title(self):
        return self.page.title()