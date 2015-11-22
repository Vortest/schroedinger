from selenium import webdriver

class BrowserSession(object):
    SAUCE_HOST = "http://%s:%s@ondemand.saucelabs.com:80/wd/hub"
    REMOTE_HOST = "http://%s:%s/wd/hub"
    def __init__(self, config):
        self.config = config

    @property
    def desired_caps(self):
        return {
            "deviceName" : self.config.device_name,
            "browserName": self.config.browser,
            "platform": self.config.platform,
            "version": self.config.version,
            "deviceOrientation": self.config.orientation
        }

    def start_sauce_session(self):
        self.driver = webdriver.Remote(
            command_executor=BrowserSession.SAUCE_HOST % (self.config.sauce_user, self.config.sauce_key),
            desired_capabilities=self.desired_caps
        )

    def get_caps(self):
        if self.browser == "Firefox":
            self.use_defaults(webdriver.DesiredCapabilities.FIREFOX)
        elif self.browser == "Chrome":
            self.use_defaults(webdriver.DesiredCapabilities.CHROME)
        elif self.browser == "IE":
            self.use_defaults(webdriver.DesiredCapabilities.INTERNETEXPLORER)
        elif self.browser == "Safari":
            self.use_defaults(webdriver.DesiredCapabilities.SAFARI)
        elif self.browser == "IPhone":
            self.use_defaults(webdriver.DesiredCapabilities.IPHONE)
        elif self.browser == "IPad":
            self.use_defaults(webdriver.DesiredCapabilities.IPAD)
        elif self.browser == "Android":
            self.use_defaults(webdriver.DesiredCapabilities.ANDROID)


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