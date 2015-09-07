import logging


class ExecutableResult(object):
    total_indents = 0

    def __init__(self, step_results, passed, message, exception=None):
        self.step_results = step_results
        self.passed = passed
        self.message = message
        self.exception = exception

    def __str__(self):
        ExecutableResult.total_indents += 1
        message = "Executable Passed=%s %s \r\n" % (self.passed, self.message)
        for result in self.step_results:
            for indent in range(0,ExecutableResult.total_indents):
                message += " "
            message += str(result)
        ExecutableResult.total_indents -= 1
        return message


