from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.account_name_dashboard = (By.XPATH, '//*[@class="MuiTypography-root MuiTypography-h2 joy-1gim5zg"]')
        self.courses_page_sidebar_button = (By.ID, '/courses')

    def account_name_dashboard_get_text(self):
        account_name_dashboard = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.account_name_dashboard)
        )
        return account_name_dashboard.text

    def click_courses_page_sidebar_button(self):
        courses_page_sidebar_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.courses_page_sidebar_button)
        )
        courses_page_sidebar_button.click()