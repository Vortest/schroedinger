from app.page_parser import PageParser
from app.test_base import TestBase


class FilterTest(TestBase):
    def test_children(self):
        self.parser = PageParser(self.driver,"http://www.google.com/")
        self.elements = self.parser.get_all_elements()
