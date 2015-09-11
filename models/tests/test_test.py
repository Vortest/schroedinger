from app.test_base import TestBase
from models.action import Action
from models.test import Test

class TestTest(TestBase):
    def test_save_test(self):
        actions = Action.objects[:3]
        test = Test(name="Some test", actions = actions)
        test.save()