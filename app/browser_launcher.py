from selenium import webdriver

import config
from webdriver_wrapper import WebDriver
import logging

def launch_browser(config=None):
    for i in range(0,3):
        try:
            if config:
                browser = config.browser
            else:
                browser = "Firefox"
            if browser == "Firefox":
                driver = webdriver.Firefox()
            elif browser == "Chrome":
                driver = webdriver.Chrome()
            else:
                raise ValueError("Unsupported Browser: %s" % browser)
            # driver.maximize_window()
            print "Launched browser %s" % browser
            return WebDriver(driver)
        except Exception as e:
            logging.exception("Could not launch browser : %s" % str(e))
