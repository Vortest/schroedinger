from app.executable import Executable
from models.test import Test


class Suite(Executable):
    def __init__(self, tests):
        super(Suite,self).__init__(tests)
        for test in tests:
            assert isinstance(test, Test)