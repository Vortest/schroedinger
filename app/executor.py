
from models.result import Result
from app import state_builder

step_results = []

def execute(executable, driver):
    for step in executable.get_steps():
        try:
            step.execute(driver)
            result = Result(passed=True, message=str(step.__class__))
        except Exception as e:
            result = Result(passed=False, message="%s" % str(step.__class__),exception=str(e))
            result.last_state = state_builder.get_current_state(driver)
            result.last_html = driver.html
            result.screenshot = driver.get_screenshot_as_base64()
            return result
        finally:
            step_results.append(result)
    return Result(step_results = step_results,passed = True, message = str(executable.__class__))