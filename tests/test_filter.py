import unittest
from selenium.webdriver.common.by import By
from test_base import TestBase


class FilterTest(TestBase):
    def test_one(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element(By.NAME,"q").click()
