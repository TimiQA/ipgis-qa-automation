import pytest
from playwright.sync_api import expect
from pages.main_page import MainPage
from data.translations import translations

class TestMainLayout:
    
    @pytest.mark.parametrize("lang_code, locale", [
        ("en", "en-US"),
        ("ru", "ru-RU"),
        ("zh", "zh-CN")
    ])
    def test_homepage_multilang_rendering(self, browser, lang_code, locale):
        context = browser.new_context(locale=locale)
        page = context.new_page()
        texts = translations[lang_code]
        
        main_page = MainPage(page, texts)
        main_page.open()
        
        # Умное ожидание от Playwright. Ждет, пока React не отрисует текст
        expect(main_page.ip_address_label).to_be_visible()
        expect(main_page.sensor_status).to_be_visible()
        
        context.close()