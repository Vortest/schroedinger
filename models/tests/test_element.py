import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.expected_element import ExpectedElement, Locator
from models.post import Post, Comment
from app.browser_manager import BrowserManager

class TestElement(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        element = ExpectedElement(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        cls.element_id = element.id

    def test_save(self):
        assert self.element_id is not None

    def test_get_elements(self):
        elements = ExpectedElement.objects.all()
        assert len(elements) > 0

    def test_get_element(self):
        elements = ExpectedElement.objects(id=self.element_id)
        for element in elements:
            print element.id