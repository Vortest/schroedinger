from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.result import Result
from models.state import State
from models.suite import Suite
from models.test import Test

class TestSuite(TestBase):
    def test_save_test(self):
        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        state1 = State(elements=[], url="")
        state2= State(elements=[element], url="http://www.google.com")
        state1.save()
        state2.save()
        commands = [Command(command=Command.NAVIGATE,params="http://www.google.com/"),
                    Command(command=Command.SENDKEYS,element = element,params="Something")]
        action = Action(name = "Some Action",steps=commands,start_state=state1, end_state=state2)
        action.save()
        test = Test(name="Some test", actions = [action])
        test.save()
        suite = Suite(tests=[test], url="http://www.google.com./")
        suite.execute(self.driver)
        suite.save()
        assert suite.suite_results[-1].passed, suite.suite_results[-1].message