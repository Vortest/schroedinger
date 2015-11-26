from selenium import webdriver
from app import browser_launcher
from app.browser_session import BrowserSession


class SuiteExecutor:
    def __init__(self, suite):
        self.suite = suite

    def execute(self):
        for config in self.suite.suite_config.configs:
            browser = BrowserSession(config)
            browser.start_session()
            self.driver = browser.driver
            self.suite.execute(self.driver, config)
            self.driver.quit()

