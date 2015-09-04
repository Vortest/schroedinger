from executable import Executable
from executable_result import ExecutableResult


class SeleniumCommand(Executable):

    def __init__(self, command, params):
        self.command = command
        self.params = params
        self.step_results = []

    def execute(self):
        try:
            result = ExecutableResult(self, True, "Execute %s %s" % (self.command, self.params))
            print "Execute : %s" % self
            if self.command == "Click":
                raise Exception("Something failed")
        except Exception as e:
            result = ExecutableResult(self, False, "Command raised an exception %s" % str(e))
        finally:
            self.step_results.append(result)
            return result

    def __str__(self):
        return "Command(%s %s)" % (self.command, self.params)