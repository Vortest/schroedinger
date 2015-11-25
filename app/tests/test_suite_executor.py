import unittest
from selenium.webdriver.common.by import By
from app.suite_executor import SuiteExecutor
from app.test_base import TestBase
from app.test_builder import TestGenerator
from models.action import Action
from models.command import Command
from models.element_state import ElementState, Locator
from models.state import State
from models.suite import Suite as TestSuite
from models.suite_config import SuiteConfig, RunConfig
from models.test import Test


class TestExecutor(unittest.TestCase):
    def test_local_suite(self):
        element = ElementState(locators = [Locator(by=By.NAME,value="q")])
        element.save()
        state1 = State(elements=[], url="")
        state2= State(elements=[element], url="http://www.google.com")
        state1.save()
        state2.save()
        params = {}
        params["url"] = "http://www.google.com/"
        params["search"] = "Something"
        commands = [Command(command=Command.NAVIGATE,config_key="url"),
                    Command(command=Command.SENDKEYS,element = element,config_key="search")]
        action = Action(name = "Some Action",steps=commands,start_state=state1, end_state=state2)
        action.save()
        test = Test(name="Some test", actions = [action])
        test.save()
        suite = TestSuite(tests=[test], url="http://www.google.com/")

        config1 = RunConfig(browser="Firefox", params = params)
        config2 = RunConfig(browser="Chrome", params = params)
        configs = SuiteConfig(configs=[config1, config2], suite=suite)
        suite.suite_config = configs
        suite.save()
        executor = SuiteExecutor(suite)
        executor.execute()





