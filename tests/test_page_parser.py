from test_base import TestBase
from page_parser import PageParser

class TestPageParser(TestBase):
    def test_parse_page(self):
        elements = PageParser(self.driver,"http://www.google.com").get_all_elements()
        for element in elements:
            element.highlight()