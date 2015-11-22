from app import browser_launcher


class SuiteExecutor:
    def __init__(self, suite, configs):
        self.suite = suite
        self.configs = configs

    def execute(self):
        for config in self.configs.configs:
            self.driver = browser_launcher.launch_browser(config)
            self.suite.execute(self.driver, config.params)
            self.driver.quit()

