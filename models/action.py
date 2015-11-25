import datetime

from flask import url_for
from api import db
import logging
from app.executable import Executable
from models.command import Command
from models.result import Result


class Action(db.Document, Executable):

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(required=True)
    start_state = db.ReferenceField("State", required=True)
    end_state = db.ReferenceField("State", required=True)
    steps = db.ListField(db.EmbeddedDocumentField(Command),required=False)
    execution_results = []

    def execute(self, driver, config):
        logging.debug("Executing Action %s" % self.name)
        if not self.start_state.is_state_present(driver):
            result =Result(step_results=self.execution_results,passed=False,message="State %s not present" % self.start_state)
            result.failed_state = self.start_state
            result.actual_state = self.start_state.get_current_state(driver)
            result.actual_state.save()
            result.html = driver.html
            result.screenshot = driver.get_screenshot_as_base64()
            return result
        result = Executable.execute(self, driver, config)
        if not result.passed:
            result.failed_state = self.start_state
            result.actual_state = self.start_state.get_current_state(driver)
            result.actual_state.save()
            result.html = driver.html
            result.screenshot = driver.get_screenshot_as_base64()
        return result
