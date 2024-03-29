import unittest
from selenium.webdriver.common.by import By
from app import state_builder
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element_state import ElementState, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager
from models.state import State
import app.action_builder as action_builder
from models.suite_config import RunConfig


class TestAction(TestBase):

    def test_save_action(self):
        element = ElementState(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        google_home = State(url=self.driver.current_url, elements=[element])
        google_home.save()
        action = action_builder.get_nav_action("http://www.google.com/",google_home)
        action.save()

        state1 = State(elements=[element], url="http://www.google.com")
        state1.save()


        state2= State(elements=[element], url="http://www.google.com")

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

        element = ElementState(locators = [Locator(by=By.NAME,value="q")])
        element2= ElementState(locators= [Locator(by=By.NAME,value="btnG")])
        element.save()
        element2.save()
        state1 = State(elements=[], url="")
        state2= State(elements=[element], url="http://www.google.com")
        state3= State(elements=[element2], url="http://www.google.com")
        state1.save()
        state2.save()
        state3.save()
        commands = [Command(command=Command.NAVIGATE,config_key="url"),
                    Command(command=Command.SENDKEYS,element = element,config_key="search"),
                    Command(command=Command.CLICK,element=element2)]
        action = Action(name = "Google Search",steps=commands,start_state=state1, end_state=state3)
        action.save()
        results = action.execute(self.driver,config=RunConfig(params={"url":"http://www.google.com/","search":"Something"}))


    def test_verify_state_action(self):

        element = ElementState(locators = [Locator(by=By.NAME,value="q")])
        element2= ElementState(locators= [Locator(by=By.NAME,value="btnK")])
        element.save()
        element2.save()
        state1 = State(elements=[], url="")
        state1.save()

        state = State(elements=[element], url="http://www.google.com")
        state.save()
        verify_state = action_builder.get_verify_state_action(state)
        commands = [Command(command=Command.NAVIGATE,config_key="url")]
        action = Action(name = "Google Nav",steps=commands,start_state=state1, end_state=state)
        action.save()
        state.actions = []

        results = action.execute(self.driver, config=RunConfig(params={"url":"http://www.google.com/","search":"Something"}))