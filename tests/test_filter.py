import unittest
from selenium.webdriver.common.by import By
from page_parser import PageParser
from test_base import TestBase
import element_filter

class FilterTest(TestBase):
    def test_children(self):
        self.parser = PageParser(self.driver,"http://www.google.com/")
        self.elements = self.parser.get_all_elements()
