import logging
from app.element import Element
from executable import Executable
from executable_result import ExecutableResult


class SeleniumCommand(Executable):
    NAVIGATE = "Navigate"
    CLICK = "Click"
    SENDKEYS = "SendKeys"

    params = ""
    locator = ""

    def __init__(self, **kwargs):
        self.driver = kwargs["driver"]
        if "locator" in kwargs:
            self.locator = kwargs["locator"]
        if "params" in kwargs:
            self.params = kwargs["params"]
        self.command = kwargs["command"]

        self.step_results = []

    def execute(self):
        try:
            result = ExecutableResult([], True, "Execute %s %s (%s)" % (self.command, self.locator, self.params))
            logging.info("Execute : %s" % self)
            if self.command == self.NAVIGATE:
                self.driver.get(self.params)
            if self.command == self.CLICK:
                Element(self.driver, self.locator).click()
            if self.command == self.SENDKEYS:
                Element(self.driver, self.locator).send_keys(self.params)
        except Exception as e:
            result = ExecutableResult([], False, "Command raised an exception %s" % str(e))
        finally:
            logging.debug("Command %s" % result.passed)
            self.step_results.append(result)
            return result

    def __str__(self):
        return "Command(%s %s %s)" % (self.command, self.locator, self.params)