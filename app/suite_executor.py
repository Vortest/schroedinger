class SuiteExecutor:
    class SuiteConfig:
        def __init__(self, suite, browsers, data):
            self.suite = suite
            self.browsers = browsers
            self.data = data

    def __init__(self, suite, config):
        self.suite = suite
        self.config = config


