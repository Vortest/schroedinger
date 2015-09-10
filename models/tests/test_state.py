import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.element import Element, Locator
from models.post import Post, Comment
from models.state import State


class TestState(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.locator = Locator(by=By.NAME, value="q")
        element = Element(locators = [cls.locator])
        element.save()
        state = State(elements = [element], url="http://www.google.com")
        state.save()
        cls.state_id = state.id

    def test_save_state(self):
        assert self.state_id is not None

    def test_state_element(self):
        state = State.objects(id=self.state_id).first()
        element = state.elements[0]
        assert len(element.locators) == 1

    def test_get_state(self):
        state = State.objects(id=self.state_id)[0]
        assert state.id == self.state_id

    def test_update_element_locator(self):
        state = State.objects(id=self.state_id).first()
        element = state.elements[0]
        old_locator = element.locators[0]
        element_id = element.id
        new_locator = Locator(by=By.XPATH,value="//something")
        new_element = Element.objects(id=element_id).first()
        new_element.locators[0] = new_locator
        new_element.save()

        newstate = State.objects(id=self.state_id).first()
        element = newstate.elements[0]
        newlocator = element.locators[0]

        assert newlocator == new_locator
        assert newlocator != old_locator