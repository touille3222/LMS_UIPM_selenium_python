import time

import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage


class TestLoginPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Inisialisasi WebDriver sebelum setiap test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.login_page.open_login_page("https://uipm.vertical.id/login")
        yield
        """Menutup WebDriver setelah setiap test."""
        self.driver.quit()

    def test_successful_login(self):
        time.sleep(5)
        self.login_page.enter_username("uipm.admin_university.000001")
        self.login_page.enter_password("uipm.01000001")
        self.login_page.click_login_button()
        time.sleep(5)  # Menunggu 5 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        print(self.driver.current_url)