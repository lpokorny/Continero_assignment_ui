from selenium.webdriver.common.by import By

from POM.base_page import BasePage
from logger_config import logger

"""For catching the possibility, that there is no link in the first paragraph in every article, 
I chose to use XPATH with parametrized <p> number inside, for each retry the number increments so that we are
trying to look through another paragraph if no link was found in the previous one"""


class RandomPage(BasePage):

    first_link_xpath = '//*[@id="mw-content-text"]/div[1]/p[{}]/a[1]'
    paragraph_xpath = '//*[@id="mw-content-text"]/div[1]/p[{}]'
    title = '[class="mw-page-title-main"]'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_first_link(self):
        found_first_link = False

        for i in range(1, 5):
            parametrized_paragraph_xpath = self.paragraph_xpath.format(i)
            parametrized_first_link_in_paragraph = self.first_link_xpath.format(i)

            """Measuring links length allows us to skip the explicit wait for element to be clickable, 
            if there are no links in the paragraph"""
            try:
                paragraph = self.driver.find_element(By.XPATH, parametrized_paragraph_xpath)
                links = paragraph.find_elements(By.TAG_NAME, 'a')

                if len(links) > 0:
                    locator = (By.XPATH, parametrized_first_link_in_paragraph)
                    self.click(locator)
                    found_first_link = True
                    break
            except Exception:
                logger.debug(f"Could not find first link in paragraph {i}")

        if not found_first_link:
            logger.error(f"Could not find first link in any paragraph at {self.driver.current_url}")
            raise Exception("Could not find first link in any paragraph")

    def check_title_name_contains_philosophy(self):
        title_element = self.driver.find_element(By.CSS_SELECTOR, self.title)
        if "Philosophy" in title_element.text:
            logger.info(f"Philosophy related article reached {self.driver.current_url}")
            return True
        else:
            return False