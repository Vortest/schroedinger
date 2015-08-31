import unittest
from browser_manager import BrowserManager
import config
import logging
from page_parser import PageParser
import webelement_wrapper

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = BrowserManager.get_driver()

    def test(self):
        logging.debug("Test")
        parser = PageParser("http://www.google.com/")
        eles = parser.get_all_elements()
        for ele in eles:
            ele.highlight()

    def tearDown(self):
        self.driver.quit()



    #open page
    #parse page
    #parse elements
    #build locators
    #create elements
    #create state
    #save page