import pytest
from selenium.webdriver.common.by import By
from app.suite import Suite
from app.test import Test
from app.test_base import TestBase
from app.selenium_command import SeleniumCommand
from app.action import Action
from app.step import Step

class TestExecutableChain(TestBase):
    def test_exe_commands(self):
        navigate_command = SeleniumCommand(driver=self.driver,command="Navigate",params="http://www.google.com/")
        command_1= SeleniumCommand(driver=self.driver, command=SeleniumCommand.SENDKEYS, locator=[(By.NAME,"q")], params="Something")
        command_2= SeleniumCommand(driver=self.driver, command=SeleniumCommand.CLICK,locator=[(By.NAME,"btnG")])

        step1 = Step(navigate_command)
        step2 = Step(command_1)
        step3 = Step(command_2)

        action1 = Action([step1, step2, step3])
        test1= Test([action1])
        suite1 = Suite([test1])

        results = suite1.execute()
        print results
        assert results.passed, results.message



