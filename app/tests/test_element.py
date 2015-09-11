import os
from selenium.webdriver.common.by import By
from selenium.common import exceptions
from app import config

from app.webelement import WebElement
from app.test_base import TestBase
from models.element import Locator


class ElementTest(TestBase):
    def test_one_locator(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.NAME,value="q")]
        WebElement(self.driver, locators).send_keys("something")

    def test_multiple_locator(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.CLASS_NAME,value="Invalid"),Locator(by=By.NAME,value="q")]
        WebElement(self.driver, locators).send_keys("ters")

    def test_diff_elements(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.NAME,value="q"),(By.NAME,"btnK")]
        WebElement(self.driver, locators).send_keys("ters")

    def test_element_not_found(self):
        self.driver.get("http://www.google.com")
        with self.assertRaises(exceptions.NoSuchElementException):
            WebElement(self.driver, [Locator(by=By.CLASS_NAME,value="q")]).click()

    def test_element_highlight(self):
        self.driver.get("http://www.google.com")
        locators = [Locator(by=By.NAME,value="q"),(By.NAME,"btnK")]
        WebElement(self.driver, locators).highlight()

    def test_find_parent(self):
        self.driver.get("http://www.google.com")
        elment = WebElement(self.driver, [Locator(by=By.NAME,value="q")])
        parent = elment.find_parent()
        assert parent.get_attribute("id") == "gs_lc0"

    def test_element_screenshot(self):
        self.driver.get("http://www.google.com")
        elment = WebElement(self.driver, [Locator(by=By.NAME,value="q")])
        elment.screenshot(os.path.join(config.ROOT_DIR, "element.png"))

    def test_element_screenshot_string(self):
        self.driver.get("http://www.google.com")
        elment = WebElement(self.driver, [Locator(by=By.NAME,value="q")])
        screenshot = elment.screenshot_as_base64
        assert screenshot is not "" and not None

    def test_element_html(self):
        self.driver.get("http://www.google.com")
        elment = WebElement(self.driver, [Locator(by=By.NAME,value="q")])
        print elment.html


