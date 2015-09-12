from app.test_base import TestBase
from models.action import Action
from models.result import Result
from models.suite import Suite
from models.test import Test

class TestSuite(TestBase):
    def test_save_test(self):
        actions = Action.objects[:3]
        test = Test(name="Some test", actions = actions)
        test.save()
        suite = Suite(tests=[test], url="http://www.google.com./")
        suite.execute(self.driver)
        suite.save()
        assert suite.results[-1].passed, suite.results[-1].message