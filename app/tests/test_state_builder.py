from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from app.webelement import WebElement
from app import state_builder
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element_state import Locator, ElementState


class StateTest(TestBase):
    def test_builder_reuses_elements(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        new_state = state_builder.get_new_state(self.driver, state)
        for newelement in new_state.elements:
            found = False
            for stateelement in state.elements:
                if newelement.id == stateelement.id:
                    found = True
            assert found, "Element ID not found, element was not reused %s" % newelement.id

    def test_buidler_reuses_some_elemnts(self):
        self.url = "http://www.google.com/"
        self.driver.get(self.url)
        state = state_builder.get_current_state(self.driver)
        self.driver.get("https://images.google.com/?gws_rd=ssl")
        new_state = state_builder.get_new_state(self.driver, state)
        count = 0
        for newelement in new_state.elements:
            found = False
            for stateelement in state.elements:
                if newelement.id == stateelement.id:
                    count += 1

        assert count >= 10, count

