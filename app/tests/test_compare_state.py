from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from app import state_builder
from app.state_comparer import StateComparer
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element import Element, Locator
from models.state import State
from models.suite import Suite
from models.test import Test


class TestUpdateState(TestBase):
    def test_compare_state(self):

        element = Element(locators = [Locator(by=By.LINK_TEXT,value="Images")])
        element.save()
        element2 = Element(locators = [Locator(by=By.NAME,value="INVALID")])
        element2.save()
        state2= State(elements=[element,element2], url="http://www.google.com")
        state2.save()

        self.driver.get("http://www.google.com")
        comparer = StateComparer(self.driver)
        comparison = comparer.get_compare(state2)

        assert comparison == (1,15), comparison
