import datetime

from flask import url_for
from api import db
import logging
from app.executable import Executable
from models.command import Command

class Action(db.Document, Executable):

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(verbose_name="name", required=True)
    start_state = db.ReferenceField("State", required=True)
    end_state = db.ReferenceField("State", required=True)
    execution_steps = db.ListField(db.EmbeddedDocumentField(Command))
    execution_results = []

    def execute(self, driver):
        self.start_state.verify_state(driver)
        results = Executable.execute(self, driver)
        self.end_state.verify_state(driver)
        return results