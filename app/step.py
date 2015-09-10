from models.command import Command
from executable import Executable

class Step(Executable):

    def __init__(self, command):
        assert isinstance(command, Command)
        super(Step,self).__init__([command])

