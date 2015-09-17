from selenium.webdriver.common.by import By
from app import state_builder
from app.state_comparer import StateComparer
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.state import State
from models.suite import Suite
from models.test import Test
from app import element_filter
from app.state_comparer import StateComparer

class TestUpdateState(TestBase):
    def test_compare_state(self):
        self.driver.get("http://www.google.com/")
        state1 = state_builder.get_blank_state()
        state1.save()
        state2 = state_builder.get_current_state(self.driver)
        state2.save()
        self.driver.get("https://www.google.com/#q=something")
        state3 = state_builder.get_current_state(self.driver)
        state3.save()

        search_fields = element_filter.filter_contains_text(state2.elements,"Search")
        search_field = search_fields[0]
        commands1 = [Command(command=Command.NAVIGATE,params="http://www.google.com/")]
        commands2 = [Command(command=Command.SENDKEYS,element = search_field,params="Something")]
        nav_action = Action(name = "Google Nav",steps=commands1,start_state=state1, end_state=state2)
        search_action = Action(name = "Google Search",steps=commands2,start_state=state2, end_state=state3)
        nav_action.save()
        search_action.save()
        test = Test(name="Google Search Failure",actions=[nav_action,search_action])
        test.save()
        suite = Suite(name="Failure Example",tests=[test])
        suite.execute(self.driver)
        suite.save(cascade=True)
        print suite.id
        assert suite.suite_results[-1].passed

        # search_field.locators = [Locator(by=By.CLASS_NAME,value="INVALID")]
        # search_field.save()
        suite.execute(self.driver)
        results = suite.suite_results[-1]
        assert not results.passed

        comparison = StateComparer(self.driver).compare_state(results.failed_state, results.actual_state)

        assert len(comparison[0].elements) == len(comparison[1].elements)



    def test_missing_elements(self):
        self.driver.get("http://www.google.com/")
        state = state_builder.get_current_state(self.driver)
        state.save()
        state.elements.remove(state.elements[0])
        extra = state_builder.get_extra_elements(self.driver, state)
        assert len(extra) == 1, len(extra)