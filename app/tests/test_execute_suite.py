from app.test_base import TestBase
from models.suite import Suite


class TestExecuteSuite(TestBase):
    def test_execute_suite(self):
        suites = Suite.objects()[:5]
        for suite in suites:
            results = suite.execute(self.driver)
            print results.message
