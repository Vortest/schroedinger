import logging
from selenium import webdriver

from webdriver_wrapper import WebDriver

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

    def start_session(self):
        logging.debug("Starting %s session for %s %s" % (self.config.host, self.config.browser, self.config.device_name))
        if self.config.host == "localhost" and self.config.device_name !="":
            self.start_emulated_session()
        elif self.config.host == "sauce":
            self.start_sauce_session()
        else:
            self.start_local_session()

    def start_sauce_session(self):
        driver = webdriver.Remote(
            command_executor=BrowserSession.SAUCE_HOST % (self.config.sauce_user, self.config.sauce_key),
            desired_capabilities=self.desired_caps
        )
        self.driver = WebDriver(driver)

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

    def start_emulated_session(self):
        mobile_emulation = { "deviceName": self.config.device_name}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(chrome_options = chrome_options)
        self.driver = WebDriver(driver)


    def start_remote_session(self):
        driver = webdriver.Remote(
            command_executor=BrowserSession.REMOTE_HOST % (self.config.host,self.config.port),
            desired_capabilities=self.desired_caps
        )
        self.driver = WebDriver(driver)

    def start_local_session(self):
        browser = str(self.config.browser).lower()
        if browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "chrome":
            driver = webdriver.Chrome()
        self.driver = WebDriver(driver)

    def set_resolution(self):
        self.driver.set_window_size(self.config.width, self.config.height)

    def use_defaults(self, device):
        self.browser = device["browserName"]
        self.version = device["version"]
        self.platform = device["platform"]

    def end(self):
        self.driver.quit()