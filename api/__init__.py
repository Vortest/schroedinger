from flask import Flask
from flask_restful import Api

from flask_mongoengine MongoEngine

app = Flask(__name__)
api = Api(app)

app.config["MONGODB_SETTINGS"] = {'DB': "vortest"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

