import datetime

from flask import url_for
from api import db
import logging
from app.executable import Executable
from models.command import Command

class Action(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    name = db.StringField(verbose_name="name", required=True)
    end_state = db.ReferenceField("State")
    commands = db.ListField(db.EmbeddedDocumentField(Command))
