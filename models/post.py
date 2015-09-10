import datetime

from flask import url_for
from api import db

class Comment(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    body = db.StringField(required=True)
    author = db.StringField(max_length=255, required=True)

class Post(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    title = db.StringField(max_length=255, required=True)
    body = db.StringField(required=True)
    comments = db.ListField(db.EmbeddedDocumentField('Comment'))

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at' ],
        'ordering': ['-created_at']
    }
