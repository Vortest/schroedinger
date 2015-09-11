import datetime
from api import db
from app.executable import Executable
from models.action import Action
from models.element import Element


class Test(db.Document, Executable):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(max_length=255, required=False)
    actions = db.ListField(db.ReferenceField(Action))

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }
