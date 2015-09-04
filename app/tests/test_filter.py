from app.page_parser import PageParser
from app.test_base import TestBase


class FilterTest(TestBase):
    def test_children(self):
        self.driver.get("http://www.google.com/")
        self.parser = PageParser(self.driver)
        self.elements = self.parser.get_all_elements()
