from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pytest

from logger_config import logger
from POM.random_page import RandomPage


class TestAllRoadLeadToPhilosophy:

    random_article = "https://en.wikipedia.org/wiki/Special:Random"
    recorded_urls = []

    @pytest.fixture(autouse=True)
    def setup_method(self):
        # driver setup
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def test_philosophy_related_article_is_reached(self):
        random_page = RandomPage(self.driver)

        self.driver.get(self.random_article)

        philosophy_related_article_found = random_page.check_title_name_contains_philosophy()

        while not philosophy_related_article_found:
            random_page.click_first_link()
            self.recorded_urls.append(self.driver.current_url)
            philosophy_related_article_found = random_page.check_title_name_contains_philosophy()

        logger.info(f'Number of redirects: {len(self.recorded_urls)}')
