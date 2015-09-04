import logging

from selenium.webdriver.common.by import By

from app.test_base import TestBase


class DriverTest(TestBase):
    def test_get(self):
        self.driver.get("http://www.google.com")
        logging.debug(self.driver.current_url)
        assert self.driver.current_url == "https://www.google.com/?gws_rd=ssl"

    def test_find_element(self):
        self.driver.get("https://www.google.com/")
        self.driver.find_element(By.NAME,"q").send_keys("Something")

    def test_find_elemnets(self):
        self.driver.get("https://www.google.com/")
        elements = self.driver.find_elements(By.CLASS_NAME,"gb_R")
        assert len(elements) != 1