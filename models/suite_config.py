import datetime
import logging
from api import db
from models.suite import Suite

class RunConfig(db.EmbeddedDocument):
    browser = db.StringField(max_length=255, required=True)
    browser_version = db.StringField(max_length=255, required=False)
    resolution = db.StringField(max_length=255, required=False)
    os = db.StringField(max_length=255, required=False)
    os_version = db.StringField(max_length=255, required=False)
    domain = db.StringField(max_length=255, required=False)
    username = db.StringField(max_length=255, required=False)
    password = db.StringField(max_length=255, required=False)
    params = db.DictField(required=False)

class SuiteConfig(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    start_after = db.DateTimeField(default=datetime.datetime.now, required=True)
    configs = db.ListField(db.EmbeddedDocumentField(RunConfig,required=True))
    suite = db.ReferenceField(Suite, required=True)
    params = db.DictField(required=False)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }
