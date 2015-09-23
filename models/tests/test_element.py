import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.element_state import ElementState, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager

class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        element = ElementState(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        cls.element_id = element.id

    def test_save(self):
        assert self.element_id is not None

    def test_get_elements(self):
        elements = ElementState.objects[:4]
        assert len(elements) == 4

    def test_get_element(self):
        elements = ElementState.objects(id=self.element_id)
        for element in elements:
            print element.id

