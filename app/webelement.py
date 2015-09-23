import logging
from browser_manager import BrowserManager
from models.element_state import Locator
from webdriver_wrapper import WebDriver
from wrapped_webelement import WrappedWebElement
from selenium.common import exceptions
from test_base import TestBase
import time

class WebElement(WrappedWebElement):

    def __init__(self, driver, locators, timeout = 5):
        assert isinstance(locators,list)
        assert isinstance(locators[0],Locator)
        assert isinstance(driver, WebDriver)
        self._element = None
        self.locators = locators
        self._driver = driver
        self.timeout = timeout

    def __repr__(self):
        repr = "ELEMENT: "
        for locator in self.locators:
            repr += "{}:{}, ".format(locator.by,locator.value)
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
                all_eles = []
                for locator in self.locators:
                    eles = self.driver.find_elements(locator.by,locator.value)
                    all_eles.extend(eles)
                if len(all_eles) > 0:
                    self._element = max(all_eles, key=all_eles.count)
                    return self._element
            else:
                return self._element
            logging.debug("Waiting for element %s" % self)
            time.sleep(1)
        raise exceptions.NoSuchElementException("Could not find an element matching any of the following locators: {}".format(self.locators))

    def highlight(self, length=-1, color="yellow"):
        self.element.highlight(length,color)

    def is_present(self, timeout=1):
        self.timeout = timeout
        try:
            element = self.element
            return True
        except:
            return False

    def verify(self, timeout=5):
        self.timeout = timeout
        return self.element

    def __eq__(self, other):
        try:
            same = self.rect == other.rect
            return same
        except Exception as e:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
