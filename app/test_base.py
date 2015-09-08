import unittest
import logging
from browser_manager import BrowserManager
import thread
import threading

class TestBase(unittest.TestCase):
    test_names = []
    test_name = None

    @property
    def driver(self):
        return BrowserManager.get_driver(TestBase.test_name)

    def setUp(self):
        TestBase.test_name = self._testMethodName
        logging.debug("set up test %s" % self._testMethodName)
        logging.debug("THREAD :%s" % threading.currentThread().ident)

    def tearDown(self):
        logging.debug("tear down test %s" % self._testMethodName)
        try:
            self.driver.quit()
        except Exception as e:
            logging.exception("Exception caught quitting browser : %s" % str(e))

    @classmethod
    def setUpClass(cls):
        logging.debug("set up class %s" % cls.__name__)

    @classmethod
    def tearDownClass(cls):
        logging.debug("tear down class %s" % cls.__name__)