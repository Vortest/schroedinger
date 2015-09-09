import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.element import Element, Locator
from models.post import Post, Comment
from models.state import State


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.locator = Locator(by=By.NAME, value="zq")
        element = Element(locators = [cls.locator])
        element.save()
        state = State(elements = [element])
        state.save()
        cls.state_id = state.id

    def test_save_state(self):
        assert self.state_id is not None

    def test_state_element(self):
        state = State.objects(id=self.state_id)[0]
        element = state.elements[0]
        assert len(element.locators) == 1

    def test_get_state(self):
        state = State.objects(id=self.state_id)[0]
        assert state.id == self.state_id


