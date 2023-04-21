from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver

from logger_config import logger


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        driver.maximize_window()

    def click(self, locator):
        try:
            self.wait.until(visibility_of_element_located(locator))
            self.driver.find_element(*locator).click()
        except Exception:
            logger.error(f'Error occurred when attempted to click {locator}')
            raise