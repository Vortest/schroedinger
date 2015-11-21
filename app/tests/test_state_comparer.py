from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app import state_builder
from app.state_comparer import StateComparer
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element_state import ElementState, Locator
from models.state import State
from models.suite import Suite
from models.test import Test
from app import element_filter

class TestStateComparer(TestBase):
    def test_get_compare(self):

        element = ElementState(locators = [Locator(by=By.LINK_TEXT,value="Images")])
        element.save()
        element2 = ElementState(locators = [Locator(by=By.NAME,value="INVALID")])
        element2.save()
        state2= State(elements=[element,element2], url="http://www.google.com")
        state2.save()

        self.driver.get("http://www.google.com")
        comparer = StateComparer(self.driver)
        comparison = comparer.compare_to_live_state(state2)

        assert comparison == (1,19), comparison

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

        search_field.locators = [Locator(by=By.CLASS_NAME,value="INVALID")]
        search_field.save()
        suite.execute(self.driver)
        results = suite.suite_results[-1]
        assert not results.passed


        comparison = StateComparer(self.driver).compare_states(results.failed_state, results.actual_state)

        assert len(comparison[0].elements) == len(comparison[1].elements)

    def test_match_elements(self):
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
        assert suite.suite_results[-1].passed, suite.suite_results[-1].exception

        search_field.locators = [Locator(by=By.CLASS_NAME,value="INVALID")]
        search_field.save()
        suite = Suite(name="Failure Example",tests=[test])
        suite.execute(self.driver)
        suite.save(cascade=True)
        print suite.id
        results = suite.suite_results[-1]
        assert not results.passed, results.message
        comparer = StateComparer(self.driver)
        elements = comparer.match_elements(results.failed_state, results.actual_state)
        for element in elements:
            old_element = element[0]
            new_element = element[1]
            old_element.locators = new_element.locators
            old_element.save()

        suite.execute(self.driver)
        assert suite.suite_results[-1].passed, suite.suite_results[-1].exception

