from selenium.webdriver.common.by import By

from app.webelement import WebElement
from app.test_base import TestBase
from models.command import Command


class TestSeleniumCommands(TestBase):
    def test_click(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.CLICK,locator=[(By.NAME,"q")])
        results = command.execute()
        assert results.passed, results.message

    def test_send_keys(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.SENDKEYS,locator=[(By.NAME,"q")],params="Something")
        results = command.execute()

        assert WebElement(self.driver, [(By.NAME,"q")]).value == "Something"
        assert results.passed, results.message

    def test_navigate(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.NAVIGATE,params="http://www.google.com/")
        results = command.execute()

        assert "google" in self.driver.current_url
        assert results.passed, results.message