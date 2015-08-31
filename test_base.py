import unittest
import logging
from browser_manager import BrowserManager

class TestBase(unittest.TestCase):

    @property
    def driver(self):
        return BrowserManager.get_driver(self._testMethodName)

    def setUp(self):
        self.test_name = self._testMethodName
        logging.debug("set up test %s" % self._testMethodName)

    def tearDown(self):
        logging.debug("tear down test %s" % self._testMethodName)
        self.driver.quit()

    @classmethod
    def setUpClass(cls):
        logging.debug("set up class %s" % cls.__name__)

    @classmethod
    def tearDownClass(cls):
        logging.debug("tear down class %s" % cls.__name__)