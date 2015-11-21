from app import browser_launcher


class SuiteExecutor:
    def __init__(self, suite, config):
        self.suite = suite
        self.config = config

    def execute(self):
        self.driver = browser_launcher.launch_browser(self.config)
        results = self.suite.execute(self.driver, self.config)
        self.driver.quit()
        return results
