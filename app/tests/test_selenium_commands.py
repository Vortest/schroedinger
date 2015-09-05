from selenium.webdriver.common.by import By
from app.element import Element
from app.test_base import TestBase
from app.selenium_command import SeleniumCommand

class TestSeleniumCommands(TestBase):
    def test_click(self):
        self.driver.get("http://www.google.com/")
        command = SeleniumCommand(driver=self.driver, command=SeleniumCommand.CLICK,locator=[(By.NAME,"q")])
        results = command.execute()
        assert results.passed, results.message

    def test_send_keys(self):
        self.driver.get("http://www.google.com/")
        command = SeleniumCommand(driver=self.driver, command=SeleniumCommand.SENDKEYS,locator=[(By.NAME,"q")],params="Something")
        results = command.execute()

        assert Element(self.driver, [(By.NAME,"q")]).value == "Something"
        assert results.passed, results.message

    def test_navigate(self):
        self.driver.get("http://www.google.com/")
        command = SeleniumCommand(driver=self.driver, command=SeleniumCommand.NAVIGATE,params="http://www.google.com/")
        results = command.execute()

        assert "google" in self.driver.current_url
        assert results.passed, results.message