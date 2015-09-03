import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from decorators import timeit
from element import Element
from locator_builder import LocatorBuilder
from page_parser import PageParser
from state_builder import StateBuilder
from test_base import TestBase
from selenium.common import exceptions
from testfixtures import compare
from testfixtures import Comparison as C

class CrawlerTest(TestBase):
    def test_crawl(self):
        url = "http://www.google.com/"
        self.driver.get(url)
        state_builder = StateBuilder(self.driver)
        initial_state = state_builder.get_current_state()
        new_states = []
        for element in initial_state.elements:
            try:
                self.driver.get(url)
                if(element.is_displayed()):
                    element.click()
                    new_state = state_builder.get_current_state()
                    if new_state == initial_state:
                        print "looks like this is the same state"
                    else:
                        print 'new state found at %s' % self.driver.current_url
                        new_states.append(new_state)
            except Exception as e:
                print "Couldn't crawl element"
        print "%s states" % len(new_states)
        for state in new_states:
            print state

    def test_generate(self):
        url = "http://www.google.com/"
        self.driver.get(url)
        state_builder = StateBuilder(self.driver)
        initial_state = state_builder.get_current_state()
        print "there are {} elemnets1 founds".format(len(initial_state.elements))

        import element_filter
        text_fields = element_filter.filter_elements(initial_state.elements,"input",("type","text"))
        submit_fields = element_filter.filter_elements(initial_state.elements,"input",("type","submit"))

        print "Found %s text field" % len(text_fields)
        for field in text_fields:
            field.highlight(1)
            field.send_keys("SOMETHING")
        new_state = state_builder.get_current_state()

        if new_state != initial_state:
            print "new state detected"
        else:
            for field in submit_fields:
                field.highlight()
                field.click()