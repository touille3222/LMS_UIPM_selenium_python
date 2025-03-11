from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CoursePage:
    def __init__(self, driver):
        self.driver = driver

        # Definisi lokator elemen
        self.filter_button = (By.XPATH, '//*[@aria-label="Show/Hide filters"]')
        self.scrollbar_horizontal = (By.XPATH, '//*[@class="MuiTableContainer-root joy-13sfx72"]')
        self.status_filter = (By.XPATH, '//*[@class="MuiBox-root joy-1tzeee1"]')
        self.major_filter = (By.XPATH, '//*[@aria-label="Filter by Jurusan"]')
        self.published_filter = (By.XPATH, '//*[@data-value="true"]')
        self.draft_filter = (By.XPATH, '//*[@data-value="false"]')

    def click_filter_button(self):
        filter_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.filter_button)
        )
        filter_button.click()

    def scroll_to_right(self):
        scrollbar_horizontal = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.scrollbar_horizontal)
        )
        self.driver.execute_script("arguments[0].scrollLeft += 200;", scrollbar_horizontal)

    def click_major_filter(self, major):
        major_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.major_filter)
        )
        major_filter.click()
        major_filter.send_keys(major)

    def click_status_filter(self):
        status_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.status_filter)
        )
        status_filter.click()

    def click_published_filter(self):
        published_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.published_filter)
        )
        published_filter.click()

    def click_draft_filter(self):
        draft_filter = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.draft_filter)
        )
        draft_filter.click()

    def check_row_major(self):
        all_rows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@aria-label="S1 Fakultas03 Jurusan01"]'))
        )

        for row in all_rows:
            print(row.text)
            assert row.text == 'S1 Fakultas03 Jurusan01'

    def check_row_is_published(self):
        all_rows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@class="MuiChip-label MuiChip-labelMd joy-tymi7a"]'))
        )

        for row in all_rows:
            print(row.text)
            assert row.text == 'Diterbitkan'

    def check_row_is_draft(self):
        all_rows = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//*[@class="MuiChip-label MuiChip-labelMd joy-tymi7a"]'))
        )

        for row in all_rows:
            print(row.text)
            assert row.text == 'Draft'