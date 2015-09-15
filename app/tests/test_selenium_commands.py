from selenium.webdriver.common.by import By
from app.webelement import WebElement
from app.test_base import TestBase
from models.command import Command
from models.element import Element, Locator


class TestSeleniumCommands(TestBase):
    def test_click(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.CLICK,element=Element(locators=[Locator(by=By.NAME,value="q")]))
        command.execute(self.driver)

    def test_send_keys(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.SENDKEYS,element=Element(locators=[Locator(by=By.NAME,value="q")]),params="Something")
        command.execute(self.driver)

        assert WebElement(self.driver, [Locator(by=By.NAME,value="q")]).value == "Something"

    def test_navigate(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.NAVIGATE,params="http://www.google.com/")
        command.execute(self.driver)

        assert "google" in self.driver.current_url
