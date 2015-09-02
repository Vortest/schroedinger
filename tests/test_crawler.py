import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from decorators import timeit
from element import Element
from locator_builder import LocatorBuilder
from page_parser import PageParser
from test_base import TestBase
from selenium.common import exceptions
from testfixtures import compare
from testfixtures import Comparison as C

class CrawlerTest(TestBase):
    def test_crawl(self):
        url = "http://www.bluemodus.com"
        self.driver.get(url)
        self.elements = []
        self.parser = PageParser(self.driver)
        self.get_elements()


        for element in self.elements:
            try:
                self.driver.get(url)
                if(element.is_displayed()):
                    element.click()
                    new_state_elements = self.get_elements
                    if len(new_state_elements) == len(self.elements):
                        print "looks like this is the same state"
                    else:
                        print 'new state found'
                        for new_ele in new_state_elements:
                            new_ele.highlight()
            except Exception as e:
                print "Couldn't crawl element"


    def test_crawl(self):
        url = "http://www.google.co.uk"
        self.driver.get(url)
        self.elements = []
        self.parser = PageParser(self.driver)
        self.elements1 = self.get_elements()
        print "there are {} elemnets1 founds".format(len(self.elements1))
        for element in self.elements1:
            print element

        url = "http://www.google.com"
        self.driver.get(url)
        self.parser = PageParser(self.driver)
        self.elements2 = self.get_elements()
        print "there are {} elemnets founds".format(len(self.elements2))
        for element in self.elements2:
            assert element in self.elements1, "ELement not found" + element.html


    @timeit
    def get_elements(self):
        elements = []
        webelements = self.parser.get_all_elements()
        for webelement in webelements:
            webelement.highlight()
            builder = LocatorBuilder(webelement)
            locators = builder.get_locators()
            if len(locators)>0:
                element = Element(self.driver,locators)
                elements.append(element)
        return elements