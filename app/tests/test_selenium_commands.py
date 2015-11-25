from selenium.webdriver.common.by import By
from app.webelement import WebElement
from app.test_base import TestBase
from models.command import Command
from models.element_state import ElementState, Locator
from models.suite_config import RunConfig


class TestSeleniumCommands(TestBase):
    def test_click(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.CLICK,element=ElementState(locators=[Locator(by=By.NAME,value="q")]))
        command.execute(self.driver, config=RunConfig())

    def test_send_keys(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.SENDKEYS,element=ElementState(locators=[Locator(by=By.NAME,value="q")]),config_key="search")
        command.execute(self.driver, config=RunConfig(params={"search":"Something"}))

        assert WebElement(self.driver, [Locator(by=By.NAME,value="q")]).value == "Something"

    def test_navigate(self):
        self.driver.get("http://www.google.com/")
        command = Command(driver=self.driver, command=Command.NAVIGATE,config_key="url")
        command.execute(self.driver, config=RunConfig(params={"url":"http://www.google.com/"}))

        assert "google" in self.driver.current_url
