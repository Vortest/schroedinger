from models.result import Result
class Executable(object):

    def __init__(self, steps):
        for step in steps:
            assert isinstance(step, Executable)
        self.execution_steps = steps
        self.execution_results = []

    def execute(self, driver):
        for step in self.execution_steps:
            try:
                step_results = step.execute(driver)
            except Exception as e:
                step_results = Result(step_results=self.execution_results,passed=False,message="Could not execute",exception=e)
            finally:
                self.execution_results.append(step_results)
        for result in self.execution_results:
            if not result.passed:
               return Result(step_results=self.execution_results,passed=False,message=result.message)
        return Result(step_results=self.execution_results,passed=True,message="%s" % self.__class__)