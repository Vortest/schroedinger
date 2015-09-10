import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager
from models.state import State


class TestAction(unittest.TestCase):

    def test_action(self):

        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        state1 = State(elements=[element], url="http://www.google.com")
        state2= State(elements=[element], url="http://www.google.com")
        state1.save()
        state2.save()
        commands = [Command(command=Command.NAVIGATE,params="http://www.google.com/"),
                    Command(command=Command.SENDKEYS,element = element,params="Something")]
        action = Action(name = "Some Action",commands=commands,end_state=state2)
        state1.actions = [action]
        state1.save()
        assert state1.actions[0].commands == commands
        assert state1.actions[0].end_state == state2




