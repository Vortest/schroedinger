from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from app.test_builder import TestGenerator
from app.webelement import WebElement
from app import state_builder
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element_state import Locator, ElementState


class TestTestGenerator(TestBase):
    def test_generate_nav_test(self):
        generator = TestGenerator(self.driver)
        test = generator.generate_navigate_test("http://www.google.com/")
        result = test.execute(self.driver)
        assert result.passed, result.message