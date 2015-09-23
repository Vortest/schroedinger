import datetime
from api import db
from models.element_state import ElementState
from models.state import State


class Page(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    url = db.StringField(max_length=255, required=False)
    default_state = db.ReferenceField(State, required=True)
    states = db.ListField(db.ReferenceField(State))

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }
