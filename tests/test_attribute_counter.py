from selenium.webdriver.common.by import By
from attribute_counter import AttributeCounter
from test_base import TestBase
from locator_builder import LocatorBuilder
from attribute_builder import AttributeBuilder

class TestAttributeCounter(TestBase):
    def test_unique(self):
        self.driver.get("http://www.google.com/")
        html = self.driver.page_source
        assert AttributeCounter(html,("name","q")).count == 1

    def test_unique(self):
        self.driver.get("http://www.google.com/")
        html = self.driver.page_source
        counter = AttributeCounter(html,("class","gsfi"))
        assert counter.count == 4
