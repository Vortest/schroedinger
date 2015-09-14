
from models.result import Result

step_results = []

def execute(executable, driver):
    for step in executable.get_steps():
        try:
            step.execute(driver)
            result = Result(passed=True, message=str(step.__class__))
        except Exception as e:
            result = Result(passed=False, message="%s" % str(step.__class__),exception=str(e))
            return result
        finally:
            step_results.append(result)
    return Result(step_results = step_results,passed = True, message = str(executable.__class__))