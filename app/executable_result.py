class ExecutableResult(object):
    def __init__(self, step_results, passed, message):
        self.step_results = step_results
        self.passed = passed
        self.message = message

    def __str__(self):
        message = "%s %s \r\n" % (self.passed, self.message)
        print message
        for step in self.step_results:
            step = "%s\r\n" % step
            message += step
        return message
