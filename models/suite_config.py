import datetime
import logging
from api import db

class RunConfig(db.EmbeddedDocument):
    browser = db.StringField(max_length=255, required=True)
    device_name = db.StringField(max_length=255, default='')
    version = db.StringField(max_length=255, default='')
    platform = db.StringField(max_length=255, default='')
    resolution = db.StringField(max_length=255, default='')
    orientation = db.StringField(max_length=255, default='')
    domain = db.StringField(max_length=255, default='')
    host = db.StringField(max_length=255, default="localhost")
    sauce_user = db.StringField(max_length=255, default='')
    sauce_key = db.StringField(max_length=255, default='')
    username = db.StringField(max_length=255, default='')
    password = db.StringField(max_length=255, default='')
    params = db.DictField(default={})

    @staticmethod
    def default():
        config = RunConfig(browser="Firefox")
        return config


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



