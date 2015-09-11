import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager
from models.state import State


class TestAction(TestBase):

    def test_save_action(self):

        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        state1 = State(elements=[element], url="http://www.google.com")
        state2= State(elements=[element], url="http://www.google.com")
        state1.save()
        state2.save()
        commands = [Command(command=Command.NAVIGATE,params="http://www.google.com/"),
                    Command(command=Command.SENDKEYS,element = element,params="Something")]
        action = Action(name = "Some Action",steps=commands,start_state=state1, end_state=state2)
        action.save()
        state1.actions = [action]
        state1.save()
        print state1.id
        assert state1.actions[0].steps == commands
        assert state1.actions[0].end_state == state2

    def test_execute(self):

        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element2= Element(locators= [Locator(by=By.NAME,value="btnG")])
        element.save()
        element2.save()
        state1 = State(elements=[], url="")
        state2= State(elements=[element], url="http://www.google.com")
        state3= State(elements=[element2], url="http://www.google.com")
        state1.save()
        state2.save()
        state3.save()
        commands = [Command(command=Command.NAVIGATE,params="http://www.google.com/"),
                    Command(command=Command.SENDKEYS,element = element,params="Something"),
                    Command(command=Command.CLICK,element=element2)]
        action = Action(name = "Google Search",steps=commands,start_state=state1, end_state=state3)
        action.save()
        results = action.execute(self.driver)
        assert results.passed, results.message

