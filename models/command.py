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

    def get_steps(self):
        return self

    def execute(self, driver):
        logging.info("Execute : %s" % self.__repr__())
        if self.command not in self.COMMANDS:
            raise ValueError("Command not supported %s" % self.command)
        if self.command == self.NAVIGATE:
            driver.get(self.params)
        if self.command == self.CLICK:
            WebElement(driver, self.element.locators).click()
        if self.command == self.SENDKEYS:
            WebElement(driver, self.element.locators).send_keys(self.params)


    def __repr__(self):
        return "Command(%s %s %s)" % (str(self.command), str(self.element), self.params)