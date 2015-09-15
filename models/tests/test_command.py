import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager

class TestCommand(TestBase):
    @classmethod
    def setUpClass(cls):
        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        command = Command(command=Command.SENDKEYS,element=element,params="Something")
        cls.element_id = command.element.id

    def test_params(self):
        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        command = Command(command=Command.SENDKEYS,element=element,params="Something")

    def test_invalid_command(self):
        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        command = Command(command="INVALID",element=element,params="Something")
        response = command.execute(self.driver)
        assert not response.passed, response.exception

    def test_execute(self):
        command = Command(command=Command.NAVIGATE,params="http://www.google.com/")
        command.execute(self.driver)


