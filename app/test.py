from action import Action
from executable import Executable

class Test(Executable):

    def __init__(self, actions):
        super(Test, self).__init__(actions)
        self.actions = actions
        for action in actions:
            assert isinstance(action, Action)

    def execute(self):
        results = super(Test, self).execute()
        return results