import datetime
from api import db
from app.executable import Executable
from models.result import Result
from models.test import Test


class Suite(db.Document, Executable):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=False)
    url = db.StringField(max_length=255, required=False)
    tests = db.ListField(db.ReferenceField(Test))
    results = db.ListField(db.EmbeddedDocumentField(Result))
    execution_steps = []
    execution_results = []

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def execute(self, driver):
        self.execution_steps = self.tests
        suite_results = Executable.execute(self, driver)
        self.results.append(suite_results)