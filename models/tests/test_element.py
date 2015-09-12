import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.element import Element, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager

class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        element = Element(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        cls.element_id = element.id

    def test_save(self):
        assert self.element_id is not None

    def test_get_elements(self):
        elements = Element.objects[:10]
        assert len(elements) == 10

    def test_get_element(self):
        elements = Element.objects(id=self.element_id)
        for element in elements:
            print element.id