import logging
import datetime
from api import db


class Result(db.EmbeddedDocument):
    total_indents = 0

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    passed = db.BooleanField(required=True)
    message = db.StringField(required=True)
    exception = db.StringField(max_length=255, required=False)
    step_results = db.ListField(db.EmbeddedDocumentField('self'))

    def __str__(self):
        Result.total_indents += 1
        message = "Executable Passed=%s %s \r\n" % (self.passed, self.message)
        for result in self.step_results:
            for indent in range(0,Result.total_indents):
                message += " "
            message += str(result)
        Result.total_indents -= 1
        return message


