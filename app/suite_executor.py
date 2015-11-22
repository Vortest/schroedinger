from app import browser_launcher


class SuiteExecutor:
    def __init__(self, suite, configs):
        self.suite = suite
        self.configs = configs

    def execute(self):
        for config in self.configs:
            self.driver = browser_launcher.launch_browser(self.config)
            results = self.suite.execute(self.driver, self.config)
            self.driver.quit()
            return results
