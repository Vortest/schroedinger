import datetime
import logging
from api import db
from app.executable import Executable
from models.result import Result
from models.test import Test
from app import state_builder

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
        logging.debug("Executing Suite %s" % self.name)
        self.driver = driver
        suite_result = Result(passed=True,message="Passed",exception="Passed")

        for test in self.tests:
            test_result = test.execute(driver)
            suite_result.step_results.append(test_result)
            if not test_result.passed:
                suite_result.passed = False
                suite_result.message = str(self.__class__)
                suite_result.exception = test_result.exception
                suite_result.failed_state = test_result.failed_state
                suite_result.actual_state = test_result.actual_state
                suite_result.html = self.driver.page_source
                suite_result.screenshot = self.driver.get_screenshot_as_base64()

        self.suite_results.append(suite_result)
        self.cascade_save()
        return suite_result
