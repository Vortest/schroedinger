from app.suite_executor import SuiteExecutor
from app.test_builder import TestGenerator
from models.suite import Suite
from models.suite_config import RunConfig, SuiteConfig
from models.tests.test_suite import TestSuite


class SuiteGenerator(object):
    def __init__(self, driver):
        self.driver = driver
        
    def generate_suite(self, url, browsers):
        generator = TestGenerator(self.driver)
        params = {"url":url,"search":"Something"}
        test = generator.generate_navigate_test(url)
        suite = Suite(tests=[test], url=url,name="Generated Navigation Suite")

        configs = []
        for browser in browsers:
            config1 = RunConfig(browser=browser, params = params)
            configs.append(config1)
        config = SuiteConfig(configs=configs, suite=suite)
        suite.config = config
        suite.save()
        return suite