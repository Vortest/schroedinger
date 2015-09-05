from app.attribute_counter import AttributeCounter
from app.test_base import TestBase


class TestAttributeCounter(TestBase):
    def test_unique(self):
        self.driver.get("http://www.google.com/")
        html = self.driver.page_source
        assert AttributeCounter(html,("id","lst-ib")).count == 1

    def test_multiple(self):
        self.driver.get("http://www.google.com/")
        html = self.driver.page_source
        counter = AttributeCounter(html,("class","gsfi"))
        assert counter.count == 4
