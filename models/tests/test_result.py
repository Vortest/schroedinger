from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element_state import ElementState, Locator
from models.state import State
from models.suite import Suite
from models.test import Test

class TestResult(TestBase):

    def test_save_result(self):
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
        commands = [Command(command=Command.NAVIGATE,params="http://www.google.com/"),
                    Command(command=Command.SENDKEYS,element = element,params="Something"),
                    Command(command=Command.CLICK,element=element2)]
        action = Action(name = "Google Search",steps=commands,start_state=state1, end_state=state3)
        action.save()
        test = Test(name="Some test",actions=[action])
        test.save()
        suite = Suite(name="some name",tests=[test])
        suite.execute(self.driver)
        suite.save()
        assert suite.suite_results[-1].passed, suite.suite_results[-1].message
        assert suite.suite_results[-1].step_results[-1].passed, suite.suite_results[-1].step_results[-1].exception
        assert suite.suite_results[-1].step_results[-1].step_results[0].step_results[2].passed

    def test_failure_report(self):
        element = ElementState(locators = [Locator(by=By.NAME,value="INVALID")])
        element2= ElementState(locators= [Locator(by=By.NAME,value="INVALID")])
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
        suite = Suite(name="some name",tests=[test])
        suite.execute(self.driver)
        suite.save()
        assert not suite.suite_results[-1].passed
        assert suite.suite_results[-1].actual_state is not None
        assert suite.suite_results[-1].failed_state is not None
        assert suite.suite_results[-1].html is not None and not ""
        assert suite.suite_results[-1].screenshot is not None and not ""
