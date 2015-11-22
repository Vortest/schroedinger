import datetime
import logging
from api import db

class RunConfig(db.EmbeddedDocument):
    browser = db.StringField(max_length=255, required=True)
    device_name = db.StringField(max_length=255, required=False)
    version = db.StringField(max_length=255, required=False)
    platform = db.StringField(max_length=255, required=False)
    resolution = db.StringField(max_length=255, required=False)
    orientation = db.StringField(max_length=255, required=False)
    domain = db.StringField(max_length=255, required=False)
    host = db.StringField(max_length=255, required=False)
    sauce_user = db.StringField(max_length=255, required=False)
    sauce_key = db.StringField(max_length=255, required=False)
    username = db.StringField(max_length=255, required=False)
    password = db.StringField(max_length=255, required=False)
    params = db.DictField(default={}, required=False)

class SuiteConfig(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    start_after = db.DateTimeField(default=datetime.datetime.now, required=True)
    configs = db.ListField(db.EmbeddedDocumentField(RunConfig,required=True))

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    @staticmethod
    def default():
        suite= SuiteConfig(configs=[RunConfig(browser="Firefox")])
        suite.save()
        return suite



