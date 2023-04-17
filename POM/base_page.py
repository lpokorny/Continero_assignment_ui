from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.remote.webdriver import WebDriver

from logger_config import logger


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.logger = logger
        driver.maximize_window()

    def click(self, locator):
        try:
            self.wait.until(element_to_be_clickable(locator))
            self.driver.find_element(*locator).click()
        except Exception:
            self.logger.error(f'Error occurred when attempted to click {locator}')
            raise