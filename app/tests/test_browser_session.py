import unittest
from selenium import webdriver
from app.browser_session import BrowserSession
from models.suite_config import SuiteConfig, RunConfig


class TestBrowserSession(unittest.TestCase):
    def test_launch_local(self):
        session = BrowserSession()
        session.browser = "Firefox"
        session.start_local_session()
        session.driver.get("http://www.google.com")
        session.driver.quit()

    def test_firefox(self):
        config = RunConfig(browser = "Firefox", sauce_user = "bkitchener1", sauce_key = "c479e821-57e7-4b3f-8548-48e520585187")
        session = BrowserSession(config)
        session.start_sauce_session()
        session.driver.get("http://www.google.com")
        session.driver.quit()

    def test_iphone_6(self):
        config = RunConfig(browser = "Safari", device_name="iPhone 6", version="8.0", sauce_user = "bkitchener1", sauce_key = "c479e821-57e7-4b3f-8548-48e520585187")
        session = BrowserSession(config)
        session.start_sauce_session()
        session.driver.get("http://www.google.com")
        session.driver.quit()