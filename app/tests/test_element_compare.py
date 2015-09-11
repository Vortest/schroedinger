from selenium.webdriver.common.by import By

from app.webelement import WebElement
from app.test_base import TestBase
from models.element import Locator


class FilterTest(TestBase):
    def test_element_equal(self):
        locators1 = [Locator(by=By.NAME,value="q")]
        locators2 = [Locator(by=By.NAME,value="q")]
        element1 = WebElement(self.driver, locators1)
        element2 = WebElement(self.driver, locators2)

        assert element1 == element2
        assert element2 == element1

    def test_different_locators_equal(self):
        locators1 = [Locator(by=By.NAME,value="q"),Locator(by=By.CLASS_NAME,value="foo")]
        locators2 = [Locator(by=By.CLASS_NAME,value="bar"),Locator(by=By.NAME,value="q")]
        element1 = WebElement(self.driver, locators1)
        element2 = WebElement(self.driver, locators2)

        assert element1 == element2
        assert element2 == element1

    def test_missing_locator_fails(self):
        locators1 = [Locator(by=By.NAME,value="z"),Locator(by=By.CLASS_NAME,value="foo")]
        locators2 = [Locator(by=By.NAME,value="bar"),Locator(by=By.NAME,value="q")]
        element1 = WebElement(self.driver, locators1)
        element2 = WebElement(self.driver, locators2)

        with self.assertRaises(AssertionError):
            assert element1 == element2
            assert element2 == element1

    def test_inequality(self):
        locators1 = [Locator(by=By.NAME,value="z"),Locator(by=By.CLASS_NAME,value="foo")]
        locators2 = [Locator(by=By.NAME,value="bar"),Locator(by=By.NAME,value="q")]
        element1 = WebElement(self.driver, locators1)
        element2 = WebElement(self.driver, locators2)

        assert element1 != element2
        assert element2 != element1



