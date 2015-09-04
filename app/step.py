from selenium_command import SeleniumCommand
from executable import Executable

class Step(Executable):

    def __init__(self, command):
        assert isinstance(command, SeleniumCommand)
        super(Step,self).__init__([command])

