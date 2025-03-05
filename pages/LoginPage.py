from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.username_field = (By.XPATH, '//*[@class="MuiInput-input joy-1u0jcuo"]')
        self.password_field = (By.XPATH, '//*[@placeholder="Input your password"]')
        self.login_button = (By.XPATH, '(//*[@type="button"])[2]')
        self.alert_wrong_username_password = (By.XPATH, '//*[@role="presentation"]')

    def enter_username(self, username):
        """Memasukkan username."""
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.username_field)
        )
        username_field.click()
        username_field.clear()
        username_field.send_keys(username)

    def enter_password(self, password):
        """Memasukkan password."""
        password_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.password_field)
        )
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

    def click_login_button(self):
        """Klik tombol login."""
        self.driver.find_element(*self.login_button).click()

    def alert_wrong_username_password_is_present(self):
        alert_wrong_username_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.alert_wrong_username_password)
        )
        alert_wrong_username_password.is_displayed()

    def get_text_alert_wrong_username_password(self):
        alert_wrong_username_password = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.alert_wrong_username_password)
        )
        return alert_wrong_username_password.text