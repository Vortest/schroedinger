import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from element import Element
from test_base import TestBase
from selenium.common import exceptions

class FilterTest(TestBase):
    def test_element_equal(self):
        locators1 = [(By.NAME,"q")]
        locators2 = [(By.NAME,"q")]
        element1 = Element(self.driver, locators1)
        element2 = Element(self.driver, locators2)

        assert element1 == element2
        assert element2 == element1

    def test_different_locators_equal(self):
        locators1 = [(By.NAME,"q"),(By.CLASS_NAME,"foo")]
        locators2 = [(By.CLASS_NAME,"bar"),(By.NAME,"q")]
        element1 = Element(self.driver, locators1)
        element2 = Element(self.driver, locators2)

        assert element1 == element2
        assert element2 == element1

    def test_missing_locator_fails(self):
        locators1 = [(By.NAME,"z"),(By.CLASS_NAME,"foo")]
        locators2 = [(By.NAME,"bar"),(By.NAME,"q")]
        element1 = Element(self.driver, locators1)
        element2 = Element(self.driver, locators2)

        with self.assertRaises(AssertionError):
            assert element1 == element2
            assert element2 == element1

    def test_inequality(self):
        locators1 = [(By.NAME,"z"),(By.CLASS_NAME,"foo")]
        locators2 = [(By.NAME,"bar"),(By.NAME,"q")]
        element1 = Element(self.driver, locators1)
        element2 = Element(self.driver, locators2)

        assert element1 != element2
        assert element2 != element1



