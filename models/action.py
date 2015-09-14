import datetime

from flask import url_for
from api import db
import logging
from app.executable import Executable
from models.command import Command

class Action(db.Document, Executable):

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(required=True)
    start_state = db.ReferenceField("State", required=True)
    end_state = db.ReferenceField("State", required=True)
    commands = db.ListField(db.EmbeddedDocumentField(Command),required=False)
    execution_results = []

    def execute(self, driver):
        logging.debug("Executing Action %s" % self.name)
        self.start_state.verify_state(driver)
        for command in self.commands:
            command.execute(driver)
        self.end_state.verify_state(driver)
