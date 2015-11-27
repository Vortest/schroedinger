from app.browser_session import BrowserSession
from app.suite_executor import SuiteExecutor
from app.test_builder import TestGenerator
from models.suite import Suite
from models.suite_config import RunConfig, SuiteConfig
from models.tests.test_suite import TestSuite


class SuiteGenerator(object):
    def __init__(self, browsers):
        self.browsers = browsers
        self.configs=[]
        for browser in self.browsers:
            if browser.lower() == "iphone":
                config = RunConfig(browser="Chrome", device_name="Apple iPhone 5", host="localhost")
            elif browser.lower() == "ipad":
                config = RunConfig(browser="Chrome", device_name="Apple iPad", host="localhost")
            elif browser.lower() == "kindle":
                config = RunConfig(browser="Chrome", device_name="Amazon Kindle Fire HDX", host="localhost")
            elif browser.lower() == "galaxy":
                config = RunConfig(browser="Chrome", device_name="Samsung Galaxy S4", host="localhost")
            else:
                config = RunConfig(browser=browser)
            self.configs.append(config)

    def generate_suite(self, url):
        suite = Suite(url=url,name="Generated Navigation Suite")
        suite_config = SuiteConfig(suite=suite)
        for config in self.configs:
            params = {"url":url}
            config.params = params
            suite_config.configs.append(config)
            session = BrowserSession(config)
            session.start_session()
            self.driver = session.driver
            generator = TestGenerator(self.driver)
            test = generator.generate_navigate_test(url)
            suite.tests.append(test)

        suite_config.save()
        suite.suite_config = suite_config
        suite.save()
        session.end()
        return suite