import time

import pytest
from selenium import webdriver

from pages.CoursePage import CoursePage
from pages.LoginPage import LoginPage
from pages.DashboardPage import DashboardPage

class TestCoursePage:
    @pytest.fixture(autouse=True)
    def setup(self):
        """Inisialisasi WebDriver sebelum setiap test."""
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.course_page = CoursePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.dashboard_page = DashboardPage(self.driver)
        self.driver.get("https://uipm.vertical.id/login")
        yield
        """Menutup WebDriver setelah setiap test."""
        self.driver.quit()

    def test_filter_major(self):
        time.sleep(3)
        self.login_page.enter_username("uipm.admin_university.000001")
        self.login_page.enter_password("uipm.01000001")
        self.login_page.click_login_button()
        time.sleep(7)  # Menunggu 3 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        assert "Halo Administrator Univ1!" == self.dashboard_page.account_name_dashboard_get_text()
        self.dashboard_page.click_courses_page_sidebar_button()
        time.sleep(3)
        assert self.driver.current_url == "https://uipm.lms.vertical.id/courses"
        time.sleep(3)
        self.course_page.click_filter_button()
        self.course_page.click_major_filter("S1 Fakultas03 Jurusan01")
        time.sleep(3)
        self.course_page.check_row_major()
        time.sleep(3)

    def test_filter_status_published(self):
        time.sleep(3)
        self.login_page.enter_username("uipm.admin_university.000001")
        self.login_page.enter_password("uipm.01000001")
        self.login_page.click_login_button()
        time.sleep(7)  # Menunggu 3 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        assert "Halo Administrator Univ1!" == self.dashboard_page.account_name_dashboard_get_text()
        self.dashboard_page.click_courses_page_sidebar_button()
        time.sleep(3)
        assert self.driver.current_url == "https://uipm.lms.vertical.id/courses"
        time.sleep(3)
        self.course_page.click_filter_button()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.course_page.scroll_to_right()
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.course_page.click_status_filter()
        self.course_page.click_published_filter()
        self.course_page.check_row_is_published()
        time.sleep(3)

    def test_filter_status_draft(self):
        time.sleep(3)
        self.login_page.enter_username("uipm.admin_university.000001")
        self.login_page.enter_password("uipm.01000001")
        self.login_page.click_login_button()
        time.sleep(7)  # Menunggu 3 detik setelah login
        assert self.driver.current_url == "https://uipm.lms.vertical.id/dashboard"
        assert "Halo Administrator Univ1!" == self.dashboard_page.account_name_dashboard_get_text()
        self.dashboard_page.click_courses_page_sidebar_button()
        time.sleep(3)
        assert self.driver.current_url == "https://uipm.lms.vertical.id/courses"
        time.sleep(3)
        self.course_page.click_filter_button()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.course_page.scroll_to_right()
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.course_page.click_status_filter()
        self.course_page.click_draft_filter()
        self.course_page.check_row_is_draft()
        time.sleep(3)