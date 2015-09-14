from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.state import State
from models.suite import Suite
from models.test import Test

class TestResult(TestBase):

    def test_save_result(self):
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
        test = Test(name="Some test",actions=[action])
        test.save()
        self.suite = Suite(name="some name",tests=[test])
        self.suite.save()
        self.suite.execute(self.driver)
        self.suite.save()
        #assert self.suite.results[-1].passed, self.suite.results[-1].message

    def test_failure_report(self):
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
        test = Test(name="Some test",actions=[action])
        test.save()
        self.suite = Suite(name="some name",tests=[test])
        self.suite.save()
        self.suite.tests[0].actions[0].steps[1].element.locators[0].value="zx"
        self.suite.save()
        self.suite.execute(self.driver)
        #assert TestResult.suite.results[-1].passed
