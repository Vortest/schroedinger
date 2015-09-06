from selenium.webdriver.common.by import By
from selenium.common import exceptions

from app.element import Element
from app.test_base import TestBase


class ElementTest(TestBase):
    def test_one_locator(self):
        self.driver.get("http://www.google.com")
        locators = [(By.NAME,"q")]
        Element(self.driver, locators).send_keys("something")

    def test_multiple_locator(self):
        self.driver.get("http://www.google.com")
        locators = [(By.CLASS_NAME,"Invalid"),(By.NAME,"q")]
        Element(self.driver, locators).send_keys("ters")

    def test_diff_elements(self):
        self.driver.get("http://www.google.com")
        locators = [(By.NAME,"q"),(By.NAME,"btnK")]
        Element(self.driver, locators).send_keys("ters")

    def test_element_not_found(self):
        self.driver.get("http://www.google.com")
        with self.assertRaises(exceptions.NoSuchElementException):
            Element(self.driver, [(By.CLASS_NAME,"q")]).click()

    def test_element_highlight(self):
        self.driver.get("http://www.google.com")
        locators = [(By.NAME,"q"),(By.NAME,"btnK")]
        Element(self.driver, locators).highlight()
