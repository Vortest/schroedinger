from app.test_base import TestBase
from models.action import Action
from models.suite import Suite
from models.test import Test
from models.suite_config import SuiteConfig, RunConfig

class TestSuiteConfig(TestBase):
    def test_suite_config(self):
        params = {
            "url" : "http://www.google.com/",
            "search" : "Something"
        }
        suite = Suite.objects().first()
        config1 = RunConfig(browser="Firefox", params = params)
        config2 = RunConfig(browser="Chrome", params = params)
        suite_config = SuiteConfig(configs=[config1, config2], suite=suite, params = params)
        suite_config.save()