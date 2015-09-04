from app.suite import Suite
from app.test import Test
from app.test_base import TestBase
from app.selenium_command import SeleniumCommand
from app.action import Action
from app.step import Step

class TestExecutableChain(TestBase):
    def test_exe(self):
        navigate_command = SeleniumCommand("Navigate", "Some URl")
        click_1= SeleniumCommand("Click", "Something")
        click_2= SeleniumCommand("SendKeys","SomethingElse")

        step1 = Step(navigate_command)
        step2 = Step(click_1)
        step3 = Step(click_2)

        action1 = Action([step1, step2, step3])
        test1= Test([action1])
        suite1 = Suite([test1])

        results = suite1.execute()
        print results


