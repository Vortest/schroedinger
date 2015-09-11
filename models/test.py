from app.action import Action
from api import db
from app.executable import Executable

class Test(db.Document, Executable):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    html = db.StringField(max_length=255, required=False)
    screenshot = db.StringField(required=False)
    elements = db.ListField(db.ReferenceField(Element))
    actions = db.ListField(db.EmbeddedDocumentField(Action))
    url = db.StringField(max_length=255, required=True)

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at'],
        'ordering': ['-created_at']
    }
    def __init__(self, actions):
        super(Test, self).__init__(actions)
        self.actions = actions
        for action in actions:
            assert isinstance(action, Action)

    def execute(self):
        results = super(Test, self).execute()
        return results