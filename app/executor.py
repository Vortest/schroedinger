
from models.result import Result
class Executor(object):

    def __init__(self, steps):
        for step in steps:
            assert hasattr(step, "execute")
        self.execution_steps = steps
        self.execution_results = []

    def execute(self, driver):
        for step in self.execution_steps:
            try:
                step_results = step.execute(driver)
            except Exception as e:
                step_results = Result(self.execution_results,False,"Could not execute",e)
            finally:
                self.execution_results.append(step_results)
        for result in self.execution_results:
            if not result.passed:
               return Result(self.execution_results,False,result.message)
        return Result(self.execution_results,True,"%s" % self.__class__)