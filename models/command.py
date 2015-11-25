import logging
import datetime

from api import db
from app.webelement import WebElement
from app.executable import Executable
from models.result import Result
from models.element_state import ElementState


class Command(db.EmbeddedDocument, Executable):

    NAVIGATE = "Navigate"
    CLICK = "Click"
    SENDKEYS = "SendKeys"
    VERIFY = "Verify"

    COMMANDS = (NAVIGATE, CLICK, SENDKEYS, VERIFY)

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    command = db.StringField(required=True, choices=COMMANDS)
    element = db.ReferenceField(ElementState, required=False)
    config_key = db.StringField(required=False)

    execution_results = []

    def get_steps(self):
        return self

    execution_results = []
    def execute(self, driver, config):
        try:
            if self.config_key == None:
                self.param = ""
            else:
                self.param = config.params[self.config_key]
            self.driver = driver
            result = Result(passed=True, message="Execute %s %s" % (self.__repr__(),self.param))
            logging.debug("Execute : %s %s" % (self.__repr__(), self.param))
            if self.command == self.NAVIGATE:
                self.driver.get(self.param)
            elif self.command == self.CLICK:
                WebElement(self.driver, self.element.locators).click()
            elif self.command == self.SENDKEYS:
                WebElement(self.driver, self.element.locators).send_keys(self.param)
            elif self.command == self.VERIFY:
                WebElement(self.driver, self.element.locators).highlight(self.param)
            else:
                raise ValueError("Command not supported: %s" % self.command)
        except Exception as e:
            logging.debug("Exception : %s" % str(e))
            result = Result(passed=False, message="Command raised an exception %s" % str(e), exception=str(e))
        finally:
            self.execution_results.append(result)
            return result



    def __repr__(self):
        return "Command(%s %s %s)" % (str(self.command), str(self.element), self.param)