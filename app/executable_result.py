import logging


class ExecutableResult(object):
    def __init__(self, step_results, passed, message, exception=None):
        self.step_results = step_results
        self.passed = passed
        self.message = message
        self.exception = exception

    def __str__(self):
        message = "Results(%s %s) \r\n" % (self.passed, self.message)
        if self.exception:
            logging.exception(str(self.exception))
        return message
        # for step in self.step_results:
        #     step = "%s\r\n" % step
        #     message += step
        # return message
