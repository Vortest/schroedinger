from selenium import webdriver

class BrowserSession(object):
    SAUCE_HOST = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    REMOTE_HOST = "http://%s:%s/wd/hub"

    def __init__(self):
        self.width = 0
        self.height = 0
        self.host = ""
        self.port = ""
        self.sauce_user = ""
        self.sauce_key = ""
        self.browser = ""
        self.version = ""
        self.platform = ""

    @property
    def desired_caps(self):
        return {
            "platform": self.platform,
            "browserName": self.browser,
            "version": self.version
        }

    def start_sauce_session(self):
        self.driver = webdriver.Remote(
            command_executor=BrowserSession.SAUCE_HOST % (self.sauce_user, self.sauce_key),
            desired_capabilities=self.desired_caps
        )

    def start_remote_session(self):
        self.driver = webdriver.Remote(
            command_executor=BrowserSession.REMOTE_HOST % (self.host,self.port),
            desired_capabilities=self.desired_caps
        )

    def start_local_session(self):
        if self.browser == "Firefox":
            self.driver = webdriver.Firefox()
        elif self.browser == "Chrome":
            self.driver = webdriver.Chrome()

    def set_resolution(self):
        self.driver.set_window_size(self.width, self.height)

    def use_defaults(self, device):
        self.browser = device["browserName"]
        self.version = device["version"]
        self.platform = device["platform"]

    def end(self):
        self.driver.quit()