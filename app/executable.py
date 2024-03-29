
import abc
from models.result import Result
class Executable(object):

    def execute(self, driver, config={}):
        self.execution_results = []
        for step in self.steps:
            step_results = step.execute(driver, config)
            if not step_results.passed:
                return Result(step_results=self.execution_results,passed=False,message=step_results.message, failed_state=step_results.failed_state, actual_state=step_results.actual_state, exception=step_results.exception)
            self.execution_results.append(step_results)
        return Result(step_results=self.execution_results,passed=True,message="%s" % self.__class__)
