import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from test_base import TestBase


class FilterTest(TestBase):
    def test_highlight(self):
        self.driver.get("http://www.google.com")
        self.driver.find_element(By.NAME,"q").highlight()

    def test_highlight_all(self):
        self.driver.get("http://www.google.com")
        elements = self.driver.find_elements(By.CSS_SELECTOR,"*")
        for ele in elements:
            ele.highlight()

    def test_html(self):
        self.driver.get("http://www.google.com")
        print self.driver.find_element(By.NAME,"q").html