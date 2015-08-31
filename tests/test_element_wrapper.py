import unittest
from selenium.webdriver.common.by import By
import webelement_extensions
from selenium import webdriver

class FilterTest(unittest.TestCase):
    def test_one(self):
        driver = webdriver.Firefox()
        driver.get("http://www.google.com")
        driver.find_element(By.NAME,"q").click()