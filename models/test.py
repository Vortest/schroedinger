import datetime
import logging
from api import db
from app import state_builder
from app.executable import Executable
from models.action import Action
from models.element_state import ElementState
from models.result import Result


class Test(db.Document, Executable):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=False)
    actions = db.ListField(db.ReferenceField(Action))

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def execute(self, driver, config):
        logging.debug("Executing Test %s" % self.name)
        self.steps = self.actions
        suite_results = Executable.execute(self, driver, config)
        return suite_results

    def get_steps(self):
        return self.actions