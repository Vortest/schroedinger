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
        url = "http://www.percolate.com/login"
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
    #
    # def test_crawl(self):
    #     url = "http://www.google.co.uk"
    #     self.driver.get(url)
    #     self.elements = []
    #     self.parser = PageParser(self.driver)
    #     self.elements1 = self.get_elements()
    #     print "there are {} elemnets1 founds".format(len(self.elements1))
    #     for element in self.elements1:
    #         print element
    #
    #     url = "http://www.google.com"
    #     self.driver.get(url)
    #     self.parser = PageParser(self.driver)
    #     self.elements2 = self.get_elements()
    #     print "there are {} elemnets founds".format(len(self.elements2))
    #     for element in self.elements2:
    #         assert element in self.elements1, "ELement not found" + element.html
    #

    @timeit
    def get_elements(self):
        elements = []
        webelements = self.parser.get_all_elements()
        for webelement in webelements:
            webelement.highlight()
            builder = LocatorBuilder(self.driver, webelement)
            locators = builder.get_locators()
            if len(locators)>0:
                element = Element(self.driver,locators)
                elements.append(element)
        return elements