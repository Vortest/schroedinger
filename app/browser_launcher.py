from selenium import webdriver

import config
from webdriver_wrapper import WebDriver
import logging

def launch_browser():
    for i in range(0,3):
        try:
            if config.BROWSER == "Firefox":
                driver = webdriver.Firefox()
            else:
                raise ValueError("Unsupported Browser: %s" % config.BROWSER)
            return WebDriver(driver)
        except Exception as e:
            logging.exception("Could not launch browser : %s" % str(e))
