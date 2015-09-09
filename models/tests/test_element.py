import unittest
from selenium.webdriver.common.by import By
from app.test_base import TestBase
from models.element import Element, Locator
from models.post import Post, Comment


class TestElement(unittest.TestCase):
    def test_save_element(self):
        element = Element()
        element.locators.append(Locator(by=By.NAME,value="q"))
        element.save()
        print element.id

    def test_load_element(self):
        elements = Element.objects.all()
        for element in elements:
            print element.locators