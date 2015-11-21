from selenium import webdriver

import config
from webdriver_wrapper import WebDriver
import logging

def launch_browser(browser = "Firefox"):
    for i in range(0,3):
        try:
            if browser == "Firefox":
                driver = webdriver.Firefox()
            elif browser == "Chrome":
                driver = webdriver.Chrome()
            else:
                raise ValueError("Unsupported Browser: %s" % config.BROWSER)
            # driver.maximize_window()
            return WebDriver(driver)
        except Exception as e:
            logging.exception("Could not launch browser : %s" % str(e))
