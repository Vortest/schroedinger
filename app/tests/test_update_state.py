from selenium.webdriver.common.by import By
from app import state_builder
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.state import State
from models.suite import Suite
from models.test import Test


class TestUpdateState(TestBase):
    def test_update_failing_test(self):
        element = Element(locators = [Locator(by=By.NAME,value="INVALID")])
        element2= Element(locators= [Locator(by=By.NAME,value="INVALID")])
        element.save()
        element2.save()
        state1 = State(elements=[], url="")
        state2= State(elements=[element], url="http://www.google.com")
        state3= State(elements=[element2], url="http://www.google.com")
        state1.save()
        state2.save()
        state3.save()
        commands1 = [Command(command=Command.NAVIGATE,params="http://www.google.com/")]
        commands2 = [Command(command=Command.SENDKEYS,element = element,params="Something")]
        nav_action = Action(name = "Google Nav",steps=commands1,start_state=state1, end_state=state2)
        search_action = Action(name = "Google Search",steps=commands2,start_state=state2, end_state=state3)
        nav_action.save()
        search_action.save()
        test = Test(name="Google Search Failure",actions=[nav_action,search_action])
        test.save()
        suite = Suite(name="Failure Example",tests=[test])
        suite.execute(self.driver)
        suite.save(cascade=True)

        state_diff = suite.suite_results[-1].failed_state - suite.suite_results[-1].actual_state
        assert len(state_diff.elements) == 1

    def test_missing_elements(self):
        self.driver.get("http://www.google.com/")
        state = state_builder.get_current_state(self.driver)
        state.save()
        state.elements.remove(state.elements[0])
        extra = state_builder.get_extra_elements(self.driver, state)
        assert len(extra) == 1, len(extra)