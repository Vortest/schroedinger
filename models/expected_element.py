import datetime

from flask import url_for
from api import db
import logging

from app.webdriver_wrapper import WebDriver
from app.webelement_wrapper import WebElement
from selenium.common import exceptions
import time


class Locator(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    by = db.StringField(verbose_name="by", required=True)
    value = db.StringField(verbose_name="value", required=True)

    def __repr__(self):
        return "Locator(%s, %s)" % (self.by, self.value)

    def __eq__(self, other):
        if other is None:
            return False
        if self.by == other.by and self.value == other.value:
            return True
        else:
            return False

class ExpectedElement(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    html = db.StringField(max_length=255, required=False)
    locators = db.ListField(db.EmbeddedDocumentField('Locator'))
    screenshot = db.StringField(max_length=255, required=False)

    def get_absolute_url(self):
        return url_for('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.locators

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

