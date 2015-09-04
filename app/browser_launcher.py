from selenium import webdriver

import config
from webdriver_wrapper import WebDriver


def launch_browser():
    if config.BROWSER == "Firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Unsupported Browser: %s" % config.BROWSER)
    return WebDriver(driver)
