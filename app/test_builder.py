from app import action_builder
from app import state_builder
from models.suite import Suite
from models.test import Test


class TestGenerator(object):
    def __init__(self, driver):
        self.driver = driver

    def generate_navigate_test(self, url):
        self.driver.get(url)
        end_state = state_builder.get_current_state(self.driver)
        end_state.save()
        action = action_builder.get_nav_action(url, end_state)
        action.save()
        action2 = action_builder.get_verify_state_action(end_state)
        action2.save()
        test = Test(name="Navigate %s Test" % url, actions = [action,action2])
        test.save()
        return test

    def generate_login_test(self, url, username, password):
        self.driver.get(url)
        start_state = state_builder.get_current_state(self.driver)
        start_state.save()
        action = action_builder.get_nav_action(url, start_state)
        action.save()
        action2 = action_builder.get_login_action(self.driver, start_state, username, password)
        action2.save()
        end_state = state_builder.get_current_state(self.driver)
        end_state.save()

        action3 = action_builder.get_verify_state_action(end_state)
        test = Test(name="Login Test %s" % url, actions = [action,action2,action3])
        test.save()
        return test