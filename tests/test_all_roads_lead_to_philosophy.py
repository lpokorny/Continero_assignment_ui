import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from POM.Louis_H_Bean_page import LouisHBeanArticle
from POM.political_science_page import PoliticalScience
from POM.science_page import Science
from POM.scientific_method_page import ScientificMethod
from POM.empirical_evidence_page import EmpiricalEvidence
from POM.proposition import Proposition
from POM.philosophy_of_language import PhilosophyOfLanguage


class AllRoadLeadToPhilosophy(unittest.TestCase):

    starting_article = "https://en.wikipedia.org/wiki/Louis_H._Bean"
    recorded_urls = []

    def setUp(self):
        # driver setup
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

        # instantiation
        self.cycling_pages = [
            LouisHBeanArticle(self.driver),
            PoliticalScience(self.driver),
            Science(self.driver),
            ScientificMethod(self.driver),
            EmpiricalEvidence(self.driver),
            Proposition(self.driver),
        ]
        self.philosophy_of_language = PhilosophyOfLanguage(self.driver)

    def test_philosophy_related_article_is_reached(self):
        self.driver.get(self.starting_article)

        for page in self.cycling_pages:
            page.click_first_link()
            self.recorded_urls.append(self.driver.current_url)

        self.philosophy_of_language.check_title_name()

        print(f'\nNumber of redirects: {len(self.recorded_urls)}')