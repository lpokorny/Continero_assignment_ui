from selenium.webdriver.common.by import By

from POM.base_page import BasePage


class PhilosophyOfLanguage(BasePage):

    title = '[class="mw-page-title-main"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_title_name(self):
        title_element = self.driver.find_element(By.CSS_SELECTOR, self.title)
        assert "Philosophy" in title_element.text

