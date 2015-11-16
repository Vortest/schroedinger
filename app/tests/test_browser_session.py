import unittest
from selenium import webdriver
from app.browser_session import BrowserSession


class TestBrowserSession(unittest.TestCase):
    def test_launch_local(self):
        session = BrowserSession()
        session.browser = "Firefox"
        session.start_local_session()
        session.driver.get("http://www.google.com")
        session.driver.quit()

    def test_sauce(self):
        session = BrowserSession()
        session.browser = "Firefox"
        session.sauce_user = "bkitchener1"
        session.sauce_key = ""
        session.use_defaults(webdriver.DesiredCapabilities.FIREFOX)
        session.start_sauce_session()
        session.driver.get("http://www.google.com")
        session.driver.quit()