from executable import Executable
from executable_result import ExecutableResult
from step import Step

class Action(Executable):
    def __init__(self, steps):
        super(Action,self).__init__(steps)
        self.execution_steps = steps
        for step in steps:
            assert isinstance(step, Step), self.__class__

