
from executable_result import ExecutableResult
class Executable(object):

    def __init__(self, steps):
        for step in steps:
            assert isinstance(step, Executable)
        self.execution_steps = steps
        self.execution_results = []

    def execute(self):
        for step in self.execution_steps:
            try:
                step_results = step.execute()
            except Exception as e:
                step_results = ExecutableResult(self.execution_results,False,"Threw an Exception" + str(e))
            finally:
                self.execution_results.append(step_results)
        for result in self.execution_results:
            if not result.passed:
               return ExecutableResult(self.execution_results,False,"Child failed %s" % result.message)
        return ExecutableResult(self.execution_results,True,"Passed")