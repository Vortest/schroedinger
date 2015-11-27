import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from app.suite_executor import SuiteExecutor
from app.test_builder import TestGenerator
from app.webelement import WebElement
from app import state_builder
from app.test_base import TestBase
from models.action import Action
from models.command import Command
from models.element_state import Locator, ElementState
from models.suite_config import SuiteConfig, RunConfig
from app.suite_generator import SuiteGenerator

class TestSuiteGenerator(unittest.TestCase):
    def test_generate_facebook_nav_test(self):
        generator = SuiteGenerator(["chrome"])
        suite = generator.generate_suite("http://www.facebook.com/")
        SuiteExecutor(suite).execute()
        result = suite.suite_results[-1]
        assert result.passed, result.message

    def test_generate_iphone_test(self):
        generator = SuiteGenerator(["iphone"])
        suite = generator.generate_suite("http://www.facebook.com/")
        SuiteExecutor(suite).execute()
        result = suite.suite_results[-1]
        assert result.passed, result.message

    def test_generate_ipad_test(self):
        generator = SuiteGenerator(["ipad"])
        suite = generator.generate_suite("http://www.percolate.com/")
        SuiteExecutor(suite).execute()
        result = suite.suite_results[-1]
        assert result.passed, result.message