from selenium.webdriver.common.by import By
from app.test_base import TestBase
from app.webelement import WebElement
from models.element import Element, Locator


class TestElementCompare(TestBase):
    def test_compare_same_element(self):
        self.driver.get("http://www.google.com/")
        eleement1 = Element(locators=[Locator(by=By.NAME,value="q")])
        eleement2 = Element(locators=[Locator(by=By.NAME,value="q")])

        from app.element_comparer import ElementComparer
        result = ElementComparer(self.driver).compare_elements(WebElement(self.driver, eleement1.locators),WebElement(self.driver, eleement2.locators))
        assert result == 0

    def test_compare_diff_element(self):
        self.driver.get("http://www.google.com/")
        eleement1 = Element(locators=[Locator(by=By.NAME,value="q")])
        eleement2 = Element(locators=[Locator(by=By.NAME,value="btnK")])

        from app.element_comparer import ElementComparer
        result = ElementComparer(self.driver).compare_elements(WebElement(self.driver, eleement1.locators),WebElement(self.driver, eleement2.locators))
        assert result != 0, result
        print result

    def test_compare_similar_element(self):
        self.driver.get("http://www.google.com/")
        eleement1 = Element(locators=[Locator(by=By.NAME,value="btnI")])
        eleement2 = Element(locators=[Locator(by=By.NAME,value="btnK")])

        from app.element_comparer import ElementComparer
        result = ElementComparer(self.driver).compare_elements(WebElement(self.driver, eleement1.locators),WebElement(self.driver, eleement2.locators))
        assert result != 0, result
        print result


