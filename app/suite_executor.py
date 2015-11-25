from selenium import webdriver
from app import browser_launcher
from app.browser_session import BrowserSession


class SuiteExecutor:
    def __init__(self, suite, configs):
        self.suite = suite
        self.configs = configs

    def execute(self):
        for config in self.configs.configs:
            browser = BrowserSession(config)
            browser.start_local_session()
            self.driver = browser.driver
            self.suite.execute(self.driver, config)
            self.driver.quit()

