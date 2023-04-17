from selenium.webdriver.common.by import By

from POM.base_page import BasePage


class EmpiricalEvidence(BasePage):

    first_link = 'a[title="Proposition"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_first_link(self):
        locator = (By.CSS_SELECTOR, self.first_link)
        BasePage.click(self, locator)

