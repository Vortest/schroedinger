import datetime
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

    # def execute(self, driver):
    #     self.steps = self.tests
    #     suite_results = Executable.execute(self, driver)
    #     self.suite_results.append(suite_results)

    def execute(self, driver):
        self.driver = driver
        suite_result = Result(passed=True,message="Passed",exception="Passed")

        for test in self.tests:
            test_result = test.execute(driver)
            suite_result.step_results.append(test_result)
            if not test_result.passed:
                suite_result.passed =False
               # suite_result.last_state = state_builder.get_current_state(driver)
               # suite_result.last_html = driver.html
               # suite_result.screenshot = driver.get_screenshot_as_base64()
                suite_result.passed = False
                suite_result.message = str(self.__class__)
                suite_result.exception = test_result.exception

        self.suite_results.append(suite_result)
        return suite_result
