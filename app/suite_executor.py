from selenium import webdriver
from app import browser_launcher
from app.browser_session import BrowserSession


class SuiteExecutor:
    def __init__(self, suite, configs):
        self.suite = suite
        self.configs = configs

    def execute(self):
        for config in self.configs.configs:
            session = BrowserSession()
            session.browser = config.browser
            session.sauce_user = "bkitchener1"
            session.sauce_key = "c479e821-57e7-4b3f-8548-48e520585187"
            session.use_defaults(webdriver.DesiredCapabilities.FIREFOX)
            session.start_sauce_session()
            self.driver = browser_launcher.launch_browser(config)
            self.suite.execute(self.driver, config.params)
            self.driver.quit()

