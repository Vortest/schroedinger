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
from models.suite_config import SuiteConfig, RunConfig


class TestTestGenerator(TestBase):
    def test_generate_google_nav_test(self):
        generator = TestGenerator(self.driver)
        config=RunConfig(params={
            "url":"http://www.google.com/"
        })
        test = generator.generate_navigate_test("http://www.google.com/")
        for i in range(0,5):
            result = test.execute(self.driver, config)
            assert result.passed, result.message

    def test_generate_facebook_nav_test(self):
        config=RunConfig(params={
            "url":"http://www.facebook.com/"
        })

        generator = TestGenerator(self.driver)
        test = generator.generate_navigate_test("http://www.facebook.com/")
        result = test.execute(self.driver,config)
        assert result.passed, result.message

    def test_arrow_cart_nav_test(self):
        params={
            "url":"https://qacart.arrow.com:8443"
        }

        generator = TestGenerator(self.driver)
        test = generator.generate_navigate_test("http://cart.arrow.com/")
        result = test.execute(self.driver,config=RunConfig(params=params))
        assert result.passed, result.message

