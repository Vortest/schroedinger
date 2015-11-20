import datetime

from flask import url_for
from api import db
import logging
from app.executable import Executable
from models.command import Command
from models.result import Result
from models.suite import Suite

class  CrawlerTask(db.Document):

    class Status():
        COMPLETED = "Completed"
        FAILED = "Failed"
        QUEUED = "Queued"
        IN_PROGRESS = "In Progress"
        ABORTED = "Aborted"
        TIMED_OUT = "Timed Out"

    TASK_STATUS = (Status.COMPLETED, Status.FAILED, Status.QUEUED, Status.IN_PROGRESS, Status.ABORTED, Status.TIMED_OUT)

    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    start_after = db.DateTimeField(default=datetime.datetime.now, required=True)
    started_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    ended_time = db.DateTimeField(default=datetime.datetime.now, required=True)
    status = db.StringField(max_length=25,required=True, choices = TASK_STATUS)
    message = db.StringField(max_length=255,required=True)
    user = db.StringField(max_length=255, required=True)
    url = db.StringField(max_length=255, required=True)
    default_username = db.StringField(max_length=255, required=False)
    default_password = db.StringField(max_length=255, required=False)