import datetime
from api import db

class Locator(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    by = db.StringField(required=True)
    value = db.StringField(required=True)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(%s, %s)" % (self.by, self.value)

    def __eq__(self, other):
        if other is None:
            return False
        if self.by == other.by and self.value == other.value:
            return True
        else:
            return False

class Location(db.EmbeddedDocument):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    x = db.IntField(required=True)
    y = db.IntField(required=True)
    width = db.IntField(required=True)
    height = db.IntField(required=True)

class ElementType(object):
    PASSWORD = "password"
    USERNAME = "username"
    LOGIN = "login"
    LOGOUT = "logout"
    SUBMIT = "submit"
    SEARCH = "search"
    PHONE = "phone"
    ZIP = "zip"
    FIRSTNAME = "firstname"
    LASTNAME = "lastname"
    ADDRESS = "address"
    DATE = "date"
    MONTH = "month"
    YEAR = "year"
    DAY = "day"
    UNKNOWN = "unknown"

class ElementState(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    html = db.StringField(required=False)
    locators = db.ListField(db.EmbeddedDocumentField(Locator))
    screenshot = db.StringField(required=False)
    location = db.EmbeddedDocumentField(Location, required=False)
    type = db.StringField(required=False)

    def __unicode__(self):
        return self.locators

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }

    def __str__(self):
        repr = "ElementState: "
        for locator in self.locators:
            repr += "{}, ".format(str(locator))
        return repr

    def __eq__(self, other):
        if other is None:
            return False
        for locator in self.locators:
            if locator in other.locators:
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def set_location(self, element):
        self.location = Location(x=element.location['x'],y=element.location['y'],width=element.size['width'],height=element.size['height'])

