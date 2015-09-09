import datetime

from flask import url_for
from api import db
from models.element import Element


class State(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    html = db.StringField(max_length=255, required=False)
    elements = db.ListField(db.ReferenceField(Element))
    screenshot = db.StringField(required=False)


    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def __repr__(self):
        text = "State(%s)" % self.id
        return text