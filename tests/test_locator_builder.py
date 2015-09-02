import logging
from selenium.webdriver.common.by import By
from element import Element
from test_base import TestBase
from locator_builder import LocatorBuilder
from page_parser import PageParser

class TestLocatorBuilder(TestBase):
    def test_unique(self):
        self.driver.get("http://www.google.com/")
        element = self.driver.find_element(By.NAME,"q")
        locators = LocatorBuilder(self.driver, element).get_locators()
        for locator in locators:
            elements = self.driver.find_elements(locator[0],locator[1])
            assert len(elements) == 1

    def test_many(self):
        elements = PageParser(self.driver,"http://www.google.com/").get_all_elements()
        for element in elements:
            element.highlight()
            locators = LocatorBuilder(self.driver, element).get_locators()
            for locator in locators:
                try:
                    elements = self.driver.find_elements(locator[0],locator[1])
                    assert len(elements) == 1
                except:
                    logging.error("an error occured : {}".format(locator))


    def test_elements(self):
        self.driver.get("http://www.google.com")
        elements = PageParser(self.driver).get_all_elements()
        for element in elements:
            #print "looking at element {}".format(element.html)
            element.highlight()
            locators = LocatorBuilder(self.driver, element).get_locators()
            #print "Found {} locators".format(len(locators))
            print locators