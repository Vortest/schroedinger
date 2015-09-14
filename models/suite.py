import datetime
from api import db
from app import executor
from app.executable import Executable
from models.result import Result
from models.test import Test

class Suite(db.Document, Executable):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=False)
    url = db.StringField(max_length=255, required=False)
    tests = db.ListField(db.ReferenceField(Test))
    suite_results = db.ListField(db.EmbeddedDocumentField(Result), required=False)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def execute(self, driver):
        self.driver = driver
        suite_result = Result(passed=True,message="Passed")
        test_results = []
        for test in self.tests:
            result = executor.execute(test, driver)
            test_results.append(result)
            if not result.passed:
                suite_result.passed = False
                suite_result.message = result.message
                suite_result.exception = result.exception
        self.suite_results.append(suite_result)
