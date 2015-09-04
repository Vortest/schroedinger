from action import Action
from selenium_command import SeleniumCommand
from executable import Executable

class Test(Executable):

    def __init__(self, actions):
        super(Test, self).__init__(actions)
        self.actions = actions
        for action in actions:
            assert isinstance(action, Action)