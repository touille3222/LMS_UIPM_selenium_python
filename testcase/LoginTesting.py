import time

import pytest
from selenium import webdriver

from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage

class TestLoginPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Inisialisasi WebDriver sebelum setiap test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.driver.get("https://uipm.vertical.id/login")
        yield
        """Menutup WebDriver setelah setiap test."""
        self.driver.quit()

    def test_successful_login_administrator(self):
        time.sleep(3)
        self.login_page.enter_username("uipm.admin_university.000001")
        self.login_page.enter_password("uipm.01000001")
        self.login_page.click_login_button()
        time.sleep(3)  # Menunggu 3 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        assert "Halo Administrator Univ1!" == self.dashboard_page.account_name_dashboard_get_text()
        time.sleep(4)
        print(self.driver.current_url)
        print(self.dashboard_page.account_name_dashboard_get_text())

    def test_successful_login_instructor(self):
        time.sleep(3)
        self.login_page.enter_username("uipm.lecturer.02030102")
        self.login_page.enter_password("uipm.0402030102")
        self.login_page.click_login_button()
        time.sleep(3)  # Menunggu 3 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        time.sleep(4)
        print(self.driver.current_url)

    def test_successful_login_learner(self):
        time.sleep(3)
        self.login_page.enter_username("gilang321")
        self.login_page.enter_password("Password123")
        self.login_page.click_login_button()
        time.sleep(3)  # Menunggu 3 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        time.sleep(4)
        print(self.driver.current_url)

    def test_unsuccessful_login(self):
        time.sleep(3)
        self.login_page.enter_username("uipm.admin_university.000001")
        self.login_page.enter_password("wrongpassword")
        self.login_page.click_login_button()
        assert self.driver.current_url == "https://uipm.vertical.id/login"
        print(self.driver.current_url)
        self.login_page.alert_wrong_username_password_is_present()
        assert "Email/username and password do not match." == self.login_page.get_text_alert_wrong_username_password()
        time.sleep(1)
        print(self.login_page.get_text_alert_wrong_username_password())