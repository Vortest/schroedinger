import logging
import unittest
import exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from app.browser_manager import BrowserManager
from app.browser_session import BrowserSession
from app.test_base import TestBase
from app.webelement import WebElement
from models.suite_config import SuiteConfig, RunConfig
import app.by
from app.webdriver_adapter import WebdriverAdapter



class WebdriverElement(WebElement):

    def __init__(self, page, key, timeout = 5):
        self._element = None
        self.page = page
        self.key = key
        self._driver = BrowserManager.get_driver("")
        self.timeout = timeout

    def __repr__(self):
        repr = "ELEMENT: %s.%s" % (self.page,self.key)
        return repr

    @property
    def driver(self):
       return self._driver

    @property
    def element(self):
        self.locators = self.get_locators()
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
                    print "Found element %s" % self._element.html
                    self._element.highlight()
                    return self._element
            else:
                print "Found element %s" % self._element.html
                self._element.highlight()
                return self._element
            logging.debug("Waiting for element %s" % self)
            time.sleep(1)
        raise exceptions.NoSuchElementException("Could not find an element matching any of the following locators: {}".format(self.locators))

    def get_locators(self):
        adapter = WebdriverAdapter(self.driver,self.page,self.key)
        locators = adapter.get_locators()
        return locators
