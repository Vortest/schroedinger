import logging
import datetime
from api import db
from app.webelement import WebElement
from app.executable import Executable
from app.executable_result import ExecutableResult
from models.element import Element


class Command(db.EmbeddedDocument):

    NAVIGATE = "Navigate"
    CLICK = "Click"
    SENDKEYS = "SendKeys"

    COMMANDS = (NAVIGATE, CLICK, SENDKEYS)

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    command = db.StringField(required=True, choices=COMMANDS)
    element = db.ReferenceField(Element, required=False)
    params = db.StringField(required=False)

    #
    #     self.step_results = []
    #
    # def execute(self):
    #     try:
    #         result = ExecutableResult([], True, "Execute %s %s (%s)" % (self.command, self.locator, self.params))
    #         logging.info("Execute : %s" % self)
    #         if self.command == self.NAVIGATE:
    #             self.driver.get(self.params)
    #         if self.command == self.CLICK:
    #             WebElement(self.driver, self.locator).click()
    #         if self.command == self.SENDKEYS:
    #             WebElement(self.driver, self.locator).send_keys(self.params)
    #     except Exception as e:
    #         result = ExecutableResult([], False, "Command raised an exception %s" % str(e))
    #     finally:
    #         logging.debug("Command %s" % result.passed)
    #         self.step_results.append(result)
    #         return result

    # def __str__(self):
    #     return "Command(%s %s %s)" % (self.command, self.element, self.params)