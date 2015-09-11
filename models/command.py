import logging
import datetime

from api import db
from app.webelement import WebElement
from app.executable import Executable
from models.result import Result
from models.element import Element


class Command(db.EmbeddedDocument, Executable):

    NAVIGATE = "Navigate"
    CLICK = "Click"
    SENDKEYS = "SendKeys"

    COMMANDS = (NAVIGATE, CLICK, SENDKEYS)

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    command = db.StringField(required=True, choices=COMMANDS)
    element = db.ReferenceField(Element, required=False)
    params = db.StringField(required=False)

    execution_results = []
    def execute(self, driver):
        try:
            self.driver = driver
            result = Result(passed=True, message="Execute %s" % self.__repr__())
            logging.info("Execute : %s" % self.__repr__())
            if self.command == self.NAVIGATE:
                self.driver.get(self.params)
            if self.command == self.CLICK:
                WebElement(self.driver, self.element.locators).click()
            if self.command == self.SENDKEYS:
                WebElement(self.driver, self.element.locators).send_keys(self.params)
        except Exception as e:
            result = Result(passed=False, message="Command raised an exception %s" % str(e), exception=e)
        finally:
            logging.debug("Command %s" % result.passed)
            self.execution_results.append(result)
            return result

    def __repr__(self):
        return "Command(%s %s %s)" % (str(self.command), str(self.element), self.params)