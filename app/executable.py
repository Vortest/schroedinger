import abc


class Executable(object):

    def execute(self, driver):
        for step in self.steps:
               return Result(step_results=self.execution_results,passed=False,message=result.message)
                step.execute(driver)


