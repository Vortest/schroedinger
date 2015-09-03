import unittest
from selenium.webdriver.common.by import By
from page_parser import PageParser
from state_builder import StateBuilder
from test_base import TestBase
import element_filter
from state import State

class StateTest(TestBase):
    def test_state_builder(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()
        assert len(state.elements) == 17

    def test_compare_same_page(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.com/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()
        assert state == state2

    def test_compare_diff_page(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.bluemodus.com/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        with self.assertRaises(AssertionError):
            assert state == state2

    def test_compare_similar_pages(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.co.uk/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        assert state == state2


    def test_subtract_state(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.google.co.uk/"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        uk_diff = state2 - state
        us_diff = state - state2
        print uk_diff
        for element in uk_diff.elements:
            element.highlight(2)

    def test_find_similar(self):
        self.url = "http://www.percolate.com/platform"
        self.driver.get(self.url)
        builder = StateBuilder(self.driver)
        state = builder.get_current_state()

        self.url2 = "http://www.percolate.com/services"
        self.driver.get(self.url2)
        builder = StateBuilder(self.driver)
        state2 = builder.get_current_state()

        for element in state2.elements:
            if element in state.elements:
                print "Found %s " %  element.html
                element.highlight



