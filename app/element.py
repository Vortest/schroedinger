import logging
from browser_manager import BrowserManager
from webdriver_wrapper import WebDriver
from webelement_wrapper import WebElement
from selenium.common import exceptions
from test_base import TestBase
import time

class Element(WebElement):

    def __init__(self, driver, locators, timeout = 5):
        assert isinstance(locators,list)
        assert isinstance(locators[0],tuple)
        assert isinstance(driver, WebDriver)
        self._element = None
        self.locators = locators
        self._driver = driver
        self.timeout = timeout

    def __repr__(self):
        repr = "ELEMENT: "
        for locator in self.locators:
            repr += "{}:{}, ".format(locator[0],locator[1])
        return repr

    @property
    def driver(self):
       return self._driver

    @property
    def element(self):
        start_time = time.time()
        end_time = start_time + self.timeout
        while time.time() < end_time:
            if self._element is None or self._element.is_stale():
                for locator in self.locators:
                    eles = self.driver.find_elements(locator[0],locator[1])
                    if len(eles) > 0:
                        self._element = eles[0]
                        return self._element
            else:
                return self._element
            logging.debug("Waiting for element")
            time.sleep(1)
        raise exceptions.NoSuchElementException("Could not find an element matching any of the following locators: {}".format(self.locators))

    def highlight(self, length=.1):
        self.element.highlight(length)

    def is_present(self, time=1):
        start_time = time.time()
        end_time = start_time + time
        while time.time() < end_time:
            if self._element is None or self._element.is_stale():
                for locator in self.locators:
                    eles = self.driver.find_elements(locator[0],locator[1])
                    if len(eles) > 0:
                        self._element = eles[0]
                        return True
            logging.debug("Waiting for element")
            time.sleep(1)
        return False

    def __eq__(self, other):
        for locator in self.locators:
            if locator in other.locators:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
